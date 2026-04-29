#!/usr/bin/env python3
"""Static checks for the careleaver.eu GitHub Pages site."""

from __future__ import annotations

import argparse
import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urldefrag, urlparse
from urllib.request import Request, urlopen


ROOT = Path(".")

REQUIRED_FILES = [
    "AGENTS.md",
    "PROJECT_BRIEF.md",
    "STATE.md",
    "ROADMAP.md",
    "SOURCE_POLICY.md",
    "CONTENT_SAFETY.md",
    "OPERATING_MODEL.md",
    "OVERNIGHT_RUNBOOK.md",
    "index.html",
    "quellen.html",
    "CNAME",
    "robots.txt",
    "sitemap.xml",
    "research/source-log.md",
    "research/open-questions.md",
    "research/qa-report.md",
]

PUBLIC_FILES = ["index.html", "quellen.html", "robots.txt", "sitemap.xml"]

EXTERNAL_LINK_SCHEMES = {"http", "https"}
SITE_HOSTS = {"careleaver.eu", "www.careleaver.eu"}

FORM_CONTROL_TAGS = {"input", "select", "textarea"}
INTERACTIVE_TEXT_TAGS = {"a", "button"}

PLACEHOLDER_PATTERNS = [
    r"lorem ipsum",
    r"REPLACE_ME",
    r"your@email",
    r"example\.com",
    r"555-555",
    r"INSERT_",
    r"TBD_CONTACT",
    r"Die alten Platzhalter",
    r"sollen ergänzt werden, bevor",
]


class LinkParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.ids: set[str] = set()
        self.id_counts: dict[str, int] = {}
        self.links: list[tuple[str, str, int]] = []
        self.blank_links_missing_rel: list[tuple[str, int]] = []
        self.html_lang = ""
        self.main_count = 0
        self.h1_count = 0
        self.heading_levels: list[tuple[int, int]] = []
        self.skip_links: list[tuple[str, int]] = []
        self.labels_for: set[str] = set()
        self.form_controls: list[tuple[str, dict[str, str], int, bool]] = []
        self.images_missing_alt: list[tuple[str, int]] = []
        self.th_missing_scope: list[int] = []
        self.navs_missing_label: list[int] = []
        self.aria_references: list[tuple[str, list[str], int]] = []
        self.interactive_missing_name: list[tuple[str, str, int]] = []
        self._label_depth = 0
        self._text_stack: list[dict[str, object]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        tag = tag.lower()
        attr_map = {key.lower(): value or "" for key, value in attrs}
        line = self.getpos()[0]

        if tag == "html":
            self.html_lang = attr_map.get("lang", "")
        if tag == "main":
            self.main_count += 1
        if tag == "h1":
            self.h1_count += 1
        if re.fullmatch(r"h[1-6]", tag):
            self.heading_levels.append((int(tag[1]), line))
        if tag == "label":
            self._label_depth += 1
            label_target = attr_map.get("for")
            if label_target:
                self.labels_for.add(label_target)
        if tag == "nav" and not (
            attr_map.get("aria-label") or attr_map.get("aria-labelledby") or attr_map.get("title")
        ):
            self.navs_missing_label.append(line)
        if tag in FORM_CONTROL_TAGS:
            self.form_controls.append((tag, attr_map, line, self._label_depth > 0))
        if tag == "img" and "alt" not in attr_map:
            self.images_missing_alt.append((attr_map.get("src", ""), line))
        if tag == "th" and "scope" not in attr_map:
            self.th_missing_scope.append(line)

        element_id = attr_map.get("id")
        if element_id:
            self.ids.add(element_id)
            self.id_counts[element_id] = self.id_counts.get(element_id, 0) + 1

        for attribute in ("aria-labelledby", "aria-describedby", "aria-controls"):
            references = attr_map.get(attribute, "").split()
            if references:
                self.aria_references.append((attribute, references, line))

        href = attr_map.get("href")
        if href:
            self.links.append((href, tag, line))
            if href == "#main" or "skip-link" in attr_map.get("class", "").split():
                self.skip_links.append((href, line))
        if attr_map.get("target") == "_blank":
            rel = set(attr_map.get("rel", "").split())
            if not {"noopener", "noreferrer"}.issubset(rel):
                self.blank_links_missing_rel.append((href or tag, line))
        if tag in INTERACTIVE_TEXT_TAGS:
            self._text_stack.append({"tag": tag, "line": line, "attrs": attr_map, "text": []})

    def handle_data(self, data: str) -> None:
        for item in self._text_stack:
            text = item["text"]
            assert isinstance(text, list)
            text.append(data)

    def handle_endtag(self, tag: str) -> None:
        tag = tag.lower()
        if tag == "label":
            self._label_depth = max(0, self._label_depth - 1)

        for index in range(len(self._text_stack) - 1, -1, -1):
            item = self._text_stack[index]
            if item["tag"] != tag:
                continue
            self._text_stack.pop(index)
            attrs = item["attrs"]
            assert isinstance(attrs, dict)
            text = item["text"]
            assert isinstance(text, list)
            accessible_text = " ".join("".join(text).split())
            has_programmatic_name = attrs.get("aria-label") or attrs.get("aria-labelledby") or attrs.get("title")
            if not accessible_text and not has_programmatic_name:
                line = item["line"]
                assert isinstance(line, int)
                target = attrs.get("href", tag)
                self.interactive_missing_name.append((tag, target, line))
            break


def fail(errors: list[str]) -> None:
    if errors:
        for error in errors:
            print(error)
        raise SystemExit(1)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run static checks for careleaver.eu.")
    parser.add_argument(
        "--external",
        action="store_true",
        help="Also check external HTTP(S) links from HTML files.",
    )
    parser.add_argument(
        "--soft-external",
        action="store_true",
        help="Report external-link failures as warnings instead of failing the command.",
    )
    parser.add_argument(
        "--external-timeout",
        type=float,
        default=15.0,
        help="Timeout in seconds per external-link request.",
    )
    return parser.parse_args()


def check_required_files(errors: list[str]) -> None:
    for name in REQUIRED_FILES:
        if not (ROOT / name).is_file():
            errors.append(f"Missing required file: {name}")

    cname = ROOT / "CNAME"
    if cname.exists() and cname.read_text(encoding="utf-8").strip() != "careleaver.eu":
        errors.append("CNAME must contain exactly careleaver.eu")


def check_public_placeholders(errors: list[str]) -> None:
    compiled = [re.compile(pattern, re.IGNORECASE) for pattern in PLACEHOLDER_PATTERNS]
    for name in PUBLIC_FILES:
        text = (ROOT / name).read_text(encoding="utf-8")
        for pattern in compiled:
            if pattern.search(text):
                errors.append(f"{name}: public placeholder pattern found: {pattern.pattern}")


def parse_html_files() -> dict[Path, LinkParser]:
    parsed: dict[Path, LinkParser] = {}
    for path in sorted(ROOT.glob("*.html")):
        parser = LinkParser()
        parser.feed(path.read_text(encoding="utf-8"))
        parsed[path] = parser
    return parsed


def check_internal_links(errors: list[str]) -> None:
    parsed = parse_html_files()

    for path, parser in parsed.items():
        duplicates = sorted(element_id for element_id, count in parser.id_counts.items() if count > 1)
        for element_id in duplicates:
            errors.append(f"{path}: duplicate HTML id found: {element_id}")

        for href, _tag, line in parser.links:
            parsed_url = urlparse(href)
            if parsed_url.scheme in {"http", "https"} and parsed_url.netloc not in SITE_HOSTS:
                continue
            if parsed_url.scheme in {"mailto", "tel", "sms", "data"}:
                continue
            if href.startswith("javascript:"):
                continue

            if parsed_url.scheme in {"http", "https"}:
                link_path = parsed_url.path or "/"
                fragment = parsed_url.fragment
            else:
                link_path, fragment = urldefrag(href)
            if not link_path:
                target = path
            elif link_path in {"/", "./"}:
                target = Path("index.html")
            else:
                target = (path.parent / link_path.lstrip("/")).resolve().relative_to(ROOT.resolve())

            target = Path(target)
            if target.is_dir():
                target = target / "index.html"
            if target.suffix == "":
                target = target.with_suffix(".html")

            if not target.exists():
                errors.append(f"{path}:{line}: missing internal target {href}")
                continue

            if fragment:
                target_parser = parsed.get(target)
                if target_parser is None and target.suffix == ".html":
                    target_parser = LinkParser()
                    target_parser.feed(target.read_text(encoding="utf-8"))
                    parsed[target] = target_parser
                if target_parser and fragment not in target_parser.ids:
                    errors.append(f"{path}:{line}: missing anchor #{fragment} for {href}")

        for href, line in parser.blank_links_missing_rel:
            errors.append(f"{path}:{line}: target=_blank link missing rel noopener noreferrer: {href}")


def form_control_has_label(
    tag: str,
    attrs: dict[str, str],
    in_wrapping_label: bool,
    labels_for: set[str],
) -> bool:
    input_type = attrs.get("type", "text").lower()
    if tag == "input" and input_type == "hidden":
        return True
    if tag == "input" and input_type in {"button", "submit", "reset"}:
        return bool(attrs.get("value") or attrs.get("aria-label") or attrs.get("aria-labelledby") or attrs.get("title"))
    return bool(
        in_wrapping_label
        or (attrs.get("id") and attrs["id"] in labels_for)
        or attrs.get("aria-label")
        or attrs.get("aria-labelledby")
        or attrs.get("title")
    )


def check_accessibility_basics(errors: list[str]) -> None:
    parsed = parse_html_files()

    for path, parser in parsed.items():
        if not parser.html_lang:
            errors.append(f"{path}: html element missing lang attribute")
        elif not parser.html_lang.lower().startswith("de"):
            errors.append(f"{path}: html lang should start with de, found {parser.html_lang}")

        if parser.main_count != 1:
            errors.append(f"{path}: expected exactly one main element, found {parser.main_count}")
        if parser.h1_count != 1:
            errors.append(f"{path}: expected exactly one h1, found {parser.h1_count}")
        if "main" not in parser.ids:
            errors.append(f"{path}: skip target id=\"main\" missing")
        if not any(href == "#main" for href, _line in parser.skip_links):
            errors.append(f"{path}: skip link to #main missing")

        previous_level = 0
        for level, line in parser.heading_levels:
            if previous_level and level > previous_level + 1:
                errors.append(f"{path}:{line}: heading level jumps from h{previous_level} to h{level}")
            previous_level = level

        for attribute, references, line in parser.aria_references:
            for reference in references:
                if reference not in parser.ids:
                    errors.append(f"{path}:{line}: {attribute} references missing id {reference}")

        for tag, attrs, line, in_wrapping_label in parser.form_controls:
            if not form_control_has_label(tag, attrs, in_wrapping_label, parser.labels_for):
                control_id = attrs.get("id") or attrs.get("name") or tag
                errors.append(f"{path}:{line}: form control missing accessible label: {control_id}")

        for tag, target, line in parser.interactive_missing_name:
            errors.append(f"{path}:{line}: {tag} missing accessible text/name: {target}")
        for source, line in parser.images_missing_alt:
            errors.append(f"{path}:{line}: img missing alt attribute: {source or '[inline]'}")
        for line in parser.th_missing_scope:
            errors.append(f"{path}:{line}: table header missing scope attribute")
        for line in parser.navs_missing_label:
            errors.append(f"{path}:{line}: nav missing aria-label, aria-labelledby, or title")


def collect_external_links() -> dict[str, list[str]]:
    links: dict[str, list[str]] = {}
    for path, parser in parse_html_files().items():
        for href, _tag, line in parser.links:
            parsed_url = urlparse(href)
            if parsed_url.scheme not in EXTERNAL_LINK_SCHEMES:
                continue
            if parsed_url.netloc in SITE_HOSTS:
                continue
            url, _fragment = urldefrag(href)
            links.setdefault(url, []).append(f"{path}:{line}")
    return links


def probe_external_link(url: str, timeout: float) -> tuple[bool, str]:
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "User-Agent": "careleaver.eu static link checker",
    }
    last_error = "not checked"

    for method in ("HEAD", "GET"):
        request = Request(url, headers=headers, method=method)
        if method == "GET":
            request.add_header("Range", "bytes=0-0")
        try:
            with urlopen(request, timeout=timeout) as response:
                status = response.getcode()
                if 200 <= status < 400:
                    return True, f"HTTP {status}"
                last_error = f"HTTP {status}"
        except HTTPError as error:
            last_error = f"HTTP {error.code}"
            if method == "HEAD" and error.code in {403, 405, 406, 429, 500, 501, 502, 503}:
                continue
            return False, last_error
        except (TimeoutError, URLError, OSError) as error:
            last_error = str(error)
            if method == "HEAD":
                continue
            return False, last_error

    return False, last_error


def check_external_links(timeout: float) -> list[str]:
    errors: list[str] = []
    for url, references in sorted(collect_external_links().items()):
        ok, detail = probe_external_link(url, timeout)
        if not ok:
            joined_refs = ", ".join(references[:3])
            if len(references) > 3:
                joined_refs += f", +{len(references) - 3} more"
            errors.append(f"{joined_refs}: external link failed ({detail}): {url}")
    return errors


def check_index_guardrails(errors: list[str]) -> None:
    index = (ROOT / "index.html").read_text(encoding="utf-8")
    required_snippets = [
        '<html lang="de-AT">',
        '<meta name="description"',
        '<link rel="canonical" href="https://careleaver.eu/">',
        'id="schnelle-hilfe"',
        'id="was-brauchst-du"',
        'id="quellen"',
        "2026-04-29",
        "2026-07-29",
        "Lokale Daten löschen",
        'href="quellen.html"',
    ]
    for snippet in required_snippets:
        if snippet not in index:
            errors.append(f"index.html: missing required snippet: {snippet}")

    forbidden_snippets = [
        "Anspruchs-Check",
        "18-25",
        "Diese Seite entscheidet, ob",
    ]
    for snippet in forbidden_snippets:
        if snippet in index:
            errors.append(f"index.html: forbidden risky wording found: {snippet}")


def check_sources_page_guardrails(errors: list[str]) -> None:
    page = (ROOT / "quellen.html").read_text(encoding="utf-8")
    required_snippets = [
        '<html lang="de-AT">',
        '<meta name="description"',
        '<link rel="canonical" href="https://careleaver.eu/quellen.html">',
        'id="review"',
        'id="aenderungen"',
        "2026-04-29",
        "2026-07-29",
        "keine Rechtsberatung",
        "kein Notruf",
    ]
    for snippet in required_snippets:
        if snippet not in page:
            errors.append(f"quellen.html: missing required snippet: {snippet}")

    forbidden_snippets = [
        "Anspruchs-Check",
        "18-25",
        "Diese Seite entscheidet, ob",
    ]
    for snippet in forbidden_snippets:
        if snippet in page:
            errors.append(f"quellen.html: forbidden risky wording found: {snippet}")


def main() -> None:
    args = parse_args()
    errors: list[str] = []
    check_required_files(errors)
    check_public_placeholders(errors)
    check_internal_links(errors)
    check_accessibility_basics(errors)
    check_index_guardrails(errors)
    check_sources_page_guardrails(errors)
    fail(errors)

    if args.external or args.soft_external:
        external_errors = check_external_links(args.external_timeout)
        if external_errors and args.soft_external:
            for error in external_errors:
                print(f"WARNING: {error}")
            print(f"External link check completed with {len(external_errors)} warning(s)")
        elif external_errors:
            fail(external_errors)
        else:
            print("External links OK")

    print("Site checks OK")


if __name__ == "__main__":
    main()

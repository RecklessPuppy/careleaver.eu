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
        self._line = 1

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attr_map = {key: value or "" for key, value in attrs}
        line = self.getpos()[0]
        element_id = attr_map.get("id")
        if element_id:
            self.ids.add(element_id)
            self.id_counts[element_id] = self.id_counts.get(element_id, 0) + 1
        href = attr_map.get("href")
        if href:
            self.links.append((href, tag, line))
        if attr_map.get("target") == "_blank":
            rel = set(attr_map.get("rel", "").split())
            if not {"noopener", "noreferrer"}.issubset(rel):
                self.blank_links_missing_rel.append((href or tag, line))


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

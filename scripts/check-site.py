#!/usr/bin/env python3
"""Static checks for the careleaver.eu GitHub Pages site."""

from __future__ import annotations

import argparse
import json
import re
import unicodedata
import xml.etree.ElementTree as ET
from collections.abc import Iterator
from dataclasses import dataclass
from datetime import date, timedelta
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
DATE_PATTERN = re.compile(r"\b20\d{2}-\d{2}-\d{2}\b")
NEXT_REVIEW_CONTEXT_PATTERN = re.compile(
    r"n(?:\u00e4|ae)chste.*?pr(?:\u00fc|ue)fung[^0-9]*(.*)$",
    re.IGNORECASE,
)
DEFAULT_REVIEW_WARNING_DAYS = 14

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

REQUIRED_JSONLD_TYPES = {
    Path("index.html"): {"WebSite", "WebPage"},
    Path("quellen.html"): {"WebSite", "WebPage", "BreadcrumbList"},
}

ALLOWED_JSONLD_TYPES = {"WebSite", "WebPage", "BreadcrumbList", "ListItem"}
FORBIDDEN_JSONLD_TYPES = {
    "ContactPoint",
    "GovernmentOrganization",
    "LegalService",
    "LocalBusiness",
    "MedicalOrganization",
    "NGO",
    "Organization",
    "Person",
}
FORBIDDEN_JSONLD_KEYS = {
    "address",
    "author",
    "contactPoint",
    "creator",
    "email",
    "founder",
    "provider",
    "publisher",
    "sameAs",
    "telephone",
}

EXPECTED_APPOINTMENT_CARD_IDS = [
    "termin-care-ma11",
    "termin-u25",
    "termin-wohnbeihilfe",
    "termin-fsw-wohnungslosenhilfe",
    "termin-kija",
]

REQUIRED_APPOINTMENT_CARD_LABELS = [
    "Offizielle Seite öffnen",
    "Was vorbereiten",
    "Fragen stellen",
    "Das schriftlich erbitten",
    "Nicht für Entscheidungen auf diese Website verlassen",
    "Geprüft",
    "Nächste Prüfung",
]


@dataclass(frozen=True)
class ReviewDate:
    path: Path
    label: str
    due: date
    line: int


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
        self.tables_missing_caption: list[int] = []
        self.th_missing_scope: list[int] = []
        self.navs_missing_label: list[int] = []
        self.aria_references: list[tuple[str, list[str], int]] = []
        self.interactive_missing_name: list[tuple[str, str, int]] = []
        self.json_ld_scripts: list[tuple[str, int]] = []
        self.canonical_links: list[tuple[str, int]] = []
        self._label_depth = 0
        self._text_stack: list[dict[str, object]] = []
        self._json_ld_parts: list[str] | None = None
        self._json_ld_line = 0
        self._table_stack: list[dict[str, object]] = []

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
        if tag == "table":
            self._table_stack.append({"line": line, "has_caption": False})
        if tag == "caption" and self._table_stack:
            self._table_stack[-1]["has_caption"] = True
        if tag == "th" and "scope" not in attr_map:
            self.th_missing_scope.append(line)
        if tag == "script" and attr_map.get("type", "").lower() == "application/ld+json":
            self._json_ld_parts = []
            self._json_ld_line = line
        if tag == "link" and "canonical" in attr_map.get("rel", "").lower().split():
            self.canonical_links.append((attr_map.get("href", ""), line))

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
        if self._json_ld_parts is not None:
            self._json_ld_parts.append(data)
        for item in self._text_stack:
            text = item["text"]
            assert isinstance(text, list)
            text.append(data)

    def handle_endtag(self, tag: str) -> None:
        tag = tag.lower()
        if tag == "label":
            self._label_depth = max(0, self._label_depth - 1)
        if tag == "script" and self._json_ld_parts is not None:
            self.json_ld_scripts.append(("".join(self._json_ld_parts), self._json_ld_line))
            self._json_ld_parts = None
            self._json_ld_line = 0
        if tag == "table" and self._table_stack:
            table = self._table_stack.pop()
            if not table["has_caption"]:
                line = table["line"]
                assert isinstance(line, int)
                self.tables_missing_caption.append(line)

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


class ReviewTableParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.tables: list[list[list[tuple[str, str, int]]]] = []
        self._table_rows: list[list[tuple[str, str, int]]] | None = None
        self._current_row: list[tuple[str, str, int]] | None = None
        self._current_cell_parts: list[str] | None = None
        self._current_cell_tag = ""
        self._current_cell_line = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        del attrs
        tag = tag.lower()
        if tag == "table":
            self._table_rows = []
        elif tag == "tr" and self._table_rows is not None:
            self._current_row = []
        elif tag in {"th", "td"} and self._current_row is not None:
            self._current_cell_parts = []
            self._current_cell_tag = tag
            self._current_cell_line = self.getpos()[0]

    def handle_data(self, data: str) -> None:
        if self._current_cell_parts is not None:
            self._current_cell_parts.append(data)

    def handle_endtag(self, tag: str) -> None:
        tag = tag.lower()
        if tag in {"th", "td"} and self._current_cell_parts is not None and self._current_row is not None:
            text = " ".join("".join(self._current_cell_parts).split())
            self._current_row.append((text, self._current_cell_tag, self._current_cell_line))
            self._current_cell_parts = None
            self._current_cell_tag = ""
            self._current_cell_line = 0
        elif tag == "tr" and self._current_row is not None and self._table_rows is not None:
            if any(cell[0] for cell in self._current_row):
                self._table_rows.append(self._current_row)
            self._current_row = None
        elif tag == "table" and self._table_rows is not None:
            self.tables.append(self._table_rows)
            self._table_rows = None


def fail(errors: list[str]) -> None:
    if errors:
        for error in errors:
            print(error)
        raise SystemExit(1)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run static checks for careleaver.eu.")
    parser.add_argument(
        "--today",
        type=parse_iso_date,
        default=date.today(),
        help="Date to use for review-date checks, in YYYY-MM-DD format.",
    )
    parser.add_argument(
        "--review-warning-days",
        type=int,
        default=DEFAULT_REVIEW_WARNING_DAYS,
        help="Warn when a source review date is due within this many days.",
    )
    parser.add_argument(
        "--soft-review-dates",
        action="store_true",
        help="Report overdue source reviews as warnings instead of failing the command.",
    )
    parser.add_argument(
        "--report-review-dates",
        action="store_true",
        help="Print a short source-review date report.",
    )
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


def parse_iso_date(value: str) -> date:
    try:
        return date.fromisoformat(value)
    except ValueError as error:
        raise argparse.ArgumentTypeError(f"Expected YYYY-MM-DD date, got {value}") from error


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
        for line in parser.tables_missing_caption:
            errors.append(f"{path}:{line}: table missing caption")
        for line in parser.th_missing_scope:
            errors.append(f"{path}:{line}: table header missing scope attribute")
        for line in parser.navs_missing_label:
            errors.append(f"{path}:{line}: nav missing aria-label, aria-labelledby, or title")


def iter_json_objects(value: object) -> Iterator[dict[str, object]]:
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from iter_json_objects(child)
    elif isinstance(value, list):
        for child in value:
            yield from iter_json_objects(child)


def jsonld_types(node: dict[str, object]) -> set[str]:
    raw_type = node.get("@type")
    if isinstance(raw_type, str):
        return {raw_type}
    if isinstance(raw_type, list):
        return {item for item in raw_type if isinstance(item, str)}
    return set()


def check_structured_data(errors: list[str]) -> None:
    parsed = parse_html_files()

    for path, required_types in REQUIRED_JSONLD_TYPES.items():
        parser = parsed.get(path)
        if parser is None:
            errors.append(f"{path}: unable to parse structured data")
            continue
        if not parser.json_ld_scripts:
            errors.append(f"{path}: missing application/ld+json structured data")
            continue

        discovered_types: set[str] = set()
        for json_ld, line in parser.json_ld_scripts:
            try:
                document = json.loads(json_ld)
            except json.JSONDecodeError as error:
                errors.append(f"{path}:{line}: invalid JSON-LD: {error.msg}")
                continue

            for node in iter_json_objects(document):
                node_types = jsonld_types(node)
                discovered_types.update(node_types)

                for node_type in sorted(node_types):
                    if node_type in FORBIDDEN_JSONLD_TYPES:
                        errors.append(f"{path}:{line}: JSON-LD type needs owner review before use: {node_type}")
                    elif node_type not in ALLOWED_JSONLD_TYPES:
                        errors.append(f"{path}:{line}: unexpected JSON-LD type: {node_type}")

                for key in sorted(FORBIDDEN_JSONLD_KEYS.intersection(node)):
                    errors.append(f"{path}:{line}: JSON-LD key needs owner review before use: {key}")

        missing_types = sorted(required_types - discovered_types)
        for missing_type in missing_types:
            errors.append(f"{path}: missing required JSON-LD type: {missing_type}")


def public_html_files() -> list[Path]:
    return sorted(ROOT.glob("*.html"))


def expected_canonical_url(path: Path) -> str:
    if path.name == "index.html" and path.parent == ROOT:
        return "https://careleaver.eu/"
    if path.name == "index.html":
        return f"https://careleaver.eu/{path.parent.as_posix().strip('/')}/"
    return f"https://careleaver.eu/{path.as_posix()}"


def path_from_site_url(url: str) -> Path | None:
    parsed_url = urlparse(url)
    if parsed_url.scheme != "https" or parsed_url.netloc != "careleaver.eu":
        return None
    path = parsed_url.path or "/"
    if path == "/":
        return Path("index.html")
    if path.endswith("/"):
        return Path(path.lstrip("/")) / "index.html"
    return Path(path.lstrip("/"))


def sitemap_urls(errors: list[str]) -> list[tuple[str, int]]:
    sitemap = ROOT / "sitemap.xml"
    try:
        tree = ET.parse(sitemap)
    except ET.ParseError as error:
        errors.append(f"sitemap.xml: invalid XML: {error}")
        return []

    namespace = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    root = tree.getroot()
    if root.tag != "{http://www.sitemaps.org/schemas/sitemap/0.9}urlset":
        errors.append("sitemap.xml: root element must be sitemap urlset")

    line_lookup = {
        line.strip(): line_number
        for line_number, line in enumerate(sitemap.read_text(encoding="utf-8").splitlines(), start=1)
    }
    urls: list[tuple[str, int]] = []

    for url_element in root.findall("sm:url", namespace):
        loc = url_element.find("sm:loc", namespace)
        lastmod = url_element.find("sm:lastmod", namespace)
        if loc is None or not loc.text or not loc.text.strip():
            errors.append("sitemap.xml: url entry missing loc")
            continue
        loc_text = loc.text.strip()
        urls.append((loc_text, line_lookup.get(f"<loc>{loc_text}</loc>", 1)))

        if lastmod is None or not lastmod.text or not lastmod.text.strip():
            errors.append(f"sitemap.xml: {loc_text} missing lastmod")
            continue
        try:
            date.fromisoformat(lastmod.text.strip())
        except ValueError:
            errors.append(f"sitemap.xml: {loc_text} has invalid lastmod date: {lastmod.text.strip()}")

    return urls


def check_sitemap_and_canonical_consistency(errors: list[str]) -> None:
    parsed = parse_html_files()
    expected_by_path = {path: expected_canonical_url(path) for path in public_html_files()}

    for path, expected_url in expected_by_path.items():
        parser = parsed.get(path)
        if parser is None:
            errors.append(f"{path}: unable to parse canonical link")
            continue
        if len(parser.canonical_links) != 1:
            errors.append(f"{path}: expected exactly one canonical link, found {len(parser.canonical_links)}")
            continue
        canonical_url, line = parser.canonical_links[0]
        if canonical_url != expected_url:
            errors.append(f"{path}:{line}: canonical must be {expected_url}, found {canonical_url}")

    urls = sitemap_urls(errors)
    sitemap_url_set = {url for url, _line in urls}
    expected_urls = set(expected_by_path.values())

    for expected_url in sorted(expected_urls - sitemap_url_set):
        errors.append(f"sitemap.xml: missing canonical URL {expected_url}")
    for url, line in urls:
        target = path_from_site_url(url)
        if target is None:
            errors.append(f"sitemap.xml:{line}: sitemap URL must use https://careleaver.eu/: {url}")
            continue
        if target not in expected_by_path:
            errors.append(f"sitemap.xml:{line}: sitemap URL has no matching root HTML page: {url}")

    robots = (ROOT / "robots.txt").read_text(encoding="utf-8")
    if "Sitemap: https://careleaver.eu/sitemap.xml" not in robots.splitlines():
        errors.append("robots.txt: missing exact sitemap directive for https://careleaver.eu/sitemap.xml")


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
        '"@type": "WebPage"',
        '"@id": "https://careleaver.eu/#webpage"',
        'id="schnelle-hilfe"',
        'id="was-brauchst-du"',
        'id="h-kleiner-schritt"',
        'id="begriffe"',
        'id="gesundheit"',
        'id="arbeit"',
        'id="termin-karten"',
        'id="briefe"',
        'id="bundeslaender"',
        'id="quellen"',
        'value="otherState"',
        'value="letter"',
        'value="work"',
        "Ich bin nicht in Wien / anderes Bundesland",
        "Brief, Bescheid oder mögliche Frist",
        "Schule, Lehre oder Arbeit",
        "Zu Ausbildung und Arbeit",
        "Diese Website berechnet keine Fristen",
        "Begriffe schnell erklärt",
        "Diese Begriffsliste ist keine Rechtsberatung",
        "Zuständige Stelle",
        "Vertrauensperson fragen",
        'id="support-person-script"',
        "Ich frage vorher bei der Stelle, ob und wie du dabei sein kannst.",
        "Wir veröffentlichen konkrete Bundesland-Routen erst nach Quellenprüfung.",
        "Gesundheitsportal Österreich",
        "ÖGK Mitversicherung",
        "Keine Diagnose, Therapieempfehlung oder Versicherungsentscheidung.",
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

    if re.search(r"font-size\s*:[^;]*(?:vw|vh|vmin|vmax)", index, flags=re.IGNORECASE):
        errors.append("index.html: font-size should not use viewport-relative units")

    check_accessibility_css_guardrails(Path("index.html"), index, errors, requires_pill_targets=True)
    check_appointment_cards(index, errors)
    check_template_privacy_fields(errors)
    if index.count('a[href^="http"]::after') < 2 or "attr(href)" not in index:
        errors.append("index.html: print output should expose external URLs, including section-print popups")


def check_accessibility_css_guardrails(
    path: Path,
    text: str,
    errors: list[str],
    *,
    requires_pill_targets: bool = False,
) -> None:
    if "@media (prefers-reduced-motion: reduce)" not in text:
        errors.append(f"{path}: missing prefers-reduced-motion CSS guardrail")
    if not re.search(r"nav\s+a\s*\{[^}]*min-height\s*:\s*44px", text, flags=re.IGNORECASE | re.DOTALL):
        errors.append(f"{path}: nav links should keep a 44px touch target")
    if requires_pill_targets and not re.search(
        r"\.pill\s*\{[^}]*min-height\s*:\s*44px",
        text,
        flags=re.IGNORECASE | re.DOTALL,
    ):
        errors.append(f"{path}: crisis/action pills should keep a 44px touch target")


def check_appointment_cards(index: str, errors: list[str]) -> None:
    card_count = index.count('class="card appointment-card"')
    if card_count != len(EXPECTED_APPOINTMENT_CARD_IDS):
        errors.append(
            "index.html: expected "
            f"{len(EXPECTED_APPOINTMENT_CARD_IDS)} appointment cards, found {card_count}"
        )

    for card_id in EXPECTED_APPOINTMENT_CARD_IDS:
        pattern = re.compile(
            r'<article class="card appointment-card" id="' + re.escape(card_id) + r'">(.*?)</article>',
            flags=re.DOTALL,
        )
        match = pattern.search(index)
        if not match:
            errors.append(f"index.html: missing appointment card #{card_id}")
            continue

        card = match.group(1)
        for label in REQUIRED_APPOINTMENT_CARD_LABELS:
            if label not in card:
                errors.append(f"index.html: appointment card #{card_id} missing label: {label}")
        if "Prüfe die offizielle Seite und frage die zuständige Stelle." not in card:
            errors.append(f"index.html: appointment card #{card_id} missing official-page decision warning")
        if "2026-04-29" not in card or "2026-07-29" not in card:
            errors.append(f"index.html: appointment card #{card_id} missing review dates")


def check_template_privacy_fields(errors: list[str]) -> None:
    parser = parse_html_files().get(Path("index.html"))
    if parser is None:
        errors.append("index.html: unable to parse template privacy fields")
        return

    sensitive_prefixes = ("plan-", "appointment-")
    for tag, attrs, line, _in_wrapping_label in parser.form_controls:
        control_id = attrs.get("id", "")
        if not control_id.startswith(sensitive_prefixes):
            continue
        if attrs.get("autocomplete", "").lower() != "off":
            errors.append(
                f"index.html:{line}: sensitive template field #{control_id} should use autocomplete=\"off\""
            )


def check_sources_page_guardrails(errors: list[str]) -> None:
    page = (ROOT / "quellen.html").read_text(encoding="utf-8")
    required_snippets = [
        '<html lang="de-AT">',
        '<meta name="description"',
        '<link rel="canonical" href="https://careleaver.eu/quellen.html">',
        '"@type": "WebPage"',
        '"@type": "BreadcrumbList"',
        '"@id": "https://careleaver.eu/quellen.html#webpage"',
        'id="review"',
        'id="aenderungen"',
        "2026-04-29",
        "2026-07-29",
        "Bundesland-Navigation ergänzt",
        "Brief- und Fristenroute ergänzt",
        "Begriffe-Lesehilfe ergänzt",
        "Begleitperson-Vorlage ergänzt",
        "Arbeits- und Ausbildungsroute ergänzt",
        "Druck-URLs ergänzt",
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

    if re.search(r"font-size\s*:[^;]*(?:vw|vh|vmin|vmax)", page, flags=re.IGNORECASE):
        errors.append("quellen.html: font-size should not use viewport-relative units")

    check_accessibility_css_guardrails(Path("quellen.html"), page, errors)
    if 'a[href^="http"]::after' not in page or "attr(href)" not in page:
        errors.append("quellen.html: print output should expose external URLs")


def fold_text(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value.lower())
    return "".join(character for character in normalized if not unicodedata.combining(character))


def review_dates_from_text(path: Path, label: str, text: str, line: int, errors: list[str]) -> list[ReviewDate]:
    dates: list[ReviewDate] = []
    for match in DATE_PATTERN.finditer(text):
        raw_date = match.group(0)
        try:
            due = date.fromisoformat(raw_date)
        except ValueError:
            errors.append(f"{path}:{line}: invalid review date {raw_date} for {label}")
            continue
        dates.append(ReviewDate(path=path, label=label, due=due, line=line))
    return dates


def review_dates_from_html(path: Path, errors: list[str]) -> list[ReviewDate]:
    text = path.read_text(encoding="utf-8")
    items: list[ReviewDate] = []

    parser = ReviewTableParser()
    parser.feed(text)
    for table in parser.tables:
        header_index = -1
        review_index = -1
        label_index = 0

        for row_index, row in enumerate(table):
            folded_cells = [fold_text(cell[0]) for cell in row]
            matching_indexes = [
                cell_index for cell_index, cell_text in enumerate(folded_cells) if "nachste prufung" in cell_text
            ]
            if matching_indexes:
                header_index = row_index
                review_index = matching_indexes[0]
                for cell_index, cell_text in enumerate(folded_cells):
                    if "bereich" in cell_text:
                        label_index = cell_index
                        break
                break

        if header_index < 0 or review_index < 0:
            continue

        for row in table[header_index + 1 :]:
            if len(row) <= review_index:
                continue
            label = row[label_index][0] if len(row) > label_index and row[label_index][0] else "review row"
            review_cell = row[review_index]
            row_dates = review_dates_from_text(path, label, review_cell[0], review_cell[2], errors)
            if not row_dates:
                errors.append(f"{path}:{review_cell[2]}: review row has no YYYY-MM-DD date: {label}")
            items.extend(row_dates)

    for line_number, line in enumerate(text.splitlines(), start=1):
        next_review_match = NEXT_REVIEW_CONTEXT_PATTERN.search(line)
        if not next_review_match:
            continue
        items.extend(
            review_dates_from_text(path, "inline next-review note", next_review_match.group(1), line_number, errors)
        )

    return items


def review_dates_from_source_log(path: Path, errors: list[str]) -> list[ReviewDate]:
    items: list[ReviewDate] = []
    current_heading = "source log"
    in_code_block = False

    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        stripped = line.strip()
        if stripped.startswith("```"):
            in_code_block = not in_code_block
            continue
        if in_code_block:
            continue
        if stripped.startswith("## "):
            current_heading = stripped.removeprefix("## ").strip()
            continue
        if not fold_text(stripped).startswith("- review by:"):
            continue
        row_dates = review_dates_from_text(path, current_heading, stripped, line_number, errors)
        if not row_dates:
            errors.append(f"{path}:{line_number}: source entry has Review by but no YYYY-MM-DD date: {current_heading}")
        items.extend(row_dates)

    return items


def collect_review_dates(errors: list[str]) -> list[ReviewDate]:
    items: list[ReviewDate] = []
    for path in sorted(ROOT.glob("*.html")):
        items.extend(review_dates_from_html(path, errors))

    source_log = ROOT / "research/source-log.md"
    if source_log.exists():
        items.extend(review_dates_from_source_log(source_log, errors))

    return items


def check_review_dates(
    errors: list[str],
    warnings: list[str],
    today: date,
    warning_days: int,
    soft_review_dates: bool,
) -> list[ReviewDate]:
    items = collect_review_dates(errors)
    if not items:
        errors.append("No source review dates found in public HTML or source log")
        return items

    warning_window = today + timedelta(days=warning_days)
    for item in sorted(items, key=lambda review: (review.due, str(review.path), review.line, review.label)):
        location = f"{item.path}:{item.line}"
        if item.due < today:
            message = f"{location}: source review overdue since {item.due.isoformat()}: {item.label}"
            if soft_review_dates:
                warnings.append(message)
            else:
                errors.append(message)
        elif item.due <= warning_window:
            days_left = (item.due - today).days
            warnings.append(f"{location}: source review due in {days_left} day(s) on {item.due.isoformat()}: {item.label}")

    return items


def print_review_date_report(items: list[ReviewDate], today: date) -> None:
    print(f"Source review dates as of {today.isoformat()}:")
    for item in sorted(items, key=lambda review: (review.due, str(review.path), review.line, review.label))[:20]:
        days_left = (item.due - today).days
        if days_left < 0:
            status = f"overdue by {-days_left} day(s)"
        elif days_left == 0:
            status = "due today"
        else:
            status = f"due in {days_left} day(s)"
        print(f"- {item.due.isoformat()} ({status}) {item.path}:{item.line} {item.label}")


def main() -> None:
    args = parse_args()
    errors: list[str] = []
    warnings: list[str] = []
    check_required_files(errors)
    check_public_placeholders(errors)
    check_internal_links(errors)
    check_accessibility_basics(errors)
    check_structured_data(errors)
    check_sitemap_and_canonical_consistency(errors)
    check_index_guardrails(errors)
    check_sources_page_guardrails(errors)
    review_dates = check_review_dates(
        errors,
        warnings,
        args.today,
        args.review_warning_days,
        args.soft_review_dates,
    )
    fail(errors)

    for warning in warnings:
        print(f"WARNING: {warning}")

    if args.report_review_dates:
        print_review_date_report(review_dates, args.today)

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

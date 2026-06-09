from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote

from generate_product_i18n import COMPONENTS, LANGUAGES, LOCALIZED_UI, PRODUCTS


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "README.md",
    "README.en.md",
    "LICENSE",
    "CONTRIBUTING.md",
    "CONTRIBUTING.en.md",
    "SECURITY.md",
    "SECURITY.en.md",
    "SUPPORT.md",
    "SUPPORT.en.md",
    "CODE_OF_CONDUCT.md",
    "CODE_OF_CONDUCT.en.md",
    "CHANGELOG.md",
    "CHANGELOG.en.md",
    "CODEX_PROJECT_READINESS.md",
    "CODEX_PROJECT_READINESS.en.md",
    "AGENTS.md",
    "docs/de/index.md",
    "docs/de/FAQ.md",
    "docs/de/I18N.md",
    "docs/de/RELEASE_PROCESS.md",
    "docs/de/MAINTAINER_CHECKLIST.md",
    "docs/en/index.md",
    "docs/en/FAQ.md",
    "docs/en/I18N.md",
    "docs/en/RELEASE_PROCESS.md",
    "docs/en/MAINTAINER_CHECKLIST.md",
]

PACKAGE_READMES = [
    "Code-Review Refactoring Coach/README.en.md",
    "Custom-GPT-Generator/README.en.md",
    "Entscheidungsvorlagen Builder/README.en.md",
    "KI-Integration Sicherheitsberater/README.en.md",
    "N8N-Generator/README.en.md",
    "OpenWebUI Model Builder/README.en.md",
    "OpenWebUI Model Builder/Problemfälle/README.en.md",
    "Promptgenerator/README.en.md",
    "Präsentationscreator/README.en.md",
    "Research Briefing Builder/README.en.md",
    "Testfall-Generator/README.en.md",
    "Unterrichtsfolien & Handout Builder/README.en.md",
]

LANGUAGE_LINK_FILES = [
    "README.md",
    "README.en.md",
    "CONTRIBUTING.md",
    "CONTRIBUTING.en.md",
    "SECURITY.md",
    "SECURITY.en.md",
    "SUPPORT.md",
    "SUPPORT.en.md",
    "CODE_OF_CONDUCT.md",
    "CODE_OF_CONDUCT.en.md",
    "CHANGELOG.md",
    "CHANGELOG.en.md",
    "CODEX_PROJECT_READINESS.md",
    "CODEX_PROJECT_READINESS.en.md",
    "docs/de/index.md",
    "docs/en/index.md",
    *PACKAGE_READMES,
]

TEXT_SUFFIXES = {
    ".css",
    ".editorconfig",
    ".gitattributes",
    ".gitignore",
    ".html",
    ".js",
    ".json",
    ".md",
    ".py",
    ".svg",
    ".ts",
    ".txt",
    ".yaml",
    ".yml",
}

FORBIDDEN_PROSE_SPELLINGS = [
    "vollstaendig",
    "vollstaendige",
    "vollstaendigen",
    "fuer",
    "ueber",
    "pruefen",
    "pruefung",
    "unterstuetzt",
    "unterstuetzung",
    "moeglich",
    "koennen",
    "koennte",
    "muessen",
    "zusaetzlich",
    "praesentation",
    "erklaeren",
    "oeffentlich",
    "rueckfrage",
    "schluessel",
]

LINK_PATTERN = re.compile(r"(!?)\[[^\]]*\]\(([^)]+)\)")
FENCED_CODE_PATTERN = re.compile(r"```.*?```", re.DOTALL)
INLINE_CODE_PATTERN = re.compile(r"`[^`\n]+`")
FORBIDDEN_PATTERN = re.compile(
    r"\b(" + "|".join(re.escape(word) for word in FORBIDDEN_PROSE_SPELLINGS) + r")\b",
    re.IGNORECASE,
)
TECHNICAL_LINE_MARKERS = (
    "Technische Modell-ID",
    "Technische ID",
    "technische Modell-ID",
    "technische ID",
)
UNICODE_FIXTURES = ["ä", "ö", "ü", "Ä", "Ö", "Ü", "ß", "é", "ñ", "中文", "العربية", "עברית", "😀"]


def tracked_files() -> list[str]:
    discovered = {
        str(path.relative_to(ROOT)).replace("\\", "/")
        for path in ROOT.rglob("*")
        if path.is_file() and ".git" not in path.parts
    }
    try:
        raw = subprocess.check_output(["git", "ls-files", "-z"], cwd=ROOT)
    except (OSError, subprocess.CalledProcessError):
        return sorted(discovered)
    tracked = {item.decode("utf-8") for item in raw.split(b"\0") if item}
    return sorted(discovered | tracked)


def read_text(path: Path, errors: list[str]) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError as exc:
        errors.append(f"{path.relative_to(ROOT)}: not valid UTF-8: {exc}")
    return ""


def validate_required_files(errors: list[str]) -> None:
    for item in [*REQUIRED_FILES, *PACKAGE_READMES]:
        if not (ROOT / item).exists():
            errors.append(f"Missing required repository file: {item}")


def validate_language_links(errors: list[str]) -> None:
    for item in LANGUAGE_LINK_FILES:
        path = ROOT / item
        if not path.exists():
            continue
        first_lines = "\n".join(read_text(path, errors).splitlines()[:6])
        if "Deutsch" not in first_lines or "English" not in first_lines:
            errors.append(f"{item}: missing visible Deutsch/English language links near the top")


def validate_links(markdown_files: list[Path], errors: list[str]) -> None:
    for path in markdown_files:
        text = read_text(path, errors)
        for match in LINK_PATTERN.finditer(text):
            raw_target = match.group(2).strip()
            if " " in raw_target and not raw_target.startswith("<"):
                raw_target = raw_target.split(" ", 1)[0]
            raw_target = raw_target.strip("<>")
            if not raw_target or raw_target.startswith(("#", "http://", "https://", "mailto:")):
                continue
            target_without_fragment = raw_target.split("#", 1)[0]
            if not target_without_fragment:
                continue
            target_path = (path.parent / unquote(target_without_fragment)).resolve()
            try:
                target_path.relative_to(ROOT)
            except ValueError:
                errors.append(f"{path.relative_to(ROOT)}: link leaves repository: {raw_target}")
                continue
            if not target_path.exists():
                errors.append(f"{path.relative_to(ROOT)}: missing local link target: {raw_target}")


def validate_utf8_and_umlauts(files: list[str], errors: list[str]) -> None:
    for relative_path in files:
        path = ROOT / relative_path
        suffix = path.suffix.lower()
        if suffix not in TEXT_SUFFIXES and path.name not in TEXT_SUFFIXES:
            continue

        text = read_text(path, errors)
        if suffix != ".md":
            continue

        prose_text = FENCED_CODE_PATTERN.sub("", text)
        prose_text = INLINE_CODE_PATTERN.sub("", prose_text)
        for line_number, line in enumerate(prose_text.splitlines(), start=1):
            if any(marker in line for marker in TECHNICAL_LINE_MARKERS):
                continue
            match = FORBIDDEN_PATTERN.search(line)
            if match:
                errors.append(
                    f"{relative_path}:{line_number}: use real UTF-8 umlaut spelling instead of {match.group(0)!r}"
                )


def validate_unicode_fixtures(errors: list[str]) -> None:
    fixture_text = read_text(ROOT / "docs/de/I18N.md", errors) + "\n" + read_text(ROOT / "docs/en/I18N.md", errors)
    for fixture in UNICODE_FIXTURES:
        if fixture not in fixture_text:
            errors.append(f"Missing Unicode fixture in i18n docs: {fixture}")


def validate_product_language_packs(errors: list[str]) -> None:
    for product in PRODUCTS:
        for language in LANGUAGES:
            ui = LOCALIZED_UI[language.code]
            locale_root = ROOT / product.folder / "i18n" / language.code
            if not locale_root.exists():
                errors.append(f"{product.folder}: missing product language pack: i18n/{language.code}")
                continue
            for filename in COMPONENTS:
                path = locale_root / filename
                relative = path.relative_to(ROOT).as_posix()
                if not path.exists():
                    errors.append(f"{relative}: missing localized product component")
                    continue
                text = read_text(path, errors)
                if language.label not in text:
                    errors.append(f"{relative}: missing language label {language.label!r}")
                if ui["canonical"] not in text:
                    errors.append(f"{relative}: missing canonical source section")
                if ui["rules"] not in text:
                    errors.append(f"{relative}: missing localized locale-rules section")
                if language.code != "en":
                    forbidden_english_headings = ("Languages:", "## Canonical Source Files", "## Locale Rules")
                    for heading in forbidden_english_headings:
                        if heading in text:
                            errors.append(f"{relative}: non-English language pack still contains English boilerplate heading: {heading}")
                    if re.search(r"\bfallback\b", text, re.IGNORECASE):
                        errors.append(f"{relative}: non-English language pack still contains untranslated fallback term")
                required_terms = ("JSON", "API", "UTF-8")
                if any(term not in text for term in required_terms):
                    errors.append(f"{relative}: missing technical identifier preservation rule")


def main() -> int:
    errors: list[str] = []
    files = tracked_files()
    markdown_files = [ROOT / item for item in files if item.endswith(".md")]

    validate_required_files(errors)
    validate_language_links(errors)
    validate_links(markdown_files, errors)
    validate_utf8_and_umlauts(files, errors)
    validate_unicode_fixtures(errors)
    validate_product_language_packs(errors)

    if errors:
        for error in errors:
            print(error)
        return 1

    print(f"Checked {len(markdown_files)} Markdown files.")
    print("Validated required i18n files, product language packs, language links, local links, UTF-8 and Unicode fixtures.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

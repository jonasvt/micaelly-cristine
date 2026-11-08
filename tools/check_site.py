"""Quick quality check of the built site (run after `python build.py`).

    python tools/check_site.py

Checks every page in dist/: internal links/assets exist, #anchors exist,
one <h1>, every <img> has alt, <html lang> set. Prints external links for a manual look.
"""

from __future__ import annotations

import re
import sys
import urllib.parse
from pathlib import Path

DIST = Path(__file__).resolve().parents[1] / "dist"


def main() -> int:
    problems: list[str] = []
    external: set[str] = set()
    pages = [p for p in DIST.rglob("*.html") if p.name != "404.html"]
    for html in pages:
        s = html.read_text(encoding="utf-8")
        rel = html.relative_to(DIST)
        ids = set(re.findall(r'id="([^"]+)"', s))
        if len(re.findall(r"<h1[ >]", s)) != 1:
            problems.append(f"{rel}: expected exactly one <h1>")
        if not re.search(r'<html lang="[^"]+"', s):
            problems.append(f"{rel}: missing <html lang>")
        for img in re.findall(r"<img [^>]*>", s):
            if " alt=" not in img:
                problems.append(f"{rel}: <img> without alt: {img[:80]}")
        for url in re.findall(r'(?:href|src|poster|data-src)="([^"]+)"', s):
            if url.startswith("mailto:"):
                continue
            if url.startswith("http"):
                external.add(url)
                continue
            if url.startswith("#"):
                if url[1:] and url[1:] not in ids:
                    problems.append(f"{rel}: missing anchor {url}")
                continue
            target = (html.parent / urllib.parse.unquote(url.split("#")[0])).resolve()
            if target.is_dir():
                target = target / "index.html"
            if not target.exists():
                problems.append(f"{rel}: broken link {url}")
    print(f"Checked {len(pages)} pages.")
    print("External links:\n  " + "\n  ".join(sorted(external)))
    if problems:
        print("\nPROBLEMS:\n  " + "\n  ".join(problems))
        return 1
    print("\nNo problems found.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

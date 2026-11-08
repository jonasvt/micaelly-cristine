"""Static site generator for Micaelly Cristine's portfolio.

    python build.py            # build into dist/
    python build.py --serve    # build, then serve dist/ at http://127.0.0.1:8000

Content lives in content/*.json (English + Portuguese side by side).
Templates live in src/templates/, static files in src/static/.
Requires: Python 3.10+ and Jinja2 (pip install -r requirements.txt).
"""

from __future__ import annotations

import argparse
import functools
import http.server
import json
import shutil
from datetime import date
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, StrictUndefined

ROOT = Path(__file__).resolve().parent
CONTENT = ROOT / "content"
TEMPLATES = ROOT / "src" / "templates"
STATIC = ROOT / "src" / "static"
DIST = ROOT / "dist"

LANGS = ("en", "pt")  # first one is the default and lives at the site root

# page id -> (template, output path relative to the language root)
PAGES = {
    "home": ("home.html", "index.html"),
    "ai": ("ai-video.html", "ai-video-creator/index.html"),
}


def load_json(name: str) -> dict:
    return json.loads((CONTENT / name).read_text(encoding="utf-8"))


def tr(value, lang: str):
    """Pick the right language from {"en": ..., "pt": ...}; pass anything else through."""
    if isinstance(value, dict) and set(value) <= set(LANGS) and value:
        return value.get(lang) or value[LANGS[0]]
    return value


def page_url(site_url: str, lang: str, page: str) -> str:
    """Absolute, pretty URL of a page (used for canonical, hreflang, sitemap)."""
    prefix = "" if lang == LANGS[0] else f"{lang}/"
    out = PAGES[page][1].removesuffix("index.html")
    return site_url.rstrip("/") + "/" + prefix + out


def rel_root(lang: str, page: str) -> str:
    """Relative path from a page back to the site root ("", "../", "../../")."""
    depth = PAGES[page][1].count("/") + (0 if lang == LANGS[0] else 1)
    return "../" * depth


def rel_link(from_lang: str, from_page: str, to_lang: str, to_page: str) -> str:
    root = rel_root(from_lang, from_page)
    prefix = "" if to_lang == LANGS[0] else f"{to_lang}/"
    out = PAGES[to_page][1].removesuffix("index.html")
    return (root + prefix + out) or "./"


def sync_static() -> None:
    """Mirror src/static into dist/static without wiping dist first.
    (On Windows a file being streamed by the preview server can't be deleted,
    so unchanged files are left alone and only changed/removed ones are touched.)"""
    DIST.mkdir(exist_ok=True)
    out = DIST / "static"
    wanted = set()
    for src in STATIC.rglob("*"):
        rel = src.relative_to(STATIC)
        dst = out / rel
        wanted.add(dst)
        if src.is_dir():
            dst.mkdir(parents=True, exist_ok=True)
            continue
        st = src.stat()
        if dst.exists() and dst.stat().st_size == st.st_size and dst.stat().st_mtime >= st.st_mtime:
            continue
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)
    for old in sorted(out.rglob("*"), reverse=True):
        if old not in wanted:
            try:
                old.unlink() if old.is_file() else old.rmdir()
            except OSError:
                pass


def build() -> None:
    site = load_json("site.json")
    data = {
        "home": load_json("home.json"),
        "ai": load_json("ai-video.json"),
        "ui": load_json("ui.json"),
    }

    env = Environment(
        loader=FileSystemLoader(TEMPLATES),
        autoescape=True,
        undefined=StrictUndefined,
        trim_blocks=True,
        lstrip_blocks=True,
    )

    sync_static()

    site_url = site["site_url"]
    sitemap: list[str] = []

    for lang in LANGS:
        for page, (template_name, out_path) in PAGES.items():
            env.filters["t"] = functools.partial(tr, lang=lang)
            ctx = {
                "lang": lang,
                "page": page,
                "site": site,
                "ui": data["ui"],
                "c": data[page],
                "home": data["home"],
                "root": rel_root(lang, page),
                "canonical": page_url(site_url, lang, page),
                "alternates": {l: page_url(site_url, l, page) for l in LANGS},
                "lang_links": {l: rel_link(lang, page, l, page) for l in LANGS},
                "link": lambda to_page, _l=lang, _p=page: rel_link(_l, _p, _l, to_page),
                "year": date.today().year,
            }
            html = env.get_template(template_name).render(**ctx)
            target = DIST / ("" if lang == LANGS[0] else lang) / out_path
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(html, encoding="utf-8")

            indexable = page != "ai" or site.get("ai_page_indexable", False)
            if indexable:
                sitemap.append(page_url(site_url, lang, page))

    # 404 page (GitHub Pages serves /404.html for unknown paths).
    env.filters["t"] = functools.partial(tr, lang="en")
    (DIST / "404.html").write_text(
        env.get_template("404.html").render(site=site, ui=data["ui"], lang="en", year=date.today().year),
        encoding="utf-8",
    )

    today = date.today().isoformat()
    urls = "\n".join(f"  <url><loc>{u}</loc><lastmod>{today}</lastmod></url>" for u in sitemap)
    (DIST / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        f"{urls}\n</urlset>\n",
        encoding="utf-8",
    )
    (DIST / "robots.txt").write_text(
        f"User-agent: *\nAllow: /\n\nSitemap: {site_url.rstrip('/')}/sitemap.xml\n",
        encoding="utf-8",
    )
    (DIST / ".nojekyll").write_text("", encoding="utf-8")
    if site.get("custom_domain"):
        (DIST / "CNAME").write_text(site["custom_domain"] + "\n", encoding="utf-8")

    print(f"Built {len(LANGS) * len(PAGES)} pages into {DIST}")


def serve(port: int = 8000) -> None:
    handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(DIST))
    with http.server.ThreadingHTTPServer(("127.0.0.1", port), handler) as httpd:
        print(f"Serving http://127.0.0.1:{port}/  (Ctrl+C to stop)")
        httpd.serve_forever()


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--serve", action="store_true")
    ap.add_argument("--port", type=int, default=8000)
    args = ap.parse_args()
    build()
    if args.serve:
        serve(args.port)

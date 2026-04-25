#!/usr/bin/env python3
"""
Mira Palace demo-site generator.

Reads page definitions from ./pages/*.py and renders each to ../site/*.html
using a shared template + nav + footer.

Run from the project root:
    python scripts/build.py
"""

from __future__ import annotations
import importlib, pathlib, sys, datetime

ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPTS = ROOT / "scripts"
SITE = ROOT / "site"
PAGES_DIR = SCRIPTS / "pages"

sys.path.insert(0, str(SCRIPTS))
from common import render_page, SITE_META, write_media_manifest, VIDEO_OPTIONS, MUSIC_OPTIONS  # noqa: E402

# ---- Discover and render every page module -------------------------------

def main() -> None:
    SITE.mkdir(parents=True, exist_ok=True)

    # Static assets: css/js/favicon live under site/assets/ — already committed;
    # this script only (re)writes the HTML pages.

    modules = sorted(p.stem for p in PAGES_DIR.glob("*.py") if p.stem != "__init__")
    count = 0
    for mod_name in modules:
        mod = importlib.import_module(f"pages.{mod_name}")
        for page in mod.PAGES:
            out_path = SITE / page["path"]
            out_path.parent.mkdir(parents=True, exist_ok=True)
            html = render_page(page)
            out_path.write_text(html, encoding="utf-8")
            count += 1
            print(f"  {page['path']}")

    # Media manifest — every video / track found on disk goes into a JS file
    # the browser loads before site.js
    manifest_path = SITE / "assets" / "js" / "media-manifest.js"
    write_media_manifest(manifest_path)
    n_vid = sum(1 for k, _, _ in VIDEO_OPTIONS if k != "none")
    n_aud = sum(1 for k, _, _ in MUSIC_OPTIONS if k != "none")
    print(f"  assets/js/media-manifest.js  ({n_vid} videos, {n_aud} tracks)")

    # Sitemap
    build_sitemap()

    print(f"\nGenerated {count} pages.")
    print(f"Site root: {SITE}")


def build_sitemap() -> None:
    base = SITE_META["base_url"].rstrip("/")
    urls = []
    for p in sorted(SITE.rglob("*.html")):
        if p.name == "404.html":
            continue
        rel = p.relative_to(SITE).as_posix()
        if rel == "index.html":
            rel = ""
        elif rel.endswith("/index.html"):
            rel = rel[:-10]
        urls.append(f"{base}/{rel}")

    sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    today = datetime.date.today().isoformat()
    for u in urls:
        sitemap += f"  <url><loc>{u}</loc><lastmod>{today}</lastmod></url>\n"
    sitemap += "</urlset>\n"
    (SITE / "sitemap.xml").write_text(sitemap, encoding="utf-8")

    # Demo site: keep crawlers out. The site is technically public on a
    # GitHub Pages URL, but we don't want it indexed by Google or scraped
    # while it's still under owner review.
    robots = "User-agent: *\nDisallow: /\n"
    (SITE / "robots.txt").write_text(robots, encoding="utf-8")


if __name__ == "__main__":
    main()

"""Batch-convert every JPG under site/assets/img/ to WebP.

R024 image optimisation step. Runs as part of Release.ps1 and the GitHub
Actions build. Uses Pillow (PIL).

Rules:
  - Reads *.jpg files (case-insensitive).
  - Writes *.webp alongside, quality 82, method 6 (best compression).
  - Skips the WebP write if it already exists AND is newer than the JPG
    source — so re-running the script is cheap (a no-op on unchanged files).
  - Does NOT delete the source JPGs. They stay in the repo as the master
    copy; WebP is a derivative. Copy-Photos.ps1 still refreshes JPGs from
    the reference folder, and the WebP re-derives on next build.

Usage:
    python3 scripts/convert-images.py            # convert everything
    python3 scripts/convert-images.py --force    # re-encode even if fresh
"""
from __future__ import annotations
import sys, pathlib, argparse
try:
    from PIL import Image
except ImportError:
    print("[convert-images] ERROR: Pillow not installed. Install with:")
    print("    pip install pillow --break-system-packages")
    print("    (or in a venv: pip install pillow)")
    sys.exit(1)


# ------------------------------------------------------------------ config

# All folders under site/assets/img/ get scanned recursively. Add any
# new photo folders to `scan_roots` only if you want to constrain scope.
QUALITY = 82         # 82 = best perceptual quality per byte for photos
METHOD  = 6          # Pillow's WebP encoder effort (0-6). 6 = slowest, smallest.
JPG_EXTS = (".jpg", ".jpeg")


def convert_one(jpg: pathlib.Path, force: bool = False) -> tuple[str, int, int]:
    """Convert a single JPG to WebP. Returns (status, jpg_size, webp_size)."""
    webp = jpg.with_suffix(".webp")
    jpg_size = jpg.stat().st_size

    if webp.exists() and not force:
        # Skip if the WebP is fresher than the JPG source
        if webp.stat().st_mtime >= jpg.stat().st_mtime:
            return ("skip", jpg_size, webp.stat().st_size)

    with Image.open(jpg) as img:
        img = img.convert("RGB")
        img.save(
            webp,
            "WEBP",
            quality=QUALITY,
            method=METHOD,
        )
    return ("wrote", jpg_size, webp.stat().st_size)


def main() -> int:
    parser = argparse.ArgumentParser(description="JPG → WebP batch converter")
    parser.add_argument("--force", action="store_true",
                        help="Re-encode even when WebP is fresher than JPG")
    args = parser.parse_args()

    root = pathlib.Path(__file__).resolve().parent.parent
    img_root = root / "site" / "assets" / "img"

    if not img_root.exists():
        print(f"[convert-images] image root not found: {img_root}")
        return 1

    jpgs = [p for p in img_root.rglob("*") if p.suffix.lower() in JPG_EXTS]
    if not jpgs:
        print("[convert-images] no JPGs found — nothing to do")
        return 0

    print(f"[convert-images] scanning {len(jpgs)} JPGs under {img_root}")
    written = 0
    skipped = 0
    total_jpg = 0
    total_webp = 0
    for jpg in jpgs:
        status, js, ws = convert_one(jpg, force=args.force)
        total_jpg += js
        total_webp += ws
        if status == "wrote":
            written += 1
        else:
            skipped += 1

    saving = total_jpg - total_webp
    pct = (saving / total_jpg * 100) if total_jpg else 0
    print(f"[convert-images] wrote={written} skip={skipped} "
          f"jpg_total={total_jpg/1024/1024:.2f} MB "
          f"webp_total={total_webp/1024/1024:.2f} MB "
          f"saving={saving/1024/1024:.2f} MB ({pct:.1f}%)")
    return 0


if __name__ == "__main__":
    sys.exit(main())

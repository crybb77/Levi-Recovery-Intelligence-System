"""
Simple utility to resize all PNG icons in `assets/icons` to a uniform square size.
Usage:
    python scripts/resize_icons.py --size 64

This script requires Pillow: `pip install pillow`.
"""
from PIL import Image
from pathlib import Path
import argparse

ICON_DIR = Path(__file__).parent.parent / "assets" / "icons"

parser = argparse.ArgumentParser()
parser.add_argument("--size", type=int, default=64, help="Output width/height in pixels")
parser.add_argument("--inplace", action="store_true", help="Overwrite original files (default false)")
args = parser.parse_args()

out_dir = ICON_DIR if args.inplace else ICON_DIR / "resized"
out_dir.mkdir(parents=True, exist_ok=True)

for p in ICON_DIR.glob("*.png"):
    if p.is_file():
        img = Image.open(p).convert("RGBA")
        img = img.resize((args.size, args.size), Image.LANCZOS)
        target = out_dir / p.name
        img.save(target)
        print(f"Saved {target}")

print("Done.")

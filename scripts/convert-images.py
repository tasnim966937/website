#!/usr/bin/env python3
"""
Convert images to WebP format for photography albums.

Usage:
    python scripts/convert-images.py <source_folder> <album_slug> [--quality 70] [--max-width 2000]

Examples:
    python scripts/convert-images.py "C:/Photos/DC" dc
    python scripts/convert-images.py "C:/Photos/NYC" nyc --quality 75 --max-width 2400
"""

import argparse
import os
import sys
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    print("Error: Pillow not installed. Run: pip install -r requirements.txt")
    sys.exit(1)


def convert_image(input_path, output_path, max_width, quality):
    """Convert an image to WebP format with optional resizing."""
    img = Image.open(input_path)
    if img.mode != 'RGB':
        img = img.convert('RGB')
    
    width, height = img.size
    if width > max_width:
        ratio = max_width / width
        new_size = (max_width, int(height * ratio))
        img = img.resize(new_size, Image.Resampling.LANCZOS)
    
    img.save(output_path, 'WEBP', quality=quality)
    img.close()
    return os.path.getsize(output_path)


def main():
    parser = argparse.ArgumentParser(
        description='Convert images to WebP format for photography albums.',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python scripts/convert-images.py "C:/Photos/DC" dc
  python scripts/convert-images.py "C:/Photos/NYC" nyc --quality 75
  python scripts/convert-images.py "C:/Photos/LA" la --max-width 2400 --thumb-width 600
        """
    )
    parser.add_argument('source', help='Source folder containing JPG images')
    parser.add_argument('slug', help='Album slug (e.g., "dc", "yosemite")')
    parser.add_argument('--quality', type=int, default=70, help='WebP quality 1-100 (default: 70)')
    parser.add_argument('--max-width', type=int, default=2000, help='Max width for full-size images (default: 2000)')
    parser.add_argument('--thumb-width', type=int, default=800, help='Max width for thumbnails (default: 800)')
    parser.add_argument('--thumb-quality', type=int, default=70, help='WebP quality for thumbnails (default: 70)')
    
    args = parser.parse_args()
    
    # Resolve paths
    script_dir = Path(__file__).parent.parent
    source_dir = Path(args.source)
    output_dir = script_dir / 'photography' / args.slug
    thumbs_dir = output_dir / 'thumbs'
    
    # Validate source
    if not source_dir.exists():
        print(f"Error: Source folder not found: {source_dir}")
        sys.exit(1)
    
    # Create output directories
    output_dir.mkdir(parents=True, exist_ok=True)
    thumbs_dir.mkdir(parents=True, exist_ok=True)
    
    # Find images
    extensions = ('.jpg', '.jpeg', '.png', '.JPG', '.JPEG', '.PNG')
    files = sorted([f for f in source_dir.iterdir() if f.suffix in extensions])
    
    if not files:
        print(f"Error: No images found in {source_dir}")
        sys.exit(1)
    
    print(f"Converting {len(files)} images to photography/{args.slug}/")
    print(f"Settings: quality={args.quality}, max_width={args.max_width}, thumb_width={args.thumb_width}")
    print()
    
    converted = []
    total_full = 0
    total_thumb = 0
    
    for i, src_file in enumerate(files, 1):
        base = src_file.stem
        full_out = output_dir / f"{base}.webp"
        thumb_out = thumbs_dir / f"{base}.webp"
        
        print(f"[{i}/{len(files)}] {base}...", end=" ", flush=True)
        
        try:
            full_size = convert_image(str(src_file), str(full_out), args.max_width, args.quality)
            thumb_size = convert_image(str(src_file), str(thumb_out), args.thumb_width, args.thumb_quality)
            
            converted.append(base)
            total_full += full_size
            total_thumb += thumb_size
            print(f"Full:{full_size//1024}KB Thumb:{thumb_size//1024}KB")
        except Exception as e:
            print(f"Error: {e}")
    
    # Summary
    print()
    print(f"Done! {len(converted)} images converted")
    print(f"Total size: {(total_full + total_thumb) / 1024 / 1024:.2f} MB")
    print(f"Average full-size: {total_full / len(converted) / 1024:.0f} KB")
    print()
    print("Add to photography.html albums array:")
    print(f"  slug: '{args.slug}',")
    print(f"  cover: 'photography/{args.slug}/{converted[0]}.webp',")
    print(f"  images: [")
    
    # Print in rows of 8
    for i in range(0, len(converted), 8):
        chunk = converted[i:i+8]
        line = ",".join(f"'{name}'" for name in chunk)
        comma = "," if i + 8 < len(converted) else ""
        print(f"    {line}{comma}")
    print(f"  ]")


if __name__ == "__main__":
    main()

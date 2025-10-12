#!/usr/bin/env python3
"""
Crop black book pages to remove excess white space and improve extraction quality.
This script applies consistent cropping to all pages in the black book directory.
"""

import os
import sys
from pathlib import Path
from PIL import Image
import argparse
from tqdm import tqdm

def crop_image(input_path, output_path, boundaries):
    """
    Crop a single image with specified boundaries.

    Args:
        input_path: Path to input image
        output_path: Path to save cropped image
        boundaries: Tuple of (left, top, right, bottom) crop coordinates
    """
    try:
        img = Image.open(input_path)
        cropped = img.crop(boundaries)
        cropped.save(output_path, 'PNG', optimize=True)

        # Calculate size reduction
        original_size = os.path.getsize(input_path)
        new_size = os.path.getsize(output_path)
        reduction = (1 - new_size/original_size) * 100

        return {
            'success': True,
            'original_size': original_size,
            'new_size': new_size,
            'reduction': reduction,
            'original_dims': img.size,
            'new_dims': cropped.size
        }
    except Exception as e:
        return {
            'success': False,
            'error': str(e)
        }

def process_directory(input_dir, output_dir, boundaries, test_pages=None):
    """
    Process all PNG files in a directory or just test pages.

    Args:
        input_dir: Input directory path
        output_dir: Output directory path
        boundaries: Crop boundaries (left, top, right, bottom)
        test_pages: List of page numbers to test, or None for all
    """
    input_path = Path(input_dir)
    output_path = Path(output_dir)

    # Create output directory if it doesn't exist
    output_path.mkdir(parents=True, exist_ok=True)

    # Get all PNG files
    if test_pages:
        # Process only specified test pages
        png_files = []
        for page_num in test_pages:
            page_file = input_path / f"page-{page_num:02d}.png"
            if page_file.exists():
                png_files.append(page_file)
            else:
                print(f"Warning: page-{page_num:02d}.png not found")
    else:
        # Process all PNG files
        png_files = sorted(input_path.glob("page-*.png"))

    if not png_files:
        print("No PNG files found to process")
        return

    print(f"Processing {len(png_files)} files...")

    results = []
    total_original = 0
    total_new = 0

    for png_file in tqdm(png_files, desc="Cropping images"):
        output_file = output_path / png_file.name
        result = crop_image(png_file, output_file, boundaries)

        if result['success']:
            total_original += result['original_size']
            total_new += result['new_size']
            results.append({
                'file': png_file.name,
                'reduction': result['reduction'],
                'new_dims': result['new_dims']
            })
        else:
            print(f"Error processing {png_file.name}: {result['error']}")

    # Print summary
    print("\n" + "="*50)
    print("CROPPING SUMMARY")
    print("="*50)
    print(f"Files processed: {len(results)}")
    print(f"Crop boundaries: Left={boundaries[0]}, Top={boundaries[1]}, Right={boundaries[2]}, Bottom={boundaries[3]}")
    print(f"New dimensions: {boundaries[2]-boundaries[0]}x{boundaries[3]-boundaries[1]} pixels")

    if results:
        avg_reduction = sum(r['reduction'] for r in results) / len(results)
        total_reduction = (1 - total_new/total_original) * 100

        print(f"Average size reduction: {avg_reduction:.1f}%")
        print(f"Total size reduction: {total_reduction:.1f}%")
        print(f"Total original size: {total_original/(1024*1024):.1f} MB")
        print(f"Total new size: {total_new/(1024*1024):.1f} MB")
        print(f"Space saved: {(total_original-total_new)/(1024*1024):.1f} MB")

def main():
    parser = argparse.ArgumentParser(description='Crop black book pages to improve extraction')
    parser.add_argument('--input', '-i',
                       default='data/source/black_book',
                       help='Input directory with original images')
    parser.add_argument('--output', '-o',
                       default='data/source/black_book_cropped',
                       help='Output directory for cropped images')
    parser.add_argument('--left', type=int, default=800,
                       help='Left boundary for crop (default: 800)')
    parser.add_argument('--top', type=int, default=200,
                       help='Top boundary for crop (default: 200)')
    parser.add_argument('--right', type=int, default=3200,
                       help='Right boundary for crop (default: 3200)')
    parser.add_argument('--bottom', type=int, default=2500,
                       help='Bottom boundary for crop (default: 2500)')
    parser.add_argument('--test', action='store_true',
                       help='Test mode: only process pages 1, 10, and 50')
    parser.add_argument('--test-pages', type=int, nargs='+',
                       help='Specific page numbers to test')

    args = parser.parse_args()

    # Set crop boundaries
    boundaries = (args.left, args.top, args.right, args.bottom)

    # Determine test pages
    test_pages = None
    if args.test:
        test_pages = [1, 10, 50]
    elif args.test_pages:
        test_pages = args.test_pages

    # Process images
    process_directory(args.input, args.output, boundaries, test_pages)

    if test_pages:
        print(f"\nTest complete! Check the cropped images in: {args.output}")
        print("If results look good, run without --test flag to process all pages.")

if __name__ == "__main__":
    main()
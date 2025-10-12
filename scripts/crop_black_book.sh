#!/bin/bash

# Black Book PNG Cropping Script
# This script crops the black book PNG images to remove borders and standardize dimensions
# It handles two different source sizes:
# - Standard pages (1-64, 67-95): 3300x2550
# - Special pages (65-66): 1650x1275

SOURCE_DIR="data/source/black_book"
OUTPUT_DIR="data/source/black_book_cropped"

# Create output directory if it doesn't exist
mkdir -p "$OUTPUT_DIR"

# Process each PNG file
for file in "$SOURCE_DIR"/page-*.png; do
    if [ -f "$file" ]; then
        filename=$(basename "$file")
        page_num=$(echo "$filename" | sed 's/page-\([0-9]*\)\.png/\1/')

        # Get image dimensions
        dimensions=$(identify -format "%wx%h" "$file")
        width=$(echo "$dimensions" | cut -d'x' -f1)
        height=$(echo "$dimensions" | cut -d'x' -f2)

        echo "Processing $filename (${width}x${height})..."

        if [ "$width" = "1650" ] && [ "$height" = "1275" ]; then
            # Special handling for half-size pages (65-66)
            # These pages need different crop parameters
            echo "  Using half-size crop parameters for page $page_num"
            magick "$file" -crop 1400x900+125+340 -resize 2330x1520! "$OUTPUT_DIR/$filename"
        elif [ "$width" = "3300" ] && [ "$height" = "2550" ]; then
            # Standard pages - original crop parameters
            echo "  Using standard crop parameters for page $page_num"
            magick "$file" -crop 2330x1520+485+515 "$OUTPUT_DIR/$filename"
        else
            echo "  WARNING: Unexpected dimensions for $filename: ${width}x${height}"
            echo "  Copying without crop"
            cp "$file" "$OUTPUT_DIR/$filename"
        fi
    fi
done

echo "Cropping complete. Verifying output..."

# Verify all output files have correct dimensions
for file in "$OUTPUT_DIR"/page-*.png; do
    if [ -f "$file" ]; then
        filename=$(basename "$file")
        dimensions=$(identify -format "%wx%h" "$file")
        if [ "$dimensions" != "2330x1520" ]; then
            echo "WARNING: $filename has incorrect dimensions: $dimensions"
        fi
    fi
done

echo "Done! Cropped files are in $OUTPUT_DIR"
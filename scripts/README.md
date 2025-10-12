# Image Processing Scripts

This directory contains utility scripts for processing the document images, specifically for cropping borders to improve extraction quality.

## Available Scripts

### 1. crop_black_book.sh (Shell Script)
Bash script that uses ImageMagick to crop Black Book PNG images.

**Features:**
- Removes borders from Black Book pages
- Handles two different source sizes automatically
- Standardizes output to 2330x1520 pixels
- Verifies output dimensions

**Usage:**
```bash
./crop_black_book.sh
```

**Requirements:**
- ImageMagick (`magick` command)
- Bash shell

### 2. crop_black_book.py (Python Script)
Python version of the cropping tool with progress bar and detailed statistics.

**Features:**
- Same cropping as shell script
- Progress bar with tqdm
- Size reduction statistics
- Batch processing support

**Usage:**
```bash
# Crop all pages
./crop_black_book.py

# Crop specific pages
./crop_black_book.py --start 1 --end 10

# Custom input/output directories
./crop_black_book.py --input data/source/black_book --output data/cropped
```

**Requirements:**
- Python 3.x
- PIL/Pillow (`pip install Pillow`)
- tqdm (`pip install tqdm`)

### 3. crop_flight_logs.py
Python script for cropping Flight Logs PNG images.

**Features:**
- Optimized for flight log page layout
- Removes excess margins
- Preserves tabular data clarity

**Usage:**
```bash
./crop_flight_logs.py

# With options
./crop_flight_logs.py --input data/source/flight_logs --output data/cropped
```

**Requirements:**
- Python 3.x
- PIL/Pillow
- tqdm

## Why Crop Images?

Cropping document images before extraction provides several benefits:

1. **Improved OCR/Vision Accuracy**: Removing borders eliminates noise
2. **Consistent Dimensions**: Standardized size helps with batch processing
3. **Reduced File Size**: Smaller images = faster processing
4. **Better Focus**: AI models concentrate on content, not margins

## Crop Parameters

### Black Book Pages
- **Standard pages (1-64, 67-95)**:
  - Source: 3300x2550
  - Crop: 2330x1520 at offset (485, 515)

- **Special pages (65-66)**:
  - Source: 1650x1275 (half-size)
  - Crop: 1400x900 at offset (125, 340)
  - Then resize to 2330x1520 for consistency

### Flight Logs
- Crop parameters optimized for tabular layout
- Preserves date columns and passenger lists
- See script source for specific dimensions

## Installation

### Quick Start
```bash
# Install all Python dependencies from project root
pip install -r requirements.txt
```

### For Shell Scripts
```bash
# Ubuntu/Debian
sudo apt-get install imagemagick

# macOS
brew install imagemagick

# Verify installation
magick -version
```

### For Python Scripts Only
```bash
# If you only need the image processing scripts
pip install Pillow tqdm

# Or use the full requirements file from project root
pip install -r ../requirements.txt
```

## Directory Structure

Scripts expect the following structure:
```
data/
├── source/
│   ├── black_book/        # Original PNGs
│   │   ├── page-01.png
│   │   ├── page-02.png
│   │   └── ...
│   └── flight_logs/       # Original PNGs
│       ├── page-001.png
│       ├── page-002.png
│       └── ...
└── source/
    ├── black_book_cropped/  # Output directory
    └── flight_logs_cropped/ # Output directory
```

## Performance

Typical processing times:
- Shell script: ~1-2 seconds per image
- Python script: ~0.5-1 second per image
- Full Black Book (95 pages): ~2-3 minutes
- Full Flight Logs (118 pages): ~2-4 minutes

## Troubleshooting

### Permission Denied
```bash
chmod +x crop_black_book.sh
chmod +x crop_black_book.py
chmod +x crop_flight_logs.py
```

### ImageMagick Policy Error
If you get policy errors with ImageMagick, edit `/etc/ImageMagick-*/policy.xml`:
```xml
<!-- Change this line -->
<policy domain="coder" rights="none" pattern="PDF" />
<!-- To this -->
<policy domain="coder" rights="read|write" pattern="PDF" />
```

### Python Module Not Found
```bash
pip install --user Pillow tqdm
# Or in virtual environment
python -m venv venv
source venv/bin/activate
pip install Pillow tqdm
```

## Contributing

If you improve the crop parameters or add support for Birthday Book cropping, please submit a pull request with:
1. Updated script
2. Test results showing improvement
3. Documentation of new parameters

## License

These scripts are part of the Epstein Network Analysis Project and released under MIT License.
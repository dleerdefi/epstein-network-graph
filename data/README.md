# Data Directory Structure

## /extracted/
Contains manually verified JSON extractions from original documents.

### /extracted/flight_logs/
- **Status**: Pages 1-12 completed and manually verified
- **Format**: `page_XXXX_analysis.json`
- **Contents**: Flight date, aircraft, route, passengers, validation notes

## /external_sources/
Reference data from external public sources.

### /external_sources/flight_logs/
- `EPSTEIN FLIGHT LOGS UNREDACTED.pdf` - Public domain PDF from Archive.org

### /external_sources/name_references/
- `epstein_names_master_list.json` - Compiled list of 85+ names from WTRF/Newsweek court document reporting

## /source/
Original source documents and processed image files organized by document type.

### /source/pdf/
Original PDF documents:
- `jeffey-epstein-50th-birthday-book.pdf` - 50th Birthday Book (191MB)
- `EXHIBITS_STM_UNDISPUTED_FACTS.PDF` - Black Book unredacted (6.0MB)
- `epstein-flight-logs-released-in-usa-vs-maxwell.pdf` - Flight Logs (69MB)

### /source/birthday_book/
- `birthday_book_pdf/` - Chunked PDFs (10-page segments for processing)
- `birthday_book_images/` - PNG conversions from source PDF

### /source/black_book/
- PNG conversions with full page borders (pages 1-95)

### /source/black_book_cropped/
- Border-removed PNGs for improved extraction accuracy

### /source/flight_logs/
- PNG conversions with full page borders (pages 1-118)

### /source/flight_logs_cropped/
- Border-removed PNGs for improved extraction accuracy

---

## Data Quality Notes
- Each extracted page has been manually reviewed and corrected
- Confidence scores included where uncertainty exists
- Known OCR errors documented and corrected in name references
- All dates validated for chronological consistency
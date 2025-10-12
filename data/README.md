# Data Directory Structure

## /extracted/
Contains manually verified JSON extractions from original documents.

### /extracted/flight_logs/
- **Status**: Pages 1-8 completed and manually verified
- **Format**: `page_XXXX_analysis.json`
- **Contents**: Flight date, aircraft, route, passengers, validation notes

## /external_sources/
Reference data from external public sources.

### /external_sources/flight_logs/
- `EPSTEIN FLIGHT LOGS UNREDACTED.pdf` - Public domain PDF from Archive.org

### /external_sources/name_references/
- `epstein_names_master_list.json` - Compiled list of 85+ names from WTRF/Newsweek court document reporting

## /source/
(To be added) Original PNG files of documents

---

## Data Quality Notes
- Each extracted page has been manually reviewed and corrected
- Confidence scores included where uncertainty exists
- Known OCR errors documented and corrected in name references
- All dates validated for chronological consistency
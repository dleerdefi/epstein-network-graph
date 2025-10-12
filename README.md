# Epstein Network Analysis Project

## Project Scope

This project aims to transform three key Epstein network documents (50th Birthday Book, Black Book, and Flight Logs) containing over 340 pages of handwritten and printed text into a fully searchable, queryable knowledge system. Starting with publicly available PDFs, we convert to PNG and use Claude Code's multimodal AI to extract every name, address, phone number, date, and relationship mentioned across these documents. The extracted data is structured into JSON format, validated through community review, and will ultimately be imported into a Neo4j graph database to map the complete network of connections - showing who knew whom, who traveled together, and how frequently they appeared across different contexts.

The goal is to implement a hybrid agentic GraphRAG (Graph Retrieval-Augmented Generation) system that allows anyone to ask questions like "Who flew most frequently in 1995?" or "Show all connections for [person]" and receive accurate, data-driven answers with network visualizations. 

Instead of researchers manually searching through thousands of pages or relying on incomplete summaries, they'll have access to a comprehensive, cross-referenced database where every entity, relationship, and temporal pattern has been extracted, validated, and made queryable. This is purely a data science project focused on making public documents accessible - we do not make claims or conduct investigations, we simply structure the information for analysis.

## Overview

This project makes the Epstein network documents searchable and queryable through modern data science tools. Instead of manually searching through thousands of pages, anyone can ask questions in plain English and receive objective, data-driven responses with network visualizations.

We are analyzing three specific publicly-available documents to map the network:
- **50th Birthday Book** - Birthday greetings and messages from associates
- **Black Book** - Address/contact directory
- **Flight Logs** - Aviation records from private aircraft

This is a **non-partisan, objective data extraction project**. We focus exclusively on these network-mapping documents, NOT on court cases or legal proceedings. The goal is to build a Neo4j knowledge graph and natural language interface so anyone can explore the data without bias or editorializing.

## Project Objectives

1. **Extract** structured data from three document collections using multimodal AI vision
2. **Validate** and refine extracted data through multiple passes and community review
3. **Build** a Neo4j knowledge graph representing entities and relationships
4. **Implement** hybrid agentic GraphRAG for natural language data exploration
5. **Enable** researchers to query the network using plain English

## Source Documents

### Original Documents (Public Access)
- **50th Birthday Book** (2003): Album of birthday greetings and messages given to Epstein for his 50th birthday
  - [View on DocumentCloud](https://www.documentcloud.org/documents/26086390-jeffey-epstein-50th-birthday-book/)
  - 238 pages of messages, drawings, and photos from associates

- **Black Book**: Personal address/contact directory containing 1,500+ names with phone numbers and addresses
  - [View on DocumentCloud](https://www.documentcloud.org/documents/1508273-jeffrey-epsteins-little-black-book-redacted/)
  - 92 pages (redacted version)

- **Flight Logs** (1991-2019): Aviation records from Epstein's private aircraft documenting ~1,000 trips
  - [View on DocumentCloud](https://www.documentcloud.org/documents/6404379-Epstein-Flight-Logs-Lolita-Express/)
  - 118 pages of passenger manifests and flight records

### Additional Sources & External Data
- [House Oversight Committee Releases](https://oversight.house.gov/release/oversight-committee-releases-epstein-records-provided-by-the-department-of-justice/)
- [Complete Black Book CSV](data/external_sources/black_book/) - Full 95 pages from epsteinsblackbook.com
- [Unredacted Flight Logs PDF](data/external_sources/flight_logs/) - Pages 39-118

## What This Repository Provides

### Resources Available
1. **Cropped PNG Images** - Border-removed versions for cleaner extraction (valuable for anyone doing their own analysis)
2. **Structured JSON Data** - Machine-readable extractions from multimodal AI analysis
3. **Processing Scripts** - Python and shell scripts for image cropping
4. **Work-in-Progress Extractions** - Making handwritten and poor-quality scans more accessible
5. **External Validated Data** - Third-party sources for cross-reference

### Directory Structure
```
.
├── data/
│   ├── source/
│   │   ├── pdfs/              # Original PDF documents
│   │   ├── pngs/              # Converted PNG images (full page)
│   │   └── cropped/           # Border-removed PNGs (cleaner for extraction)
│   ├── extracted/
│   │   ├── v1 - first pass/   # Initial AI extraction (complete)
│   │   └── v2 - second pass/  # Manual review and refinement (in progress)
│   └── external_sources/      # Third-party validated data
├── scripts/                   # Image processing utilities
│   ├── crop_black_book.sh    # Shell script for Black Book cropping
│   ├── crop_black_book.py    # Python version with progress bar
│   └── crop_flight_logs.py   # Flight logs cropping script
└── requirements.txt           # Python dependencies
```

### Installation

For Python scripts and future development:
```bash
# Install Python dependencies
pip install -r requirements.txt

# For image processing scripts only
pip install Pillow tqdm
```

The handwriting in many documents is extremely difficult to parse. This project works toward making the data clearer and available in formats suitable for analysis, visualization, and querying.

## Current Extraction Status

| Document | V1 Status | V2 Status | Notes |
|----------|-----------|-----------|-------|
| **50th Birthday Book** | ✅ 128 pages complete | 🔄 Pages 1-11 manually revised | Handwritten messages challenging to extract |
| **Black Book** | ✅ 95 pages complete | 🔄 Pages 1-81 extracted | External CSV provides complete 95 pages |
| **Flight Logs** | ✅ 118 pages complete | 🔄 Pages 1-8 manually revised so far | Pages 39-118 available from unredacted PDF |

### Extraction Challenges

The documents present significant extraction difficulties:
- Handwritten annotations and messages
- Mixed print and cursive text
- Poor scan quality in some sections
- Character confusion (i/l, 0/O, 6/8, z/s)
- Partial redactions in public versions

Multimodal AI extraction provides better results than traditional OCR but still requires extensive manual review and community validation to achieve usable accuracy.

## Project Phases

### Phase 1: Data Extraction (Current)
- Multimodal AI vision analysis of document images
- Two-pass extraction methodology
- Community validation and correction

### Phase 2: Data Processing (Upcoming)
- Entity deduplication and standardization
- Relationship mapping and validation
- Timeline construction from temporal data

### Phase 3: Knowledge Graph (Future)
- Neo4j database implementation
- Entity and relationship modeling
- Graph optimization for query performance

### Phase 4: GraphRAG Implementation (Future)
- Hybrid agentic system development
- Natural language query interface
- RAG pipeline with graph traversal

## Technical Approach

### Extraction Methodology
- **Primary Tool**: Claude's multimodal vision (not traditional OCR)
- **Image Processing**: Cropped borders for improved accuracy
- **Validation**: Multi-pass extraction with manual review
- **External Sources**: Integration of verified third-party data

### Why Multimodal AI?
Traditional OCR fails on:
- Handwritten annotations
- Mixed print/cursive text
- Complex layouts and tables
- Poor quality scans

Claude's vision capabilities provide:
- Context-aware extraction
- Relationship inference
- Layout understanding
- Signature analysis

## Data Format

All extracted data is structured JSON with:
- Complete text preservation (no summaries)
- Entity identification and relationships
- Confidence scores where applicable
- Source page references
- Validation notes

### Example JSON Structure (Flight Log)
```json
{
  "page_number": 1,
  "date_header": "1991 JUL",
  "flights": [{
    "date": "07/12/1991",
    "aircraft": "N908JE",
    "route": {"from": "MIA", "to": "NYF"},
    "passengers": {
      "identified": ["Name1", "Name2"],
      "codes": ["JE", "GM"]
    }
  }],
  "validation": {
    "confidence": 0.85,
    "manual_review": true
  }
}
```

## Important Disclaimers

⚠️ **Data Accuracy**: Due to handwriting, scan quality, and redactions, perfect extraction is impossible. This dataset requires continuous refinement through community validation.

⚠️ **Scope**: We analyze ONLY the three network-mapping documents listed above. We do NOT examine court cases, depositions, or make investigative claims.

⚠️ **Objectivity**: This is a non-partisan data project. We extract and structure information for querying without editorializing or making judgments.

⚠️ **Work in Progress**: Extraction and validation are ongoing. Always cross-reference with original sources when accuracy is critical.

## Contributing

We welcome contributions to improve data accuracy and completeness. Please see [CONTRIBUTING.md](CONTRIBUTING.md) for:
- How to submit corrections via pull requests
- Data validation guidelines
- OSINT research standards
- Quality requirements

## Future Vision: Natural Language Querying

Once complete, anyone will be able to:
- Ask questions in plain English about the network
- Receive data-driven responses with visualizations
- Explore connections via Neo4j graph database
- Access information without reading thousands of pages

Example queries:
- "Who flew most frequently in 1995?"
- "What addresses are listed for [person]?"
- "Show network connections for [entity]"
- "Timeline of flights to specific destinations"

## License

This project processes publicly available documents. All extraction work is released under [MIT License](LICENSE).

## Acknowledgments

- Document sources: Public court records and FOIA releases
- Extraction technology: Anthropic's Claude AI
- Community contributors: See [CONTRIBUTORS.md](CONTRIBUTORS.md)

## Contact

For questions, corrections, or contributions:
- Submit issues via GitHub
- Review [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines
- Check [DATA_STATUS.md](DATA_STATUS.md) for current progress

---

*Making public documents queryable through data science. No more searching through thousands of pages - just ask questions, get objective answers.*
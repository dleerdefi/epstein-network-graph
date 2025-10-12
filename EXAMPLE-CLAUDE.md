# EXAMPLE-CLAUDE.md - AI Extraction Guidelines

This document provides guidance for using Claude's multimodal vision capabilities to extract data from documents in this project.

## Project Overview

This project extracts structured data from historical documents using Claude's advanced vision capabilities to build a comprehensive knowledge graph for network analysis.

## Extraction Methodology

### Why Multimodal Vision (Not OCR)

Traditional OCR tools fail on these documents due to:
- Handwritten annotations mixed with printed text
- Poor scan quality and age-related degradation
- Complex layouts with tables, margins, and overlapping text
- Redactions and partial information
- Signatures requiring interpretation

Claude's vision capabilities excel at:
- Understanding context and relationships
- Interpreting handwriting and signatures
- Maintaining layout awareness
- Inferring missing or partial information
- Identifying entities and relationships

## Document Types and Requirements

### 1. Birthday Book (Event Attendance Records)
- **Format**: Guest lists, event descriptions, dates
- **Key Data**: Names, dates, venues, relationships
- **Special Focus**: Group photos, signatures, event context

### 2. Black Book (Contact Directory)
- **Format**: Alphabetically organized contact entries
- **Key Data**: Names, phone numbers, addresses, emails
- **Special Focus**: Multiple numbers per contact, international formats, handwritten additions

### 3. Flight Logs (Aviation Records)
- **Format**: Tabular flight data with dates, routes, passengers
- **Key Data**: Dates, airports, passenger names/codes, aircraft IDs
- **Special Focus**: Date inference from headers, passenger identification

## Extraction Standards

### CRITICAL RULE: NO SUMMARIES
**EVERY visible element must be transcribed verbatim**. Never summarize or abbreviate content.

### Minimum Requirements Per Page

#### Text Extraction
- Full transcription of ALL visible text
- Include headers, footers, page numbers
- Preserve exact formatting and spelling
- Note unclear text as [unclear] or [illegible]

#### Entity Extraction (Minimum 5 per content page)
- **People**: Every name mentioned or visible
- **Organizations**: Companies, agencies, schools
- **Locations**: Cities, addresses, venues
- **Dates**: Full dates, years, relative references
- **Contact Info**: Phone, email, fax, addresses

#### Visual Analysis
- **Photos**: Count individuals, describe positioning
- **Signatures**: Attempt identification (never just "signature")
- **Redactions**: Note location and context
- **Marginalia**: All handwritten notes and annotations

## Quality Metrics

### Extraction Completeness
- Text: >500 characters per content page
- Entities: >90% of visible/mentioned
- Signatures: 100% attempt at identification
- Photos: 100% individual counts

### Confidence Scoring
- **High**: Clearly readable, unambiguous
- **Medium**: Partially obscured but interpretable
- **Low**: Difficult to read, requires inference

## JSON Output Structure

### Consistent Schema Requirements
All extractions must follow document-specific schemas:

```json
{
  "page_number": 1,
  "document_type": "flight_log|black_book|birthday_book",
  "content": {
    // Document-specific fields
  },
  "entities": {
    "people": [],
    "organizations": [],
    "locations": [],
    "dates": []
  },
  "confidence": {
    "overall": 0.85,
    "notes": "Specific quality issues"
  },
  "validation": {
    "manual_review": false,
    "issues": []
  }
}
```

## Special Instructions by Document Type

### Flight Logs - Date Inference Pattern
1. **Read DATE header** (e.g., "1991 APR") for starting year/month
2. **Track explicit month changes** (e.g., "MAY 1", "JUNE 26")
3. **Apply sequential logic** for day-only entries
4. **Maintain year continuity** unless explicitly changed

Example:
```
Header: "1991 APR"
25          → April 25, 1991
30          → April 30, 1991
MAY 1       → May 1, 1991 (month change)
3           → May 3, 1991
```

### Black Book - Phone Number Patterns
Preserve exact formatting:
- International: "001 212 555 1234"
- UK landlines: "0207-XXX-XXXX"
- UK mobiles: "07XXX XXX XXX"
- Note type: (h)ome, (w)ork, (m)obile, (f)ax

### Birthday Book - Event Analysis
- Count every person in photos
- Note seating arrangements and groupings
- Identify recurring attendees across events
- Document venue and date details

## Common Pitfalls to Avoid

1. **Never Summarize**: "Various phone numbers" ❌ → List each number ✅
2. **Never Skip Signatures**: "Signature" ❌ → "Possible: John Smith" ✅
3. **Never Ignore Margins**: Check all edges for annotations
4. **Never Assume Dates**: Use inference rules, not assumptions
5. **Never Overlook Redactions**: Document what's hidden

## Validation Checklist

Before submitting extraction:
- [ ] All visible text transcribed
- [ ] Minimum 5 entities extracted (if content exists)
- [ ] All signatures identification attempted
- [ ] Photos analyzed with individual counts
- [ ] Confidence scores assigned
- [ ] JSON validates against schema
- [ ] Cross-page references noted

## Extraction Workflow

1. **Visual Analysis**: Examine entire page for layout and content
2. **Text Extraction**: Transcribe all visible text verbatim
3. **Entity Identification**: Extract people, places, organizations
4. **Relationship Mapping**: Note connections and co-appearances
5. **Quality Check**: Verify completeness and accuracy
6. **JSON Generation**: Structure according to schema
7. **Validation**: Ensure all requirements met

## Remember

- **Accuracy over speed**: Take time to extract everything
- **When in doubt, extract it**: Better to have too much than miss data
- **Context matters**: Consider information from other pages
- **Preserve original**: Never "clean up" or "correct" original text
- **Document uncertainty**: Use confidence scores appropriately

---

*This guide ensures consistent, high-quality extraction across all document types using Claude's multimodal capabilities.*
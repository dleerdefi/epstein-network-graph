# Contributing to PDF Intelligence

Thank you for your interest in improving this network analysis project! This document provides guidelines for contributing corrections, validations, and enhancements to the extracted data.

## How to Contribute

### 1. Reporting Errors

If you find extraction errors or inaccuracies:
1. Open an issue with the title: `[ERROR] Document_Type - Page_Number`
2. Provide:
   - Specific field with error
   - Current incorrect value
   - Correct value with evidence
   - Source/reasoning for correction

Example:
```
Title: [ERROR] Flight_Logs - Page_15
Field: passengers.identified[2]
Current: "John Doe"
Correct: "Jane Doe"
Evidence: Matching signature on page 23, confirmed by external source
```

### 2. Submitting Corrections via Pull Request

#### Setup
1. Fork the repository
2. Clone your fork locally
3. Create a feature branch: `git checkout -b fix/document-page-field`

#### Making Changes
1. Locate the JSON file in `data/extracted/`
2. Make your correction
3. Update the `validation` section:
   ```json
   "validation": {
     "manual_review": true,
     "reviewer": "your-github-username",
     "review_date": "2024-10-11",
     "changes": ["corrected passenger name spelling"]
   }
   ```

#### Submission
1. Commit with clear message: `Fix: Correct [field] in [document] page [number]`
2. Push to your fork
3. Create Pull Request with:
   - Clear description of changes
   - Evidence/reasoning for corrections
   - Any relevant issue numbers

### 3. OSINT Research Guidelines

When researching entities mentioned in documents:

#### Acceptable Research
✅ Public records and databases
✅ Published news articles
✅ Academic publications
✅ Corporate registrations
✅ Public social media profiles
✅ Government databases

#### Research Standards
1. **Verification**: Cross-reference minimum 2 sources
2. **Documentation**: Provide links to sources
3. **Objectivity**: Report facts only, no speculation
4. **Privacy**: Respect privacy of non-public figures
5. **Relevance**: Focus on network connections, not personal details

#### Hierarchical Research Approach
When researching individuals:
1. **Tier 1**: Name, professional affiliations, public roles
2. **Tier 2**: Business relationships, organizational memberships
3. **Tier 3**: Public event attendance, documented connections
4. **Out of Scope**: Personal life, family (unless publicly relevant), speculation

### 4. Data Validation Contributions

Help validate existing extractions:

#### Validation Process
1. Select unvalidated pages (check `validation.manual_review = false`)
2. Compare JSON against source PNG
3. Document findings:
   - ✅ Confirmed accurate
   - ⚠️ Minor issues (list them)
   - ❌ Major issues (detail required)

#### Validation Checklist
- [ ] All visible names extracted
- [ ] Phone numbers correctly formatted
- [ ] Dates properly inferred
- [ ] Email addresses complete
- [ ] Addresses include all visible parts
- [ ] Signatures identification attempted
- [ ] Cross-references noted

### 5. Code of Conduct

#### Required Behavior
- **Accuracy First**: Never guess or fabricate data
- **Evidence-Based**: All corrections need supporting evidence
- **Respectful**: Professional discourse only
- **Objective**: No editorializing or personal opinions
- **Collaborative**: Work with other contributors

#### Prohibited Behavior
- ❌ Doxxing or harassment
- ❌ Speculation presented as fact
- ❌ Malicious or false corrections
- ❌ Copyright violations
- ❌ Personal attacks or discrimination

## Quality Standards

### For Data Corrections
- Must improve accuracy demonstrably
- Include evidence or clear reasoning
- Maintain consistent JSON structure
- Update metadata appropriately

### For New Extractions
- Follow [EXAMPLE-CLAUDE.md](EXAMPLE-CLAUDE.md) guidelines
- Minimum 5 entities per content page
- Attempt all signature identifications
- Include confidence scores
- Document uncertainty appropriately

### For OSINT Contributions
- Minimum 2 source verification
- Public information only
- Network-relevant data focus
- Clear source attribution

## Review Process

1. **Automated Checks**: JSON validation, schema compliance
2. **Peer Review**: Community verification of changes
3. **Maintainer Review**: Final approval and merge
4. **Post-Merge**: Added to validation tracking

## Recognition

Contributors are recognized in:
- [CONTRIBUTORS.md](CONTRIBUTORS.md) - All contributors
- Commit history - Individual contributions
- JSON metadata - Reviewer attribution

## Getting Help

- **Questions**: Open an issue with `[QUESTION]` tag
- **Discussion**: Use GitHub Discussions
- **Guidelines**: Review [EXAMPLE-CLAUDE.md](EXAMPLE-CLAUDE.md)
- **Status**: Check [DATA_STATUS.md](DATA_STATUS.md)

## Priorities

Current priority areas needing contribution:
1. **Flight Logs v2**: Pages 9-38 need extraction/validation
2. **Black Book v2**: Pages 82-95 need extraction
3. **Birthday Book v2**: Pages 12-137 need manual review
4. **Cross-referencing**: Entity matching across documents
5. **Name Standardization**: Resolving variations and aliases

## Tools and Resources

### Recommended Tools
- JSON validators and formatters
- Image viewers with zoom capability
- Text comparison tools
- Git GUI clients (optional)

### Useful Resources
- [Original Documents](data/source/) - PNG images
- [External Sources](data/external_sources/) - Third-party data
- [Extraction Guidelines](EXAMPLE-CLAUDE.md) - Methodology
- [Data Status](DATA_STATUS.md) - Current progress

---

*By contributing, you agree to uphold the quality standards and code of conduct outlined above. Your efforts help build a more accurate and complete knowledge graph for network analysis.*
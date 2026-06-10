# Research Repository

This directory stores research briefs compiled by the Research Assistant skill for jonbeckett.com blog articles.

## Directory Structure

```
docs/research/
├── README.md                          ← this file
└── YYYY/
    └── YYYY-MM-DD-topic-slug/        ← one folder per article topic
        ├── RESEARCH-BRIEF.md          ← compiled research brief
        └── sources.json               ← raw source metadata
```

## Conventions

### Folder Naming
Research folders follow the blog post slug pattern: `YYYY-MM-DD-topic-slug`
- Date matches the planned publication date or research date
- Slug is lowercase with hyphens, matching the eventual blog post filename

### Research Brief (`RESEARCH-BRIEF.md`)
All research briefs MUST follow the standard template defined in `.cline/skills/research-assistant/SKILL.md`:
- Executive Summary
- Key Facts (with source table)
- Expert Opinions (with quotes and attribution)
- Statistics and Data
- Historical Timeline
- Counterpoints
- Gaps and Limitations
- Suggested Article Structure
- Source Bibliography

### Source Metadata (`sources.json`)
Machine-readable source catalog for each research project:

```json
{
  "topic": "Article topic",
  "researchDate": "YYYY-MM-DD",
  "sources": [
    {
      "title": "Source title",
      "authors": ["Author Name"],
      "publication": "Publication Name",
      "url": "https://...",
      "accessedDate": "YYYY-MM-DD",
      "type": "primary|secondary|tertiary"
    }
  ]
}
```

## Usage

When the Research Assistant skill is engaged for a new article topic:

1. Create `docs/research/YYYY/YYYY-MM-DD-topic-slug/` directory
2. Compile research into `RESEARCH-BRIEF.md` using the standard template
3. Record all sources in `sources.json`
4. Flag any unverified claims in "Gaps and Limitations"

## Existing Research

_No research briefs stored yet._
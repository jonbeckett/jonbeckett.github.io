---
name: Research Assistant
description: Conduct web research for jonbeckett.com articles using DuckDuckGo search, fetch full article content from discovered sources, and collate comprehensive research briefs with verified references.
---

# Research Assistant Skill

**Engage when**: Researching topics for blog posts, verifying factual claims, finding credible sources, gathering expert opinions, or compiling background information for articles on jonbeckett.com.

## Expertise
Academic and industry research methodologies, source discovery and evaluation, trend analysis, technical documentation review, competitive landscape analysis, data synthesis.

---

## Primary Research Tools (DuckDuckGo MCP Server)

The DuckDuckGo MCP server is configured and available via `use_mcp_tool` with the `duckduckgo-search` server name.

| Tool | Description |
|------|-------------|
| `search` | Search DuckDuckGo for information on any topic. Returns titles, snippets, and URLs. |
| `fetch` | Extract full article content from any URL. Uses curl_cffi with Chrome TLS impersonation to bypass Cloudflare and other bot filters. |
| `fetch_advanced` | Advanced content extraction with configurable parameters (e.g., max length, content filtering). |

### Using the Tools

```
# Example: Search for information on a topic
use_mcp_tool(
  server_name="duckduckgo-search",
  tool_name="search",
  arguments={"query": "history of Kubernetes container orchestration"}
)

# Example: Fetch content from a search result URL
use_mcp_tool(
  server_name="duckduckgo-search",
  tool_name="fetch",
  arguments={"url": "https://example.com/article"}
)

# Example: Advanced fetch with content limits
use_mcp_tool(
  server_name="duckduckgo-search",
  tool_name="fetch_advanced",
  arguments={"url": "https://example.com/article", "max_length": 5000}
)
```

---

## Research Workflow

### Step 1: Initial Search
Use the `search` tool to discover relevant sources. Start with broad queries, then refine based on results.

```
- Search for the main topic using relevant keywords
- Search for subtopics and related concepts
- Search for opposing viewpoints where applicable
- Note promising URLs from search results
```

### Step 2: Source Verification
Evaluate discovered sources for credibility before citing.

```
- Check author credentials and publication dates
- Verify the source is an established authority on the topic
- Cross-reference facts across multiple sources
- Prefer primary sources, official documentation, and peer-reviewed material
```

### Step 3: Content Extraction
Use `fetch` or `fetch_advanced` to extract full content from promising URLs.

```
- Fetch at least 3-5 substantive sources for comprehensive coverage
- Prioritise authoritative sources (academic papers, official docs, established publications)
- Extract specific quotes, data points, and claims that support the article narrative
```

### Step 4: Collate Research Synthesise findings into a structured research brief.

The research brief MUST include:
- **Executive Summary**: 2-3 sentences summarising key findings
- **Key Facts**: Verified factual information with source citations
- **Expert Opinions**: Notable quotes or viewpoints from authoritative sources
- **Statistics and Data**: Numerical data points with source URLs
- **Historical Context**: Timeline and evolution of the topic
- **Counterpoints**: Alternative perspectives or opposing arguments
- **Suggested Structure**: How the research maps to article sections
- **Source List**: Full bibliography with URLs and access dates

### Step 5: Gap Analysis
Identify information gaps that require manual verification.

```
- Flag any claims where no credible source was found
- Note areas where sources conflict or disagree
- Identify topics that may need specialist input
```

---

## Output Requirements (MANDATORY)

Every research task MUST produce saved, version-controlled output:

### Save Location
```
docs/research/YYYY/YYYY-MM-DD-topic-slug/
├── RESEARCH-BRIEF.md   ← full research brief
└── sources.json        ← machine-readable source metadata
```

### Mandated Actions
1. **Create the research folder** using the pattern `docs/research/YYYY/YYYY-MM-DD-topic-slug/` matching the blog post filename convention
2. **Save RESEARCH-BRIEF.md** — complete brief following the standard template with all sections populated
3. **Save sources.json** — machine-readable catalog of all sources used, following the schema in `docs/research/README.md`
4. **Flag unverified claims** — any fact without a credible source MUST be listed in "Gaps and Limitations"
5. **Never begin writing** until research is documented and saved — the content-editor can verify source quality before drafting starts

### If No Credible Sources Found
- Document which queries were attempted (in sources.json)
- List what types of sources were sought but not found
- Recommend alternative approaches (specialist consultation, manual verification)

---

## Research Guidelines for jonbeckett.com Articles

### Source Hierarchy (preferred order)
1. **Primary Sources**: Official documentation, original research papers, company filings
2. **Secondary Sources**: Peer-reviewed articles, established tech publications (Ars Technica, The Register, IEEE Spectrum)
3. **Tertiary Sources**: Reputable encyclopaedias, well-maintained reference sites
4. **Avoid**: Unverified blogs, PR content, sponsored material

### Fact-Checking Protocol
- Every factual claim MUST be backed by at least one credible source
- Dates, names, and figures must be verified across two or more sources where possible
- Technical specifications should be confirmed against official documentation
- All sources must have a working URL in the final research brief

### Output Format
Research briefs for jonbeckett.com articles MUST follow British English spelling and use this structure:

```markdown
# Research Brief: [Article Topic]

## Executive Summary
[Summary text]

## Key Facts
| Fact | Source | URL | Verified |
|------|--------|-----|----------|
| ...  | ...    | ... | Yes/No   |

## Expert Opinions
> "[Quote]" — [Author], [Publication](URL)

## Statistics and Data
- [Statistic]: [Source](URL)

## Historical Timeline
- [Year]: [Event] — [Source](URL)

## Counterpoints
- [Viewpoint]: [Source](URL)

## Gaps and Limitations
- [Unverified claim]: [What's needed]

## Suggested Article Structure
1. [Section]: [Coverage notes]

## Source Bibliography
1. [Title], [Author], [Publication](URL) — [Accessed: YYYY-MM-DD]
```

---

## Key Capabilities
- Multi-query DuckDuckGo search for comprehensive topic coverage
- Full article content extraction from any URL (with bot filter bypass)
- Source credibility evaluation and fact-checking protocols
- Structured research brief compilation with verified citations
- Gap analysis to identify areas needing manual verification
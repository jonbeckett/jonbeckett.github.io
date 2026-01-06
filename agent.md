# Agent Guide for Writing Blog Posts

This guide provides comprehensive instructions for AI agents writing posts for jonbeckett.com. Follow these guidelines to maintain consistency with the established style, structure, and quality standards.

## Content Quality Standards

### Depth and Comprehensiveness
- Posts should be **substantial** (2,000-5,000+ words)
- Provide **comprehensive coverage** of the topic from multiple angles
- Include **historical context** and evolution where relevant
- Offer **practical applications** and real-world examples
- Present **forward-looking perspectives** and future implications
- Balance **analytical depth** with **accessibility**

### Writing Style
- **Professional yet approachable** tone
- **Analytical and thoughtful** approach to complex topics
- **Personal insights** and commentary woven throughout
- **Clear structure** with logical flow between sections
- **Evidence-based** arguments with specific examples
- **Balanced perspectives** acknowledging trade-offs and limitations

## Post Structure Template

### Required Front Matter
```yaml
---
title: "Post Title: Descriptive Subtitle"
layout: single
date: YYYY-MM-DD
categories:
  - primary-category
  - secondary-category
tags:
  - tag1
  - tag2
  - tag3
  - tag4
  - tag5
excerpt: "A compelling 1-2 sentence summary that captures the essence and value proposition of the post."
---
```

### Header Images from Unsplash
For posts requiring banner images, add a header section with Unsplash images:

```yaml
header:
  overlay_image: "https://images.unsplash.com/photo-[PHOTO-ID]?w=1200&h=400&fit=crop&crop=entropy&auto=format&q=80"
  overlay_filter: "linear-gradient(90deg, rgba(0,0,0,0.6) 0%, rgba(0,0,0,0.3) 100%)"
  caption: "Photo by [Photographer Name](https://unsplash.com/@username) on [Unsplash](https://unsplash.com)"
  teaser: "https://images.unsplash.com/photo-[PHOTO-ID]?w=600&h=300&fit=crop&crop=entropy&auto=format&q=80"
```

**Important Notes:**
- Use the **same photo ID** for both `overlay_image` and `teaser` fields
- The `overlay_image` uses 1200x400 dimensions for the full-width banner
- The `teaser` uses 600x300 dimensions for homepage/archive listings
- Always include proper attribution in the `caption` field
- Use `overlay_filter: "linear-gradient(90deg, rgba(0,0,0,0.6) 0%, rgba(0,0,0,0.3) 100%)"` for consistent gradient overlay
- Search for images that relate to your post topic but avoid overly literal matches
- Choose high-quality, professional photos that complement the content

### Extracting Photo URLs from Unsplash Pages

When given an Unsplash page URL (e.g., `https://unsplash.com/photos/description-PHOTO_ID`), you need to extract the correct photo ID for the images.unsplash.com URL format:

**Common Photo ID Formats:**
- Standard format: `photo-1234567890123-abcdef123456` (numeric timestamp + alphanumeric)
- Working examples from the site:
  - `photo-1461749280684-dccba630e2f6` (programming/coding)
  - `photo-1555066931-4365d14bab8c` (technology)
  - `photo-1517842645767-c639042777db` (productivity)

**How to Find the Correct Photo ID:**
1. **From Unsplash Page URL**: The ID at the end may not be the correct format
2. **Fetch the page content** using tools to find the actual image URL
3. **Look for img src URLs** that contain `images.unsplash.com/photo-[ID]`
4. **Extract the photo ID** from those URLs (the part after `photo-`)

**Troubleshooting Photo URLs:**
- If a photo URL doesn't work, it may be a premium/plus image with different ID format
- Premium images use `premium_photo-` prefix and won't work with standard format
- Find alternative similar-themed images with standard IDs that work
- Test the URL by checking if `https://images.unsplash.com/photo-[ID]` loads

**URL Parameters to Use:**
- Banner: `?w=1200&h=400&fit=crop&crop=entropy&auto=format&q=80`
- Teaser: `?w=600&h=300&fit=crop&crop=entropy&auto=format&q=80`
- These parameters ensure optimal sizing and quality for the site

### Standard Post Structure
```markdown
# Post Title: Descriptive Subtitle

Opening paragraph that hooks the reader and establishes context. Should immediately communicate why this topic matters and what the reader will gain.

---

## Introduction/Background Section
- Historical context or evolution
- Why this topic is relevant now
- Key challenges or problems addressed

## Core Content Sections (3-6 major sections)
### Section Title
Detailed exploration of key concepts, methodologies, or technologies.

### Another Section Title
Continue building understanding with examples and analysis.

---

## Practical Applications
- Real-world implementations
- Case studies or examples
- Best practices and recommendations

## Challenges and Considerations
- Common pitfalls
- Limitations and trade-offs
- When to use vs. avoid

## Future Outlook
- Emerging trends
- Potential developments
- Long-term implications

## Conclusion
- Summary of key insights
- Actionable takeaways
- Final thoughts on broader implications

---
```

## Content Categories and Focus Areas

### Productivity and Personal Systems
- **Focus**: Methodologies, tools, and systems for personal effectiveness
- **Examples**: GTD, note-taking systems, bullet journaling, time management
- **Approach**: Balance theory with practical implementation guidance

### Technology and Software Development
- **Focus**: Enterprise technology, development practices, and industry trends
- **Examples**: Cloud platforms, programming languages, development methodologies
- **Approach**: Technical depth with business context and practical implications

### Tools and Methodologies
- **Focus**: Specific tools, frameworks, and systematic approaches
- **Examples**: Version control, testing frameworks, productivity tools
- **Approach**: Historical evolution, current best practices, future directions

## British English Spelling Requirements

**CRITICAL**: All posts must use British English spellings exclusively. Common conversions include:

### -ise/-isation endings (NOT -ize/-ization)
- organise, organisation, recognise, realise, specialise
- optimise, optimisation, customise, customisation
- analyse, analyse, utilise, summarise, categorise

### -our endings (NOT -or)
- behaviour, colour, honour, favour, labour, humour
- rigour, vigour, harbour, flavour, endeavour

### -re endings (NOT -er)
- centre, theatre, metre, litre, fibre, calibre

### -ce endings for nouns (NOT -se)
- licence (noun), defence, offence, practice (noun)
- Note: license/practise are verbs, licence/practice are nouns

### Other important conversions
- analogue (NOT analog), catalogue, dialogue
- grey (NOT gray), tyre (NOT tire)
- focussed (NOT focused), travelled (NOT traveled)
- materialise (NOT materialize), digitise (NOT digitize)

### Verification checklist
Before publishing, search for and correct these American spellings:
- Words ending in -ize, -ization, -or (when should be -our), -er (when should be -re)
- Common words: center, defense, license (noun), realize, organize, analyze, optimize

## Section Development Guidelines

### Historical Context Sections
- Trace the evolution of the topic over time
- Identify key milestones and turning points
- Explain how past developments led to current state
- Use specific dates, names, and events where relevant

### Technical Explanation Sections
- Start with fundamental concepts before advancing to complexity
- Use analogies and examples to clarify abstract concepts
- Include code examples or practical demonstrations when appropriate
- Explain the "why" behind technical decisions, not just the "how"

### Practical Application Sections
- Provide specific, actionable guidance
- Include step-by-step processes where helpful
- Address common implementation challenges
- Offer troubleshooting advice for typical problems

### Analysis and Commentary Sections
- Present multiple perspectives on controversial topics
- Acknowledge limitations and trade-offs honestly
- Support arguments with evidence and examples
- Connect local insights to broader industry trends

## Tone and Voice Guidelines

### Professional but Personal
- Write as an experienced practitioner sharing insights
- Include personal observations and lessons learned
- Maintain authority without being prescriptive
- Acknowledge uncertainty and areas of ongoing debate

### Analytical and Thoughtful
- Present evidence-based arguments
- Consider multiple angles and perspectives
- Identify underlying principles and patterns
- Connect specific examples to broader themes

### Accessible Expertise
- Explain complex concepts clearly without oversimplifying
- Define technical terms when first introduced
- Use analogies and real-world examples
- Assume intelligent but not necessarily specialist audience

## Quality Assurance Checklist

### Content Quality
- [ ] Post exceeds 2,000 words with substantial depth
- [ ] Includes historical context and evolution
- [ ] Provides practical applications and examples
- [ ] Offers forward-looking perspective
- [ ] Balances multiple viewpoints fairly

### Structure and Organisation
- [ ] Follows standard template structure
- [ ] Uses horizontal rules (---) to separate major sections
- [ ] Has clear, descriptive headings and subheadings
- [ ] Maintains logical flow between sections
- [ ] Includes compelling introduction and conclusion

### Language and Style
- [ ] Uses British English spellings exclusively
- [ ] Maintains professional yet approachable tone
- [ ] Includes personal insights and commentary
- [ ] Supports arguments with evidence and examples
- [ ] Explains technical concepts clearly

### Technical Requirements
- [ ] Proper YAML front matter with all required fields
- [ ] Title matches main heading exactly
- [ ] Appropriate categories and tags assigned
- [ ] Compelling excerpt written
- [ ] Markdown formatting correct throughout

## Site Configuration Requirements

### Category and Tag Archives
**CRITICAL**: This site is hosted on GitHub Pages, which does NOT support the `jekyll-archives` plugin. The site configuration MUST use the Liquid method for category and tag archives:

```yaml
# CORRECT configuration for GitHub Pages
category_archive:
  type: liquid
  path: /categories/
tag_archive:
  type: liquid  
  path: /tags/

# NEVER use jekyll-archives on GitHub Pages (will break links)
# jekyll-archives:
#   enabled:
#     - categories
#     - tags
```

**Important Notes:**
- Using `type: jekyll-archives` will break all category and tag links site-wide
- The `liquid` method creates anchor links like `/categories/#productivity` and `/tags/#gtd`
- Category and tag pages use anchor links within the same page, not separate pages
- Do NOT modify the archive configuration in `_config.yml` without understanding the implications

## Research and Fact-Checking

### Source Requirements
- Verify historical dates, names, and events
- Cross-reference technical specifications and capabilities
- Ensure currency of information about evolving technologies
- Cite or reference authoritative sources where appropriate

### Accuracy Standards
- Double-check technical details and specifications
- Verify compatibility information and version numbers
- Confirm current status of projects, companies, and initiatives
- Validate code examples and implementation details

## Publishing Considerations

### SEO and Discoverability
- Use descriptive, search-friendly titles
- Include relevant keywords naturally in content
- Create compelling excerpts that encourage clicks
- Use appropriate heading structure (H1, H2, H3)

### Reader Experience
- Break up long sections with subheadings
- Use lists and bullet points for scannable content
- Include practical examples and case studies
- Provide clear takeaways and action items

### Maintenance
- Consider longevity of information provided
- Flag areas that may require future updates
- Provide context that will remain relevant over time
- Include timeless principles alongside current practices

---

## Example Categories and Tags

### Common Categories
- productivity, technology, software-development, tools, methodology
- microsoft, cloud, programming, testing, version-control
- note-taking, planning, workflow, automation

### Tag Examples
- gtd, zettelkasten, bullet-journal, productivity, workflow
- azure, github, linux, programming-languages, tdd
- ai, enterprise, development, testing, methodology

---

This guide ensures consistency, quality, and adherence to British English standards across all blog posts. Refer to existing posts for additional examples of successful implementation of these guidelines.
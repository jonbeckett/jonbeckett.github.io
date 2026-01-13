# GitHub Copilot Instructions for jonbeckett.com

This is a personal technology blog focusing on software development, productivity, and technology evolution. The site is built with Jekyll and uses the Minimal Mistakes theme, hosted on GitHub Pages.

## Project Overview

**Author**: Jonathan Beckett  
**Tech Stack**: Jekyll, Minimal Mistakes theme, GitHub Pages  
**Content Focus**: Software development, productivity, technology evolution, AI/ML, enterprise technology  
**Deployment**: Automated via GitHub Actions to GitHub Pages

## Blog Post Structure

### File Naming Convention
All blog posts must follow this exact naming pattern:
```
_posts/YYYY/YYYY-MM-DD-slug-title.md
```

- Posts are organized by year in subdirectories under `_posts/`
- Date format: `YYYY-MM-DD` (e.g., `2026-01-13`)
- Slug: lowercase with hyphens, descriptive and SEO-friendly
- Extension: `.md` (Markdown)

**Examples**:
- `_posts/2026/2026-01-13-kubernetes-evolution.md`
- `_posts/2026/2026-01-14-testing-strategies-modern-web.md`

### Front Matter Template

Every blog post MUST start with YAML front matter using this exact structure:

```yaml
---
title: "Main Title: Subtitle for Context"
layout: single
date: YYYY-MM-DD
categories:
  - primary-category
  - secondary-category
tags:
  - tag1
  - tag2
  - tag3
excerpt: "A compelling one-sentence description that appears in post previews and social media shares. Should be engaging and informative."
header:
  overlay_image: "https://images.unsplash.com/photo-[ID]?w=1200&h=400&fit=crop&crop=entropy&auto=format&q=80"
  overlay_filter: "linear-gradient(90deg, rgba(0,0,0,0.9) 0%, rgba(0,0,0,0.5) 100%)"
  caption: "Photo by [Photographer Name](https://unsplash.com/@photographer) on [Unsplash](https://unsplash.com)"
  teaser: "https://images.unsplash.com/photo-[ID]?w=600&h=300&fit=crop&crop=entropy&auto=format&q=80"
---
```

**Front Matter Guidelines**:
- **title**: Use quotation marks, can include colons and subtitles
- **layout**: Always `single` for blog posts
- **date**: Format as `YYYY-MM-DD` (must match filename date)
- **categories**: 1-3 categories, lowercase with hyphens
- **tags**: 3-6 relevant tags, lowercase with hyphens
- **excerpt**: Single sentence, 120-200 characters, compelling summary
- **header images**: Use Unsplash images with proper attribution
  - overlay_image: 1200x400px for desktop
  - teaser: 600x300px for thumbnails
  - Always include photographer credit in caption

**Common Categories**:
- artificial-intelligence
- enterprise
- software-development
- productivity
- web-development
- cloud-computing
- devops
- testing
- automation

## Writing Style Guidelines

### Voice and Tone
- **Perspective**: First person plural ("we") or third person analytical
- **Tone**: Professional but accessible, technical yet readable
- **Style**: Narrative-driven with technical depth
- **Balance**: Blend storytelling with technical analysis

### Content Depth and Length
- **Target Length**: 2,000-5,000+ words for substantive posts
- **Comprehensiveness**: Provide comprehensive coverage from multiple angles
- **Historical Context**: Include evolution and background where relevant
- **Practical Applications**: Offer real-world examples and implementations
- **Forward-Looking**: Present future implications and emerging trends
- **Evidence-Based**: Support arguments with specific examples and data

### Content Structure
1. **Opening Hook**: Start with a compelling scenario or observation
2. **Historical Context**: Often includes technology evolution and history
3. **Technical Deep Dive**: Detailed explanations with code/architecture examples
4. **Practical Applications**: Real-world implications and use cases
5. **Future Outlook**: Forward-looking analysis and predictions

### Technical Writing Standards
- Use code blocks with proper syntax highlighting (```language)
- Include detailed technical explanations when discussing concepts
- Reference specific technologies, companies, and products accurately
- Provide architectural context for technical decisions
- Include performance implications and trade-offs
- Use proper Markdown formatting throughout

### Stylistic Patterns
- Often references science fiction (Blade Runner, Philip K. Dick) for metaphorical context
- Uses vivid, sometimes poetic language alongside technical precision
- Employs section headers with descriptive, engaging titles
- Includes historical timelines and evolution of technologies
- Balances optimism with critical analysis

### Markdown Formatting
- Use `##` for main sections (H2)
- Use `###` for subsections (H3)
- Use `####` sparingly for sub-subsections
- Emphasis: `**bold**` for strong emphasis, `*italic*` for subtle emphasis
- Code: `` `inline code` `` for commands, variables, file names
- Lists: Use `-` for unordered lists, maintain consistent indentation
- Links: Use descriptive link text, not "click here"

### British English Spelling (REQUIRED)

**CRITICAL**: All posts MUST use British English spellings exclusively.

**Common -ise/-isation endings** (NOT -ize/-ization):
- organise, organisation, recognise, realise, specialise
- optimise, optimisation, customise, customisation
- analyse, utilise, summarise, categorise, materialise, digitise

**-our endings** (NOT -or):
- behaviour, colour, honour, favour, labour, humour
- rigour, vigour, harbour, flavour, endeavour

**-re endings** (NOT -er):
- centre, theatre, metre, litre, fibre, calibre

**-ce endings for nouns** (NOT -se):
- licence (noun), defence, offence, practice (noun)
- Note: license/practise are verbs, licence/practice are nouns

**Other important British spellings**:
- analogue (NOT analog), catalogue, dialogue
- grey (NOT gray), tyre (NOT tire)
- focussed (NOT focused), travelled (NOT traveled)

**Verification Checklist**:
Before publishing, search for and correct these American spellings:
- Words ending in -ize, -ization
- Words ending in -or when should be -our
- Words ending in -er when should be -re
- Common words: center, defense, license (noun), realize, organize, analyze, optimize

## Common Patterns to Follow

### Opening Paragraph Pattern
Start with an engaging scenario or observation that sets up the topic:
```markdown
In the sprawling headquarters of a Fortune 500 company, something remarkable 
is happening. Hundreds of AI agents are working around the clock...
```

### Historical Context Pattern
Include evolution and historical perspective:
```markdown
## The Promethean Fire: Turing's Vision (1940s-1950s)

In 1950, Alan Turing published a paper that would echo through decades...
```

### Technical Explanation Pattern
Provide deep technical detail with context:
```markdown
The breakthrough came with brute force tree searching—the computer equivalent 
of exploring every possible future simultaneously. But the real algorithmic 
revolution was alpha-beta pruning...
```

### Code Example Pattern
When including code, provide context and explanation:
````markdown
The implementation relies on TypeScript's type system:

```typescript
interface AgentConfig {
  name: string;
  capabilities: string[];
  model: ModelType;
}
```

This approach ensures type safety while maintaining flexibility...
````

## Image Guidelines

### Unsplash Images
- Always use Unsplash for header images
- Format: `https://images.unsplash.com/photo-[ID]?w=[width]&h=[height]&fit=crop&crop=entropy&auto=format&q=80`
- Required sizes:
  - overlay_image: w=1200&h=400
  - teaser: w=600&h=300
- Always include photographer attribution in caption
- Use high-quality, relevant images that match post theme

### Extracting Photo IDs from Unsplash Pages

When given an Unsplash page URL (e.g., `https://unsplash.com/photos/description-PHOTO_ID`), extract the correct photo ID:

**Photo ID Format**:
- Standard format: `photo-1234567890123-abcdef123456` (numeric timestamp + alphanumeric)
- Working examples from existing posts:
  - `photo-1461749280684-dccba630e2f6`
  - `photo-1555066931-4365d14bab8c`
  - `photo-1517842645767-c639042777db`

**How to Find the Correct Photo ID**:
1. The ID in the Unsplash page URL may not be the correct format
2. Fetch the page content to find the actual image URL
3. Look for `img src` URLs containing `images.unsplash.com/photo-[ID]`
4. Extract the photo ID from those URLs (the part after `photo-`)

**Troubleshooting Photo URLs**:
- If a photo URL doesn't work, it may be a premium/plus image
- Premium images use `premium_photo-` prefix and won't work with standard format
- Find alternative similar-themed images with standard IDs
- Always verify the URL loads: `https://images.unsplash.com/photo-[ID]`

**URL Parameters**:
- Banner: `?w=1200&h=400&fit=crop&crop=entropy&auto=format&q=80`
- Teaser: `?w=600&h=300&fit=crop&crop=entropy&auto=format&q=80`

### Image Selection Criteria
- Choose images that visually represent the topic
- Prefer abstract, technology-themed, or conceptual images
- Ensure images work well with dark gradient overlay
- Avoid overly literal interpretations
- Search for high-quality, professional photos
- Verify image loads before using

## File Organization

```
_posts/
  └── YYYY/
      ├── YYYY-MM-DD-post-slug.md
      └── YYYY-MM-DD-another-post.md
_pages/
  ├── about.md
  ├── categories.md
  ├── posts.md
  └── tags.md
_data/
  └── navigation.yml
_includes/
  └── head/
      └── custom.html
assets/
  ├── css/
  │   └── main.scss
  └── images/
```

## Common Commands

### Local Development
```bash
# Install dependencies
bundle install

# Serve locally
bundle exec jekyll serve

# Serve with drafts
bundle exec jekyll serve --drafts

# Build site
bundle exec jekyll build
```

### Creating New Posts
1. Create file in `_posts/YYYY/` following naming convention
2. Add complete front matter
3. Write content following style guidelines
4. Find appropriate Unsplash image
5. Test locally before committing

## Jekyll Configuration Notes

- Theme: Minimal Mistakes (remote theme)
- Layout: Use `layout: single` for all posts
- Breadcrumbs: Enabled site-wide
- Comments: Currently disabled (can enable Giscus if needed)
- Analytics: Google Analytics configured

### Category and Tag Archives (CRITICAL)

**IMPORTANT**: This site uses GitHub Pages, which does NOT support the `jekyll-archives` plugin.

The site MUST use the Liquid method for category and tag archives:

```yaml
# CORRECT configuration for GitHub Pages
category_archive:
  type: liquid
  path: /categories/
tag_archive:
  type: liquid  
  path: /tags/
```

**Do NOT modify to use jekyll-archives**:
- Using `type: jekyll-archives` will break all category and tag links site-wide
- The `liquid` method creates anchor links like `/categories/#productivity` and `/tags/#gtd`
- Category and tag pages use anchor links within the same page, not separate pages
- Never change the archive configuration in `_config.yml` without understanding implications

## SEO Best Practices

- Write descriptive, keyword-rich titles
- Create compelling excerpts (shown in search results)
- Use relevant categories and tags
- Include meta descriptions via excerpt
- Use descriptive file names (slug becomes URL)
- Ensure headers create logical hierarchy

## Avoid These Common Mistakes

❌ **Don't**:
- Create posts without proper front matter
- Use incorrect file naming convention
- Skip Unsplash image attribution
- Write generic, SEO-keyword-stuffed content
- Use inconsistent Markdown formatting
- Include posts outside year subdirectories
- Forget to test locally before committing

✅ **Do**:
- Follow the established naming convention exactly
- Include complete, properly formatted front matter
- Write narrative-driven, technically accurate content
- Use proper Markdown and code formatting
- Include relevant images with attribution
- Organize posts by year in subdirectories
- Maintain consistent voice and style

## Author Context

Jonathan Beckett is a software/web developer with expertise in:
- Microsoft ecosystem (document/content management, PowerShell, Power Automate)
- Modern JavaScript/TypeScript development
- BDD with Cucumber/Gherkin
- Web automation with Playwright
- DevOps and pipeline optimization
- Linux and open source software background
- Creator of early blogging platform

When suggesting content or code examples, draw from these areas of expertise while maintaining the established writing style.

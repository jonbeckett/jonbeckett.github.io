# Content Creation Rules

## Blog Post File Naming Convention
All blog posts MUST follow this exact naming pattern:
```
_post/YYYY/YYYY-MM-DD-slug-title.md
```
- Posts are organized by year in subdirectories under `_posts/`
- Date format: `YYYY-MM-DD` (e.g., `2026-01-13`)
- Slug: lowercase with hyphens, descriptive and SEO-friendly
- Extension: `.md` (Markdown)

**Examples**:
- `_posts/2026/2026-01-13-kubernetes-evolution.md`
- `_posts/2026/2026-01-14-testing-strategies-modern-web.md`

## Front Matter Template
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
  og_image:      "https://images.unsplash.com/photo-[ID]?w=1200&h=630&fit=crop&crop=entropy&auto=format&q=80"
  overlay_filter: "linear-gradient(90deg, rgba(0,0,0,0.9) 0%, rgba(0,0,0,0.5) 100%)"
  caption: "Photo by [Photographer Name](https://unsplash.com/@photographer) on [Unsplash](https://unsplash.com)"
  teaser: "https://images.unsplash.com/photo-[ID]?w=600&h=300&fit=crop&crop=entropy&auto=format&q=80"
---
```

## Front Matter Guidelines
- **title**: Use quotation marks, can include colons and subtitles
- **layout**: Always `single` for blog posts
- **date**: Format as `YYYY-MM-DD` (must match filename date)
- **categories**: 1-3 categories, lowercase with hyphens
- **tags**: 3-6 relevant tags, lowercase with hyphens
- **excerpt**: Single sentence, 120-200 characters, compelling summary
- **header images**: Use Unsplash images with proper attribution
  - overlay_image: 1200x400px for desktop headers
  - og_image: 1200x630px for social media sharing (LinkedIn, Facebook, Twitter) — uses same photo ID as overlay_image
  - teaser: 600x300px for thumbnails and archive listings
  - Always include photographer credit in caption

## Common Categories
- artificial-intelligence
- enterprise
- software-development
- productivity
- web-development
- cloud-computing
- devops
- testing
- automation

## Content Creation Standards
- **Length**: 2,000-5,000+ words for comprehensive coverage
- **Structure**: Hook → History → Technical → Applications → Future
- **Language**: British English spelling exclusively
- **Tone**: Professional but accessible, narrative-driven with technical depth

## Required Content Elements
- Opening hook: Compelling scenario or observation
- Historical context: Evolution and background of the topic
- Technical explanations: Detailed analysis with code/architecture examples
- Practical applications: Real-world implications and use cases
- Future outlook: Forward-looking analysis and predictions
- Code examples: Proper syntax highlighting and context

## Pre-Publication Checklist
1. YAML front matter is valid and complete
2. File naming convention is followed exactly
3. Images load correctly from Unsplash
4. Local build succeeds without errors (`bundle exec jekyll serve`)
5. All internal links are valid
6. British English spelling is used throughout

## Header Image Options - CRITICAL FIX

**Option A: Local banner images (RECOMMENDED for reliability)**
- Place custom banner images in `assets/images/banners/` directory
- Banner dimensions should be 1200x400px minimum
- Reference using relative path: `/assets/images/banners/banner-X.jpg`
- These are always available and never return 404

**Option B: Valid Unsplash images (use with caution)**
- Find suitable free Unsplash images relevant to article topic at unsplash.com
- To extract the correct photo ID: visit the Unsplash photo page and copy the ID from the URL (format: `photo-[timestamp]-[alphanumeric]`, e.g., `photo-1515879218367-8466d910aaa4`)
- NEVER invent random photo IDs — they will return 404 errors
- Always verify the image URL loads correctly in a browser before including it in a blog post
- Use same photo ID across all image size variations (overlay, OG, teaser)
- Always include photographer credit in caption with link to photographer's Unsplash profile

**CRITICAL**: Always test header image URLs load before committing. Invalid/made-up Unsplash photo IDs are the #1 source of broken header images.

## Image URL Configuration (Unsplash only)
| Purpose | Dimensions | URL Pattern |
|---------|------------|-------------|
| Header overlay | 1200x400 | `?w=1200&h=400&fit=crop&crop=entropy&auto=format&q=80` |
| Social media (OG) | 1200x630 | `?w=1200&h=630&fit=crop&crop=entropy&auto=format&q=80` |
| Teaser/thumbnail | 600x300 | `?w=600&h=300&fit=crop&crop=entropy&auto=format&q=80` |

## Attribution Requirements
- Always include photographer credit in caption
- Format: "Photo by [Photographer Name](https://unsplash.com/@photographer) on Unsplash"
- Verify images are free to use (Unsplash license)
- Avoid premium/premium-restricted images
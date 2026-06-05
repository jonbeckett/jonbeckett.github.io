---
name: Blog Post Authoring
globs:
  - _posts/**/*.md
alwaysApply: true
description: Standards for creating and updating blog posts, including naming and front matter.
---

# Blog Post Authoring

- Follow post filename format: _posts/YYYY/YYYY-MM-DD-slug-title.md.
- Ensure front matter date matches the filename date.
- Use layout: single for posts.
- Include clear categories and tags in lowercase hyphenated format.
- Write a concise, compelling excerpt suited for previews and sharing.
- Keep structure coherent: opening hook, context, technical substance, practical implications, closing outlook.
- Maintain consistency with existing post style and markdown conventions in this repository.
- Source header imagery from Unsplash and include attribution in front matter.

## Style and Depth Requirements

- Expected post length: 2,000 to 5,000+ words for comprehensive topics.
- Write in a professional but accessible narrative style.
- Blend historical context with technical depth and practical implications.
- Use British English spelling throughout.
- Include meaningful code or architecture examples when they improve clarity.

## Recommended Structure

- Opening hook: compelling scenario, observation, or framing question.
- Historical context: how the topic evolved and why it matters.
- Technical section: concrete detail, examples, trade-offs, and implementation notes.
- Practical applications: where this is used and what teams should do.
- Future outlook: realistic forward-looking implications.

## Front Matter Template Reference

Use this shape for new posts and keep values aligned with file naming and topic taxonomy.

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
excerpt: "A compelling one-sentence summary for previews and social sharing."
header:
  overlay_image: "https://images.unsplash.com/photo-[ID]?w=1200&h=400&fit=crop&crop=entropy&auto=format&q=80"
  overlay_filter: "linear-gradient(90deg, rgba(0,0,0,0.9) 0%, rgba(0,0,0,0.5) 100%)"
  caption: "Photo by [Photographer Name](https://unsplash.com/@username) on [Unsplash](https://unsplash.com)"
  teaser: "https://images.unsplash.com/photo-[ID]?w=600&h=300&fit=crop&crop=entropy&auto=format&q=80"
---
```

## Required Header Image Front Matter

- Include a header block in every new post.
- Use Unsplash image URLs for both overlay and teaser.
- Use the same Unsplash photo ID for both image URLs with different dimensions.
- Include photographer attribution in caption linking to Unsplash profile and site.
- Follow the mandatory image discovery and URL-construction process in 06-unsplash-image-selection-and-url-construction.md.

### Required Fields

- header.overlay_image: https://images.unsplash.com/photo-[ID]?w=1200&h=400&fit=crop&crop=entropy&auto=format&q=80
- header.overlay_filter: linear gradient string suitable for text readability
- header.caption: Photo by [Photographer Name](https://unsplash.com/@username) on [Unsplash](https://unsplash.com)
- header.teaser: https://images.unsplash.com/photo-[ID]?w=600&h=300&fit=crop&crop=entropy&auto=format&q=80

## Front Matter Checks

- title: present and descriptive
- layout: single
- date: YYYY-MM-DD and aligned with file name
- categories: relevant and consistent
- tags: relevant and consistent
- excerpt: present and meaningful
- header: present and complete with Unsplash URLs and attribution

## Validation Checks

- Confirm overlay and teaser URLs render successfully.
- Confirm caption contains photographer name and Unsplash profile link.
- Confirm front matter YAML is valid before finalising.
- Confirm final draft meets expected depth and length for the topic.

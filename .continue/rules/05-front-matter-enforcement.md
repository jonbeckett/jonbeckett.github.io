---
name: Mandatory Post Front Matter
alwaysApply: true
description: Enforce required front matter fields for blog posts, including Unsplash header imagery and attribution.
---

# Mandatory Post Front Matter

Apply these checks whenever creating or editing files under _posts.

## Required Fields for Posts

- title
- layout: single
- date aligned with filename date
- categories with 1 to 3 items
- tags with 3 to 8 items
- excerpt
- header.overlay_image using Unsplash URL
- header.overlay_filter present
- header.caption with photographer attribution and Unsplash links
- header.teaser using Unsplash URL

## Unsplash Requirements

- Use the images.unsplash.com photo URL format.
- Use the same photo ID for overlay and teaser with different dimensions.
- overlay_image dimensions: 1200x400 via URL parameters.
- teaser dimensions: 600x300 via URL parameters.
- Apply the full mandatory workflow in 06-unsplash-image-selection-and-url-construction.md.

## Stop Conditions

- Do not finalise a post draft if required front matter is missing.
- Do not finalise a post draft if header attribution is incomplete.
- Do not finalise a post draft if image URLs are not valid Unsplash links.

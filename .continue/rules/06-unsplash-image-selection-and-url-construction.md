---
name: Unsplash Image Selection and URL Construction
globs:
  - _posts/**/*.md
alwaysApply: true
description: Mandatory workflow for finding Unsplash images and building correct images.unsplash.com URLs from candidate photos.
---

# Unsplash Image Selection and URL Construction

Use this rule whenever creating or updating post header images. Follow every step in order.

## Objective

- Find a relevant, high-quality Unsplash photo for the post topic.
- Derive the canonical Unsplash image URL from the selected candidate.
- Populate front matter fields consistently:
  - header.overlay_image
  - header.teaser
  - header.caption

## Step 1: Understand the Post Topic Before Searching

- Read the post title, excerpt, and opening section.
- Identify 2 to 5 concrete visual concepts (objects, setting, mood, activity).
- Prioritise literal relevance first, then metaphorical relevance.
- Avoid generic images unless the topic is broad and no specific concept fits.

Example concept mapping:

- Topic: test automation at scale
- Concepts: CI pipelines, server racks, observability dashboards, engineering collaboration

## Step 2: Build Good Unsplash Search Queries

- Start with 2 or 3 precise keyword combinations.
- Include both technical and visual descriptors.
- If first results are weak, widen by replacing niche terms with broader synonyms.
- Try at least 3 search queries before selecting an image.

Query patterns:

- primary-subject + context (example: cloud infrastructure team)
- technical-term + environment (example: data centre monitoring)
- metaphor + tone (example: complexity network architecture)

## Step 3: Find Candidate Images on Unsplash

- Search on Unsplash and open multiple candidates in separate tabs.
- Prefer landscape-oriented photos for banner compatibility.
- Ensure subject clarity in the centre or strong composition across wide crops.
- Reject candidates with heavy text overlays, logos, or cluttered framing.

Candidate quality checks:

- relevance to the article
- enough resolution for cropping
- visual readability under dark overlay
- no distracting branding or UI text in focal area

## Step 4: Capture Candidate Metadata (Mandatory)

For each serious candidate, capture:

- photo page URL
- photographer display name
- photographer username
- photo identifier (photo ID)

Photo page URL typically looks like:

- https://unsplash.com/photos/slug-or-description-PHOTO_ID

Photographer profile URL format:

- https://unsplash.com/@username

## Step 5: Extract the Unsplash PHOTO_ID Correctly

Use one of the reliable extraction methods below.

Method A: From images URL (preferred)

- If candidate URL contains images.unsplash.com/photo-..., extract the value after photo-.
- Remove query parameters and fragments.

Example:

- Input: https://images.unsplash.com/photo-1701234567890-abcdEFGHijkl?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80
- PHOTO_ID: 1701234567890-abcdEFGHijkl

Method B: From photo page URL

- In https://unsplash.com/photos/<slug>-<PHOTO_ID>, PHOTO_ID is the final hyphen-delimited token.
- If the slug has multiple hyphens, only the last token is the ID.

Example:

- Input: https://unsplash.com/photos/office-team-reviewing-dashboard-1701234567890-abcdEFGHijkl
- PHOTO_ID: 1701234567890-abcdEFGHijkl

Method C: From download/open-image link

- Some links include photo-<PHOTO_ID> directly; apply Method A.
- Ignore tracking parameters like ixid, utm_*, or download flags.

## Step 6: Build Canonical URLs From the Selected PHOTO_ID

Always build clean, deterministic URLs from the extracted PHOTO_ID.
Do not paste raw search-result URLs with long tracking query strings.

Required output formats:

- overlay_image:
  - https://images.unsplash.com/photo-PHOTO_ID?w=1200&h=400&fit=crop&crop=entropy&auto=format&q=80
- teaser:
  - https://images.unsplash.com/photo-PHOTO_ID?w=600&h=300&fit=crop&crop=entropy&auto=format&q=80

Rules:

- Use the same PHOTO_ID for overlay and teaser.
- Keep parameter order stable for consistency.
- Keep protocol as https.
- Do not include unnecessary ixid/ixlib/utm parameters in image URLs.

## Step 7: Build the Caption Attribution

Use this exact caption pattern:

- Photo by [Photographer Name](https://unsplash.com/@username) on [Unsplash](https://unsplash.com)

Attribution rules:

- Photographer name must match Unsplash profile display name.
- Username link must match the selected photographer.
- Do not omit either attribution link.

## Step 8: Insert Into Front Matter

Required header block structure:

```yaml
header:
  overlay_image: "https://images.unsplash.com/photo-PHOTO_ID?w=1200&h=400&fit=crop&crop=entropy&auto=format&q=80"
  overlay_filter: "linear-gradient(90deg, rgba(0,0,0,0.9) 0%, rgba(0,0,0,0.5) 100%)"
  caption: "Photo by [Photographer Name](https://unsplash.com/@username) on [Unsplash](https://unsplash.com)"
  teaser: "https://images.unsplash.com/photo-PHOTO_ID?w=600&h=300&fit=crop&crop=entropy&auto=format&q=80"
```

## Step 9: Validate Before Finalising

Validation checklist (all mandatory):

- Both `overlay_image` and `teaser` resolve successfully in browser.
- Both URLs use images.unsplash.com/photo-PHOTO_ID.
- Overlay uses 1200x400 and teaser uses 600x300.
- Same PHOTO_ID is used in both URLs.
- Caption links resolve to correct photographer profile and Unsplash home.
- YAML syntax remains valid after edit.
- Chosen image remains relevant after wide crop and dark overlay.

## Failure Handling and Recovery

If any check fails:

- If URL fails to load: re-extract PHOTO_ID from source and rebuild URL.
- If crop looks poor: choose a new candidate and repeat from Step 3.
- If attribution is uncertain: reopen candidate page and recapture name/username.
- If multiple candidates are close: prefer clearer focal subject and stronger wide composition.

Do not finalise the post until all mandatory checks pass.

## Quick Reference

- Candidate page format: https://unsplash.com/photos/slug-PHOTO_ID
- Canonical base URL: https://images.unsplash.com/photo-PHOTO_ID
- Overlay params: ?w=1200&h=400&fit=crop&crop=entropy&auto=format&q=80
- Teaser params: ?w=600&h=300&fit=crop&crop=entropy&auto=format&q=80
- Caption format: Photo by [Name](https://unsplash.com/@username) on [Unsplash](https://unsplash.com)

This rule is mandatory for all post header image selection and URL construction tasks.
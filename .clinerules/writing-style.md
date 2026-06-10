# Writing Style Rules

## Voice and Tone
- Professional but accessible, narrative-driven with technical depth
- Use conversational elements and real-world examples to make technical concepts relatable
- Maintain authoritative voice while being approachable

## Content Structure Pattern
1. **Introduction**: Compelling hook/scenario with context and preview of what reader will learn
2. **Historical Context**: Evolution and background of the topic
3. **Technical Deep Dive**: Detailed analysis with code/architecture examples
4. **Practical Applications**: Real-world implications and use cases
5. **Future Outlook**: Forward-looking analysis and predictions

## British English Standards (CRITICAL)
**ALL content MUST use British English spellings exclusively.**

### Common -ise/-isation endings (NOT -ize/-ization)
- organise, organisation, recognise, realise, specialise
- optimise, optimisation, customise, customisation
- analyse, utilise, summarise, categorise, materialise, digitise

### -our endings (NOT -or)
- behaviour, colour, honour, favour, labour, humour, rigour, vigour
- harbour, flavour, endeavour

### -re endings (NOT -er)
- centre, theatre, metre, litre, fibre, calibre

### -ce endings for nouns (NOT -se)
- licence (noun), defence, offence, practice (noun)
- **Note**: license/practise are verbs; licence/practice are nouns

### Other Important British Spellings
- analogue (NOT analog), catalogue, dialogue, grey (NOT gray)
- tyre (NOT tire), focussed (NOT focused), travelled (NOT traveled)

### Pre-Publication Verification
Before publishing, search for and correct these American spellings:
- Words ending in -ize, -ization
- Words ending in -or when should be -our
- Words ending in -er when should be -re
- Common words: center, defense, license (noun), realize, organize, analyze, optimise

## File Structure Reference
```
_posts/
  └── YYYY/
      ├── YYYY-MM-DD-post-slug.md    # Blog posts by year
      └── YYYY-MM-DD-another-post.md
_pages/
    ├── about.md
    ├── categories.md
    ├── disclaimer.md
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
_config.yml          # Main site configuration
Gemfile              # Ruby dependencies
```

## Local Development Commands
```bash
# Install dependencies
bundle install

# Serve locally with live reload
bundle exec jekyll serve

# Serve with drafts (for preview)
bundle exec jekyll serve --drafts

# Build site for production
bundle exec jekyll build

# Clean generated files
bundle exec jekyll clean
```

## Development Workflow
1. Make changes to posts or configuration
2. Test locally with `bundle exec jekyll serve`
3. Review changes at `http://localhost:4000`
4. Commit and push to trigger automatic deployment

## Deployment Process
1. **Local Development**: Test changes locally
2. **Git Push**: Push to main branch
3. **GitHub Actions**: Automatic build and deployment
4. **GitHub Pages**: Site updated at jonbeckett.github.io

## Common Technical Issues

### Build Failures
- Check for YAML syntax errors in front matter
- Ensure all required front matter fields are present
- Verify Markdown syntax is correct
- Check for broken image URLs

### Archive Configuration
- Never change archive type from `liquid` to `jekyll-archives`
- This will break all category and tag links site-wide
- GitHub Pages has limited plugin support

## QUICK REFERENCE

### Essential File Patterns
```
_posts/YYYY/YYYY-MM-DD-slug-title.md   # Blog posts
_pages/*.md                             # Static pages
_config.yml                            # Site configuration
_data/navigation.yml                    # Navigation menu
```

### Core Front Matter (Minimal)
```yaml
---
title: "Main Title: Subtitle"
layout: single
date: YYYY-MM-DD
categories: [primary-category]
tags: [tag1, tag2, tag3]
excerpt: "Compelling one-sentence description"
---
```

### Critical Reminders
- **British English spellings exclusively** (organise, colour, centre, optimise)
- **Target length**: 2,000-5,000+ words
- **Content structure**: Hook → History → Technical → Applications → Future
- **Archive type**: Must use `liquid` NOT `jekyll-archives` (GitHub Pages limitation)
- **Layout**: Always `single` for blog posts
- **Unsplash images**: Always include photographer attribution
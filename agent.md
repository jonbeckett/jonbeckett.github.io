# Agent Instructions for jonbeckett.com

This repository contains a Jekyll-based personal technology blog with specialized AI agent skills for content management and creation.

## Quick Project Overview

- **Platform**: Jekyll static site generator with Minimal Mistakes theme
- **Hosting**: GitHub Pages with automated deployment
- **Content Focus**: Software development, productivity, technology evolution
- **Author**: Jonathan Beckett (software developer, Microsoft ecosystem, JavaScript/TypeScript, DevOps)

## Agent Skills Directory

This project uses a modular skill-based approach. Each skill contains detailed, actionable instructions for specific aspects of blog management:

### 📝 **Content Creation**
- **[Blog Post Creation](.github/copilot/skills/blog-post-creation.md)** - File naming, front matter templates, workflow
- **[Writing Style Guidelines](.github/copilot/skills/writing-style-guidelines.md)** - Voice, structure, technical writing standards

### 🎨 **Visual and Language Standards**
- **[Image Management](.github/copilot/skills/image-management.md)** - Unsplash integration, URL construction, attribution
- **[British English Standards](.github/copilot/skills/british-english-standards.md)** - Required spelling conventions and validation

### ⚙️ **Technical Management**
- **[Jekyll Technical Setup](.github/copilot/skills/jekyll-technical-setup.md)** - Development, deployment, configuration
- **[Quality Control](.github/copilot/skills/quality-control.md)** - Checklists, common mistakes, best practices

## Critical Requirements

### File Structure
```
_posts/YYYY/YYYY-MM-DD-slug-title.md
```

### British English Only
- organise (not organize), colour (not color), centre (not center)
- See [British English Standards](.github/copilot/skills/british-english-standards.md) for complete guide

### Image Attribution Required
- All Unsplash images must include proper photographer attribution
- See [Image Management](.github/copilot/skills/image-management.md) for extraction and validation process

### GitHub Pages Limitations
- Must use `type: liquid` for archives (not `jekyll-archives`)
- See [Jekyll Technical Setup](.github/copilot/skills/jekyll-technical-setup.md) for details

## Getting Started

1. **For new blog posts**: Start with [Blog Post Creation](.github/copilot/skills/blog-post-creation.md)
2. **For content writing**: Follow [Writing Style Guidelines](.github/copilot/skills/writing-style-guidelines.md)
3. **For images**: Use comprehensive [Image Management](.github/copilot/skills/image-management.md) process
4. **For technical setup**: Reference [Jekyll Technical Setup](.github/copilot/skills/jekyll-technical-setup.md)
5. **Before publishing**: Complete [Quality Control](.github/copilot/skills/quality-control.md) checklist

## Essential Quick Commands

```bash
# Start local development
bundle exec jekyll serve

# View site locally
# http://localhost:4000

# Build for production
bundle exec jekyll build
```

## Complete Workflow Summary

### Creating a New Blog Post
1. Create `_posts/YYYY/YYYY-MM-DD-slug-title.md`
2. Add complete front matter (title, date, categories, tags, excerpt, images)
3. Write 2,000+ word content with British English spelling
4. Find and validate Unsplash images with proper attribution
5. Test locally, validate, and deploy

### Critical Success Factors
- **File naming exactness**: `_posts/2026/2026-01-30-example-post.md`
- **British English mandatory**: organise, colour, centre (never organize, color, center)
- **Image validation required**: Extract photo IDs from Unsplash page source, test URLs
- **Jekyll limitations**: Use `type: liquid` for archives, not `jekyll-archives`

## Author Context

Jonathan Beckett specializes in:
- Microsoft ecosystem (PowerShell, Power Automate, document management)
- JavaScript/TypeScript development  
- BDD with Cucumber/Gherkin
- Web automation with Playwright
- DevOps and CI/CD optimization
- Linux and open source software

Content should draw from this expertise while maintaining the established narrative-driven, technically deep writing style.
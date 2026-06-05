---
name: Jekyll and GitHub Pages Safety
globs:
  - _config.yml
  - Gemfile
  - _pages/**/*.md
  - _posts/**/*.md
  - docs/**/*.md
alwaysApply: true
description: Protect Jekyll and GitHub Pages compatibility and deployment behaviour.
---

# Jekyll and GitHub Pages Safety

- Preserve GitHub Pages compatibility in configuration changes.
- Do not introduce unsupported plugin patterns without explicit approval.
- Keep category and tag archive behaviour compatible with existing liquid-based setup.
- Prefer incremental, reversible changes to site config and templates.
- When changing build-related files, verify expected local commands and deployment assumptions.

## Operational Reminders

- Typical local validation flow: bundle install, bundle exec jekyll serve, then bundle exec jekyll build.
- Check YAML front matter validity when modifying markdown posts or pages.
- Treat broken links, invalid front matter, and archive config regressions as high-risk issues.

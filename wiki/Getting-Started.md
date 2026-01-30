# Getting Started

This guide will help you get the jonbeckett.com blog running locally on your machine for development or testing purposes.

## Prerequisites

Before you begin, ensure you have the following installed on your system:

### Required Software

1. **Ruby** (version 2.7 or higher)
   - Check version: `ruby --version`
   - Install via [RVM](https://rvm.io/) or [rbenv](https://github.com/rbenv/rbenv) for version management

2. **Bundler** (Ruby package manager)
   - Install: `gem install bundler`
   - Check version: `bundle --version`

3. **Git** (for version control)
   - Check version: `git --version`
   - Download from [git-scm.com](https://git-scm.com/)

### Optional But Recommended

- **Text Editor**: VS Code, Sublime Text, Atom, or your preferred editor
- **Terminal**: Comfortable command-line interface (iTerm2, Terminal, Windows Terminal, etc.)

## Quick Start (5 Minutes)

### 1. Clone the Repository

```bash
git clone https://github.com/jonbeckett/jonbeckett.github.io.git
cd jonbeckett.github.io
```

### 2. Install Dependencies

```bash
bundle install
```

This command installs all Ruby gems specified in the `Gemfile`, including Jekyll and all required plugins.

### 3. Serve the Site Locally

```bash
bundle exec jekyll serve
```

The site will be available at `http://localhost:4000`

### 4. Watch for Changes

By default, Jekyll watches for file changes and automatically rebuilds the site. Simply save your changes and refresh the browser to see updates.

## Development Workflow

### Running Jekyll with Live Reload

For the best development experience:

```bash
bundle exec jekyll serve --livereload
```

This enables automatic browser refresh when files change.

### Running on a Different Port

If port 4000 is already in use:

```bash
bundle exec jekyll serve --port 4001
```

### Building for Production

To generate the production-ready static files without serving:

```bash
bundle exec jekyll build
```

The generated site will be in the `_site/` directory.

## Understanding the Project Structure

```
jonbeckett.github.io/
├── _config.yml          # Jekyll configuration
├── _posts/              # Blog post content
│   └── 2026/           # Posts organized by year
├── _pages/              # Static pages (About, Categories, etc.)
├── _includes/           # Reusable HTML components
├── _data/               # Data files (YAML, JSON, CSV)
├── assets/              # Images, CSS, JavaScript
│   └── images/         # Image files
├── index.html           # Homepage template
├── Gemfile              # Ruby dependencies
└── CNAME               # Custom domain configuration
```

## Creating Your First Post

### 1. Create a New File

Create a new Markdown file in `_posts/YYYY/` directory:

```bash
_posts/2026/2026-01-30-my-first-post.md
```

**Naming Convention**: `YYYY-MM-DD-title-with-hyphens.md`

### 2. Add Front Matter

Every post must start with YAML front matter:

```yaml
---
title: "My First Post"
layout: single
date: 2026-01-30
categories:
  - software-development
tags:
  - jekyll
  - blogging
excerpt: "A brief description of the post"
---

# My First Post

Your content goes here...
```

### 3. Write Content in Markdown

Use standard Markdown syntax for formatting:

```markdown
## Heading 2
### Heading 3

**Bold text** and *italic text*

- Bullet point 1
- Bullet point 2

[Link text](https://example.com)

```code block```
```

### 4. Preview Your Post

Save the file and check `http://localhost:4000` to see your post appear.

## Common Tasks

### Updating Dependencies

Keep gems up to date:

```bash
bundle update
```

### Clearing the Cache

If you encounter build issues:

```bash
bundle exec jekyll clean
bundle exec jekyll serve
```

### Testing Before Push

Always test locally before pushing to GitHub:

```bash
# Build the site
bundle exec jekyll build

# Check for broken links (if you have html-proofer)
# bundle exec htmlproofer ./_site
```

## Troubleshooting

### "Command not found: bundle"

Install Bundler:
```bash
gem install bundler
```

### "Permission denied" errors

Use a Ruby version manager (RVM or rbenv) instead of system Ruby, or prefix commands with `sudo` (not recommended).

### Port 4000 already in use

Find and kill the process:
```bash
lsof -i :4000
kill -9 [PID]
```

Or use a different port:
```bash
bundle exec jekyll serve --port 4001
```

### Changes not reflecting

1. Stop the server (Ctrl+C)
2. Clear the cache: `bundle exec jekyll clean`
3. Restart: `bundle exec jekyll serve`

### "Could not find gem" errors

Update dependencies:
```bash
bundle install
```

## Next Steps

Once you have the site running locally:

1. Read the **[Technical Architecture](Technical-Architecture)** to understand how everything works
2. Review **[Content Guidelines](Content-Guidelines)** before creating content
3. Check out **[Development Setup](Development-Setup)** for advanced configuration
4. Explore existing posts in `_posts/` for examples

## Getting Help

- **Jekyll Documentation**: [jekyllrb.com/docs](https://jekyllrb.com/docs/)
- **Minimal Mistakes Theme**: [mmistakes.github.io/minimal-mistakes](https://mmistakes.github.io/minimal-mistakes/)
- **GitHub Pages**: [docs.github.com/pages](https://docs.github.com/pages)
- **Repository Issues**: [github.com/jonbeckett/jonbeckett.github.io/issues](https://github.com/jonbeckett/jonbeckett.github.io/issues)

---

**Ready to dive deeper?** Continue to [Technical Architecture](Technical-Architecture) to understand the complete technology stack.

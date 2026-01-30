# Technical Architecture

This document provides a comprehensive overview of the technical architecture powering jonbeckett.com, including the technology stack, infrastructure, build process, and deployment pipeline.

## Architecture Overview

jonbeckett.com is a modern static website built using the JAMstack (JavaScript, APIs, and Markup) architecture pattern, providing excellent performance, security, and scalability.

```
┌─────────────────────────────────────────────────────────┐
│                    GitHub Repository                     │
│              jonbeckett/jonbeckett.github.io            │
└───────────────────────┬─────────────────────────────────┘
                        │
                        │ Push to main branch
                        ▼
┌─────────────────────────────────────────────────────────┐
│                   GitHub Actions                         │
│              (Automated Build Pipeline)                  │
│  • Install dependencies                                  │
│  • Build Jekyll site                                     │
│  • Deploy to GitHub Pages                                │
└───────────────────────┬─────────────────────────────────┘
                        │
                        │ Deployment
                        ▼
┌─────────────────────────────────────────────────────────┐
│                   GitHub Pages                           │
│               (Static Site Hosting)                      │
│  • Serves static HTML/CSS/JS                            │
│  • Custom domain (jonbeckett.com)                       │
│  • Automatic HTTPS                                       │
│  • Global CDN distribution                               │
└─────────────────────────────────────────────────────────┘
```

## Technology Stack

### Core Framework: Jekyll

**Jekyll** is a static site generator written in Ruby that transforms plain text into static websites and blogs.

- **Version**: Managed via `github-pages` gem
- **Configuration**: `_config.yml`
- **Template Engine**: Liquid
- **Content Format**: Markdown with YAML front matter

**Why Jekyll?**
- Native GitHub Pages support
- Mature ecosystem with extensive plugins
- Fast build times for blogs
- No database or server-side processing needed
- Excellent documentation and community

### Theme: Minimal Mistakes

**Minimal Mistakes** is a flexible two-column Jekyll theme, perfect for building personal sites, blogs, and portfolios.

- **Installation**: Remote theme via `_config.yml`
- **Repository**: [mmistakes/minimal-mistakes](https://github.com/mmistakes/minimal-mistakes)
- **Customization**: Overridable layouts, includes, and styles
- **Features**: 
  - Responsive design
  - SEO optimization
  - Multiple layouts
  - Built-in analytics support
  - Social sharing
  - Comments integration

**Theme Configuration:**
```yaml
remote_theme: mmistakes/minimal-mistakes
minimal_mistakes_skin: "default"
```

### Content Management

#### Markdown Processing

- **Processor**: Kramdown (GitHub Flavored Markdown)
- **Syntax Highlighting**: Rouge
- **Features**:
  - Footnotes
  - Tables
  - Code blocks with syntax highlighting
  - Auto-generated IDs for headings
  - Table of contents generation

#### Front Matter Structure

Each post includes YAML front matter for metadata:

```yaml
---
title: "Post Title"
layout: single
date: 2026-01-30
categories:
  - category-name
tags:
  - tag1
  - tag2
excerpt: "Brief description"
header:
  overlay_image: "image-url"
  overlay_filter: "gradient"
  caption: "Photo credit"
  teaser: "teaser-image-url"
---
```

### Styling System

#### SCSS Architecture

- **Preprocessor**: Sass/SCSS
- **Compilation**: Automatic during Jekyll build
- **Organization**:
  - `_sass/`: Sass partials and variables
  - Theme styles from Minimal Mistakes
  - Custom overrides in `assets/css/main.scss`

#### Responsive Design

- Mobile-first approach
- Breakpoints defined in theme
- Flexible grid system
- Optimized for all device sizes

### Plugin Ecosystem

The site uses several Jekyll plugins to extend functionality:

```ruby
plugins:
  - jekyll-paginate      # Pagination for post lists
  - jekyll-sitemap       # Automatic sitemap.xml generation
  - jekyll-gist          # Embed GitHub Gists
  - jekyll-feed          # Automatic RSS/Atom feed
  - jekyll-include-cache # Performance optimization
  - jekyll-archives      # Category and tag archives
```

**Plugin Highlights:**

- **jekyll-paginate**: Splits post listings across multiple pages (10 posts per page)
- **jekyll-sitemap**: SEO-friendly XML sitemap for search engines
- **jekyll-feed**: Generates RSS feed at `/feed.xml`
- **jekyll-archives**: Creates archive pages for categories and tags

## Infrastructure

### Hosting: GitHub Pages

**GitHub Pages** provides free, reliable hosting for static websites directly from GitHub repositories.

**Features:**
- Automatic deployment from Git repository
- Free SSL/TLS certificates
- Custom domain support via CNAME
- 99.9% uptime SLA
- Unlimited bandwidth (within fair use)
- Global CDN distribution

**Configuration:**
- **Source Branch**: `main`
- **Build Method**: GitHub Actions
- **Custom Domain**: `jonbeckett.com` (via CNAME file)
- **SSL**: Automatic HTTPS enforcement

### Domain Configuration

**Custom Domain Setup:**

1. **CNAME File**: Contains the custom domain
   ```
   jonbeckett.com
   ```

2. **DNS Configuration** (at domain registrar):
   - A records pointing to GitHub Pages IP addresses
   - CNAME record for www subdomain

3. **SSL Certificate**: Automatically provisioned by GitHub Pages

### Content Delivery Network (CDN)

GitHub Pages automatically distributes content via:
- Global edge locations
- Automatic caching
- HTTPS everywhere
- DDoS protection

## Build Process

### Local Development Build

```bash
bundle exec jekyll serve
```

**Build Steps:**
1. Load configuration from `_config.yml`
2. Process Liquid templates
3. Convert Markdown to HTML
4. Apply layouts and includes
5. Compile Sass to CSS
6. Copy static assets
7. Generate pagination
8. Create sitemap and feed
9. Output to `_site/` directory
10. Start development server on port 4000

### Production Build (GitHub Actions)

**Workflow File**: `.github/workflows/` (if custom workflow exists)

**Build Steps:**
1. **Trigger**: Push to main branch
2. **Checkout**: Clone repository
3. **Setup**: Install Ruby and dependencies
4. **Build**: Execute Jekyll build
5. **Deploy**: Push to `gh-pages` branch (or configured deployment branch)
6. **Serve**: GitHub Pages serves the built site

**Build Time**: Typically 1-3 minutes depending on content volume

## Performance Optimizations

### Static Site Advantages

- **No Server Processing**: HTML served directly from CDN
- **No Database Queries**: All content pre-generated
- **Instant Page Loads**: Optimized static assets
- **Cacheable**: Aggressive browser and CDN caching

### Asset Optimization

- **CSS**: Minified via Sass compilation
- **HTML**: Compressed via `compress_html` in `_config.yml`
- **Images**: Manually optimized before commit
- **JavaScript**: Minimal JS, primarily from theme

### Caching Strategy

```yaml
compress_html:
  clippings: all
  ignore:
    envs: development
```

## Security

### Static Site Security Benefits

- **No Backend**: No server-side code to exploit
- **No Database**: No SQL injection vectors
- **No User Input**: No form processing vulnerabilities
- **Automatic HTTPS**: All traffic encrypted
- **GitHub Infrastructure**: Protected by GitHub's security

### Content Security

- **Version Control**: Full audit trail of all changes
- **Branch Protection**: Can be enabled for main branch
- **Review Process**: Changes can require PR reviews
- **Rollback**: Easy to revert to any previous state

## SEO & Analytics

### SEO Optimization

**Built-in Features:**
- Semantic HTML structure
- Meta tags in page head
- Open Graph protocol support
- Twitter Card metadata
- Automatic sitemap generation
- RSS/Atom feed
- Structured data support

**Configuration in `_config.yml`:**
```yaml
url: "https://jonbeckett.com"
repository: "jonbeckett/jonbeckett.github.io"
```

### Analytics

**Google Analytics Integration:**
```yaml
analytics:
  provider: "google-gtag"
  google:
    tracking_id: "G-0J6K0088RD"
```

Tracking includes:
- Page views
- User sessions
- Traffic sources
- User behavior
- Device and browser stats

## Comments System

**Giscus Integration** (GitHub Discussions-based comments):

```yaml
comments:
  provider: "giscus"
  giscus:
    repo_id: "R_kgDOQxyHhg"
    category_name: "General"
    category_id: "DIC_kwDOQxyHhs4C03Y9"
```

**Features:**
- GitHub authentication
- Markdown support
- Threaded conversations
- Reactions and emoji
- Spam protection via GitHub

## Directory Structure Explained

```
jonbeckett.github.io/
│
├── _config.yml              # Main configuration file
├── Gemfile                  # Ruby dependencies
├── Gemfile.lock            # Locked dependency versions
├── CNAME                   # Custom domain configuration
├── index.html              # Homepage template
│
├── _posts/                 # Blog post content
│   └── 2026/              # Organized by year
│       └── *.md           # Individual posts
│
├── _pages/                # Static pages
│   ├── about.md          # About page
│   ├── categories.md     # Category archive
│   ├── tags.md           # Tag archive
│   ├── posts.md          # All posts archive
│   └── disclaimer.md     # Site disclaimer
│
├── _includes/             # Reusable HTML components
│   └── (from theme)      # Theme includes
│
├── _data/                # Data files
│   └── (YAML/JSON data)  # Structured data
│
├── assets/               # Static assets
│   ├── images/          # Image files
│   └── css/             # Custom CSS
│
└── _site/               # Generated site (not committed)
    └── (built files)    # Jekyll output
```

## Scalability Considerations

### Content Growth

- **Current**: ~20-30 posts
- **Capacity**: Easily handles thousands of posts
- **Build Time**: Scales linearly with content
- **Pagination**: Prevents large page loads

### Traffic Handling

- **CDN Distribution**: Handles traffic spikes
- **Static Files**: No server load concerns
- **GitHub Pages**: Free unlimited bandwidth (fair use)
- **Caching**: Reduces repeated requests

## Development Best Practices

1. **Local Testing**: Always test locally before pushing
2. **Incremental Commits**: Small, focused commits
3. **Branch Strategy**: Feature branches for major changes
4. **Dependency Updates**: Regular gem updates
5. **Performance Monitoring**: Check build times and page load speeds
6. **SEO Validation**: Verify meta tags and structured data
7. **Accessibility**: Follow WCAG guidelines

## Future Considerations

### Potential Enhancements

- **Search Functionality**: Algolia or Lunr.js integration
- **Progressive Web App**: Service workers and offline support
- **Image Optimization**: Automatic responsive images
- **Build Optimization**: Incremental builds for faster deployment
- **Advanced Analytics**: Custom event tracking

### Migration Paths

If outgrowing GitHub Pages:
- **Netlify**: More build features, deploy previews
- **Vercel**: Edge functions, advanced caching
- **Cloudflare Pages**: Additional CDN features
- **Self-hosted**: Complete control, more complexity

---

**Related Documentation:**
- [Getting Started](Getting-Started) - Setup and installation
- [Development Setup](Development-Setup) - Advanced development configuration
- [Deployment](Deployment) - Deployment process and workflows

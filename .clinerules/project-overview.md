# Project Overview Rules

## Author Context
- **Author**: Jonathan Beckett
- **Site**: jonbeckett.com
- **Tech Stack**: Jekyll, Minimal Mistakes theme, GitHub Pages
- **Content Focus**: Software development, productivity, technology evolution, AI/ML, enterprise technology
- **Deployment**: Automated via GitHub Actions to GitHub Pages
- **Language**: British English exclusively

## Author Expertise Context
Jonathan Beckett is a software/web developer with expertise in:
- Microsoft ecosystem (document/content management, PowerShell, Power Automate)
- Modern JavaScript/TypeScript development
- BDD with Cucumber/Gherkin
- Web automation with Playwright
- DevOps and pipeline optimization
- Linux and open source software background
- Creator of early blogging platform

Draw from these areas when suggesting content or code examples while maintaining the established writing style.

## Platform Constraints
- **Static Site Generator**: Jekyll (kramdown markdown processor, Rouge syntax highlighting)
- **Theme**: Minimal Mistakes (remote_theme: mmistakes/minimal-mistakes)
- **Hosting**: GitHub Pages
- **Plugins**: jekyll-paginate, jekyll-sitemap, jekyll-gist, jekyll-feed, jekyll-include-cache, jekyll-archives
- **Analytics**: Google Analytics (G-0J6K0088RD)
- **Comments**: Disqus (configured), Giscus (fallback)

### Critical GitHub Pages Constraints
- **Plugin whitelist only** - cannot use arbitrary Jekyll plugins
- **NO jekyll-archives plugin** - must use `type: liquid` for category/tag archives
- **Theme restrictions** - use `remote_theme`, not `theme`
- **Build environment** - specific Ruby version and Linux environment
- **Execution limits** - 10-minute build timeout, 10 builds per hour
- **Size limits** - 1GB source repository, 1GB published site

### Archive Configuration (CRITICAL)
```yaml
# MUST use liquid type - NEVER jekyll-archives on GitHub Pages
category_archive:
  type: liquid
  path: /categories/
tag_archive:
  type: liquid
  path: /tags/
# jonbeckett.com

A personal blog focusing on software development, productivity, and technology evolution.

## About the Author

**Jonathan Beckett** is a software and web developer, writer, runner, and occasional retro gaming enthusiast. With years of experience convincing computers to do useful things (with varying degrees of success), Jonathan spends his professional time in the Microsoft ecosystem, building document and content management systems, writing PowerShell automation scripts, and creating workflows with PowerAutomate.

His recent focus has shifted toward TypeScript development, behavior-driven development with Cucumber and Gherkin scenarios, web automation using Playwright, and DevOps pipeline optimization. Behind all this modern technology lies a deeper history with Linux systems and open source software—a journey that once led to accidentally creating one of the early popular blogging platforms.

When not debugging "temporary" fixes from years past, Jonathan writes about software development methodologies that work in the real world, productivity and note-taking methods, technology evolution, and the eternal quest for the perfect development workflow. When away from screens, he can be found running (for both fitness and problem-solving), drinking terrible coffee, reading about everything from ancient history to quantum physics, and wrangling cats.

## Visit the blog

Visit https://jonbeckett.com to read the blog in it's native habitat.

## Technical Architecture

This blog is built using modern static site generation and deployment practices:

### Jekyll Static Site Generator
- **Framework**: Jekyll with the [Minimal Mistakes](https://mmistakes.github.io/minimal-mistakes/) remote theme
- **Content**: Written in Markdown with YAML front matter for metadata
- **Structure**: 
  - Posts organized chronologically in `_posts/`
  - Pages for navigation in `_pages/`
  - Custom includes and data files for modular content
  - SCSS stylesheets for custom styling

### GitHub Pages Hosting
- **Hosting**: Deployed automatically to GitHub Pages
- **Domain**: Custom domain configured via `CNAME` file
- **SSL**: Automatic HTTPS via GitHub Pages
- **CDN**: Global content delivery through GitHub's infrastructure

### GitHub Actions CI/CD
- **Automation**: GitHub Actions handle the build and deployment pipeline
- **Workflow**: 
  1. Content changes pushed to the main branch
  2. GitHub Actions automatically builds the Jekyll site
  3. Generated static files deployed to GitHub Pages
  4. Site updates live within minutes

### Key Features
- **Responsive Design**: Mobile-first approach with the Minimal Mistakes theme
- **SEO Optimized**: Structured data, meta tags, and sitemap generation
- **Fast Loading**: Static site with optimized assets and CDN delivery
- **Version Control**: Full site history and collaboration via Git
- **Zero Server Management**: Fully managed hosting with 99.9% uptime

## Development

To run this site locally:

```bash
# Install dependencies
bundle install

# Serve locally with live reload
bundle exec jekyll serve

# Build for production
bundle exec jekyll build
```

## Content Structure

- **Posts**: Technical articles and thoughts on software development
- **Categories**: Organized by topic (Software Development, Productivity, etc.)
- **Tags**: Granular content organization for easy discovery
- **About**: Author information and blog purpose

---

*This site represents ongoing thoughts and learnings in the world of software development and technology. All opinions are personal and subject to evolution as understanding deepens.*

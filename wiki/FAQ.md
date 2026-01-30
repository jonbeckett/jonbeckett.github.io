# Frequently Asked Questions (FAQ)

Common questions and answers about jonbeckett.com, its development, and contributing to the project.

## General Questions

### What is jonbeckett.com?

jonbeckett.com is a personal technical blog focusing on software development, productivity, and technology evolution. It's built using Jekyll and hosted on GitHub Pages, featuring in-depth articles about programming, development methodologies, productivity systems, and technology commentary.

### Who writes the content?

The blog is primarily written by Jonathan Beckett, a software and web developer based in the UK. Guest posts from other contributors are also welcome following the [Content Guidelines](Content-Guidelines).

### How often is new content published?

Content is published irregularly, typically 1-3 times per week. The focus is on quality over quantity, with preference given to well-researched, in-depth articles rather than quick posts.

### Can I subscribe to updates?

Yes! The site provides an RSS/Atom feed at [https://jonbeckett.com/feed.xml](https://jonbeckett.com/feed.xml) that you can add to your feed reader.

## Technical Questions

### What technology stack does the site use?

- **Framework**: Jekyll (Ruby-based static site generator)
- **Theme**: Minimal Mistakes (remote theme)
- **Hosting**: GitHub Pages
- **Domain**: Custom domain via CNAME
- **CI/CD**: GitHub Actions (automatic deployment)
- **Comments**: Giscus (GitHub Discussions-based)
- **Analytics**: Google Analytics

See [Technical Architecture](Technical-Architecture) for complete details.

### Why Jekyll and not [other static site generator]?

Jekyll was chosen for several reasons:
- Native GitHub Pages support (zero configuration deployment)
- Mature ecosystem with extensive plugins
- Excellent documentation and community
- Ruby-based (familiar to the author)
- Perfect for blogs and content-focused sites
- Fast build times for this site size

### Is the site open source?

Yes! The repository is public at [github.com/jonbeckett/jonbeckett.github.io](https://github.com/jonbeckett/jonbeckett.github.io). You can view all the code, content, and configuration.

### Can I use this as a template for my own blog?

While the repository is public, the content is copyrighted. You can:
- **✓** Use the technical setup as a reference
- **✓** Learn from the configuration
- **✓** Study the Jekyll implementation
- **✗** Copy content verbatim
- **✗** Clone and republish as-is

For a clean template, consider using [Minimal Mistakes Starter](https://github.com/mmistakes/mm-github-pages-starter) directly.

## Development Questions

### How do I run the site locally?

Quick start:
```bash
git clone https://github.com/jonbeckett/jonbeckett.github.io.git
cd jonbeckett.github.io
bundle install
bundle exec jekyll serve
```

Visit `http://localhost:4000` in your browser.

See [Getting Started](Getting-Started) for detailed instructions.

### What are the system requirements?

**Minimum:**
- Ruby 2.7.0 or higher
- Bundler
- Git
- 4GB RAM
- 2GB disk space

**Recommended:**
- Ruby 3.0+
- 8GB RAM
- SSD storage
- Modern multi-core CPU

See [Development Setup](Development-Setup) for installation guides.

### Which Ruby version should I use?

**Recommended**: Ruby 3.0 or higher

**Minimum**: Ruby 2.7.0

**Check your version**:
```bash
ruby --version
```

Use a version manager (rbenv or RVM) to manage multiple Ruby versions.

### Why is the build taking so long?

Build time increases with content volume. Optimization tips:

**Development:**
```bash
# Use incremental builds
bundle exec jekyll serve --incremental

# Limit posts in development config
limit_posts: 10
```

**Production:**
- Builds usually take 1-3 minutes
- GitHub Pages handles optimization automatically

See [Development Setup](Development-Setup) for more optimization tips.

### I get "command not found: bundle" error

You need to install Bundler:
```bash
gem install bundler
```

If `gem` command is not found, install Ruby first. See [Development Setup](Development-Setup).

### Port 4000 is already in use

Either kill the existing process or use a different port:

```bash
# Use different port
bundle exec jekyll serve --port 4001

# Or find and kill process on port 4000
lsof -i :4000
kill -9 <PID>
```

### Changes aren't showing up locally

Try these steps:

1. **Hard refresh browser**: Ctrl+F5 (Windows) or Cmd+Shift+R (Mac)

2. **Clear Jekyll cache**:
   ```bash
   bundle exec jekyll clean
   bundle exec jekyll serve
   ```

3. **Restart server**: Stop (Ctrl+C) and restart Jekyll

4. **Check for errors**: Look at terminal output for build errors

### How do I update dependencies?

```bash
# Update all gems
bundle update

# Update specific gem
bundle update jekyll

# Check for outdated gems
bundle outdated
```

Commit the updated `Gemfile.lock` to keep dependencies in sync.

## Content Questions

### How do I create a new blog post?

1. Create file in `_posts/YYYY/` directory
2. Name it: `YYYY-MM-DD-title-with-hyphens.md`
3. Add required front matter
4. Write content in Markdown
5. Test locally
6. Commit and push

Example:
```yaml
---
title: "My Post Title"
layout: single
date: 2026-01-30
categories:
  - software-development
tags:
  - jekyll
  - blogging
excerpt: "Brief description"
---

# Content starts here...
```

See [Content Guidelines](Content-Guidelines) for complete standards.

### What categories and tags should I use?

**Categories** (use 1-2):
- software-development
- productivity
- artificial-intelligence
- web-development
- devops
- technology

**Tags** (use 3-7, specific to content):
- Check existing posts for consistency
- Use lowercase with hyphens
- Be specific and relevant

See [Content Guidelines](Content-Guidelines) for details.

### Can I write a guest post?

Yes! Guest posts are welcome. Process:

1. Open an issue proposing your topic
2. Wait for approval
3. Write following [Content Guidelines](Content-Guidelines)
4. Submit via Pull Request
5. Address review feedback

See [Contributing](Contributing) for complete process.

### What writing style should I use?

- **British English** spelling and grammar
- **Conversational but professional** tone
- **First-person perspective** for personal experiences
- **In-depth coverage** over quick takes
- **Well-researched** with examples
- **Accessible** without oversimplification

See [Content Guidelines](Content-Guidelines) for comprehensive style guide.

### How do I add images to posts?

1. **Optimize images** before adding (compress, resize)
2. **Add to** `assets/images/` directory
3. **Use in Markdown**:
   ```markdown
   ![Alt text](/assets/images/my-image.jpg)
   ```

4. **For header images**, use Unsplash or optimized images:
   ```yaml
   header:
     overlay_image: "https://images.unsplash.com/photo-id?w=1200"
   ```

5. **Always credit** image sources

### Where can I find example posts?

Browse existing posts in the `_posts/` directory:
```bash
ls -la _posts/2026/
```

Look at recent posts to see:
- Front matter structure
- Markdown formatting
- Image usage
- Code examples
- Heading hierarchy

## Deployment Questions

### How is the site deployed?

Deployment is fully automatic:

1. Push to `main` branch
2. GitHub Actions builds site
3. Deploys to GitHub Pages
4. Live in 1-3 minutes

No manual deployment needed!

See [Deployment](Deployment) for complete details.

### How long does deployment take?

**Typical timeline**:
- Build: 1-2 minutes
- Deploy: 30-60 seconds
- CDN update: 0-2 minutes
- **Total**: 2-5 minutes from push to live

### Can I preview changes before they go live?

Yes, test locally:
```bash
bundle exec jekyll serve
```

View at `http://localhost:4000` exactly as it will appear in production.

For collaborative preview, consider:
- Netlify Deploy Previews (requires setup)
- Separate staging branch
- Fork and deploy to your own GitHub Pages

### What if something breaks in production?

Quick rollback:
```bash
# Find last working commit
git log --oneline

# Revert to previous commit
git revert <commit-hash>

# Push fix
git push origin main
```

See [Deployment](Deployment) for emergency procedures.

### How do I know if deployment succeeded?

**Check deployment status**:
1. Repository → Actions tab (view workflow runs)
2. Repository → Settings → Pages (deployment status)
3. Visit site and verify changes are live

**Command line**:
```bash
gh run list --limit 5
```

## Contributing Questions

### How can I contribute?

Several ways to contribute:

- **Report bugs** - Open an issue
- **Suggest features** - Open an issue with your idea
- **Fix bugs** - Submit a Pull Request
- **Improve docs** - Update wiki pages
- **Write content** - Submit guest posts
- **Optimize code** - Performance improvements

See [Contributing](Contributing) for guidelines.

### Do I need permission to contribute?

For minor changes (typos, bug fixes): No, just submit a PR.

For major changes (new features, significant refactoring): Yes, open an issue first to discuss.

For guest posts: Yes, propose topic in an issue first.

### What's the contribution workflow?

1. Fork the repository
2. Create feature branch
3. Make changes
4. Test locally
5. Commit with clear message
6. Push to your fork
7. Open Pull Request
8. Address review feedback
9. Merge when approved

See [Contributing](Contributing) for detailed workflow.

### How long until my PR is reviewed?

**Typical timeline**:
- Simple fixes: 1-2 days
- New features: 2-5 days
- Guest posts: 3-7 days (requires thorough review)

Reviews happen as time permits. Be patient!

### My PR was rejected. What now?

Common reasons for rejection:
- Doesn't follow guidelines
- Breaks existing functionality
- Scope too large
- Better alternative exists

**Next steps**:
- Read feedback carefully
- Ask questions if unclear
- Make requested changes
- Resubmit or close as appropriate

## Troubleshooting

### Build fails with dependency errors

```bash
# Reinstall dependencies
rm -rf vendor/bundle
bundle install

# Update gems
bundle update
```

### Images not displaying

Check:
- File path is correct
- Image file committed to repository
- Proper permissions (if local)
- Image URL is valid (if external)

### 404 errors on specific pages

Verify:
- File exists in repository
- Permalink configuration correct
- Front matter is valid
- File naming follows conventions
- Case-sensitive URLs match filenames

### Comments not working

Giscus comments require:
- GitHub Discussions enabled on repository
- Correct configuration in `_config.yml`
- JavaScript enabled in browser
- Not blocked by ad blockers

### Analytics not tracking

Check:
- Tracking ID correct in `_config.yml`
- Jekyll environment is `production`
- Ad blockers disabled for testing
- May take 24-48 hours for first data

## Performance

### How fast should the site load?

**Target metrics**:
- First Contentful Paint: < 1.5s
- Largest Contentful Paint: < 2.5s
- Time to Interactive: < 3.0s
- Overall load: < 3.0s

Static sites are inherently fast due to:
- No server processing
- CDN delivery
- Pre-generated HTML
- Optimized assets

### How can I improve performance?

The site is already optimized, but you can:
- Compress images before uploading
- Minimize custom JavaScript
- Use system fonts
- Lazy load images
- Enable browser caching

See [Technical Architecture](Technical-Architecture) for optimization details.

## Licensing and Legal

### What license is the code under?

Check the `LICENSE` file in the repository for code licensing.

### Can I use the code in my project?

The technical implementation (Jekyll configuration, layouts, includes) can serve as a reference, but:
- Original content is copyrighted
- Don't copy the blog content
- Don't clone and republish verbatim
- Attribution appreciated if using code patterns

### Can I repost or translate articles?

Contact the author for permission:
- Email: jonathan.beckett@gmail.com
- LinkedIn: [linkedin.com/in/jonathanbeckett](https://linkedin.com/in/jonathanbeckett)

Translations and republishing require explicit permission.

## Getting Help

### Where can I ask questions?

1. **Check this FAQ first**
2. **Search existing issues** on GitHub
3. **Open a new issue** for bugs or questions
4. **Email the author** for other matters

### Documentation seems incomplete

Help improve it!
1. Identify what's missing or unclear
2. Open an issue describing the gap
3. Submit a PR with improvements
4. Or just report it and someone will update

### I found a bug in the documentation

Please report it!
- Open an issue describing the error
- Or submit a PR with the fix
- Include page name and what's wrong

## Resources

### Where can I learn more?

**This Wiki**:
- [Getting Started](Getting-Started) - Setup guide
- [Technical Architecture](Technical-Architecture) - System overview
- [Content Guidelines](Content-Guidelines) - Writing standards
- [Contributing](Contributing) - Contribution guide
- [Development Setup](Development-Setup) - Advanced setup
- [Deployment](Deployment) - Deployment process

**External Resources**:
- [Jekyll Documentation](https://jekyllrb.com/docs/)
- [Minimal Mistakes Theme](https://mmistakes.github.io/minimal-mistakes/)
- [GitHub Pages Docs](https://docs.github.com/pages)
- [Markdown Guide](https://www.markdownguide.org/)

---

## Still have questions?

If your question isn't answered here:

1. **Open an issue**: [github.com/jonbeckett/jonbeckett.github.io/issues](https://github.com/jonbeckett/jonbeckett.github.io/issues)
2. **Email**: jonathan.beckett@gmail.com

**Help improve this FAQ** by suggesting questions to add!

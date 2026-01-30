# Deployment

This document explains how jonbeckett.com is deployed from development to production, including the deployment pipeline, GitHub Pages configuration, and troubleshooting deployment issues.

## Deployment Overview

jonbeckett.com uses a fully automated deployment pipeline powered by GitHub Pages and GitHub Actions. Every push to the main branch triggers an automatic build and deployment.

```
Local Development → Git Push → GitHub Actions → Build → GitHub Pages → Live Site
```

## Deployment Architecture

### Hosting Platform: GitHub Pages

**GitHub Pages** provides:
- Free static site hosting
- Automatic SSL/TLS certificates
- Custom domain support
- Global CDN distribution
- 99.9% uptime guarantee
- Built-in Jekyll support

**Specifications:**
- **Repository**: jonbeckett/jonbeckett.github.io
- **Branch**: `main` (source code)
- **Deployment Branch**: Automatic (GitHub Pages manages deployment)
- **Domain**: jonbeckett.com (via CNAME)
- **SSL**: Automatic HTTPS

## Deployment Process

### Standard Deployment Flow

**1. Local Development**
```bash
# Make changes locally
# Test thoroughly
bundle exec jekyll serve

# Commit changes
git add .
git commit -m "Add new blog post"
```

**2. Push to GitHub**
```bash
# Push to main branch
git push origin main
```

**3. Automatic Build**
- GitHub detects push to main branch
- GitHub Actions workflow triggered (or GitHub Pages built-in build)
- Jekyll builds the site
- Static files generated

**4. Deployment**
- Built site deployed to GitHub Pages
- CDN caches cleared
- Site goes live

**5. Live in Minutes**
- Typically 1-3 minutes from push to live
- DNS propagation may take longer for domain changes

### Build Process Details

**GitHub Pages Build Steps:**

1. **Checkout Repository**
   - Pull latest code from main branch

2. **Setup Ruby Environment**
   - Install Ruby (version specified by GitHub Pages)
   - Install Bundler

3. **Install Dependencies**
   ```bash
   bundle install --path vendor/bundle
   ```

4. **Build Jekyll Site**
   ```bash
   JEKYLL_ENV=production bundle exec jekyll build
   ```

5. **Deploy Static Files**
   - Upload `_site/` directory to GitHub Pages servers
   - Update CDN cache

6. **Verify Deployment**
   - Health check
   - HTTPS certificate validation

## GitHub Pages Configuration

### Repository Settings

**Location**: Repository → Settings → Pages

**Configuration:**
- **Source**: Deploy from a branch
- **Branch**: `main` / (root)
- **Custom domain**: jonbeckett.com
- **Enforce HTTPS**: ✓ Enabled

### CNAME Configuration

**File**: `/CNAME`

```
jonbeckett.com
```

**Purpose:**
- Tells GitHub Pages to serve site on custom domain
- Prevents domain from being overwritten during builds
- Required for custom domain support

### DNS Configuration

**At Domain Registrar** (configure A and CNAME records):

**A Records** (point to GitHub Pages):
```
@  A  185.199.108.153
@  A  185.199.109.153
@  A  185.199.110.153
@  A  185.199.111.153
```

**CNAME Record** (for www subdomain):
```
www  CNAME  jonbeckett.github.io.
```

**Verification:**
```bash
# Check A records
dig jonbeckett.com +short

# Check CNAME
dig www.jonbeckett.com +short
```

## GitHub Actions Workflow

If using a custom GitHub Actions workflow (optional for GitHub Pages):

### Workflow File

**Location**: `.github/workflows/jekyll.yml`

```yaml
name: Build and Deploy Jekyll Site

on:
  push:
    branches:
      - main

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    
    steps:
      - name: Checkout
        uses: actions/checkout@v3
        
      - name: Setup Ruby
        uses: ruby/setup-ruby@v1
        with:
          ruby-version: '3.2'
          bundler-cache: true
          
      - name: Build Jekyll site
        run: bundle exec jekyll build
        env:
          JEKYLL_ENV: production
          
      - name: Deploy to GitHub Pages
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./_site
```

### Workflow Features

- **Automatic trigger** on main branch push
- **Ruby caching** for faster builds
- **Production environment** variable set
- **Automated deployment** to gh-pages branch

## Deployment Environments

### Production

**URL**: https://jonbeckett.com

**Environment Variables:**
```yaml
JEKYLL_ENV: production
```

**Configuration:**
- Full analytics enabled
- Comment system active
- All optimizations enabled
- Minified CSS/HTML

### Preview/Staging (Optional)

Can be set up using:
- **Netlify Deploy Previews** (for PRs)
- **Separate branch** deployment
- **GitHub Pages alternative URL** (username.github.io)

## Deployment Checklist

Before deploying:

- [ ] All changes tested locally
- [ ] No broken links
- [ ] Images optimized and working
- [ ] New posts have correct front matter
- [ ] Build succeeds locally
- [ ] No console errors
- [ ] Responsive design verified
- [ ] SEO meta tags present
- [ ] Analytics working (if applicable)
- [ ] Comments enabled (if applicable)

## Monitoring Deployment

### Check Deployment Status

**1. GitHub Actions Tab**
- Navigate to repository → Actions
- View workflow runs
- Check for failures

**2. GitHub Pages Settings**
- Repository → Settings → Pages
- Shows last deployment status
- Displays current published URL

**3. Command Line**
```bash
# Check latest deployment
gh run list --limit 5

# View specific workflow run
gh run view [run-id]
```

### Verify Live Site

**Manual Checks:**
```bash
# Check site is accessible
curl -I https://jonbeckett.com

# Verify HTTPS
curl -sI https://jonbeckett.com | grep -i "HTTP/2 200"

# Check specific page
curl -I https://jonbeckett.com/about/
```

**Automated Monitoring:**
- Use **UptimeRobot** or similar service
- Monitor uptime and performance
- Alert on downtime

## Rollback Procedure

### How to Rollback

If a deployment breaks the site:

**1. Quick Rollback via Git:**
```bash
# Find last working commit
git log --oneline

# Reset to previous commit
git reset --hard <commit-hash>

# Force push (be careful!)
git push --force origin main
```

**2. Revert Specific Commit:**
```bash
# Safer: revert problematic commit
git revert <commit-hash>

# Push revert
git push origin main
```

**3. Manual Fix:**
```bash
# Fix the issue
# Test locally
# Commit and push fix
git add .
git commit -m "Fix deployment issue"
git push origin main
```

### Recovery Time

- **Typical**: 2-5 minutes from push to live
- **DNS changes**: Up to 24-48 hours (rare)
- **SSL issues**: Usually auto-resolve in minutes

## Troubleshooting Deployment Issues

### Build Failures

**Symptom**: Build fails in GitHub Actions

**Solutions:**

1. **Check Build Logs**
   ```
   Repository → Actions → Failed workflow → View logs
   ```

2. **Common Causes:**
   - Syntax errors in Markdown/YAML
   - Missing dependencies in Gemfile
   - Invalid Jekyll configuration
   - Broken Liquid syntax

3. **Fix Process:**
   ```bash
   # Test build locally
   bundle exec jekyll build --verbose
   
   # Fix errors
   # Commit and push
   ```

### Page Not Found (404)

**Symptom**: Deployment succeeds but pages return 404

**Causes & Solutions:**

1. **Incorrect Permalinks:**
   - Check permalink configuration in `_config.yml`
   - Verify post/page front matter

2. **Missing Files:**
   - Ensure files are committed to repository
   - Check `.gitignore` isn't excluding files

3. **Case Sensitivity:**
   - URLs are case-sensitive
   - Check file naming matches URLs

### Site Not Updating

**Symptom**: Changes pushed but site not updating

**Solutions:**

1. **Clear Browser Cache:**
   - Hard refresh: Ctrl+F5 (Windows) or Cmd+Shift+R (Mac)
   - Clear browser cache completely

2. **Check Deployment Status:**
   - Verify build completed successfully
   - Check GitHub Pages settings

3. **CDN Cache:**
   - May take a few minutes to update
   - Usually clears automatically

4. **Force Rebuild:**
   ```bash
   # Make empty commit to trigger rebuild
   git commit --allow-empty -m "Trigger rebuild"
   git push origin main
   ```

### SSL Certificate Issues

**Symptom**: SSL warning or certificate errors

**Solutions:**

1. **Disable and Re-enable HTTPS:**
   - Settings → Pages → Uncheck "Enforce HTTPS"
   - Wait 5 minutes
   - Re-enable "Enforce HTTPS"

2. **Verify DNS:**
   ```bash
   dig jonbeckett.com +short
   # Should show GitHub Pages IPs
   ```

3. **Wait for Propagation:**
   - New domains may take 24-48 hours
   - Certificate provisioning is automatic

### Custom Domain Not Working

**Symptom**: Site accessible at username.github.io but not custom domain

**Solutions:**

1. **Check CNAME File:**
   - Verify `/CNAME` contains correct domain
   - No http:// or https:// prefix
   - No trailing slash

2. **Verify DNS Records:**
   ```bash
   dig jonbeckett.com +short
   dig www.jonbeckett.com +short
   ```

3. **GitHub Pages Settings:**
   - Custom domain field populated
   - DNS check passed (green checkmark)

## Performance Optimization

### Build Performance

**Optimization Techniques:**

1. **Incremental Builds** (local only):
   ```bash
   bundle exec jekyll serve --incremental
   ```

2. **Limit Posts** (development):
   ```yaml
   # _config_dev.yml
   limit_posts: 10
   ```

3. **Exclude Unnecessary Files:**
   ```yaml
   exclude:
     - node_modules/
     - vendor/
     - .git/
   ```

### Site Performance

**Automatically Optimized:**
- Static HTML delivery
- Global CDN caching
- Minified CSS/HTML
- GZIP compression

**Manual Optimizations:**
- Optimize images before upload
- Minimize JavaScript
- Use system fonts
- Lazy load images

## Deployment Best Practices

### 1. Test Before Deploy

Always test locally:
```bash
bundle exec jekyll build
bundle exec jekyll serve
# Verify changes at localhost:4000
```

### 2. Use Meaningful Commit Messages

```bash
# Good
git commit -m "Add post about Jekyll deployment"
git commit -m "Fix broken link in about page"

# Avoid
git commit -m "update"
git commit -m "fixes"
```

### 3. Deploy During Low Traffic

- Schedule major updates for low-traffic times
- Minimize user impact
- Easier to monitor and rollback if needed

### 4. Keep Dependencies Updated

```bash
# Regular updates
bundle update

# Security patches
bundle audit check --update
```

### 5. Monitor After Deployment

- Check site immediately after deployment
- Verify critical pages load
- Monitor analytics for unusual patterns
- Watch for error reports

## Continuous Deployment

### Current Setup

- **Trigger**: Push to main branch
- **Build**: Automatic via GitHub Pages/Actions
- **Deploy**: Automatic to production
- **Rollback**: Manual via Git revert

### Branch Protection (Optional)

Enable branch protection for main:

1. Repository → Settings → Branches
2. Add rule for `main`
3. Configure:
   - Require pull request reviews
   - Require status checks
   - Prevent force pushes (except admins)

### Pull Request Workflow

For safer deployments:

```bash
# Create feature branch
git checkout -b feature/new-post

# Make changes, commit
git add .
git commit -m "Add new post"

# Push to fork
git push origin feature/new-post

# Create PR on GitHub
# Review, test
# Merge to main (triggers deployment)
```

## Deployment Metrics

### Key Metrics to Monitor

1. **Build Time**: Should be < 2 minutes
2. **Deploy Time**: Total process < 5 minutes
3. **Uptime**: Target 99.9%
4. **Page Load Time**: < 3 seconds
5. **Build Success Rate**: > 99%

### Monitoring Tools

- **GitHub Actions**: Build logs and history
- **GitHub Pages**: Deployment status
- **UptimeRobot**: Uptime monitoring
- **Google Analytics**: Traffic and performance
- **Lighthouse**: Performance scoring

## Emergency Procedures

### Site Down

1. Check GitHub Pages status
2. Verify DNS resolution
3. Check SSL certificate
4. Review recent deployments
5. Rollback if necessary

### Critical Bug

1. Assess impact
2. Quick fix if possible
3. Otherwise, rollback immediately
4. Fix properly in separate branch
5. Test thoroughly
6. Deploy fix

### Lost Content

1. Check Git history
2. Restore from commit
3. Verify backups
4. Document incident
5. Improve backup procedures

## Backup and Recovery

### Git as Backup

- Every change tracked in Git
- Full history preserved
- Easy restoration

### Additional Backups

```bash
# Clone repository as backup
git clone --mirror https://github.com/jonbeckett/jonbeckett.github.io.git

# Archive entire site
tar -czf jonbeckett-backup-$(date +%Y%m%d).tar.gz jonbeckett.github.io/
```

## Resources

- **GitHub Pages Documentation**: [docs.github.com/pages](https://docs.github.com/pages)
- **GitHub Actions Documentation**: [docs.github.com/actions](https://docs.github.com/actions)
- **Jekyll Deployment**: [jekyllrb.com/docs/deployment](https://jekyllrb.com/docs/deployment/)

---

**Deployment is automatic and reliable.** The system is designed for safety, with easy rollback capabilities and comprehensive monitoring.

**Related Documentation:**
- [Getting Started](Getting-Started) - Initial setup
- [Development Setup](Development-Setup) - Development environment
- [Technical Architecture](Technical-Architecture) - System architecture

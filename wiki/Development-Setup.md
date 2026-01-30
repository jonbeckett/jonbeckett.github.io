# Development Setup

This guide provides detailed instructions for setting up a complete development environment for jonbeckett.com, including advanced configurations, tools, and workflows for efficient development.

## System Requirements

### Minimum Requirements

- **Operating System**: macOS, Linux, or Windows 10/11 with WSL2
- **RAM**: 4GB minimum, 8GB recommended
- **Disk Space**: 2GB free space
- **Internet**: Broadband connection for initial setup

### Recommended Specifications

- **RAM**: 8GB or more
- **SSD**: For faster build times
- **Modern CPU**: Multi-core for parallel builds

## Installing Ruby

Jekyll requires Ruby 2.7.0 or higher. Choose your installation method based on your operating system.

### macOS

**Using Homebrew (Recommended):**

```bash
# Install Homebrew if not already installed
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Ruby
brew install ruby

# Add to PATH (add to ~/.zshrc or ~/.bash_profile)
echo 'export PATH="/usr/local/opt/ruby/bin:$PATH"' >> ~/.zshrc

# Reload shell configuration
source ~/.zshrc

# Verify installation
ruby --version
```

**Using rbenv (Alternative):**

```bash
# Install rbenv
brew install rbenv ruby-build

# Initialize rbenv
rbenv init

# Install Ruby
rbenv install 3.2.0
rbenv global 3.2.0

# Verify
ruby --version
```

### Linux (Ubuntu/Debian)

```bash
# Update package list
sudo apt-get update

# Install Ruby and development tools
sudo apt-get install ruby-full build-essential zlib1g-dev

# Avoid installing gems as root
echo '# Install Ruby Gems to ~/gems' >> ~/.bashrc
echo 'export GEM_HOME="$HOME/gems"' >> ~/.bashrc
echo 'export PATH="$HOME/gems/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc

# Verify installation
ruby --version
gem --version
```

### Windows

**Using WSL2 (Recommended):**

1. Install WSL2:
   ```powershell
   wsl --install -d Ubuntu
   ```

2. Follow Linux installation steps above within WSL2

**Using RubyInstaller (Alternative):**

1. Download from [rubyinstaller.org](https://rubyinstaller.org/)
2. Run installer (choose version with DevKit)
3. Complete MSYS2 installation when prompted
4. Verify in Command Prompt:
   ```cmd
   ruby --version
   ```

## Installing Bundler

Bundler manages Ruby gem dependencies:

```bash
gem install bundler

# Verify installation
bundle --version
```

## Repository Setup

### 1. Fork and Clone

```bash
# Fork repository on GitHub first, then:
git clone https://github.com/YOUR-USERNAME/jonbeckett.github.io.git
cd jonbeckett.github.io

# Add upstream remote
git remote add upstream https://github.com/jonbeckett/jonbeckett.github.io.git

# Verify remotes
git remote -v
```

### 2. Install Dependencies

```bash
# Install all gems specified in Gemfile
bundle install

# This installs:
# - Jekyll
# - github-pages gem
# - All plugins
# - Dependencies
```

### 3. Configure Git

```bash
# Set your identity
git config user.name "Your Name"
git config user.email "your.email@example.com"

# Optional: Set default branch name
git config --global init.defaultBranch main
```

## Development Server

### Basic Server

```bash
# Start Jekyll development server
bundle exec jekyll serve

# Access at: http://localhost:4000
# Press Ctrl+C to stop
```

### Advanced Server Options

```bash
# Live reload (auto-refresh browser)
bundle exec jekyll serve --livereload

# Different port
bundle exec jekyll serve --port 4001

# Show drafts
bundle exec jekyll serve --drafts

# Future-dated posts
bundle exec jekyll serve --future

# Incremental build (faster)
bundle exec jekyll serve --incremental

# Verbose output
bundle exec jekyll serve --verbose

# Multiple options combined
bundle exec jekyll serve --livereload --drafts --future --port 4001
```

### Development Server Configuration

Create `_config_dev.yml` for development-specific settings:

```yaml
# Development-only configuration
url: "http://localhost:4000"
environment: development

# Faster builds
limit_posts: 10
incremental: true

# Additional debugging
show_drafts: true
future: true
```

Use with:
```bash
bundle exec jekyll serve --config _config.yml,_config_dev.yml
```

## IDE and Editor Setup

### Visual Studio Code

**Recommended Extensions:**

```bash
# Install via Extensions marketplace or command line
code --install-extension yzhang.markdown-all-in-one
code --install-extension davidanson.vscode-markdownlint
code --install-extension ginfuru.ginfuru-vscode-jekyll-syntax
code --install-extension shd101wyy.markdown-preview-enhanced
code --install-extension streetsidesoftware.code-spell-checker
```

**VS Code Settings** (`.vscode/settings.json`):

```json
{
  "editor.formatOnSave": true,
  "editor.wordWrap": "on",
  "files.associations": {
    "*.md": "markdown",
    "*.html": "liquid"
  },
  "markdown.preview.fontSize": 14,
  "markdown.validate.enabled": true,
  "cSpell.words": [
    "jekyll",
    "bundler",
    "kramdown",
    "jonbeckett"
  ],
  "[markdown]": {
    "editor.quickSuggestions": true,
    "editor.defaultFormatter": "yzhang.markdown-all-in-one"
  }
}
```

### Other Editors

**Sublime Text:**
- Markdown Preview
- MarkdownEditing
- SublimeLinter

**Atom:**
- markdown-preview-plus
- linter-markdownlint
- language-liquid

## Build Optimization

### Faster Builds

**1. Use Incremental Builds:**
```bash
bundle exec jekyll serve --incremental
```

**2. Limit Posts During Development:**

Add to `_config_dev.yml`:
```yaml
limit_posts: 10
```

**3. Exclude Unnecessary Files:**

In `_config.yml`:
```yaml
exclude:
  - node_modules/
  - vendor/
  - .git/
  - .vscode/
  - README.md
  - Gemfile.lock
```

**4. Use LiveReload Instead of Polling:**
```bash
bundle exec jekyll serve --livereload
```

### Build Performance Monitoring

```bash
# Profile build
bundle exec jekyll build --profile

# Analyze what's taking time
```

## Version Control Workflow

### Branching Strategy

```bash
# Create feature branch
git checkout -b feature/your-feature-name

# Create fix branch
git checkout -b fix/bug-description

# Create content branch
git checkout -b content/post-title
```

### Daily Workflow

```bash
# Start your day: Update from upstream
git checkout main
git pull upstream main

# Create feature branch
git checkout -b feature/new-feature

# Make changes...

# Stage and commit
git add .
git commit -m "feat: Add new feature"

# Push to your fork
git push origin feature/new-feature

# Create Pull Request on GitHub
```

### Keeping Fork Updated

```bash
# Fetch latest from upstream
git fetch upstream

# Merge upstream/main into your main
git checkout main
git merge upstream/main

# Push updates to your fork
git push origin main
```

## Testing

### Manual Testing

```bash
# Clean build
bundle exec jekyll clean
bundle exec jekyll build

# Serve locally
bundle exec jekyll serve

# Test checklist:
# - All pages load
# - Links work
# - Images display
# - No 404s
# - Responsive design
# - No console errors
```

### Automated Testing (Optional)

**HTML Proofer** - Check for broken links and HTML issues:

```ruby
# Add to Gemfile
gem 'html-proofer'
```

```bash
# Install
bundle install

# Run tests
bundle exec htmlproofer ./_site \
  --disable-external \
  --allow-hash-href \
  --assume-extension
```

## Dependency Management

### Updating Gems

```bash
# Update all gems
bundle update

# Update specific gem
bundle update jekyll

# Show outdated gems
bundle outdated
```

### Security Updates

```bash
# Check for vulnerabilities
bundle audit check --update

# Install bundle-audit if not present
gem install bundler-audit
```

### Gemfile.lock

Always commit `Gemfile.lock`:
- Ensures consistent builds
- Locks dependency versions
- Critical for reproducibility

## Debugging

### Common Issues and Solutions

**Build Failures:**

```bash
# Clear cache and rebuild
bundle exec jekyll clean
rm -rf _site .jekyll-cache
bundle exec jekyll build --verbose
```

**Dependency Conflicts:**

```bash
# Reinstall all gems
rm -rf vendor/bundle
bundle install
```

**SSL Certificate Errors:**

```bash
# Update certificates
gem update --system
```

**Port Already in Use:**

```bash
# Find process on port 4000
lsof -i :4000

# Kill process
kill -9 <PID>

# Or use different port
bundle exec jekyll serve --port 4001
```

### Debug Mode

Enable verbose output:

```bash
bundle exec jekyll serve --verbose --trace
```

Check liquid template errors:
```yaml
# In _config.yml
liquid:
  error_mode: strict
  strict_filters: true
  strict_variables: true
```

## Development Tools

### Useful Command Aliases

Add to `~/.bashrc` or `~/.zshrc`:

```bash
# Jekyll shortcuts
alias jserve='bundle exec jekyll serve --livereload'
alias jbuild='bundle exec jekyll build'
alias jclean='bundle exec jekyll clean'
alias jdraft='bundle exec jekyll serve --drafts --future'

# Git shortcuts
alias gs='git status'
alias ga='git add'
alias gc='git commit -m'
alias gp='git push'
alias gl='git log --oneline'
```

### Make Commands (Optional)

Create `Makefile`:

```makefile
.PHONY: install serve build clean

install:
	bundle install

serve:
	bundle exec jekyll serve --livereload

build:
	bundle exec jekyll build

clean:
	bundle exec jekyll clean

draft:
	bundle exec jekyll serve --drafts --future

update:
	bundle update
```

Usage:
```bash
make install
make serve
make build
```

## Browser DevTools

### Useful for Development

**Chrome DevTools:**
- Inspect responsive design
- Check console for errors
- Monitor network requests
- Test accessibility
- Performance profiling

**Firefox Developer Tools:**
- Similar features to Chrome
- Excellent CSS grid inspector
- Accessibility inspector

### Testing Responsive Design

```bash
# Serve on network (accessible from mobile devices)
bundle exec jekyll serve --host=0.0.0.0

# Find your local IP
# macOS/Linux:
ifconfig | grep inet
# Access from mobile: http://YOUR-IP:4000
```

## Performance Profiling

### Build Time Analysis

```bash
# Profile build performance
bundle exec jekyll build --profile

# Shows:
# - Time per file
# - Slowest includes
# - Plugin performance
```

### Page Load Performance

Use browser DevTools:
1. Open DevTools (F12)
2. Go to Network tab
3. Reload page
4. Analyze load times
5. Check for bottlenecks

## Environment Variables

### Setting Environment Variables

**macOS/Linux:**
```bash
export JEKYLL_ENV=production
bundle exec jekyll build
```

**Windows (PowerShell):**
```powershell
$env:JEKYLL_ENV="production"
bundle exec jekyll build
```

### Using in Configuration

```yaml
# Different configs per environment
production:
  analytics: true
  
development:
  analytics: false
```

## Documentation

### Keeping Documentation Updated

When making changes:
1. Update relevant wiki pages
2. Keep README.md current
3. Document new features
4. Update configuration examples
5. Add troubleshooting tips

## Next Steps

Now that your development environment is set up:

1. Review [Content Guidelines](Content-Guidelines) for writing standards
2. Check [Technical Architecture](Technical-Architecture) to understand the platform
3. Read [Contributing](Contributing) before making contributions
4. Explore the codebase and existing posts
5. Start developing!

## Resources

### Official Documentation

- **Jekyll**: [jekyllrb.com/docs](https://jekyllrb.com/docs/)
- **Minimal Mistakes**: [mmistakes.github.io/minimal-mistakes](https://mmistakes.github.io/minimal-mistakes/)
- **GitHub Pages**: [docs.github.com/pages](https://docs.github.com/pages)
- **Liquid Templates**: [shopify.github.io/liquid](https://shopify.github.io/liquid/)
- **Kramdown**: [kramdown.gettalong.org](https://kramdown.gettalong.org/)

### Community

- **Jekyll Forum**: [talk.jekyllrb.com](https://talk.jekyllrb.com/)
- **Stack Overflow**: Tag `jekyll`
- **GitHub Issues**: For this specific project

---

**You're all set!** Your development environment is ready for productive work on jonbeckett.com.

**Related Documentation:**
- [Getting Started](Getting-Started) - Quick start guide
- [Technical Architecture](Technical-Architecture) - Understanding the stack
- [Deployment](Deployment) - How deployment works

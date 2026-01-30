# Contributing

Thank you for your interest in contributing to jonbeckett.com! This guide outlines how you can contribute to this blog, whether through content, code improvements, bug fixes, or documentation.

## Ways to Contribute

There are several ways you can contribute to this project:

1. **Report Issues** - Found a bug or broken link? Let us know!
2. **Suggest Improvements** - Ideas for new features or enhancements
3. **Fix Bugs** - Submit fixes for identified issues
4. **Improve Documentation** - Help make the docs clearer
5. **Submit Content** - Guest posts and article contributions
6. **Enhance Design** - Suggest or implement UI/UX improvements
7. **Optimize Performance** - Help make the site faster

## Getting Started

### Prerequisites

Before contributing, ensure you have:

1. A GitHub account
2. Git installed locally
3. Ruby and Bundler installed
4. Familiarity with Markdown and Jekyll
5. Understanding of the project (read the [Getting Started](Getting-Started) guide)

### Development Setup

1. **Fork the Repository**

   Click the "Fork" button at the top of the [repository page](https://github.com/jonbeckett/jonbeckett.github.io).

2. **Clone Your Fork**

   ```bash
   git clone https://github.com/YOUR-USERNAME/jonbeckett.github.io.git
   cd jonbeckett.github.io
   ```

3. **Add Upstream Remote**

   ```bash
   git remote add upstream https://github.com/jonbeckett/jonbeckett.github.io.git
   ```

4. **Install Dependencies**

   ```bash
   bundle install
   ```

5. **Create a Branch**

   ```bash
   git checkout -b feature/your-feature-name
   # or
   git checkout -b fix/your-bugfix-name
   ```

## Contributing Content

### Guest Post Guidelines

Guest posts are welcome! Follow these guidelines:

**Before Writing:**
1. Open an issue proposing your topic
2. Wait for approval to avoid duplicate work
3. Review [Content Guidelines](Content-Guidelines)
4. Check existing posts to avoid overlap

**Writing Process:**
1. Follow the [Content Guidelines](Content-Guidelines) strictly
2. Create your post in `_posts/YYYY/` directory
3. Use proper file naming: `YYYY-MM-DD-post-title.md`
4. Include all required front matter
5. Test locally before submitting

**Submission:**
1. Commit your post to your fork
2. Open a Pull Request
3. Provide a clear description
4. Be responsive to feedback
5. Make requested changes promptly

### Author Attribution

Guest posts will include author information:

```yaml
---
author: Your Name
author_profile: true
# Additional author info in _data/authors.yml if needed
---
```

## Contributing Code

### Code Contribution Process

1. **Find or Create an Issue**
   - Check existing issues for tasks to work on
   - Create a new issue for significant changes
   - Discuss approach before implementing

2. **Branch Naming Conventions**
   - `feature/` - New features
   - `fix/` - Bug fixes
   - `docs/` - Documentation updates
   - `refactor/` - Code refactoring
   - `style/` - Styling changes

   Examples:
   - `feature/add-search-functionality`
   - `fix/broken-pagination`
   - `docs/update-setup-guide`

3. **Make Your Changes**
   - Follow existing code style
   - Test thoroughly locally
   - Keep changes focused and minimal
   - Write clear commit messages

4. **Test Your Changes**
   ```bash
   # Build the site
   bundle exec jekyll build
   
   # Serve locally
   bundle exec jekyll serve
   
   # Test at http://localhost:4000
   ```

5. **Commit Guidelines**
   ```bash
   # Good commit messages
   git commit -m "Fix broken pagination on category pages"
   git commit -m "Add search functionality using Lunr.js"
   git commit -m "Update README with deployment instructions"
   
   # Avoid vague messages
   git commit -m "fix stuff"
   git commit -m "updates"
   git commit -m "WIP"
   ```

6. **Push and Create Pull Request**
   ```bash
   git push origin your-branch-name
   ```
   
   Then open a Pull Request on GitHub.

### Pull Request Guidelines

**PR Title:**
- Clear and descriptive
- Use imperative mood: "Add feature" not "Added feature"
- Examples:
  - "Fix broken links in about page"
  - "Add dark mode toggle"
  - "Update dependencies to latest versions"

**PR Description Should Include:**
- What changes were made
- Why the changes were needed
- How to test the changes
- Screenshots (for visual changes)
- Related issue numbers (e.g., "Closes #42")

**PR Template:**
```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Code refactoring
- [ ] Performance improvement

## Changes Made
- List of specific changes
- One item per change

## Testing
- [ ] Tested locally
- [ ] All links verified
- [ ] Responsive design checked
- [ ] Build completes successfully

## Screenshots (if applicable)
[Add screenshots here]

## Related Issues
Closes #[issue number]
```

### Code Review Process

1. Maintainer reviews PR
2. Feedback provided if changes needed
3. You address feedback and push updates
4. Approval granted when ready
5. PR merged by maintainer

**Review Timeline:**
- Most PRs reviewed within 2-3 days
- Complex changes may take longer
- Be patient and responsive

## Reporting Issues

### Creating Good Bug Reports

When reporting a bug, include:

1. **Clear Title**
   - Specific and descriptive
   - Example: "Pagination broken on categories page"

2. **Environment**
   - Browser and version
   - Operating system
   - Device type (desktop/mobile)

3. **Steps to Reproduce**
   ```markdown
   1. Go to 'Categories' page
   2. Click on 'Software Development'
   3. Scroll to bottom
   4. Click 'Next Page'
   ```

4. **Expected Behavior**
   - What should happen

5. **Actual Behavior**
   - What actually happens

6. **Screenshots/Error Messages**
   - Visual proof of issue
   - Console errors if applicable

### Feature Requests

For feature suggestions, include:

1. **Problem Statement**
   - What problem does this solve?
   - Who would benefit?

2. **Proposed Solution**
   - How should it work?
   - Any examples from other sites?

3. **Alternatives Considered**
   - Other approaches you thought about

4. **Additional Context**
   - Mockups, examples, references

## Style Guide

### Code Style

**HTML/Liquid:**
- 2-space indentation
- Lowercase tags and attributes
- Quote attribute values
- Self-closing tags when appropriate

**CSS/SCSS:**
- 2-space indentation
- One selector per line
- Properties alphabetically ordered
- Use variables for colors and common values

**JavaScript:**
- 2-space indentation
- Semicolons required
- Single quotes for strings
- Modern ES6+ syntax

**Markdown:**
- Follow [Content Guidelines](Content-Guidelines)
- Consistent heading hierarchy
- Proper code block language specification

### File Naming

- **Posts**: `YYYY-MM-DD-post-title-in-lowercase.md`
- **Pages**: `descriptive-name.md`
- **Images**: `descriptive-name.jpg` (lowercase, hyphens)
- **Data files**: `descriptive-name.yml`

## Testing

### Before Submitting

Always test your changes locally:

```bash
# Clean build
bundle exec jekyll clean
bundle exec jekyll build

# Serve and test
bundle exec jekyll serve --livereload

# Check at http://localhost:4000
```

### Testing Checklist

- [ ] All pages load without errors
- [ ] Links work correctly
- [ ] Images display properly
- [ ] Responsive design on mobile
- [ ] No console errors
- [ ] Build completes successfully
- [ ] No broken internal links
- [ ] Proper formatting maintained

## Commit Message Guidelines

### Format

```
<type>: <subject>

<body>

<footer>
```

### Type

- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, no logic change)
- `refactor`: Code refactoring
- `perf`: Performance improvements
- `test`: Adding tests
- `chore`: Maintenance tasks

### Examples

```bash
feat: Add search functionality with Lunr.js

Implemented client-side search using Lunr.js for fast,
offline-capable search across all posts.

Closes #15

---

fix: Correct broken pagination on archive pages

The pagination was not working on category archive pages
due to incorrect liquid template logic.

---

docs: Update development setup instructions

Added missing steps for Windows users and clarified
Ruby version requirements.
```

## Community Guidelines

### Code of Conduct

We are committed to providing a welcoming and inclusive environment. Please:

- **Be respectful** - Treat everyone with respect and kindness
- **Be constructive** - Provide helpful, actionable feedback
- **Be collaborative** - Work together toward shared goals
- **Be patient** - Remember everyone is learning
- **Be open** - Welcome newcomers and different perspectives

### Communication

- **Issues**: Technical discussions, bug reports, feature requests
- **Pull Requests**: Code review and implementation discussions
- **Email**: Direct contact for sensitive matters

## Recognition

Contributors will be recognized in the following ways:

1. **Git history**: All contributions tracked via commits
2. **Author credit**: Guest posts include full author attribution
3. **Acknowledgments**: Significant contributions noted in posts/docs
4. **Contributors list**: May be added to README or dedicated page

## Getting Help

If you need assistance:

1. **Read the documentation** - Most questions answered in wiki
2. **Check existing issues** - Your question may be already answered
3. **Open an issue** - Ask for help with a specific problem
4. **Contact maintainer** - For other concerns

## License

By contributing to this project, you agree that your contributions will be licensed under the same license as the project (see LICENSE file).

## Questions?

If you have questions about contributing:

- Open an issue with the question
- Email: jonathan.beckett@gmail.com
- Check the [FAQ](FAQ)

---

**Thank you for contributing to jonbeckett.com!**

Your contributions, whether large or small, help make this blog better for everyone. We appreciate your time and effort.

**Related Documentation:**
- [Getting Started](Getting-Started) - Setup guide
- [Content Guidelines](Content-Guidelines) - Writing standards
- [Development Setup](Development-Setup) - Advanced development configuration

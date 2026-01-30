# Content Guidelines

This guide outlines the standards, best practices, and guidelines for creating content on jonbeckett.com. Following these guidelines ensures consistency, quality, and maintainability across all blog posts.

## Content Philosophy

jonbeckett.com focuses on **thoughtful, in-depth technical content** rather than quick news or hot takes. Content should:

- **Provide lasting value** - Articles remain relevant beyond the publication date
- **Go deep, not wide** - Thorough exploration of topics over superficial coverage
- **Be well-researched** - Backed by experience, examples, and credible sources
- **Remain accessible** - Technical without being unnecessarily complex
- **Encourage thinking** - Provoke reflection and discussion

## Target Audience

The primary audience consists of:

- **Software developers** - From junior to senior levels
- **Technology professionals** - DevOps, architects, tech leads
- **Productivity enthusiasts** - Those interested in workflows and systems
- **Lifelong learners** - Curious minds interested in technology evolution

Write assuming readers have:
- Basic programming knowledge
- Familiarity with common development concepts
- Interest in improving their skills and understanding
- Limited time but willingness to invest in quality content

## Content Categories

### Primary Categories

**Software Development**
- Development methodologies and practices
- Programming languages and frameworks
- Software architecture and design patterns
- Code quality and best practices
- Testing and quality assurance

**Productivity**
- Note-taking systems and methods
- Workflow optimization
- Knowledge management
- Tool comparisons and recommendations
- Personal productivity techniques

**Technology Evolution**
- Historical perspectives on technology
- Analysis of technological trends
- Impact of technology on society and work
- Future implications of current developments

**Web Development**
- Modern web technologies
- Frontend and backend development
- Performance optimization
- Accessibility and user experience

**DevOps & Automation**
- CI/CD pipelines
- Infrastructure as code
- Automation workflows
- Cloud services and platforms

## Writing Style

### Tone and Voice

- **Conversational but professional** - Approachable without being casual
- **British English** - Spelling, grammar, and idioms
- **First-person perspective** - Personal experiences and opinions
- **Honest and authentic** - Acknowledge uncertainties and limitations
- **Humor when appropriate** - Light touches, never forced

### Style Guidelines

**Structure:**
- Clear, descriptive headings (H2, H3)
- Short paragraphs (3-5 sentences)
- Bulleted lists for multiple points
- Code examples where relevant
- Logical flow from introduction to conclusion

**Language:**
- Active voice preferred over passive
- Clear, direct sentences
- Avoid jargon unless necessary (explain when used)
- Use analogies and examples for complex concepts
- Define acronyms on first use

**Examples:**
```markdown
✓ Good: "I use TypeScript for its type safety and developer experience."
✗ Avoid: "TypeScript is utilized due to type safety being beneficial."

✓ Good: "The build failed because of a missing dependency."
✗ Avoid: "A build failure was experienced as a dependency was missing."
```

## Post Structure

### Required Front Matter

Every post must include YAML front matter with essential metadata:

```yaml
---
title: "Clear, Descriptive Post Title"
layout: single
date: YYYY-MM-DD
categories:
  - primary-category
tags:
  - specific-tag-1
  - specific-tag-2
  - specific-tag-3
excerpt: "A compelling 1-2 sentence description of the post."
header:
  overlay_image: "https://example.com/image.jpg"
  overlay_filter: "linear-gradient(90deg, rgba(0,0,0,0.9) 0%, rgba(0,0,0,0.5) 100%)"
  caption: "Photo credit with link"
  teaser: "https://example.com/teaser.jpg"
---
```

### Post Organization

**1. Opening**
- Hook that draws readers in
- Context and relevance
- What the reader will learn

**2. Main Content**
- Logical sections with clear headings
- Progressive complexity (simple to advanced)
- Examples and code samples
- Visual aids where helpful (diagrams, screenshots)

**3. Conclusion**
- Summary of key points
- Actionable takeaways
- Invitation for discussion or questions

**4. Optional Sections**
- Resources and further reading
- Acknowledgments
- Updates or corrections (with dates)

### Example Structure

```markdown
---
# Front matter
---

# Post Title

Opening paragraph that hooks the reader and explains what the post covers.

## Introduction

Why this topic matters and what context readers need.

## Main Topic Section 1

Detailed exploration of the first major point.

### Subsection

Diving deeper into specifics.

## Main Topic Section 2

Second major point with examples.

## Main Topic Section 3

Final major point or synthesis.

## Conclusion

Summary and takeaways.

---

*[Optional footer note or update]*
```

## Title Guidelines

### Title Best Practices

- **Descriptive and specific** - Clearly indicates content
- **Reasonable length** - 40-70 characters ideal
- **Keyword-rich** - SEO-friendly without keyword stuffing
- **Avoid clickbait** - Accurate representation of content
- **Use title case** - Capitalize major words

### Title Examples

```markdown
✓ Good: "The AI Revolution in Note-Taking: How Artificial Intelligence is Reshaping Knowledge Work"
✓ Good: "Ruby on Rails: The Framework That Changed Web Development Forever"
✓ Good: "Moving Target: The Unique Challenges of Testing in Agile Development"

✗ Avoid: "This One Weird Trick Will Change Your Coding Forever!"
✗ Avoid: "notes" (too vague)
✗ Avoid: "The Complete Comprehensive Guide to Everything About Programming Languages and Their History" (too long)
```

## Markdown Usage

### Headings

Use proper heading hierarchy:

```markdown
# Post Title (H1 - used only once, in title)
## Main Sections (H2)
### Subsections (H3)
#### Minor subsections (H4)
```

### Code Blocks

Always specify language for syntax highlighting:

```markdown
```javascript
function example() {
  return "Hello, World!";
}
```
```

Supported languages: `javascript`, `python`, `ruby`, `bash`, `yaml`, `markdown`, `css`, `html`, etc.

### Inline Code

Use backticks for inline code, commands, file names:

```markdown
Install dependencies with `npm install` and run `npm start`.
Edit the `_config.yml` file in the root directory.
```

### Links

Descriptive link text (never "click here"):

```markdown
✓ Good: Read the [Jekyll documentation](https://jekyllrb.com/docs/) for details.
✗ Avoid: Click [here](https://jekyllrb.com/docs/) for documentation.
```

### Lists

Bulleted lists for unordered items:
```markdown
- First item
- Second item
- Third item
```

Numbered lists for sequential steps:
```markdown
1. First step
2. Second step
3. Third step
```

### Emphasis

```markdown
*Italic* for emphasis
**Bold** for strong emphasis
***Bold and italic*** for very strong emphasis
```

### Blockquotes

For quotes or callouts:

```markdown
> "Good code is its own best documentation."
> — Steve McConnell
```

## Images and Media

### Image Requirements

- **Format**: JPG for photos, PNG for graphics, SVG for logos
- **Size**: Optimize before upload (compress, resize)
- **Attribution**: Always credit source if not original
- **Alt text**: Describe image for accessibility

### Header Images

**Overlay Images** (full-width banner):
```yaml
header:
  overlay_image: "https://images.unsplash.com/photo-id?w=1200&h=400&fit=crop"
  overlay_filter: "linear-gradient(90deg, rgba(0,0,0,0.9) 0%, rgba(0,0,0,0.5) 100%)"
  caption: "Photo by [Photographer](https://unsplash.com/@photographer) on [Unsplash](https://unsplash.com)"
  teaser: "https://images.unsplash.com/photo-id?w=600&h=300&fit=crop"
```

**Image Best Practices:**
- Use Unsplash for free, high-quality stock photos
- Specify crop and size parameters in URL
- Consistent dimensions: 1200x400 for overlay, 600x300 for teaser
- Dark overlay for text readability

## SEO Guidelines

### Excerpt Optimization

Write compelling excerpts that:
- Summarize the post in 1-2 sentences
- Include primary keywords naturally
- Encourage clicks without misleading
- Stay under 160 characters for search snippets

### Keyword Usage

- Use primary keyword in title
- Include in first paragraph
- Distribute naturally throughout content
- Use in headings where appropriate
- Don't force or over-optimize

### Meta Information

All handled via front matter:
- Title → page title and social sharing
- Excerpt → meta description
- Categories/Tags → topic organization
- Header images → social media previews

## Categories and Tags

### Categories

Use **one or two** broad categories per post:

- `artificial-intelligence`
- `productivity`
- `software-development`
- `web-development`
- `devops`
- `technology`

### Tags

Use **3-7** specific tags per post:

Examples:
- `jekyll`, `static-sites`, `github-pages`
- `typescript`, `javascript`, `testing`
- `note-taking`, `productivity`, `knowledge-management`
- `ci-cd`, `github-actions`, `automation`

**Tag Guidelines:**
- Lowercase with hyphens
- Specific and relevant
- Consistent with existing tags
- Avoid tag bloat (check existing tags first)

## Code Examples

### Quality Standards

Code examples should:
- Be tested and working
- Follow language best practices
- Include comments for complex logic
- Be concise yet complete
- Use meaningful variable names

### Example Format

```javascript
// Good: Clear, working example with context
function calculateTotal(items) {
  return items.reduce((sum, item) => sum + item.price, 0);
}

const cartItems = [
  { name: 'Widget', price: 10 },
  { name: 'Gadget', price: 20 }
];

const total = calculateTotal(cartItems);
console.log(`Total: $${total}`); // Output: Total: $30
```

## Accuracy and Fact-Checking

### Research Standards

- **Verify facts** before publishing
- **Cite sources** for statistics and quotes
- **Link to documentation** for technical claims
- **Update posts** when information changes
- **Acknowledge uncertainty** when appropriate

### Technical Accuracy

- Test code examples
- Verify command syntax
- Check version compatibility
- Note environment-specific issues
- Update for deprecated features

## Revision and Updates

### Post Updates

When updating published posts:

```markdown
---

**Update (January 2026)**: [Brief description of what changed and why]

*Original post from [original date]*
```

### Version Control

- All changes tracked in Git
- Meaningful commit messages
- Preserve post history
- Document major revisions

## Checklist Before Publishing

- [ ] Front matter complete and accurate
- [ ] Title follows guidelines
- [ ] Excerpt written and compelling
- [ ] Categories and tags applied
- [ ] Header image included with attribution
- [ ] Code examples tested
- [ ] Links verified
- [ ] Spelling and grammar checked
- [ ] Markdown properly formatted
- [ ] Headings follow hierarchy
- [ ] SEO elements optimized
- [ ] Images optimized and credited
- [ ] Content provides value
- [ ] Local preview looks correct

## Common Mistakes to Avoid

1. **Vague titles** - Be specific about content
2. **Missing front matter** - Required for proper rendering
3. **Broken heading hierarchy** - Use H2, H3, H4 in order
4. **Unsourced images** - Always credit sources
5. **Untested code** - Verify all examples work
6. **Too much jargon** - Explain technical terms
7. **No conclusion** - Summarize key points
8. **Inconsistent formatting** - Follow style guide
9. **Over-optimization for SEO** - Write for humans first
10. **Forgetting the audience** - Keep readers' needs in mind

## Resources

- **Markdown Guide**: [markdownguide.org](https://www.markdownguide.org/)
- **Hemingway Editor**: Check readability
- **Grammarly**: Grammar and style checking
- **Unsplash**: Free stock photos
- **Jekyll Docs**: [jekyllrb.com/docs](https://jekyllrb.com/docs/)
- **Minimal Mistakes**: [Theme documentation](https://mmistakes.github.io/minimal-mistakes/)

---

**Remember**: Quality over quantity. One excellent, well-researched post is more valuable than several mediocre ones.

**Related Documentation:**
- [Getting Started](Getting-Started) - Setup guide
- [Technical Architecture](Technical-Architecture) - Understanding the platform
- [Contributing](Contributing) - How to contribute content

# Quality Control and Common Mistakes

This skill defines quality standards, common pitfalls, and best practices to ensure consistent, high-quality blog content.

## Quality Control Checklist

### Before Publishing
- [ ] File follows exact naming convention: `_posts/YYYY/YYYY-MM-DD-slug-title.md`
- [ ] Complete front matter with all required fields
- [ ] British English spelling used throughout
- [ ] **Unsplash images properly configured**:
  - [ ] Photo ID extracted from page source (not URL slug)
  - [ ] Both header (1200x400) and teaser (600x300) URLs tested and working
  - [ ] Photographer attribution complete and accurate
  - [ ] Images display correctly in browser preview
- [ ] Content meets minimum length requirements (2000+ words)
- [ ] Headers create logical hierarchy (H2, H3, H4)
- [ ] Code blocks use proper syntax highlighting
- [ ] Links use descriptive text, not "click here"
- [ ] Local build succeeds without errors

### Content Quality Standards
- [ ] Opening hook engages the reader immediately
- [ ] Historical context provides background and evolution
- [ ] Technical explanations are detailed but accessible
- [ ] Real-world examples and implementations included
- [ ] Forward-looking analysis and predictions provided
- [ ] Evidence-based arguments with specific examples

## Common Mistakes to Avoid

### ❌ File and Structure Mistakes
- Creating posts without proper front matter
- Using incorrect file naming convention
- Placing posts outside year subdirectories
- Missing required front matter fields
- Using American English spelling

### ❌ Content Mistakes
- Writing generic, SEO-keyword-stuffed content
- Skipping historical context and evolution
- Providing shallow technical explanations
- Missing practical applications and examples
- Forgetting forward-looking analysis

### ❌ Image Mistakes
- Using URL slug as photo ID instead of extracting from page source
- Not testing image URLs before publishing
- Incorrect Unsplash photo ID format
- Using premium/plus images that don't work with standard URLs
- Missing or incomplete photographer attribution
- Copy-pasting attribution from wrong photographer
- Broken links to photographer profiles
- Poor image selection that doesn't match content theme

### ❌ Technical Mistakes
- Inconsistent Markdown formatting
- Code blocks without syntax highlighting
- Breaking archive configuration (using jekyll-archives)
- Not testing locally before committing
- Missing or incorrect category/tag assignments

## Best Practices Checklist

### ✅ File Management
- Follow established naming convention exactly
- Organize posts by year in subdirectories
- Include complete, properly formatted front matter
- Test locally before committing changes

### ✅ Content Excellence
- Write narrative-driven, technically accurate content
- Include comprehensive coverage from multiple angles
- Provide historical context and evolution
- Offer practical applications and real-world examples
- Balance technical depth with accessibility

### ✅ Technical Standards
- Use proper Markdown and code formatting
- Maintain consistent voice and style throughout
- Include relevant images with proper attribution
- Ensure all links and references are valid
- Follow British English spelling conventions

### ✅ SEO and Discoverability
- Write descriptive, keyword-rich titles
- Create compelling excerpts for social sharing
- Use relevant categories and tags consistently
- Ensure proper header hierarchy for navigation
- Include meta descriptions via excerpt field

## Review Process

### Self-Review Steps
1. **Structure Check**: Verify file naming, front matter, and organization
2. **Content Review**: Ensure depth, accuracy, and engaging narrative
3. **Technical Review**: Check formatting, links, and code examples
4. **Language Review**: Verify British English spelling throughout
5. **Local Testing**: Build and review site locally
6. **Final Check**: Confirm all quality standards are met

### Common Quality Issues

#### Content Issues
- Lack of historical context or evolution
- Shallow technical explanations
- Missing practical applications
- Generic or keyword-stuffed writing
- Poor narrative flow

#### Technical Issues
- Broken image URLs or missing attribution
- Inconsistent Markdown formatting
- Missing syntax highlighting in code blocks
- Incorrect front matter structure
- Archive configuration problems

#### Language Issues
- American English spellings (organize vs organise)
- Inconsistent voice or tone
- Poor section header naming
- Missing or weak opening hooks
- Lack of forward-looking analysis

## Continuous Improvement

### Regular Maintenance
- Review and update common categories and tags
- Monitor for broken links or images
- Update technical examples for currency
- Refine writing style based on feedback
- Maintain consistency across all posts

### Performance Monitoring
- Track build times and site performance
- Monitor for deployment issues
- Review analytics for popular content
- Identify opportunities for content updates
- Ensure mobile responsiveness and accessibility
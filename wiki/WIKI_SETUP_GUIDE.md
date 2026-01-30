# How to Populate the GitHub Wiki

This guide explains how to transfer the wiki content from this directory to the GitHub repository wiki.

## Background

GitHub wikis are powered by a separate git repository with a `.wiki` extension. The wiki content in this directory is ready to be copied to the GitHub wiki.

## Method 1: Manual Copy (Recommended for Initial Setup)

### Step 1: Enable the Wiki

1. Go to your GitHub repository: https://github.com/jonbeckett/jonbeckett.github.io
2. Click on **Settings**
3. Scroll down to **Features**
4. Check **Wikis** to enable the wiki

### Step 2: Create Wiki Pages

For each markdown file in this directory:

1. Go to the repository's **Wiki** tab
2. Click **Create the first page** or **New Page**
3. Copy the content from the corresponding `.md` file
4. **Important**: Use the filename without the `.md` extension as the page title
   - Example: `Home.md` → page title: "Home"
   - Example: `Getting-Started.md` → page title: "Getting-Started"
5. Paste the content into the wiki editor
6. Click **Save Page**

### Page Creation Order

Create pages in this order to ensure links work:

1. Home
2. Getting-Started
3. Technical-Architecture
4. Content-Guidelines
5. Contributing
6. Development-Setup
7. Deployment
8. FAQ

### Step 3: Verify Links

After creating all pages:
1. Visit the wiki home page
2. Click through all internal links
3. Ensure navigation works correctly

## Method 2: Git Clone and Push (Advanced)

If you prefer using git:

### Step 1: Clone the Wiki Repository

```bash
# Clone the wiki repo (separate from main repo)
git clone https://github.com/jonbeckett/jonbeckett.github.io.wiki.git
cd jonbeckett.github.io.wiki
```

### Step 2: Copy Wiki Files

```bash
# Copy all markdown files from the wiki directory
cp ../jonbeckett.github.io/wiki/*.md .

# Remove README.md as it's not needed in the wiki repo
rm README.md WIKI_SETUP_GUIDE.md
```

### Step 3: Commit and Push

```bash
git add *.md
git commit -m "Add comprehensive wiki documentation"
git push origin master
```

### Step 4: Verify

Visit https://github.com/jonbeckett/jonbeckett.github.io/wiki to see the populated wiki.

## Method 3: Using GitHub's Web Interface (Easiest)

### For Each File:

1. Open the markdown file in this directory
2. Copy all content (Ctrl+A, Ctrl+C)
3. Go to GitHub repository → Wiki tab
4. Click "New Page"
5. Enter page title (filename without .md)
6. Paste content
7. Click "Save Page"

## Wiki Page Titles

Use these exact titles (GitHub will handle the URLs):

| File Name | Wiki Page Title |
|-----------|----------------|
| Home.md | Home |
| Getting-Started.md | Getting-Started |
| Technical-Architecture.md | Technical-Architecture |
| Content-Guidelines.md | Content-Guidelines |
| Contributing.md | Contributing |
| Development-Setup.md | Development-Setup |
| Deployment.md | Deployment |
| FAQ.md | FAQ |

## After Populating the Wiki

### Customize the Sidebar (Optional)

Create a `_Sidebar.md` page in the wiki:

```markdown
## Navigation

- [Home](Home)
- [Getting Started](Getting-Started)
- [Technical Architecture](Technical-Architecture)
- [Content Guidelines](Content-Guidelines)
- [Contributing](Contributing)
- [Development Setup](Development-Setup)
- [Deployment](Deployment)
- [FAQ](FAQ)
```

### Customize the Footer (Optional)

Create a `_Footer.md` page in the wiki:

```markdown
---
© 2026 Jonathan Beckett | [jonbeckett.com](https://jonbeckett.com)
```

## Maintaining the Wiki

### Keeping Content in Sync

The `wiki/` directory in the main repository serves as the source of truth. When updating:

1. **Edit files in `wiki/` directory** in the main repo
2. **Commit and push** to main repository
3. **Update corresponding wiki pages** on GitHub

### Future Updates

To update wiki pages:

**Option 1: Edit directly on GitHub**
1. Go to wiki page
2. Click "Edit"
3. Make changes
4. Save
5. Remember to update files in main repo too

**Option 2: Edit in main repo then sync**
1. Edit markdown files in `wiki/` directory
2. Commit to main repository
3. Copy updated content to GitHub wiki pages

## Troubleshooting

### Links Not Working

- Ensure page titles exactly match link targets
- GitHub wiki links are case-sensitive
- Use format: `[Text](Page-Name)` not `[Text](Page-Name.md)`

### Images Not Displaying

- Images must be uploaded to wiki or use external URLs
- Can't reference images from main repository in wiki
- Use absolute URLs for images

### Formatting Issues

- Preview pages before saving
- Check markdown syntax
- Ensure code blocks have language specified
- Verify heading hierarchy

## Benefits of This Approach

1. **Version Control**: Wiki content tracked in main repository
2. **Backup**: Wiki content safely stored in source code
3. **Review**: Changes can be reviewed via pull requests
4. **Portability**: Easy to migrate to other documentation systems
5. **Offline Access**: Documentation available locally

## Alternative: Keep Documentation in Repository

Instead of using GitHub wiki, you could:

1. Keep the `wiki/` directory as-is
2. Link to it from the README
3. Readers browse markdown files directly in the repository
4. Benefit: Single source of truth, no syncing needed
5. Drawback: Less polished interface than wiki

## Conclusion

The wiki content is ready to use. Choose the method that works best for you:

- **Quick start**: Manual copy via web interface
- **Advanced**: Git clone and push
- **Alternative**: Keep in repository and link from README

All methods are valid - pick what fits your workflow!

---

**Questions?** Open an issue in the repository or contact the maintainer.

---
name: Image Management
description: Unsplash image integration including photo ID extraction, URL construction with proper dimensions, photographer attribution, and header configuration
---

# Image Management and Unsplash Integration

This skill handles all aspects of selecting, configuring, and attributing images from Unsplash for blog posts.

## Image Requirements

### Standard Image Sizes
- **overlay_image**: 1200x400px for desktop headers
- **teaser**: 600x300px for thumbnails and previews

### URL Format Template
```
https://images.unsplash.com/photo-[ID]?w=[width]&h=[height]&fit=crop&crop=entropy&auto=format&q=80
```

### Header Configuration Template
```yaml
header:
  overlay_image: "https://images.unsplash.com/photo-[ID]?w=1200&h=400&fit=crop&crop=entropy&auto=format&q=80"
  overlay_filter: "linear-gradient(90deg, rgba(0,0,0,0.9) 0%, rgba(0,0,0,0.5) 100%)"
  caption: "Photo by [Photographer Name](https://unsplash.com/@photographer) on [Unsplash](https://unsplash.com)"
  teaser: "https://images.unsplash.com/photo-[ID]?w=600&h=300&fit=crop&crop=entropy&auto=format&q=80"
```

## Step-by-Step Image Fetching Process

### 1. Finding Images on Unsplash
1. Search Unsplash for relevant keywords (e.g., "technology", "coding", "abstract")
2. Select high-quality images that match the post theme
3. Copy the Unsplash page URL (e.g., `https://unsplash.com/photos/description-ABC123`)

### 2. Extracting Photo IDs from Unsplash Pages

**CRITICAL**: The URL slug is NOT the photo ID. You must extract the actual photo ID from the page.

#### Photo ID Format Examples
- Standard format: `photo-1234567890123-abcdef123456` (numeric timestamp + alphanumeric)
- Working examples from existing posts:
  - `photo-1461749280684-dccba630e2f6`
  - `photo-1555066931-4365d14bab8c`
  - `photo-1517842645767-c639042777db`

#### How to Find the Correct Photo ID
1. **Visit the Unsplash page URL**
2. **Right-click and view page source** OR use browser dev tools
3. **Search for "images.unsplash.com/photo-"** in the page source
4. **Extract the photo ID** from URLs like:
   ```
   https://images.unsplash.com/photo-1461749280684-dccba630e2f6?ixlib=rb-4.0.3
   ```
   The photo ID here is: `1461749280684-dccba630e2f6`
5. **The complete photo ID** becomes: `photo-1461749280684-dccba630e2f6`

### 3. Constructing and Verifying Image URLs

#### Build the URLs
```
# Header image (1200x400)
https://images.unsplash.com/photo-[ID]?w=1200&h=400&fit=crop&crop=entropy&auto=format&q=80

# Teaser image (600x300)  
https://images.unsplash.com/photo-[ID]?w=600&h=300&fit=crop&crop=entropy&auto=format&q=80
```

#### MANDATORY: Test URLs Before Using
1. **Paste each URL into browser address bar**
2. **Verify image loads successfully**
3. **Check image quality and aspect ratio**
4. **If image doesn't load**: Find alternative image (may be premium/plus)

## Troubleshooting Common Image Problems

### Image URL Doesn't Load
**Problem**: URL returns 404 or broken image

**Solutions**:
1. **Check if premium/plus image**: Premium images use `premium_photo-` prefix and require subscription
2. **Verify photo ID format**: Must be exact format from page source, not URL slug
3. **Try without parameters first**: Test `https://images.unsplash.com/photo-[ID]` alone
4. **Find alternative image**: Search for similar themes with standard photo IDs

### Wrong Image Aspect Ratio
**Problem**: Image appears stretched or cropped incorrectly

**Solutions**:
1. **Check original image dimensions** on Unsplash
2. **Use `fit=crop&crop=entropy`** parameters for smart cropping
3. **Consider different crop options**: `crop=center`, `crop=top`, `crop=bottom`
4. **Choose images with suitable aspect ratios** for headers (3:1 ratio ideal)

### Attribution Information Missing
**Problem**: Can't find photographer name or username

**Solutions**:
1. **Check page source** for metadata
2. **Look for "Photo by" text** on the page
3. **Check image title or alt text** for photographer info
4. **Visit photographer's profile** by clicking on their name
5. **Use browser dev tools** to inspect photographer links

### Image Quality Issues
**Problem**: Image appears blurry or low quality

**Solutions**:
1. **Check `q=80` parameter** is included for quality
2. **Use `auto=format`** for automatic format optimization
3. **Choose higher resolution source images** on Unsplash
4. **Avoid upscaling small images** to larger dimensions

### Testing Checklist Before Using Images
- [ ] Header URL loads successfully (1200x400)
- [ ] Teaser URL loads successfully (600x300)
- [ ] Image quality is high and sharp
- [ ] Aspect ratio looks correct
- [ ] Photographer name and username identified
- [ ] Attribution format is correct
- [ ] Image theme matches post content

## URL Parameter Reference

### Banner Images
```
?w=1200&h=400&fit=crop&crop=entropy&auto=format&q=80
```

### Teaser Images
```
?w=600&h=300&fit=crop&crop=entropy&auto=format&q=80
```

## Image Selection Criteria

- Choose images that visually represent the topic
- Prefer abstract, technology-themed, or conceptual images
- Ensure images work well with dark gradient overlay
- Avoid overly literal interpretations
- Search for high-quality, professional photos
- Verify image loads before using

## Attribution Requirements (CRITICAL)

**EVERY IMAGE MUST INCLUDE PROPER PHOTOGRAPHER ATTRIBUTION**

### Extracting Photographer Information
1. **On the Unsplash page**, look for photographer details
2. **Find the photographer's name** (usually displayed prominently)
3. **Find the photographer's username** (starts with @, like @johndoe)
4. **Extract both pieces of information** for proper attribution

### Attribution Format Template
```yaml
caption: "Photo by [Photographer Name](https://unsplash.com/@photographer-username) on [Unsplash](https://unsplash.com)"
```

### Real Attribution Examples
```yaml
# Example 1
caption: "Photo by [Sarah Dorweiler](https://unsplash.com/@sarahdorweiler) on [Unsplash](https://unsplash.com)"

# Example 2  
caption: "Photo by [Christopher Gower](https://unsplash.com/@cgower) on [Unsplash](https://unsplash.com)"

# Example 3
caption: "Photo by [Luca Bravo](https://unsplash.com/@lucabravo) on [Unsplash](https://unsplash.com)"
```

### Where to Find Attribution Info
- **Photographer name**: Usually displayed under the image
- **Username**: Look for @username format on the page
- **Profile link**: Click on photographer name to get their profile URL
- **Alternative**: Check page source for photographer metadata

## Complete Image Quality Control Process

### Pre-Publication Image Validation

#### URL Validation
- [ ] **Photo ID extracted from page source** (not URL slug)
- [ ] **Photo ID follows correct format**: `photo-[timestamp]-[alphanumeric]`
- [ ] **Header URL tested**: `https://images.unsplash.com/photo-[ID]?w=1200&h=400&fit=crop&crop=entropy&auto=format&q=80`
- [ ] **Teaser URL tested**: `https://images.unsplash.com/photo-[ID]?w=600&h=300&fit=crop&crop=entropy&auto=format&q=80`
- [ ] **Both URLs load without errors**
- [ ] **Images display correctly in browser**

#### Content Quality
- [ ] **Image theme matches post topic**
- [ ] **High resolution and professional quality**
- [ ] **Works well with dark gradient overlay**
- [ ] **Aspect ratio appropriate for layout**
- [ ] **No premium/plus restrictions**

#### Attribution Compliance
- [ ] **Photographer name identified and spelled correctly**
- [ ] **Photographer username found (with @ symbol)**
- [ ] **Attribution follows exact format**:
  ```yaml
  caption: "Photo by [Name](https://unsplash.com/@username) on [Unsplash](https://unsplash.com)"
  ```
- [ ] **Photographer profile link is valid**
- [ ] **Attribution included in both overlay_image and teaser sections**

#### Technical Integration
- [ ] **YAML front matter syntax is correct**
- [ ] **No syntax errors in header block**
- [ ] **Local Jekyll build succeeds with images**
- [ ] **Images display correctly in local preview**
- [ ] **Mobile responsive display verified**

### Common Validation Failures

#### ❌ **Photo ID Mistakes**
- Using URL slug instead of actual photo ID
- Missing or incorrect timestamp format
- Using premium photo IDs that don't work

#### ❌ **Attribution Errors**  
- Missing photographer name or username
- Broken links to photographer profiles
- Incorrect attribution format
- Copy-pasted attribution from different image

#### ❌ **Technical Issues**
- URLs return 404 or broken images
- YAML syntax errors in header block
- Missing required URL parameters
- Incorrect image dimensions

### Final Verification Steps

1. **Test in incognito browser window** to avoid cache issues
2. **Verify on different devices** (desktop, mobile)
3. **Check image loading speed** and optimization
4. **Confirm attribution accuracy** against Unsplash page
5. **Test local Jekyll build** with new images
6. **Preview entire post** with images in place
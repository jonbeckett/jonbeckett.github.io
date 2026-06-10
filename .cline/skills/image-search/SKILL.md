---
name: Image Search
description: Find and select appropriate Unsplash images for jonbeckett.com blog posts, construct valid Unsplash image URLs in all required sizes, and ensure proper photographer attribution.
---

# Image Search Skill

**Engage when**: Selecting header/overlay images for blog posts, finding cover images for article topics, constructing Unsplash image URLs in correct formats, or managing image assets for jonbeckett.com articles.

## Expertise
Unsplash image search, visual composition, stock photography licensing, image URL parameter optimisation, photographer attribution compliance.

---

## Unsplash URL & ID Format Reference

### Photo ID Structure
All Unsplash photos have a unique identifier with this format:
```
photo-[timestamp]_[alphanumeric]
```
**Examples**: `photo-1515879218367-8466d910aaa4`, `photo-1677442136019-21780ecad995`

**CRITICAL**: Never invent or guess photo IDs. Every photo ID must be obtained from a real Unsplash photo page. Invalid IDs return 404 errors — the #1 source of broken header images.

### URL Patterns

| Purpose | URL Format | Example |
|---------|------------|---------|
| **Photo page** (to find ID) | `https://unsplash.com/photos/[ID]` | `https://unsplash.com/photos/photo-1515879218367-8466d910aaa4` |
| **Photographer profile** | `https://unsplash.com/@[username]` | `https://unsplash.com/@wocintechchat` |
| **Search** | `https://unsplash.com/s/search?q=[query]& directional=false` | `https://unsplash.com/s/search?q=software+development` |
| **Direct image — overlay (1200x400)** | `https://images.unsplash.com/photo-[ID]?w=1200&h=400&fit=crop&crop=entropy&auto=format&q=80` |
| **Direct image — OG (1200x630)** | `https://images.unsplash.com/photo-[ID]?w=1200&h=630&fit=crop&crop=entropy&auto=format&q=80` |
| **Direct image — teaser (600x300)** | `https://images.unsplash.com/photo-[ID]?w=600&h=300&fit=crop&crop=entropy&auto=format&q=80` |
| **Direct image — full resolution** | `https://images.unsplash.com/photo-[ID]?w=1920&q=80` |

### Query Parameters

| Parameter | Description | Typical Values |
|-----------|-------------|----------------|
| `w` | Width in pixels | `600`, `1200`, `1920` |
| `h` | Height in pixels | `300`, `400`, `630` |
| `fit` | Crop fit mode | `crop` (most common), `clip` |
| `crop` | Crop source | `entropy` (smart crop), `center` |
| `auto=format` | Auto-output format | `q=80` recommended |
| `q` | Quality (0-100) | `80` is good balance |
| `w=1920&q=80` | Full-res, quality 80, no height constraint |

### Standard Image Sizes for jonbeckett.com

| Use Case | Dimensions | Params |
|----------|------------|--------|
| Header overlay | 1200x400 | `?w=1200&h=400&fit=crop&crop=entropy&auto=format&q=80` |
| Social media (OG) | 1200x630 | `?w=1200&h=630&fit=crop&crop=entropy&auto=format&q=80` |
| Teaser/thumbnail | 600x300 | `?w=600&h=300&fit=crop&crop=entropy&auto=format&q=80` |

**Note**: Always use the **same photo ID** across all three URL variants (overlay, OG, teaser) within a single post.

---

## Image Search Workflow

### Step 1: Understand the Article Topic
Review the article's subject matter, tone, and key themes to determine appropriate imagery:
- **Technical topics**: Abstract technology visuals, server racks, code screens, circuit patterns
- **History topics**: Period-appropriate imagery, retro computing, archival photography
- **Productivity/organisation**: Notebook scenes, workspace photos, planning visuals
- **AI/Machine learning**: Neural networks, abstract data visualisation, robot imagery

### Step 2: Search Unsplash
Search for images on Unsplash using the search URL pattern:
```
https://unsplash.com/s/search?q=[topic_keywords]
```
**Examples**:
- Software development: `https://unsplash.com/s/search?q=software+development+code`
- Artificial intelligence: `https://unsplash.com/s/search?q=artificial+intelligence+neural`
- Linux: `https://unsplash.com/s/search?q=linux+terminal+code`

### Step 3: Select an Appropriate Image
When evaluating images on Unsplash:
1. **Relevance**: The image should visually represent the article's core theme
2. **Composition**: Look for images with negative space (good for text overlay)
3. **Quality**: High resolution, clear focus, professional quality
4. **Tone**: Match the article tone — serious for technical topics, lighter for introductory pieces
5. **Diversity**: Prioritise diverse representation in people/workplace imagery

### Step 4: Extract the Photo ID
From the Unsplash photo page URL, extract the photo ID:
```
URL: https://unsplash.com/photos/white-and-black-laptop-computers-1727434032773
ID:  photo-1727434032773 (the part after "photos/" with "photo-" prefix stripped)

URL: https://unsplash.com/photos/photo-1515879218367-8466d910aaa4
ID:  photo-1515879218367-8466d910aaa4
```

Note: Some Unsplash URLs omit the `photo-` prefix in the slug. The full ID always begins with `photo-`.

### Step 5: Verify the Image Loads
**Before using any image, verify it loads correctly**:
1. Open the overlay_image URL in a browser
2. Confirm the image displays (no 404 error)
3. Check that the crop/composition works for horizontal header use

```bash
# Quick CLI check — exit code 0 means image loaded OK
curl -I "https://images.unsplash.com/photo-1515879218367-8466d910aaa4?w=1200&h=400&fit=crop&crop=entropy&auto=format&q=80" 2>&1 | grep "HTTP/"
# Should return: HTTP/2 200
```

### Step 6: Record Photographer Attribution
From the photo page, extract:
- **Photographer's full name** (displayed prominently on the photo page)
- **Photographer's Unsplash username** (from their profile URL: `unsplash.com/@username`)

Attribution format for the post:
```yaml
caption: "Photo by [Full Name](https://unsplash.com/@[username]) on [Unsplash](https://unsplash.com)"
```

---

## When to Use Local Banners Instead of Unsplash

Prefer local banner images (`assets/images/banners/`) when:
- **Topic-specific imagery**: No good general stock photo exists for the topic
- **Custom artwork**: Branded or custom-designed header graphics
- **Reliability concern**: Want guaranteed image availability regardless of Unsplash's service
- **Performance priority**: Local images load faster (no external CDN hop)

Local banner reference format:
```yaml
overlay_image: "/assets/images/banners/banner-X.jpg"
# No og_image or teaser needed for local banners — theme handles relative paths
```

---

## Image Selection by Article Category

Suggested image themes per category:

| Category | Suggested Visual Themes |
|----------|------------------------|
| **artificial-intelligence** | Neural networks, abstract data flows, robot arms, brain-computer interfaces |
| **cloud-computing** | Server farms, cloud graphics, data centre aisles, network diagrams |
| **software-development** | Code editors, programming setups, keyboard close-ups, whiteboard architecture |
| **devops** | Terminal screens, CI/CD pipeline graphics, server infrastructure |
| **enterprise** | Corporate technology, meeting rooms, boardroom presentations |
| **productivity** | Workspace setups, notebooks, planning boards, morning light scenes |
| **web-development** | Browser windows, responsive design mockups, web architecture diagrams |
| **testing** | QA workflows, test reports, debug consoles, bug tracking dashboards |
| **automation** | Robot arms, assembly lines, workflow diagrams, smart home interfaces |

---

## Unsplash Licensing Notes

- All Unsplash images are free to use under the Unsplash License
- Attribution is **not legally required** but is **required by jonbeckett.com's editorial standards**
- Avoid "Featured" or premium-restricted images — ensure the photo is freely available
- Some photographers request specific attribution formats — always follow their preference
- No modifications beyond resizing/cropping are needed for blog use

---

## Common Photo IDs Already in Use (Avoid Duplication)

Based on existing posts, these photo IDs are already used across multiple articles:

| Photo ID | Topic/Theme |
|----------|-------------|
| `photo-1677442136019-21780ecad995` | AI / technology (Google DeepMind) |
| `photo-1555949963-aa79dcee981c` | Tech/business (Christina @ wocintechchat) |
| `photo-1620712943543-bcc4688e7485` | Abstract/technology art |
| `photo-1555066931-4365d14bab8c` | Programming/code (Kevin Ku) |
| `photo-1551288049-bebda4e38f71` | Data analytics / dashboards |
| `photo-1558494949-ef010cbdcc31` | Network/technology (Jordan Harrison) |
| `photo-1504639725590-34d0984388bd` | Programming/dev setup (Zan) |
| `photo-1451187580459-43490279c0fa` | NASA / space / earth from orbit |
| `photo-1629654297299-c8506221ca97` | Linux/technology (Markus Spiske) |
| `photo-1518770660439-4636190af475` | Circuit boards / electronics |

Check existing posts before selecting to avoid unintentional image repetition across articles.

---

## Output Format

When the Image Search skill is engaged, output MUST include:

```markdown
## Selected Image

| Property | Value |
|----------|-------|
| **Photo ID** | `photo-XXXXXXXXX-XXXX` |
| **overlay_image** | `https://images.unsplash.com/photo-XXXXXXXXX-XXXX?w=1200&h=400&fit=crop&crop=entropy&auto=format&q=80` |
| **og_image** | `https://images.unsplash.com/photo-XXXXXXXXX-XXXX?w=1200&h=630&fit=crop&crop=entropy&auto=format&q=80` |
| **teaser** | `https://images.unsplash.com/photo-XXXXXXXXX-XXXX?w=600&h=300&fit=crop&crop=entropy&auto=format&q=80` |
| **Photographer** | [Name](https://unsplash.com/@username) |
| **Verified** | Yes / No (must be verified before committing) |

## Caption
Photo by [Name](https://unsplash.com/@username) on [Unsplash](https://unsplash.com)
```

---

## Key Capabilities
- Unsplash search URL construction and result evaluation
- Photo ID extraction from Unsplash page URLs
- Image URL parameter construction for all required output sizes
- Photographer attribution compliance (name + profile link)
- Image relevance scoring based on article topic and tone
- Local vs remote image recommendation based on context
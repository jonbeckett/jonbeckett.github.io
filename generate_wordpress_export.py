#!/usr/bin/env python3
"""
WordPress Export Generator
Converts Jekyll posts to WordPress export XML format
"""

import os
import re
from datetime import datetime
import frontmatter
import html

def generate_wordpress_xml(posts_data, site_info):
    """Generate WordPress export XML as a string"""
    
    xml_content = []
    xml_content.append('<?xml version="1.0" encoding="UTF-8" ?>')
    xml_content.append('<rss version="2.0"')
    xml_content.append('    xmlns:excerpt="http://wordpress.org/export/1.2/excerpt/"')
    xml_content.append('    xmlns:content="http://purl.org/rss/1.0/modules/content/"')
    xml_content.append('    xmlns:wfw="http://wellformedweb.org/CommentAPI/"')
    xml_content.append('    xmlns:dc="http://purl.org/dc/elements/1.1/"')
    xml_content.append('    xmlns:wp="http://wordpress.org/export/1.2/">')
    xml_content.append('  <channel>')
    
    # Channel metadata
    xml_content.append(f'    <title>{html.escape(site_info.get("title", "Blog Export"))}</title>')
    xml_content.append(f'    <link>{html.escape(site_info.get("url", "https://jonbeckett.github.io"))}</link>')
    xml_content.append(f'    <description>{html.escape(site_info.get("description", "Blog export from Jekyll"))}</description>')
    xml_content.append(f'    <pubDate>{datetime.now().strftime("%a, %d %b %Y %H:%M:%S +0000")}</pubDate>')
    xml_content.append('    <language>en-US</language>')
    xml_content.append('    <wp:version>1.2</wp:version>')
    xml_content.append(f'    <wp:base_site_url>{html.escape(site_info.get("url", "https://jonbeckett.github.io"))}</wp:base_site_url>')
    xml_content.append(f'    <wp:base_blog_url>{html.escape(site_info.get("url", "https://jonbeckett.github.io"))}</wp:base_blog_url>')
    
    # Author
    xml_content.append('    <wp:author>')
    xml_content.append('      <wp:author_id>1</wp:author_id>')
    xml_content.append('      <wp:author_login>admin</wp:author_login>')
    xml_content.append(f'      <wp:author_email>{html.escape(site_info.get("email", "admin@example.com"))}</wp:author_email>')
    xml_content.append(f'      <wp:author_display_name><![CDATA[{site_info.get("author", "Blog Author")}]]></wp:author_display_name>')
    xml_content.append('      <wp:author_first_name><![CDATA[]]></wp:author_first_name>')
    xml_content.append('      <wp:author_last_name><![CDATA[]]></wp:author_last_name>')
    xml_content.append('    </wp:author>')
    
    # Categories
    categories = set()
    for post in posts_data:
        if 'categories' in post['metadata']:
            for cat in post['metadata']['categories']:
                categories.add(cat)
    
    for idx, cat in enumerate(sorted(categories), 1):
        xml_content.append('    <wp:category>')
        xml_content.append(f'      <wp:term_id>{idx}</wp:term_id>')
        xml_content.append(f'      <wp:category_nicename>{html.escape(cat.lower().replace(" ", "-"))}</wp:category_nicename>')
        xml_content.append('      <wp:category_parent></wp:category_parent>')
        xml_content.append(f'      <wp:cat_name><![CDATA[{cat}]]></wp:cat_name>')
        xml_content.append('      <wp:category_description><![CDATA[]]></wp:category_description>')
        xml_content.append('    </wp:category>')
    
    # Posts
    post_id = 1
    for post in posts_data:
        xml_content.append('    <item>')
        xml_content.append(f'      <title><![CDATA[{post["metadata"].get("title", "Untitled")}]]></title>')
        xml_content.append(f'      <link>{html.escape(site_info.get("url", "https://jonbeckett.github.io"))}/{html.escape(post["slug"])}</link>')
        xml_content.append(f'      <pubDate>{post["pub_date"]}</pubDate>')
        xml_content.append(f'      <dc:creator><![CDATA[{site_info.get("author", "Blog Author")}]]></dc:creator>')
        xml_content.append(f'      <guid isPermaLink="false">{html.escape(site_info.get("url", "https://jonbeckett.github.io"))}/{html.escape(post["slug"])}</guid>')
        xml_content.append('      <description></description>')
        xml_content.append(f'      <content:encoded><![CDATA[{post["content"]}]]></content:encoded>')
        xml_content.append('      <excerpt:encoded><![CDATA[]]></excerpt:encoded>')
        xml_content.append(f'      <wp:post_id>{post_id}</wp:post_id>')
        xml_content.append(f'      <wp:post_date>{post["post_date"]}</wp:post_date>')
        xml_content.append(f'      <wp:post_date_gmt>{post["post_date"]}</wp:post_date_gmt>')
        xml_content.append('      <wp:comment_status>open</wp:comment_status>')
        xml_content.append('      <wp:ping_status>open</wp:ping_status>')
        xml_content.append(f'      <wp:post_name>{html.escape(post["slug"])}</wp:post_name>')
        xml_content.append('      <wp:status>publish</wp:status>')
        xml_content.append('      <wp:post_parent>0</wp:post_parent>')
        xml_content.append('      <wp:menu_order>0</wp:menu_order>')
        xml_content.append('      <wp:post_type>post</wp:post_type>')
        xml_content.append('      <wp:post_password></wp:post_password>')
        xml_content.append('      <wp:is_sticky>0</wp:is_sticky>')
        
        # Categories for this post
        if 'categories' in post['metadata']:
            for cat in post['metadata']['categories']:
                xml_content.append(f'      <category domain="category" nicename="{html.escape(cat.lower().replace(" ", "-"))}"><![CDATA[{cat}]]></category>')
        
        xml_content.append('    </item>')
        post_id += 1
    
    xml_content.append('  </channel>')
    xml_content.append('</rss>')
    
    return '\n'.join(xml_content)

def parse_jekyll_post(filepath):
    """Parse a Jekyll post file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            post = frontmatter.load(f)
        
        # Extract metadata
        metadata = post.metadata
        content = post.content
        
        # Get date from frontmatter or filename
        if 'date' in metadata:
            if isinstance(metadata['date'], str):
                post_date = datetime.strptime(metadata['date'], '%Y-%m-%d')
            else:
                post_date = metadata['date']
        else:
            # Extract from filename
            filename = os.path.basename(filepath)
            date_match = re.match(r'(\d{4}-\d{2}-\d{2})', filename)
            if date_match:
                post_date = datetime.strptime(date_match.group(1), '%Y-%m-%d')
            else:
                post_date = datetime.now()
        
        # Create slug from filename
        filename = os.path.basename(filepath)
        slug = re.sub(r'^\d{4}-\d{2}-\d{2}-', '', filename.replace('.md', ''))
        
        # Format dates for WordPress
        pub_date = post_date.strftime('%a, %d %b %Y %H:%M:%S +0000')
        post_date_wp = post_date.strftime('%Y-%m-%d %H:%M:%S')
        
        return {
            'filepath': filepath,
            'metadata': metadata,
            'content': content,
            'post_date': post_date_wp,
            'pub_date': pub_date,
            'slug': slug,
            'date_obj': post_date
        }
    except Exception as e:
        print(f"Error parsing {filepath}: {e}")
        return None

def main():
    """Main function to generate WordPress export"""
    
    # Site information - you can modify these values
    site_info = {
        'title': 'Jon Beckett Blog',
        'url': 'https://jonbeckett.github.io',
        'description': 'Personal blog posts',
        'author': 'Jon Beckett',
        'email': 'admin@jonbeckett.github.io'
    }
    
    # Get all post files from September 21, 2025 onwards
    post_files = []
    
    # Read the list of files from our previous terminal command
    target_files = [
        "/Users/jonbeckett/Projects/jonbeckett.github.io/_posts/2025/2025-09-21-pottering.md",
        "/Users/jonbeckett/Projects/jonbeckett.github.io/_posts/2025/2025-09-27-six-days.md",
        "/Users/jonbeckett/Projects/jonbeckett.github.io/_posts/2025/2025-09-28-an-evening-at-the-theatre.md",
        "/Users/jonbeckett/Projects/jonbeckett.github.io/_posts/2025/2025-09-30-the-need-to-slow-down.md",
        "/Users/jonbeckett/Projects/jonbeckett.github.io/_posts/2025/2025-10-02-life-without-computers.md",
        "/Users/jonbeckett/Projects/jonbeckett.github.io/_posts/2025/2025-10-03-taylor-and-the-quiet-rebellion.md",
        "/Users/jonbeckett/Projects/jonbeckett.github.io/_posts/2025/2025-10-04-one-computer-to-rule-them-all.md",
        "/Users/jonbeckett/Projects/jonbeckett.github.io/_posts/2025/2025-10-05-sunday-morning-in-spoons.md",
        "/Users/jonbeckett/Projects/jonbeckett.github.io/_posts/2025/2025-10-06-be-careful-what-you-wish-for.md",
        "/Users/jonbeckett/Projects/jonbeckett.github.io/_posts/2025/2025-10-08-decompression.md",
        "/Users/jonbeckett/Projects/jonbeckett.github.io/_posts/2025/2025-10-10-one-virtual-world.md",
        "/Users/jonbeckett/Projects/jonbeckett.github.io/_posts/2025/2025-10-12-a-step-back-in-time.md",
        "/Users/jonbeckett/Projects/jonbeckett.github.io/_posts/2025/2025-10-14-one-foot-in-front-of-the-other.md",
        "/Users/jonbeckett/Projects/jonbeckett.github.io/_posts/2025/2025-10-16-half-past-my-bedtime.md",
        "/Users/jonbeckett/Projects/jonbeckett.github.io/_posts/2025/2025-10-19-round-in-circles.md",
        "/Users/jonbeckett/Projects/jonbeckett.github.io/_posts/2025/2025-10-22-while-making-other-plans.md",
        "/Users/jonbeckett/Projects/jonbeckett.github.io/_posts/2025/2025-10-23-long-weekend.md",
        "/Users/jonbeckett/Projects/jonbeckett.github.io/_posts/2025/2025-10-24-an-accidental-writer.md",
        "/Users/jonbeckett/Projects/jonbeckett.github.io/_posts/2025/2025-10-25-the-journey-west.md",
        "/Users/jonbeckett/Projects/jonbeckett.github.io/_posts/2025/2025-10-26-quiet-days-vogon-poetry-and-impossible-creaters.md",
        "/Users/jonbeckett/Projects/jonbeckett.github.io/_posts/2025/2025-10-27-lights-in-the-sky.md",
        "/Users/jonbeckett/Projects/jonbeckett.github.io/_posts/2025/2025-10-29-to-by-young.md",
        "/Users/jonbeckett/Projects/jonbeckett.github.io/_posts/2025/2025-11-02-parties-and-leftovers-at-chore-city.md",
        "/Users/jonbeckett/Projects/jonbeckett.github.io/_posts/2025/2025-11-05-how-is-it-nearly-thursday-already.md",
        "/Users/jonbeckett/Projects/jonbeckett.github.io/_posts/2025/2025-11-09-half-past-lunchtime-on-sunday.md",
        "/Users/jonbeckett/Projects/jonbeckett.github.io/_posts/2025/2025-11-12-nuremberg.md",
        "/Users/jonbeckett/Projects/jonbeckett.github.io/_posts/2025/2025-11-15-south-west.md",
        "/Users/jonbeckett/Projects/jonbeckett.github.io/_posts/2025/2025-11-19-drinking-the-kool-aid.md",
        "/Users/jonbeckett/Projects/jonbeckett.github.io/_posts/2025/2025-11-20-the-importance-of-being-earnest.md",
        "/Users/jonbeckett/Projects/jonbeckett.github.io/_posts/2025/2025-11-22-an-early-night.md",
        "/Users/jonbeckett/Projects/jonbeckett.github.io/_posts/2025/2025-11-26-fifteen-minutes.md",
        "/Users/jonbeckett/Projects/jonbeckett.github.io/_posts/2025/2025-11-30-it-wasn-t-always-this-way.md",
        "/Users/jonbeckett/Projects/jonbeckett.github.io/_posts/2025/2025-12-07-copenhagen.md",
        "/Users/jonbeckett/Projects/jonbeckett.github.io/_posts/2025/2025-12-08-oats-harbours-mermaids-and-glogg.md",
        "/Users/jonbeckett/Projects/jonbeckett.github.io/_posts/2025/2025-12-10-the-glyptotek-and-tivoli-gardens.md",
        "/Users/jonbeckett/Projects/jonbeckett.github.io/_posts/2025/2025-12-11-unnecessarily-difficult.md",
        "/Users/jonbeckett/Projects/jonbeckett.github.io/_posts/2025/2025-12-12-a-moveable-feast.md",
        "/Users/jonbeckett/Projects/jonbeckett.github.io/_posts/2025/2025-12-14-in-search-of-my-lost-tribe.md",
        "/Users/jonbeckett/Projects/jonbeckett.github.io/_posts/2025/2025-12-14-on-the-outside-looking-in.md",
        "/Users/jonbeckett/Projects/jonbeckett.github.io/_posts/2025/2025-12-20-work-chores-and-strictly.md",
        "/Users/jonbeckett/Projects/jonbeckett.github.io/_posts/2025/2025-12-25-christmas-day.md",
        "/Users/jonbeckett/Projects/jonbeckett.github.io/_posts/2025/2025-12-26-boxing-day.md",
        "/Users/jonbeckett/Projects/jonbeckett.github.io/_posts/2025/2025-12-31-far-from-the-madding-crowd.md",
        "/Users/jonbeckett/Projects/jonbeckett.github.io/_posts/2026/2026-01-01-reconnecting.md",
        "/Users/jonbeckett/Projects/jonbeckett.github.io/_posts/2026/2026-01-02-friday.md"
    ]
    
    print(f"Processing {len(target_files)} posts...")
    
    # Parse all posts
    posts_data = []
    for filepath in target_files:
        post_data = parse_jekyll_post(filepath)
        if post_data:
            posts_data.append(post_data)
            print(f"Processed: {os.path.basename(filepath)}")
        else:
            print(f"Failed to process: {os.path.basename(filepath)}")
    
    # Sort posts by date (oldest first, which is typical for WordPress exports)
    posts_data.sort(key=lambda x: x['date_obj'])
    
    print(f"\nSuccessfully parsed {len(posts_data)} posts")
    
    # Generate WordPress XML
    print("Generating WordPress export XML...")
    xml_content = generate_wordpress_xml(posts_data, site_info)
    
    # Write to file
    output_file = '/Users/jonbeckett/Projects/jonbeckett.github.io/wordpress-export.xml'
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(xml_content)
    
    print(f"\nWordPress export file created: {output_file}")
    print(f"Contains {len(posts_data)} posts from September 21, 2025 onwards")

if __name__ == "__main__":
    main()
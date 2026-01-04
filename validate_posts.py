#!/usr/bin/env python3
"""
Jekyll Blog Post Validator
Tests blog posts for issues that could cause GitHub Actions Jekyll builds to fail.
"""

import os
import re
import yaml
import glob
from datetime import datetime, date
from pathlib import Path
import unicodedata
import sys

class BlogPostValidator:
    def __init__(self, base_path="."):
        self.base_path = Path(base_path)
        self.errors = []
        self.warnings = []
        self.posts_checked = 0
        
        # Valid layouts that should exist
        self.valid_layouts = {"post", "page", "default", "home"}
        
    def log_error(self, file_path, message):
        """Log an error for a specific file"""
        error_msg = f"ERROR: {file_path}: {message}"
        self.errors.append(error_msg)
        print(f"❌ {error_msg}")
        
    def log_warning(self, file_path, message):
        """Log a warning for a specific file"""
        warning_msg = f"WARNING: {file_path}: {message}"
        self.warnings.append(warning_msg)
        print(f"⚠️  {warning_msg}")
        
    def log_success(self, file_path, message="Valid"):
        """Log successful validation"""
        print(f"✅ {file_path}: {message}")
    
    def validate_filename_format(self, file_path):
        """Validate Jekyll post filename format (YYYY-MM-DD-title.md)"""
        filename = file_path.name
        
        # Skip index files and non-markdown files
        if filename == "index.md" or not filename.endswith(".md"):
            return True
            
        # Check if it's in _posts directory (current posts)
        if "_posts" in str(file_path):
            # Current posts must follow YYYY-MM-DD-title.md format
            pattern = r'^(\d{4})-(\d{2})-(\d{2})-(.+)\.md$'
            match = re.match(pattern, filename)
            if not match:
                self.log_error(file_path, f"Filename doesn't match Jekyll post format YYYY-MM-DD-title.md")
                return False
                
            year, month, day, title = match.groups()
            
            # Validate date components
            try:
                datetime(int(year), int(month), int(day))
            except ValueError:
                self.log_error(file_path, f"Invalid date in filename: {year}-{month}-{day}")
                return False
                
            # Check for valid title slug
            if not title or title.startswith('-') or title.endswith('-'):
                self.log_error(file_path, f"Invalid title slug in filename: '{title}'")
                return False
                
        return True
    
    def validate_front_matter(self, file_path, content):
        """Validate YAML front matter"""
        if not content.strip().startswith('---'):
            self.log_error(file_path, "Missing YAML front matter (should start with '---')")
            return None
            
        # Extract front matter
        try:
            parts = content.split('---', 2)
            if len(parts) < 3:
                self.log_error(file_path, "Incomplete YAML front matter (missing closing '---')")
                return None
                
            front_matter_str = parts[1].strip()
            if not front_matter_str:
                self.log_error(file_path, "Empty YAML front matter")
                return None
                
            # Parse YAML
            front_matter = yaml.safe_load(front_matter_str)
            if not isinstance(front_matter, dict):
                self.log_error(file_path, "YAML front matter is not a valid dictionary")
                return None
                
        except yaml.YAMLError as e:
            self.log_error(file_path, f"Invalid YAML syntax in front matter: {e}")
            return None
            
        # Validate required fields based on file type
        if "_posts" in str(file_path):
            # Posts require layout, title, and date
            required_fields = ["layout", "title", "date"]
        elif file_path.name == "index.md":
            # Index pages only require layout and title
            required_fields = ["layout", "title"]
        else:
            # Other pages require layout and title
            required_fields = ["layout", "title"]
            
        for field in required_fields:
            if field not in front_matter:
                self.log_error(file_path, f"Missing required field in front matter: {field}")
                
        # Validate layout
        if "layout" in front_matter and front_matter["layout"] not in self.valid_layouts:
            self.log_warning(file_path, f"Unknown layout: {front_matter['layout']}")
            
        # Validate date format
        if "date" in front_matter:
            date_value = front_matter["date"]
            if isinstance(date_value, str):
                # Try to parse various date formats
                date_formats = [
                    "%Y-%m-%d",
                    "%Y-%m-%d %H:%M:%S",
                    "%Y-%m-%d %H:%M:%S %z",
                    "%Y-%m-%dT%H:%M:%S",
                    "%Y-%m-%dT%H:%M:%SZ"
                ]
                
                parsed_date = None
                for fmt in date_formats:
                    try:
                        parsed_date = datetime.strptime(str(date_value).strip(), fmt)
                        break
                    except ValueError:
                        continue
                        
                if not parsed_date:
                    self.log_error(file_path, f"Invalid date format: {date_value}")
                    
            elif isinstance(date_value, (datetime, date)):
                # YAML parsed it as a Python date/datetime object - this is fine for Jekyll
                pass
            else:
                self.log_error(file_path, f"Date must be string or datetime object, got {type(date_value)}")
                
        # Validate title
        if "title" in front_matter:
            title = front_matter["title"]
            if not title or (isinstance(title, str) and not title.strip()):
                self.log_error(file_path, "Empty title in front matter")
                
        return front_matter
    
    def validate_content_encoding(self, file_path, content):
        """Validate that content is properly UTF-8 encoded"""
        try:
            # Try to encode/decode to catch any encoding issues
            content.encode('utf-8').decode('utf-8')
            
            # Check for problematic characters that might cause issues
            for i, char in enumerate(content):
                if ord(char) > 127:  # Non-ASCII character
                    try:
                        unicodedata.name(char)
                    except ValueError:
                        self.log_warning(file_path, f"Potentially problematic Unicode character at position {i}: {repr(char)}")
                        
        except UnicodeError as e:
            self.log_error(file_path, f"Encoding error: {e}")
            return False
            
        return True
    
    def validate_liquid_tags(self, file_path, content):
        """Basic validation of Liquid template tags"""
        # Check for unmatched liquid tags
        liquid_patterns = [
            (r'\{\%\s*if\s', r'\{\%\s*endif\s*\%\}'),
            (r'\{\%\s*for\s', r'\{\%\s*endfor\s*\%\}'),
            (r'\{\%\s*unless\s', r'\{\%\s*endunless\s*\%\}'),
            (r'\{\%\s*case\s', r'\{\%\s*endcase\s*\%\}'),
        ]
        
        for open_pattern, close_pattern in liquid_patterns:
            opens = len(re.findall(open_pattern, content, re.IGNORECASE))
            closes = len(re.findall(close_pattern, content, re.IGNORECASE))
            
            if opens != closes:
                tag_name = open_pattern.split('\\s')[1].rstrip('\\s')
                self.log_error(file_path, f"Unmatched Liquid {tag_name} tags: {opens} opens, {closes} closes")
    
    def validate_markdown_syntax(self, file_path, content):
        """Basic markdown syntax validation"""
        lines = content.split('\n')
        
        for i, line in enumerate(lines, 1):
            # Check for common markdown issues
            
            # Malformed links
            if '[' in line and ']' in line:
                # Check for malformed markdown links
                malformed_links = re.findall(r'\[([^\]]*)\]\s*\([^)]*$', line)
                if malformed_links:
                    self.log_warning(file_path, f"Line {i}: Potentially malformed link")
            
            # Check for headers without space after #
            if re.match(r'^#+[^#\s]', line.strip()):
                self.log_warning(file_path, f"Line {i}: Header should have space after #: {line.strip()[:50]}")
    
    def validate_date_consistency(self, file_path, front_matter):
        """Check if filename date matches front matter date"""
        if not front_matter or "date" not in front_matter:
            return
            
        filename = file_path.name
        
        # Extract date from filename if it's a post
        filename_match = re.match(r'^(\d{4})-(\d{2})-(\d{2})-', filename)
        if not filename_match:
            return  # Not a dated post
            
        filename_date = f"{filename_match.group(1)}-{filename_match.group(2)}-{filename_match.group(3)}"
        
        # Extract date from front matter
        fm_date = front_matter["date"]
        if isinstance(fm_date, str):
            fm_date_str = fm_date.split()[0]  # Take just the date part
        else:
            fm_date_str = fm_date.strftime("%Y-%m-%d")
            
        if filename_date != fm_date_str:
            self.log_warning(file_path, f"Date mismatch: filename has {filename_date}, front matter has {fm_date_str}")
    
    def validate_post(self, file_path):
        """Validate a single post"""
        try:
            # Read file content
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except UnicodeDecodeError:
            self.log_error(file_path, "File encoding error - not valid UTF-8")
            return
        except Exception as e:
            self.log_error(file_path, f"Error reading file: {e}")
            return
            
        # Run all validations
        self.validate_filename_format(file_path)
        front_matter = self.validate_front_matter(file_path, content)
        self.validate_content_encoding(file_path, content)
        self.validate_liquid_tags(file_path, content)
        self.validate_markdown_syntax(file_path, content)
        self.validate_date_consistency(file_path, front_matter)
        
        self.posts_checked += 1
        
        if not any(str(file_path) in error for error in self.errors[-10:]):  # Check recent errors
            self.log_success(file_path)
    
    def find_all_posts(self):
        """Find all markdown posts in _posts and archive directories"""
        posts = []
        
        # Current posts in _posts
        posts_dir = self.base_path / "_posts"
        if posts_dir.exists():
            posts.extend(posts_dir.glob("*.md"))
            
        # Archive posts
        archive_dir = self.base_path / "archive"
        if archive_dir.exists():
            # Find all markdown files in all subdirectories
            for year_dir in archive_dir.iterdir():
                if year_dir.is_dir():
                    posts.extend(year_dir.glob("*.md"))
                    
        return sorted(posts)
    
    def validate_all(self):
        """Validate all posts"""
        print("🔍 Starting Jekyll blog post validation...\n")
        
        posts = self.find_all_posts()
        total_posts = len(posts)
        
        if total_posts == 0:
            print("❌ No posts found to validate!")
            return False
            
        print(f"📝 Found {total_posts} posts to validate\n")
        
        for i, post_path in enumerate(posts, 1):
            print(f"[{i:4}/{total_posts}] ", end="")
            self.validate_post(post_path)
            
        # Print summary
        print(f"\n{'='*60}")
        print(f"🏁 VALIDATION SUMMARY")
        print(f"{'='*60}")
        print(f"📊 Posts checked: {self.posts_checked}")
        print(f"❌ Errors: {len(self.errors)}")
        print(f"⚠️  Warnings: {len(self.warnings)}")
        
        if self.errors:
            print(f"\n💥 ERRORS FOUND:")
            for error in self.errors:
                print(f"   {error}")
                
        if self.warnings:
            print(f"\n⚠️  WARNINGS:")
            for warning in self.warnings:
                print(f"   {warning}")
                
        if not self.errors and not self.warnings:
            print(f"\n🎉 All posts validated successfully! Jekyll build should work fine.")
            return True
        elif not self.errors:
            print(f"\n✅ No critical errors found. Jekyll build should work (warnings are non-critical).")
            return True
        else:
            print(f"\n❌ Critical errors found. These may cause Jekyll build to fail.")
            return False

def main():
    if len(sys.argv) > 1:
        base_path = sys.argv[1]
    else:
        base_path = "."
        
    validator = BlogPostValidator(base_path)
    success = validator.validate_all()
    
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
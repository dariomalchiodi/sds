#!/usr/bin/env python3
"""
Generate individual HTML redirect pages for URL shortener mappings.

This script reads the shortener-mappings.json file and generates a separate
HTML redirect page for each short code in a 'short/' subdirectory. Each page 
uses HTML meta refresh to redirect to the target URL.


Usage:
    python3 sds/generate-redirect-pages.py [build_dir]

The script will create redirect pages in build_dir/short/ (default: build/short/).
URLs will be accessible as: https://site.com/short/code.html
"""

import json
import os
import sys
from pathlib import Path

def create_redirect_html(short_code, target_url, delay=0):
    """
    Create HTML content for a redirect page.
    
    Args:
        short_code: The short code for the URL
        target_url: The destination URL
        delay: Redirect delay in seconds (default: 0 for immediate)
    
    Returns:
        HTML content as string
    """
    html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="refresh" content="{delay};url={target_url}">
    <link rel="canonical" href="{target_url}">
    <title>Redirecting to {target_url}</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            margin: 0;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
        }}
        .redirect-container {{
            text-align: center;
            padding: 2rem;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 10px;
            backdrop-filter: blur(10px);
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
        }}
        .spinner {{
            width: 40px;
            height: 40px;
            border: 4px solid rgba(255, 255, 255, 0.3);
            border-top: 4px solid white;
            border-radius: 50%;
            animation: spin 1s linear infinite;
            margin: 0 auto 1rem;
        }}
        @keyframes spin {{
            0% {{ transform: rotate(0deg); }}
            100% {{ transform: rotate(360deg); }}
        }}
        .redirect-info {{
            margin: 1rem 0;
        }}
        .short-code {{
            font-family: 'Monaco', 'Menlo', 'Ubuntu Mono', monospace;
            background: rgba(255, 255, 255, 0.2);
            padding: 0.2rem 0.5rem;
            border-radius: 4px;
            font-weight: bold;
        }}
        .target-url {{
            word-break: break-all;
            margin: 0.5rem 0;
            font-size: 0.9rem;
        }}
        .manual-link {{
            display: inline-block;
            margin-top: 1rem;
            padding: 0.5rem 1rem;
            background: rgba(255, 255, 255, 0.2);
            border: 1px solid rgba(255, 255, 255, 0.3);
            border-radius: 5px;
            color: white;
            text-decoration: none;
            transition: all 0.3s ease;
        }}
        .manual-link:hover {{
            background: rgba(255, 255, 255, 0.3);
            transform: translateY(-2px);
        }}
    </style>
</head>
<body>
    <div class="redirect-container">
        <div class="spinner"></div>
        <h2>🔗 SDS URL Shortener</h2>
        <div class="redirect-info">
            <p>Redirecting from <span class="short-code">{short_code}</span></p>
            <p class="target-url">to: {target_url}</p>
        </div>
        <p>If you're not redirected automatically, <a href="{target_url}" class="manual-link">click here</a>.</p>
    </div>
    
    <script>
        // Fallback JavaScript redirect (in case meta refresh fails)
        setTimeout(function() {{
            window.location.href = "{target_url}";
        }}, {delay * 1000 + 100});
        
        // Analytics tracking (if needed)
        console.log('SDS Shortener: Redirecting {short_code} -> {target_url}');
    </script>
</body>
</html>"""
    return html_template

def generate_redirect_pages(mappings_file="shortener-mappings.json", build_dir="build"):
    """
    Generate redirect pages for all mappings in the JSON file.
    
    Args:
        mappings_file: Path to the shortener mappings JSON file
        build_dir: Directory where redirect pages will be created
    """
    # Read mappings
    try:
        with open(mappings_file, 'r', encoding='utf-8') as f:
            mappings = json.load(f)
    except FileNotFoundError:
        print(f"❌ Error: {mappings_file} not found!")
        return False
    except json.JSONDecodeError as e:
        print(f"❌ Error: Invalid JSON in {mappings_file}: {e}")
        return False
    
    if not mappings:
        print("ℹ️  No mappings found in shortener-mappings.json")
        return True
    
    # Create build directory and short subdirectory
    build_path = Path(build_dir)
    short_path = build_path / "short"
    short_path.mkdir(parents=True, exist_ok=True)
    
    success_count = 0
    total_count = len(mappings)
    
    print(f"🔗 Generating {total_count} redirect pages in short/ directory...")
    
    for short_code, target_url in mappings.items():
        try:
            # Create HTML content
            html_content = create_redirect_html(short_code, target_url)
            
            # Write HTML file in short/ directory
            html_file = short_path / f"{short_code}.html"
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(html_content)
            
            print(f"  ✓ short/{short_code}.html -> {target_url}")
            success_count += 1
            
        except Exception as e:
            print(f"  ❌ Failed to create short/{short_code}.html: {e}")
    
    print(f"\n📊 Summary:")
    print(f"  • Generated: {success_count}/{total_count} redirect pages")
    print(f"  • Output directory: {build_dir}/short/")
    
    if success_count == total_count:
        print("✅ All redirect pages generated successfully!")
        return True
    else:
        print(f"⚠️  {total_count - success_count} pages failed to generate")
        return False

def main():
    """Main function to handle command line execution."""
    # Parse command line arguments
    if len(sys.argv) > 1:
        build_dir = sys.argv[1]
    else:
        build_dir = "build"
    
    print("🚀 SDS Redirect Page Generator")
    print("=" * 50)
    
    # Check if we're in the right directory
    if not os.path.exists("shortener-mappings.json"):
        print("❌ Error: shortener-mappings.json not found!")
        print("   Make sure you're running this from the SDS repository root.")
        sys.exit(1)
    
    # Generate redirect pages
    success = generate_redirect_pages(build_dir=build_dir)
    
    if success:
        print(f"\n🎯 Redirect pages are now available:")
        print(f"   • Local: http://localhost:8080/short/{{short_code}}.html")
        print(f"   • GitHub Pages: https://your-username.github.io/sds/short/{{short_code}}.html")
        print(f"\n💡 Test examples:")
        
        # Show a few examples from the mappings
        try:
            with open("shortener-mappings.json", 'r') as f:
                mappings = json.load(f)
                for i, (short_code, _) in enumerate(mappings.items()):
                    if i < 3:  # Show first 3 examples
                        print(f"   • http://localhost:8080/short/{short_code}.html")
        except:
            pass
        
        sys.exit(0)
    else:
        sys.exit(1)

if __name__ == "__main__":
    main()

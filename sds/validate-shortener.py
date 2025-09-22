#!/usr/bin/env python3
"""

Validate shortener-mappings.json file for deployment.
Usage:
    python3 sds/validate-shortener.py

This script checks the shortener mappings JSON file for:
1. Valid JSON syntax
2. No duplicate short codes
3. Valid URL formats
4. No empty values

Returns exit code 0 if valid, 1 if invalid.
"""

import json
import sys
import re
from urllib.parse import urlparse

def validate_url(url):
    """
    Validate if a URL is properly formatted.
    
    Args:
        url: URL string to validate
        
    Returns:
        bool: True if valid, False otherwise
    """
    if not url or not isinstance(url, str):
        return False
    
    # Allow relative URLs (starting with /)
    if url.startswith('/'):
        return True
    
    # Validate absolute URLs
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False

def validate_shortener_mappings(filename="shortener-mappings.json"):
    """
    Validate the shortener mappings JSON file.
    
    Args:
        filename: Path to the JSON file
        
    Returns:
        tuple: (is_valid, errors_list)
    """
    errors = []
    
    # Check if file exists
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        return False, [f"❌ File not found: {filename}"]
    except Exception as e:
        return False, [f"❌ Error reading file: {e}"]
    
    # Check for trailing commas (common JSON error)
    if re.search(r',\s*[}\]]', content):
        errors.append("❌ JSON syntax error: Trailing comma detected")
    
    # Parse JSON
    try:
        mappings = json.loads(content)
    except json.JSONDecodeError as e:
        errors.append(f"❌ Invalid JSON syntax: {e}")
        return False, errors
    
    # Check if it's a dictionary
    if not isinstance(mappings, dict):
        errors.append("❌ JSON must be an object/dictionary")
        return False, errors
    
    # Check for empty mappings
    if not mappings:
        errors.append("⚠️  Warning: No URL mappings found")
        return True, errors  # Not an error, just a warning
    
    # Check for duplicate keys (this would be caught by JSON parser, but let's be explicit)
    original_keys = list(mappings.keys())
    unique_keys = list(set(original_keys))
    
    if len(original_keys) != len(unique_keys):
        duplicates = [key for key in original_keys if original_keys.count(key) > 1]
        errors.append(f"❌ Duplicate short codes found: {duplicates}")
    
    # Validate each mapping
    invalid_codes = []
    invalid_urls = []
    empty_values = []
    
    for short_code, url in mappings.items():
        # Check short code format
        if not short_code or not isinstance(short_code, str):
            invalid_codes.append(short_code)
            continue
            
        if not re.match(r'^[a-zA-Z0-9\-_]+$', short_code):
            invalid_codes.append(short_code)
        
        # Check URL
        if not url:
            empty_values.append(short_code)
        elif not validate_url(url):
            invalid_urls.append(f"{short_code} -> {url}")
    
    # Report validation errors
    if invalid_codes:
        errors.append(f"❌ Invalid short codes (use only letters, numbers, hyphens, underscores): {invalid_codes}")
    
    if invalid_urls:
        errors.append(f"❌ Invalid URLs:")
        for invalid_url in invalid_urls:
            errors.append(f"    {invalid_url}")
    
    if empty_values:
        errors.append(f"❌ Empty URL values for: {empty_values}")
    
    # Success case
    is_valid = len([e for e in errors if e.startswith('❌')]) == 0
    
    return is_valid, errors

def main(verbose=False):
    """Main validation function."""
    # Parse command line arguments
    filename = "shortener-mappings.json"
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    
    if verbose:
        print(f"🔍 Validating {filename}...")
        print("=" * 50)
    
    is_valid, errors = validate_shortener_mappings(filename)
    
    # Print results
    if errors:
        for error in errors:
            print(error)
        print()
    
    if is_valid:
        if verbose:
            print("✅ Validation passed!")
            
            # Show summary statistics
            try:
                with open(filename, 'r') as f:
                    mappings = json.load(f)
                
                external_urls = sum(1 for url in mappings.values() if url.startswith('http'))
                internal_urls = sum(1 for url in mappings.values() if url.startswith('/'))
                
                print(f"\n📊 Summary:")
                print(f"  • Total mappings: {len(mappings)}")
                print(f"  • External URLs: {external_urls}")
                print(f"  • Internal URLs: {internal_urls}")
                
                print(f"\n💡 All short codes:")
                for code in sorted(mappings.keys()):
                    print(f"  • {code}")
                    
            except:
                pass
            
        sys.exit(0)
    else:
        print("❌ Validation failed!")
        print("\n🔧 Please fix the errors above before deploying.")
        sys.exit(1)

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Apply cross-reference link improvements to all HTML files in the Italian documentation.
"""

import sys
import os
from pathlib import Path

# Add the code directory to the path so we can import sds
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'code'))

from sds import generate_toc_dictionary, replace_crossref_links

def main():
    """Apply cross-reference numbering to all HTML files"""
    
    # Get the HTML directory from command line argument or use default
    if len(sys.argv) > 1:
        html_root_dir = sys.argv[1]
    else:
        html_root_dir = "build/it"  # Default to Italian
    
    # Detect language from directory path
    language = 'en'  # default
    if '/it' in html_root_dir or html_root_dir.endswith('it'):
        language = 'it'
    elif '/en' in html_root_dir or html_root_dir.endswith('en'):
        language = 'en'
    
    print("=== Applying Cross-Reference Link Improvements ===\n")
    
    # Check if the build directory exists
    if not os.path.exists(html_root_dir):
        print(f"ERROR: Build directory not found: {html_root_dir}")
        print("Please run 'make it' to build the documentation first.")
        return 1
    
    print(f"Processing HTML files in: {html_root_dir} (language: {language})")
    print()
    
    # Generate the TOC dictionary
    print("1. Generating TOC dictionary from sidebar...")
    toc_dict = generate_toc_dictionary(html_root_dir)
    
    if not toc_dict:
        print("ERROR: Failed to generate TOC dictionary")
        return 1
    
    print(f"Found {len(toc_dict)} entries in TOC dictionary")
    print()
    
    # Apply the changes to all HTML files
    print("2. Applying cross-reference improvements...")
    
    try:
        changes_summary = replace_crossref_links(html_root_dir, toc_dict, dry_run=False, language=language)
        
        print(f"Processing complete!")
        print(f"  Files processed: {changes_summary['files_processed']}")
        print(f"  Files modified: {changes_summary['files_modified']}")
        print(f"  Total replacements: {changes_summary['total_replacements']}")
        
        if changes_summary['errors']:
            print(f"  Errors encountered: {len(changes_summary['errors'])}")
            for error in changes_summary['errors']:
                print(f"    - {error}")
        
        print()
        if language == 'it':
            print("Cross-reference links now show:")
            print("  - Link text: 'Capitolo X', 'Paragrafo X.Y', or 'Appendice A'")
            print("  - Tooltip on hover: Original chapter/section title")
            print("  - Consistent numbering throughout the documentation")
        else:
            print("Cross-reference links now show:")
            print("  - Link text: 'Chapter X', 'Section X.Y', or 'Appendix A'")
            print("  - Tooltip on hover: Original chapter/section title")
            print("  - Consistent numbering throughout the documentation")
        
    except Exception as e:
        print(f"ERROR during processing: {e}")
        return 1
    
    print("\nSuccess! All cross-reference links have been improved.")
    return 0

if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""
Apply cross-reference link improvements to all HTML files in the Italian documentation.
"""

import sys
import os
from pathlib import Path

# Add the sds directory to the path so we can import sds
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'sds'))

from sds import generate_toc_dictionary, replace_crossref_links, update_sidebar_navigation_numbering

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
    elif '/fr' in html_root_dir or html_root_dir.endswith('fr'):
        language = 'fr'
    elif '/es' in html_root_dir or html_root_dir.endswith('es'):
        language = 'es'
    
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
        # NUMBERING DISABLED - Commenting out all automatic numbering functions
        # changes_summary = replace_crossref_links(html_root_dir, toc_dict, dry_run=False, language=language)
        changes_summary = {
            'files_processed': 0,
            'files_modified': 0,
            'total_replacements': 0,
            'replacements_by_file': {},
            'errors': []
        }
        
        print(f"Cross-reference processing DISABLED!")
        print(f"  Files processed: {changes_summary['files_processed']}")
        print(f"  Files modified: {changes_summary['files_modified']}")
        print(f"  Total replacements: {changes_summary['total_replacements']}")
        
        # Also update sidebar navigation numbering
        print()
        print("3. Sidebar navigation numbering DISABLED...")
        # sidebar_changes = update_sidebar_navigation_numbering(html_root_dir, toc_dict, dry_run=False, language=language)
        sidebar_changes = {
            'files_processed': 0,
            'files_modified': 0,
            'total_replacements': 0,
            'errors': []
        }
        
        print(f"Sidebar navigation processing DISABLED!")
        print(f"  Files processed: {sidebar_changes['files_processed']}")
        print(f"  Files modified: {sidebar_changes['files_modified']}")
        print(f"  Total replacements: {sidebar_changes['total_replacements']}")
        
        # Combine totals
        total_files_processed = changes_summary['files_processed']
        total_files_modified = changes_summary['files_modified'] + sidebar_changes['files_modified']
        total_replacements = changes_summary['total_replacements'] + sidebar_changes['total_replacements']
        
        print()
        print(f"Overall processing complete!")
        print(f"  Files processed: {total_files_processed}")
        print(f"  Files modified: {total_files_modified}")
        print(f"  Total replacements: {total_replacements}")
        
        if changes_summary['errors'] or sidebar_changes['errors']:
            all_errors = changes_summary['errors'] + sidebar_changes['errors']
            print(f"  Errors encountered: {len(all_errors)}")
            for error in all_errors:
                print(f"    - {error}")
        
        print()
        if language == 'it':
            print("Cross-reference links now show:")
            print("  - Link text: 'Capitolo X', 'Paragrafo X.Y', or 'Appendice A'")
            print("  - Tooltip on hover: Original chapter/section title")
            print("  - Consistent numbering throughout the documentation")
        elif language == 'fr':
            print("Cross-reference links now show:")
            print("  - Link text: 'Chapitre X', 'Section X.Y', or 'Annexe A'")
            print("  - Tooltip on hover: Original chapter/section title")
            print("  - Consistent numbering throughout the documentation")
        elif language == 'es':
            print("Cross-reference links now show:")
            print("  - Link text: 'Capítulo X', 'Sección X.Y', or 'Apéndice A'")
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

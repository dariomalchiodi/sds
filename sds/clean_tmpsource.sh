#!/bin/bash

# Clean Temporary Source Directory Script
# This script removes the tmpsource/lang directory for a specific language

# Function to display usage information
usage() {
    echo "Usage: $0 [OPTIONS] <lang>"
    echo ""
    echo "Remove the tmpsource/lang directory for a specific language."
    echo "This script cleans up temporary files created by the batch processing."
    echo ""
    echo "OPTIONS:"
    echo "  -h, --help           Show this help message and exit"
    echo "  -f, --force          Force deletion without confirmation prompt"
    echo "  -v, --verbose        Enable verbose output"
    echo "  --all                Remove entire tmpsource directory (ignores lang argument)"
    echo ""
    echo "ARGUMENTS:"
    echo "  lang                 Language code to clean (e.g., 'en', 'it')"
    echo ""
    echo "EXAMPLES:"
    echo "  $0 it                           # Remove tmpsource/it with confirmation"
    echo "  $0 -f en                        # Force remove tmpsource/en without confirmation"
    echo "  $0 -v --force it                # Verbose force removal of tmpsource/it"
    echo "  $0 --all                        # Remove entire tmpsource directory"
    echo ""
    echo "SAFETY FEATURES:"
    echo "  - Confirmation prompt (unless --force is used)"
    echo "  - Validates directory exists before attempting deletion"
    echo "  - Shows what will be deleted before confirmation"
}

# Function to log messages (only if verbose mode is enabled)
log() {
    if [ "$VERBOSE" = true ]; then
        echo "[INFO] $1"
    fi
}

# Function to display error messages
error() {
    echo "[ERROR] $1" >&2
}

# Function to display success messages
success() {
    echo "[SUCCESS] $1"
}

# Function to display warning messages
warning() {
    echo "[WARNING] $1" >&2
}

# Default values
VERBOSE=false
FORCE=false
CLEAN_ALL=false
LANG=""

# Parse command line arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        -h|--help)
            usage
            exit 0
            ;;
        -f|--force)
            FORCE=true
            shift
            ;;
        -v|--verbose)
            VERBOSE=true
            shift
            ;;
        --all)
            CLEAN_ALL=true
            shift
            ;;
        -*)
            error "Unknown option: $1"
            echo ""
            usage
            exit 1
            ;;
        *)
            if [ -z "$LANG" ]; then
                LANG="$1"
                shift
            else
                error "Too many arguments. Only one language code is expected."
                echo ""
                usage
                exit 1
            fi
            ;;
    esac
done

# Get script directory
# Get script directory and set paths relative to project root
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
TMPSOURCE_DIR="$PROJECT_ROOT/tmpsource"

# Check if tmpsource directory exists
if [ ! -d "$TMPSOURCE_DIR" ]; then
    error "tmpsource directory not found: $TMPSOURCE_DIR"
    log "Nothing to clean"
    exit 0
fi

# Handle --all option
if [ "$CLEAN_ALL" = true ]; then
    log "Cleaning entire tmpsource directory"
    
    # Count total files for information
    TOTAL_FILES=$(find "$TMPSOURCE_DIR" -type f 2>/dev/null | wc -l)
    TOTAL_DIRS=$(find "$TMPSOURCE_DIR" -type d 2>/dev/null | wc -l)
    
    echo "About to remove entire tmpsource directory:"
    echo "  Path: $TMPSOURCE_DIR"
    echo "  Contains: $TOTAL_FILES files in $TOTAL_DIRS directories"
    
    if [ "$FORCE" = false ]; then
        echo ""
        read -p "Are you sure you want to delete the entire tmpsource directory? [y/N]: " -r
        if [[ ! $REPLY =~ ^[Yy]$ ]]; then
            echo "Operation cancelled."
            exit 0
        fi
    fi
    
    log "Removing entire tmpsource directory: $TMPSOURCE_DIR"
    rm -rf "$TMPSOURCE_DIR"
    
    if [ $? -eq 0 ]; then
        success "Entire tmpsource directory removed successfully"
    else
        error "Failed to remove tmpsource directory"
        exit 1
    fi
    
    exit 0
fi

# Check if language argument was provided
if [ -z "$LANG" ]; then
    error "Language code is required (or use --all to clean everything)."
    echo ""
    usage
    exit 1
fi

# Define target directory
TARGET_DIR="$TMPSOURCE_DIR/$LANG"

# Check if language directory exists
if [ ! -d "$TARGET_DIR" ]; then
    warning "Directory not found: $TARGET_DIR"
    log "Available language directories:"
    if [ -d "$TMPSOURCE_DIR" ]; then
        ls -1 "$TMPSOURCE_DIR" 2>/dev/null | while read -r dir; do
            if [ -d "$TMPSOURCE_DIR/$dir" ]; then
                log "  $dir"
            fi
        done
    else
        log "  None (tmpsource directory doesn't exist)"
    fi
    exit 0
fi

# Count files for information
TOTAL_FILES=$(find "$TARGET_DIR" -type f 2>/dev/null | wc -l)
TOTAL_DIRS=$(find "$TARGET_DIR" -type d 2>/dev/null | wc -l)

log "Target directory: $TARGET_DIR"
log "Contains: $TOTAL_FILES files in $TOTAL_DIRS directories"

# Show what will be deleted
echo "About to remove:"
echo "  Language: $LANG"
echo "  Path: $TARGET_DIR"
echo "  Contains: $TOTAL_FILES files in $TOTAL_DIRS directories"

# Show some file examples if verbose
if [ "$VERBOSE" = true ] && [ $TOTAL_FILES -gt 0 ]; then
    echo ""
    echo "Sample files that will be deleted:"
    find "$TARGET_DIR" -name "*.md" -type f | head -5 | while read -r file; do
        echo "  $(basename "$file")"
    done
    if [ $TOTAL_FILES -gt 5 ]; then
        echo "  ... and $(($TOTAL_FILES - 5)) more files"
    fi
fi

# Confirm deletion unless force flag is set
if [ "$FORCE" = false ]; then
    echo ""
    read -p "Are you sure you want to delete this directory? [y/N]: " -r
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "Operation cancelled."
        exit 0
    fi
fi

# Perform deletion
log "Removing directory: $TARGET_DIR"
rm -rf "$TARGET_DIR"

if [ $? -eq 0 ]; then
    success "Directory $TARGET_DIR removed successfully"
    log "Cleaned up $TOTAL_FILES files and $TOTAL_DIRS directories"
    
    # Check if tmpsource directory is now empty
    if [ -d "$TMPSOURCE_DIR" ] && [ -z "$(ls -A "$TMPSOURCE_DIR" 2>/dev/null)" ]; then
        log "tmpsource directory is now empty"
        if [ "$FORCE" = true ] || [ "$VERBOSE" = true ]; then
            echo "Tip: Use '$0 --all' to remove the entire empty tmpsource directory"
        fi
    fi
else
    error "Failed to remove directory: $TARGET_DIR"
    exit 1
fi

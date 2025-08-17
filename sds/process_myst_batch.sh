#!/bin/bash

# Batch MyST Markdown Processor Script
# This script copies a source language directory and processes all .md files within it

# Function to display usage information
usage() {
    echo "Usage: $0 [OPTIONS] <lang>"
    echo ""
    echo "Copy source/lang directory to tmpsource/lang and process all .md files."
    echo "Adds interactive Python execution capabilities to all MyST Markdown files."
    echo ""
    echo "OPTIONS:"
    echo "  -h, --help           Show this help message and exit"
    echo "  --no-setup           Disable PyScript setup block inclusion"
    echo "  -v, --verbose        Enable verbose output"
    echo "  --clean              Remove existing tmpsource directory before processing"
    echo ""
    echo "ARGUMENTS:"
    echo "  lang                 Language code (e.g., 'en', 'it')"
    echo ""
    echo "EXAMPLES:"
    echo "  $0 it                           # Process Italian files with default settings"
    echo "  $0 --no-setup en               # Process English files without PyScript setup"
    echo "  $0 -v --clean it               # Process with verbose output and clean tmpsource"
    echo ""
    echo "The script will:"
    echo "  1. Copy source/lang/ to tmpsource/lang/"
    echo "  2. Find all .md files in tmpsource/lang/"
    echo "  3. Process each .md file with interactive Python capabilities"
    echo "  4. Create backup files with .backup extension"
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
INCLUDE_SETUP=true
VERBOSE=false
CLEAN=false
LANG=""

# Parse command line arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        -h|--help)
            usage
            exit 0
            ;;
        --no-setup)
            INCLUDE_SETUP=false
            shift
            ;;
        -v|--verbose)
            VERBOSE=true
            shift
            ;;
        --clean)
            CLEAN=true
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

# Check if language argument was provided
if [ -z "$LANG" ]; then
    error "Language code is required."
    echo ""
    usage
    exit 1
fi

# Get script directory and set paths relative to project root
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
CODE_DIR="$PROJECT_ROOT/code"
SOURCE_DIR="$PROJECT_ROOT/source"
TMPSOURCE_DIR="$PROJECT_ROOT/tmpsource"

# Validate source directory structure
if [ ! -d "$SOURCE_DIR" ]; then
    error "Source directory not found: $SOURCE_DIR"
    exit 1
fi

if [ ! -d "$SOURCE_DIR/$LANG" ]; then
    error "Language directory not found: $SOURCE_DIR/$LANG"
    error "Available languages:"
    ls -1 "$SOURCE_DIR" | grep -E '^[a-z]{2}$' || echo "  None found"
    exit 1
fi

# Check if the sds.py module exists
if [ ! -f "$CODE_DIR/sds.py" ]; then
    error "sds.py module not found at: $CODE_DIR/sds.py"
    exit 1
fi

# Get the Python executable path for the project
# First try virtual environment, then fall back to system Python
if [ -f "$PROJECT_ROOT/.venv/bin/python" ]; then
    PYTHON_EXEC="$PROJECT_ROOT/.venv/bin/python"
    log "Using virtual environment Python: $PYTHON_EXEC"
elif command -v python3 >/dev/null 2>&1; then
    PYTHON_EXEC="python3"
    log "Using system Python: $PYTHON_EXEC"
elif command -v python >/dev/null 2>&1; then
    PYTHON_EXEC="python"
    log "Using system Python: $PYTHON_EXEC"
else
    error "No Python executable found. Please install Python or set up a virtual environment."
    exit 1
fi

# Verify that Python can import the required modules
log "Verifying Python setup and required modules..."
if ! $PYTHON_EXEC -c "import sys; sys.path.insert(0, '$CODE_DIR'); import sds" 2>/dev/null; then
    error "Failed to import sds module. Please ensure dependencies are installed."
    error "If using system Python, run: pip install -r requirements.txt"
    error "If using virtual environment, ensure it's properly set up with dependencies."
    exit 1
fi

# Clean tmpsource directory if requested
if [ "$CLEAN" = true ] && [ -d "$TMPSOURCE_DIR" ]; then
    log "Cleaning existing tmpsource directory"
    rm -rf "$TMPSOURCE_DIR"
fi

# Create tmpsource directory if it doesn't exist
if [ ! -d "$TMPSOURCE_DIR" ]; then
    log "Creating tmpsource directory: $TMPSOURCE_DIR"
    mkdir -p "$TMPSOURCE_DIR"
fi

# Define source and destination paths
SOURCE_LANG_DIR="$SOURCE_DIR/$LANG"
DEST_LANG_DIR="$TMPSOURCE_DIR/$LANG"

log "Source directory: $SOURCE_LANG_DIR"
log "Destination directory: $DEST_LANG_DIR"
log "Include setup: $INCLUDE_SETUP"
log "Using Python: $PYTHON_EXEC"

# Copy source directory to tmpsource
if [ -d "$DEST_LANG_DIR" ]; then
    warning "Destination directory already exists: $DEST_LANG_DIR"
    warning "Removing existing directory"
    rm -rf "$DEST_LANG_DIR"
fi

log "Copying $SOURCE_LANG_DIR to $DEST_LANG_DIR"
cp -r "$SOURCE_LANG_DIR" "$DEST_LANG_DIR"

if [ $? -ne 0 ]; then
    error "Failed to copy directory"
    exit 1
fi

success "Directory copied successfully"

# Find all .md files in the destination directory
log "Finding .md files in $DEST_LANG_DIR"
MD_FILES=($(find "$DEST_LANG_DIR" -name "*.md" -type f))

if [ ${#MD_FILES[@]} -eq 0 ]; then
    warning "No .md files found in $DEST_LANG_DIR"
    exit 0
fi

log "Found ${#MD_FILES[@]} .md files to process"

# Initialize counters
PROCESSED=0
FAILED=0

# Process each .md file
for md_file in "${MD_FILES[@]}"; do
    rel_path="${md_file#$DEST_LANG_DIR/}"
    log "Processing: $rel_path"
    
    # Create Python script to call the function
    # Convert bash boolean to Python boolean
    if [ "$INCLUDE_SETUP" = "true" ]; then
        PYTHON_INCLUDE_SETUP="True"
    else
        PYTHON_INCLUDE_SETUP="False"
    fi
    
    PYTHON_SCRIPT=$(cat << EOF
import sys
import os

# Add the code directory to the path
sys.path.insert(0, '$CODE_DIR')

try:
    from sds import process_myst_file
    
    # Process the file
    backup_path = process_myst_file('$md_file', include_setup=$PYTHON_INCLUDE_SETUP)
    
    print(f"SUCCESS: {os.path.basename('$md_file')} processed successfully!")
    if '$VERBOSE' == 'true':
        print(f"  Backup created at: {backup_path}")
    
except FileNotFoundError as e:
    print(f"ERROR: {e}", file=sys.stderr)
    sys.exit(1)
except IOError as e:
    print(f"ERROR: {e}", file=sys.stderr)
    sys.exit(1)
except RuntimeError as e:
    print(f"ERROR: {e}", file=sys.stderr)
    sys.exit(1)
except Exception as e:
    print(f"ERROR: Unexpected error processing '$md_file': {e}", file=sys.stderr)
    sys.exit(1)
EOF
)

    # Execute the Python script
    if "$PYTHON_EXEC" -c "$PYTHON_SCRIPT"; then
        ((PROCESSED++))
    else
        error "Failed to process: $rel_path"
        ((FAILED++))
    fi
done

# Display summary
echo ""
echo "=== Processing Summary ==="
echo "Language: $LANG"
echo "Source: $SOURCE_LANG_DIR"
echo "Destination: $DEST_LANG_DIR"
echo "Total files found: ${#MD_FILES[@]}"
echo "Successfully processed: $PROCESSED"
echo "Failed: $FAILED"

if [ $FAILED -eq 0 ]; then
    success "All files processed successfully!"
    echo ""
    echo "The processed files are available in: $DEST_LANG_DIR"
    echo "Original files have been backed up with .backup extension"
else
    error "$FAILED files failed to process"
    exit 1
fi

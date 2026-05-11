# Minimal makefile for Sphinx documentation with MyST processing
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = source
BUILDDIR      = build
SDSDIR        = $(BUILDDIR)/sds

# Detect available CPU count for parallel language builds
NPROCS := $(shell nproc 2>/dev/null || sysctl -n hw.logicalcpu 2>/dev/null || echo 4)

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
	@echo ""
	@echo "Additional targets:"
	@echo "  it          Build Italian documentation with MyST processing"
	@echo "  en          Build English documentation with MyST processing"
	@echo "  fr          Build French documentation with MyST processing"
	@echo "  es          Build Spanish documentation with MyST processing"
	@echo "  all         Build all language versions and copy static files"
	@echo "  assets      Regenerate superhero images and copy to _static/img/"
	@echo "  copy-static Copy static files (e.g., index.html) to build directory"
	@echo "  sync-shortener Sync URL shortener files to all language directories"
	@echo "  validate-shortener Validate shortener-mappings.json for errors"
	@echo "  clean       Remove all build artifacts and temporary files"
	@echo "  clean-all   Remove all build artifacts and temporary files (alias for clean)"
	@echo "  serve       Start development server with clean URL support"
	@echo "  test        Run unit tests"
	@echo ""
	@echo "Internationalization targets:"
	@echo "  gettext-extract     Extract translatable strings from Sphinx theme"
	@echo "  update-po           Update .po translation files for all languages"
	@echo "  compile-mo          Compile .po files to .mo files"
	@echo "  update-translations Complete translation workflow (extract + update + compile)"

# Validate and generate URL shortener (runs once even when called from multiple targets)
shortener:
	@echo "Validating and generating URL shortener..."
	@python3 sds/validate-shortener.py
	@python3 sds/generate-redirect-pages.py $(SDSDIR)

# Italian documentation build target
it: shortener _it

_it:
	@echo "Building Italian documentation..."
	@echo "Step 1/6: Processing MyST files..."
	./sds/process_myst_batch.sh it
	@echo "Step 2/6: Copying shared resources..."
	@if [ -d "$(SOURCEDIR)/_static" ]; then cp -r "$(SOURCEDIR)/_static" tmpsource/; fi
	@if [ -d "$(SOURCEDIR)/_templates" ]; then cp -r "$(SOURCEDIR)/_templates" tmpsource/; fi
	@if [ -d "$(SOURCEDIR)/data" ]; then cp -r "$(SOURCEDIR)/data" tmpsource/it/; fi
	@if [ -f "$(SOURCEDIR)/references.bib" ]; then cp "$(SOURCEDIR)/references.bib" tmpsource/; fi
	@echo "Step 3/6: Building HTML with Sphinx..."
	$(SPHINXBUILD) -q -b html tmpsource/it $(SDSDIR)/it
	@echo "Step 4/6: Copying generated Python files..."
	@find tmpsource/it -name "*.py" -type f | while read pyfile; do \
		relpath=$$(realpath --relative-to=tmpsource/it "$$pyfile"); \
		targetdir="$(SDSDIR)/it/$$(dirname "$$relpath")"; \
		mkdir -p "$$targetdir"; \
		cp "$$pyfile" "$$targetdir/"; \
	done
	@echo "Step 5/6: Post-processing HTML..."
	python3 -m sds.sds post-process $(SDSDIR)/it --language it
	@echo "Step 6/6: Copying index.html to build root..."
	@if [ -f "$(SOURCEDIR)/index.html" ]; then \
		cp "$(SOURCEDIR)/index.html" "$(BUILDDIR)/sds/"; \
		echo "✓ index.html copied to build directory"; \
	fi
	@echo "Italian documentation build complete! Output: $(SDSDIR)/it/"

# English documentation build target
en: shortener _en

_en:
	@echo "Building English documentation..."
	@echo "Step 1/5: Processing MyST files..."
	./sds/process_myst_batch.sh en
	@echo "Step 2/5: Copying shared resources..."
	@if [ -d "$(SOURCEDIR)/_static" ]; then cp -r "$(SOURCEDIR)/_static" tmpsource/; fi
	@if [ -d "$(SOURCEDIR)/_templates" ]; then cp -r "$(SOURCEDIR)/_templates" tmpsource/; fi
	@if [ -f "$(SOURCEDIR)/references.bib" ]; then cp "$(SOURCEDIR)/references.bib" tmpsource/; fi
	@echo "Step 3/5: Building HTML with Sphinx..."
	$(SPHINXBUILD) -b html tmpsource/en $(SDSDIR)/en
	@echo "Step 4/5: Post-processing HTML..."
	python3 -m sds.sds post-process $(SDSDIR)/en --language en
	@echo "Step 5/5: Copying index.html to build root..."
	@if [ -f "$(SOURCEDIR)/index.html" ]; then \
		cp "$(SOURCEDIR)/index.html" "$(BUILDDIR)/sds/"; \
		echo "✓ index.html copied to build directory"; \
	fi
	@echo "English documentation build complete! Output: $(SDSDIR)/en/"

# French documentation build target
fr: shortener _fr

_fr:
	@echo "Building French documentation..."
	@echo "Step 1/5: Processing MyST files..."
	./sds/process_myst_batch.sh fr
	@echo "Step 2/5: Copying shared resources..."
	@if [ -d "$(SOURCEDIR)/_static" ]; then cp -r "$(SOURCEDIR)/_static" tmpsource/; fi
	@if [ -d "$(SOURCEDIR)/_templates" ]; then cp -r "$(SOURCEDIR)/_templates" tmpsource/; fi
	@if [ -f "$(SOURCEDIR)/references.bib" ]; then cp "$(SOURCEDIR)/references.bib" tmpsource/; fi
	@echo "Step 3/5: Building HTML with Sphinx..."
	$(SPHINXBUILD) -b html tmpsource/fr $(SDSDIR)/fr
	@echo "Step 4/5: Post-processing HTML..."
	python3 -m sds.sds post-process $(SDSDIR)/fr --language fr
	@echo "Step 5/5: Copying index.html to build root..."
	@if [ -f "$(SOURCEDIR)/index.html" ]; then \
		cp "$(SOURCEDIR)/index.html" "$(BUILDDIR)/sds/"; \
		echo "✓ index.html copied to build directory"; \
	fi
	@echo "French documentation build complete! Output: $(SDSDIR)/fr/"

# Spanish documentation build target
es: shortener _es

_es:
	@echo "Building Spanish documentation..."
	@echo "Step 1/5: Processing MyST files..."
	./sds/process_myst_batch.sh es
	@echo "Step 2/5: Copying shared resources..."
	@if [ -d "$(SOURCEDIR)/_static" ]; then cp -r "$(SOURCEDIR)/_static" tmpsource/; fi
	@if [ -d "$(SOURCEDIR)/_templates" ]; then cp -r "$(SOURCEDIR)/_templates" tmpsource/; fi
	@if [ -f "$(SOURCEDIR)/references.bib" ]; then cp "$(SOURCEDIR)/references.bib" tmpsource/; fi
	@echo "Step 3/5: Building HTML with Sphinx..."
	$(SPHINXBUILD) -b html tmpsource/es $(SDSDIR)/es
	@echo "Step 4/5: Post-processing HTML..."
	python3 -m sds.sds post-process $(SDSDIR)/es --language es
	@echo "Step 5/5: Copying index.html to build root..."
	@if [ -f "$(SOURCEDIR)/index.html" ]; then \
		cp "$(SOURCEDIR)/index.html" "$(BUILDDIR)/sds/"; \
		echo "✓ index.html copied to build directory"; \
	fi
	@echo "Spanish documentation build complete! Output: $(SDSDIR)/es/"

# Regenerate superhero assets (grid and tree images) used in book figures.
# Requires the graphviz system package (dot) in addition to the Python graphviz package.
assets:
	@echo "Generating superhero assets..."
	@cd support && python3 generate-colored-heroes.py
	@cp support/superhero-grid.png $(SOURCEDIR)/_static/img/superhero-grid.png
	@cp support/superhero-tree.png $(SOURCEDIR)/_static/img/superhero-tree.png
	@echo "✓ Assets copied to $(SOURCEDIR)/_static/img/"

# Copy static files from source to build directory
copy-static: shortener
	@echo "Copying static files..."
	@mkdir -p $(BUILDDIR)
	@if [ -f "$(SOURCEDIR)/index.html" ]; then \
		cp "$(SOURCEDIR)/index.html" "$(BUILDDIR)/sds/"; \
		echo "✓ index.html copied to build directory"; \
	fi

# Validate and generate URL shortener files
sync-shortener:
	@echo "Validating and generating URL shortener files..."
	@python3 sds/validate-shortener.py
	@python3 sds/generate-redirect-pages.py $(SDSDIR)

# Build all language versions (languages build in parallel)
all:
	@$(MAKE) shortener
	@$(MAKE) -j$(NPROCS) _it _en _fr _es
	@if [ -f "$(SOURCEDIR)/index.html" ]; then \
		cp "$(SOURCEDIR)/index.html" "$(BUILDDIR)/sds/"; \
		echo "✓ index.html copied to build directory"; \
	fi
	@echo "All language versions built successfully!"

# Clean all build artifacts and temporary files
clean-all:
	@echo "Cleaning all build artifacts..."
	rm -rf $(BUILDDIR)
	@echo "Cleaning temporary source files..."
	./sds/clean_tmpsource.sh --force --all 2>/dev/null || true
	@echo "All artifacts cleaned!"

# Standard clean target (alias for clean-all)
clean: clean-all

# Internationalization targets for Sphinx UI elements
# (Note: Content is already multilingual via separate source directories)
gettext-extract:
	@echo "Extracting translatable strings from Sphinx theme..."
	$(SPHINXBUILD) -b gettext $(SOURCEDIR)/en $(BUILDDIR)/gettext
	@echo "Message templates created in $(BUILDDIR)/gettext/"

update-po:
	@echo "Updating translation files for all languages..."
	@for lang in it fr es; do \
		echo "Updating $$lang translations..."; \
		mkdir -p locales/$$lang/LC_MESSAGES; \
		if [ -f "locales/$$lang/LC_MESSAGES/messages.po" ]; then \
			msgmerge --update locales/$$lang/LC_MESSAGES/messages.po $(BUILDDIR)/gettext/sphinx.pot; \
		else \
			msginit --locale=$$lang --input=$(BUILDDIR)/gettext/sphinx.pot --output=locales/$$lang/LC_MESSAGES/messages.po --no-translator; \
		fi; \
	done
	@echo "Translation files updated!"

compile-mo:
	@echo "Compiling translation files..."
	@for lang in it fr es; do \
		echo "Compiling $$lang translations..."; \
		msgfmt locales/$$lang/LC_MESSAGES/messages.po -o locales/$$lang/LC_MESSAGES/messages.mo; \
	done
	@echo "Translation files compiled!"

update-translations: gettext-extract update-po compile-mo
	@echo "All translation files updated and compiled!"

# Validate shortener mappings for syntax and duplicate errors
validate-shortener:
	@echo "Validating shortener mappings..."
	python3 sds/validate-shortener.py

# Start development server with clean URL support
serve:
	@echo "Starting SDS development server..."
	@if [ ! -d "$(BUILDDIR)" ]; then \
		echo "❌ Build directory not found. Please run 'make all' first."; \
		exit 1; \
	fi
	@python3 sds/serve.py

# Test target - run unit tests
test:
	@echo "Running unit tests..."
	@python3 -m pytest tests/ -v
	@echo "All tests completed!"

.PHONY: help Makefile it en fr es _it _en _fr _es all assets shortener copy-static sync-shortener validate-shortener clean clean-all gettext-extract update-po compile-mo update-translations serve test

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

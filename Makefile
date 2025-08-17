# Minimal makefile for Sphinx documentation with MyST processing
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = source
BUILDDIR      = build
SDSDIR        = $(BUILDDIR)/sds

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

# Italian documentation build target
it:
	@echo "Building Italian documentation..."
	@echo "Step 0/7: Validating and generating URL shortener..."
	@python3 sds/validate-shortener.py
	@python3 sds/generate-redirect-pages.py $(SDSDIR)
	@echo "Step 1/8: Processing MyST files..."
	./sds/process_myst_batch.sh --clean it
	@echo "Step 2/8: Copying shared resources..."
	@if [ -d "$(SOURCEDIR)/_static" ]; then cp -r "$(SOURCEDIR)/_static" tmpsource/; fi
	@if [ -d "$(SOURCEDIR)/_templates" ]; then cp -r "$(SOURCEDIR)/_templates" tmpsource/; fi
	@if [ -f "$(SOURCEDIR)/references.bib" ]; then cp "$(SOURCEDIR)/references.bib" tmpsource/; fi
	@echo "Step 3/8: Building HTML with Sphinx..."
	$(SPHINXBUILD) -b html tmpsource/it $(SDSDIR)/it
	@echo "Step 4/8: Processing remaining {py} roles in HTML..."
	python3 sds/sds.py process-py-roles $(SDSDIR)/it --language it
	@echo "Step 5/8: Applying cross-reference improvements..."
	python3 sds/apply_crossref_improvements.py $(SDSDIR)/it
	@echo "Step 6/8: Making part titles clickable and collapsible..."
	python3 sds/sds.py make-parts-clickable $(SDSDIR)/it --language it
	@echo "Step 7/8: Cleaning temporary files..."
	./sds/clean_tmpsource.sh --force --all
	@echo "Step 8/8: Copying index.html to build root..."
	@if [ -f "$(SOURCEDIR)/index.html" ]; then \
		cp "$(SOURCEDIR)/index.html" "$(BUILDDIR)/"; \
		echo "✓ index.html copied to build directory"; \
	fi
	@echo "Italian documentation build complete! Output: $(SDSDIR)/it/"
	@echo "Note: Figure/table numbering (X.Y format) is automatically handled by Sphinx configuration."

# English documentation build target
en:
	@echo "Building English documentation..."
	@echo "Step 0/7: Validating and generating URL shortener..."
	@python3 sds/validate-shortener.py
	@python3 sds/generate-redirect-pages.py $(SDSDIR)
	@echo "Step 1/8: Processing MyST files..."
	./sds/process_myst_batch.sh --clean en
	@echo "Step 2/8: Copying shared resources..."
	@if [ -d "$(SOURCEDIR)/_static" ]; then cp -r "$(SOURCEDIR)/_static" tmpsource/; fi
	@if [ -d "$(SOURCEDIR)/_templates" ]; then cp -r "$(SOURCEDIR)/_templates" tmpsource/; fi
	@if [ -f "$(SOURCEDIR)/references.bib" ]; then cp "$(SOURCEDIR)/references.bib" tmpsource/; fi
	@echo "Step 3/8: Building HTML with Sphinx..."
	$(SPHINXBUILD) -b html tmpsource/en $(SDSDIR)/en
	@echo "Step 4/8: Processing remaining {py} roles in HTML..."
	python3 sds/sds.py process-py-roles $(SDSDIR)/en --language en
	@echo "Step 5/8: Applying cross-reference improvements..."
	python3 sds/apply_crossref_improvements.py $(SDSDIR)/en
	@echo "Step 6/8: Making part titles clickable and collapsible..."
	python3 sds/sds.py make-parts-clickable $(SDSDIR)/en --language en
	@echo "Step 7/8: Cleaning temporary files..."
	./sds/clean_tmpsource.sh --force --all
	@echo "Step 8/8: Copying index.html to build root..."
	@if [ -f "$(SOURCEDIR)/index.html" ]; then \
		cp "$(SOURCEDIR)/index.html" "$(BUILDDIR)/"; \
		echo "✓ index.html copied to build directory"; \
	fi
	@echo "English documentation build complete! Output: $(SDSDIR)/en/"
	@echo "Note: Figure/table numbering (X.Y format) is automatically handled by Sphinx configuration."

# French documentation build target
fr:
	@echo "Building French documentation..."
	@echo "Step 0/7: Validating and generating URL shortener..."
	@python3 sds/validate-shortener.py
	@python3 sds/generate-redirect-pages.py $(SDSDIR)
	@echo "Step 1/8: Processing MyST files..."
	./sds/process_myst_batch.sh --clean fr
	@echo "Step 2/8: Copying shared resources..."
	@if [ -d "$(SOURCEDIR)/_static" ]; then cp -r "$(SOURCEDIR)/_static" tmpsource/; fi
	@if [ -d "$(SOURCEDIR)/_templates" ]; then cp -r "$(SOURCEDIR)/_templates" tmpsource/; fi
	@if [ -f "$(SOURCEDIR)/references.bib" ]; then cp "$(SOURCEDIR)/references.bib" tmpsource/; fi
	@echo "Step 3/8: Building HTML with Sphinx..."
	$(SPHINXBUILD) -b html tmpsource/fr $(SDSDIR)/fr
	@echo "Step 4/8: Processing remaining {py} roles in HTML..."
	python3 sds/sds.py process-py-roles $(SDSDIR)/fr --language fr
	@echo "Step 5/8: Applying cross-reference improvements..."
	python3 sds/apply_crossref_improvements.py $(SDSDIR)/fr
	@echo "Step 6/8: Making part titles clickable and collapsible..."
	python3 sds/sds.py make-parts-clickable $(SDSDIR)/fr --language fr
	@echo "Step 7/8: Cleaning temporary files..."
	./sds/clean_tmpsource.sh --force --all
	@echo "Step 8/8: Copying index.html to build root..."
	@if [ -f "$(SOURCEDIR)/index.html" ]; then \
		cp "$(SOURCEDIR)/index.html" "$(BUILDDIR)/"; \
		echo "✓ index.html copied to build directory"; \
	fi
	@echo "French documentation build complete! Output: $(SDSDIR)/fr/"
	@echo "Note: Figure/table numbering (X.Y format) is automatically handled by Sphinx configuration."

# Spanish documentation build target
es:
	@echo "Building Spanish documentation..."
	@echo "Step 0/7: Validating and generating URL shortener..."
	@python3 sds/validate-shortener.py
	@python3 sds/generate-redirect-pages.py $(SDSDIR)
	@echo "Step 1/8: Processing MyST files..."
	./sds/process_myst_batch.sh --clean es
	@echo "Step 2/8: Copying shared resources..."
	@if [ -d "$(SOURCEDIR)/_static" ]; then cp -r "$(SOURCEDIR)/_static" tmpsource/; fi
	@if [ -d "$(SOURCEDIR)/_templates" ]; then cp -r "$(SOURCEDIR)/_templates" tmpsource/; fi
	@if [ -f "$(SOURCEDIR)/references.bib" ]; then cp "$(SOURCEDIR)/references.bib" tmpsource/; fi
	@echo "Step 3/8: Building HTML with Sphinx..."
	$(SPHINXBUILD) -b html tmpsource/es $(SDSDIR)/es
	@echo "Step 4/8: Processing remaining {py} roles in HTML..."
	python3 sds/sds.py process-py-roles $(SDSDIR)/es --language es
	@echo "Step 5/8: Applying cross-reference improvements..."
	python3 sds/apply_crossref_improvements.py $(SDSDIR)/es
	@echo "Step 6/8: Making part titles clickable and collapsible..."
	python3 sds/sds.py make-parts-clickable $(SDSDIR)/es --language es
	@echo "Step 7/8: Cleaning temporary files..."
	./sds/clean_tmpsource.sh --force --all
	@echo "Step 8/8: Copying index.html to build root..."
	@if [ -f "$(SOURCEDIR)/index.html" ]; then \
		cp "$(SOURCEDIR)/index.html" "$(BUILDDIR)/"; \
		echo "✓ index.html copied to build directory"; \
	fi
	@echo "Spanish documentation build complete! Output: $(SDSDIR)/es/"
	@echo "Note: Figure/table numbering (X.Y format) is automatically handled by Sphinx configuration."

# Copy static files from source to build directory
copy-static:
	@echo "Copying static files..."
	@mkdir -p $(BUILDDIR)
	@echo "Validating shortener mappings..."
	python3 sds/validate-shortener.py
	@echo "Generating redirect pages..."
	python3 sds/generate-redirect-pages.py $(SDSDIR)
	@echo "✓ URL shortener validation and generation complete"
	@if [ -f "$(SOURCEDIR)/index.html" ]; then \
		cp "$(SOURCEDIR)/index.html" "$(BUILDDIR)/"; \
		echo "✓ index.html copied to build directory"; \
	fi

# Validate and generate URL shortener files
sync-shortener:
	@echo "Validating and generating URL shortener files..."
	@python3 sds/validate-shortener.py
	@python3 sds/generate-redirect-pages.py $(SDSDIR)

# Build all language versions
all:
	@$(MAKE) clean-all
	@echo "Building all language versions..."
	@echo "Step 0/23: Validating and generating URL shortener..."
	@python3 sds/validate-shortener.py
	@python3 sds/generate-redirect-pages.py $(SDSDIR)
	@echo "Step 1: Processing Italian MyST files..."
	./sds/process_myst_batch.sh --clean it
	@echo "Step 2: Processing English MyST files..."
	./sds/process_myst_batch.sh en
	@echo "Step 3: Processing French MyST files..."
	./sds/process_myst_batch.sh fr
	@echo "Step 4: Processing Spanish MyST files..."
	./sds/process_myst_batch.sh es
	@echo "Step 5: Copying shared resources..."
	@if [ -d "$(SOURCEDIR)/_static" ]; then cp -r "$(SOURCEDIR)/_static" tmpsource/; fi
	@if [ -d "$(SOURCEDIR)/_templates" ]; then cp -r "$(SOURCEDIR)/_templates" tmpsource/; fi
	@if [ -f "$(SOURCEDIR)/references.bib" ]; then cp "$(SOURCEDIR)/references.bib" tmpsource/; fi
	@echo "Step 6: Building Italian HTML..."
	$(SPHINXBUILD) -b html tmpsource/it $(SDSDIR)/it
	@echo "Step 7: Processing Italian {py} roles in HTML..."
	python3 sds/sds.py process-py-roles $(SDSDIR)/it --language it
	@echo "Step 8: Applying Italian cross-reference improvements..."
	python3 sds/apply_crossref_improvements.py $(SDSDIR)/it
	@echo "Step 9: Making Italian part titles clickable and collapsible..."
	python3 sds/sds.py make-parts-clickable $(SDSDIR)/it --language it
	@echo "Step 10: Building English HTML..."
	$(SPHINXBUILD) -b html tmpsource/en $(SDSDIR)/en
	@echo "Step 11: Processing English {py} roles in HTML..."
	python3 sds/sds.py process-py-roles $(SDSDIR)/en --language en
	@echo "Step 12: Applying English cross-reference improvements..."
	python3 sdss/apply_crossref_improvements.py $(SDSDIR)/en
	@echo "Step 13: Making English part titles clickable and collapsible..."
	python3 sds/sds.py make-parts-clickable $(SDSDIR)/en --language en
	@echo "Step 14: Building French HTML..."
	$(SPHINXBUILD) -b html tmpsource/fr $(SDSDIR)/fr
	@echo "Step 15: Processing French {py} roles in HTML..."
	python3 sd/sds.py process-py-roles $(SDSDIR)/fr --language fr
	@echo "Step 16: Applying French cross-reference improvements..."
	python3 sds/apply_crossref_improvements.py $(SDSDIR)/fr
	@echo "Step 17: Making French part titles clickable and collapsible..."
	python3 sds/sds.py make-parts-clickable $(SDSDIR)/fr --language fr
	@echo "Step 18: Building Spanish HTML..."
	$(SPHINXBUILD) -b html tmpsource/es $(SDSDIR)/es
	@echo "Step 19: Processing Spanish {py} roles in HTML..."
	python3 sds/sds.py process-py-roles $(SDSDIR)/es --language es
	@echo "Step 20: Applying Spanish cross-reference improvements..."
	python3 sds/apply_crossref_improvements.py $(SDSDIR)/es
	@echo "Step 21: Making Spanish part titles clickable and collapsible..."
	python3 sds/sds.py make-parts-clickable $(SDSDIR)/es --language es
	@echo "Step 22: Copying static files..."
	@$(MAKE) copy-static
	@echo "Step 23: Cleaning all temporary files..."
	./sds/clean_tmpsource.sh --force --all
	@echo "All language versions built successfully!"
	@echo "Note: Figure/table numbering (X.Y format) is automatically handled by Sphinx configuration."

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

.PHONY: help Makefile it en fr es all copy-static sync-shortener validate-shortener clean clean-all gettext-extract update-po compile-mo update-translations serve test

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

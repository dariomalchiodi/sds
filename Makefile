# Minimal makefile for Sphinx documentation with MyST processing
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = source
BUILDDIR      = build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
	@echo ""
	@echo "Additional targets:"
	@echo "  it          Build Italian documentation with MyST processing"
	@echo "  en          Build English documentation with MyST processing"
	@echo "  fr          Build French documentation with MyST processing"
	@echo "  all         Build all language versions"
	@echo "  clean-all   Remove all build artifacts and temporary files"
	@echo ""
	@echo "Internationalization targets:"
	@echo "  gettext-extract     Extract translatable strings from Sphinx theme"
	@echo "  update-po           Update .po translation files for all languages"
	@echo "  compile-mo          Compile .po files to .mo files"
	@echo "  update-translations Complete translation workflow (extract + update + compile)"

# Italian documentation build target
it:
	@echo "Building Italian documentation..."
	@echo "Step 1/5: Processing MyST files..."
	./code/process_myst_batch.sh --clean it
	@echo "Step 2/5: Copying shared resources..."
	@if [ -d "$(SOURCEDIR)/_static" ]; then cp -r "$(SOURCEDIR)/_static" tmpsource/; fi
	@if [ -d "$(SOURCEDIR)/_templates" ]; then cp -r "$(SOURCEDIR)/_templates" tmpsource/; fi
	@if [ -f "$(SOURCEDIR)/references.bib" ]; then cp "$(SOURCEDIR)/references.bib" tmpsource/; fi
	@echo "Step 3/5: Building HTML with Sphinx..."
	$(SPHINXBUILD) -b html tmpsource/it build/it
	@echo "Step 4/5: Applying cross-reference improvements..."
	python3 code/apply_crossref_improvements.py build/it
	@echo "Step 5/5: Cleaning temporary files..."
	./code/clean_tmpsource.sh --force --all
	@echo "Italian documentation build complete! Output: build/it/"
	@echo "Note: Figure/table numbering (X.Y format) is automatically handled by Sphinx configuration."

# English documentation build target
en:
	@echo "Building English documentation..."
	@echo "Step 1/5: Processing MyST files..."
	./code/process_myst_batch.sh --clean en
	@echo "Step 2/5: Copying shared resources..."
	@if [ -d "$(SOURCEDIR)/_static" ]; then cp -r "$(SOURCEDIR)/_static" tmpsource/; fi
	@if [ -d "$(SOURCEDIR)/_templates" ]; then cp -r "$(SOURCEDIR)/_templates" tmpsource/; fi
	@if [ -f "$(SOURCEDIR)/references.bib" ]; then cp "$(SOURCEDIR)/references.bib" tmpsource/; fi
	@echo "Step 3/5: Building HTML with Sphinx..."
	$(SPHINXBUILD) -b html tmpsource/en build/en
	@echo "Step 4/5: Applying cross-reference improvements..."
	python3 code/apply_crossref_improvements.py build/en
	@echo "Step 5/5: Cleaning temporary files..."
	./code/clean_tmpsource.sh --force --all
	@echo "English documentation build complete! Output: build/en/"
	@echo "Note: Figure/table numbering (X.Y format) is automatically handled by Sphinx configuration."

# French documentation build target
fr:
	@echo "Building French documentation..."
	@echo "Step 1/5: Processing MyST files..."
	./code/process_myst_batch.sh --clean fr
	@echo "Step 2/5: Copying shared resources..."
	@if [ -d "$(SOURCEDIR)/_static" ]; then cp -r "$(SOURCEDIR)/_static" tmpsource/; fi
	@if [ -d "$(SOURCEDIR)/_templates" ]; then cp -r "$(SOURCEDIR)/_templates" tmpsource/; fi
	@if [ -f "$(SOURCEDIR)/references.bib" ]; then cp "$(SOURCEDIR)/references.bib" tmpsource/; fi
	@echo "Step 3/5: Building HTML with Sphinx..."
	$(SPHINXBUILD) -b html tmpsource/fr build/fr
	@echo "Step 4/5: Applying cross-reference improvements..."
	python3 code/apply_crossref_improvements.py build/fr
	@echo "Step 5/5: Cleaning temporary files..."
	./code/clean_tmpsource.sh --force --all
	@echo "French documentation build complete! Output: build/fr/"
	@echo "Note: Figure/table numbering (X.Y format) is automatically handled by Sphinx configuration."

# Build all language versions
all:
	@$(MAKE) clean-all
	@echo "Building all language versions..."
	@echo "Step 1: Processing Italian MyST files..."
	./code/process_myst_batch.sh --clean it
	@echo "Step 2: Processing English MyST files..."
	./code/process_myst_batch.sh en
	@echo "Step 3: Processing French MyST files..."
	./code/process_myst_batch.sh fr
	@echo "Step 4: Copying shared resources..."
	@if [ -d "$(SOURCEDIR)/_static" ]; then cp -r "$(SOURCEDIR)/_static" tmpsource/; fi
	@if [ -d "$(SOURCEDIR)/_templates" ]; then cp -r "$(SOURCEDIR)/_templates" tmpsource/; fi
	@if [ -f "$(SOURCEDIR)/references.bib" ]; then cp "$(SOURCEDIR)/references.bib" tmpsource/; fi
	@echo "Step 5: Building Italian HTML..."
	$(SPHINXBUILD) -b html tmpsource/it build/it
	@echo "Step 6: Applying Italian cross-reference improvements..."
	python3 code/apply_crossref_improvements.py build/it
	@echo "Step 7: Building English HTML..."
	$(SPHINXBUILD) -b html tmpsource/en build/en
	@echo "Step 8: Applying English cross-reference improvements..."
	python3 code/apply_crossref_improvements.py build/en
	@echo "Step 9: Building French HTML..."
	$(SPHINXBUILD) -b html tmpsource/fr build/fr
	@echo "Step 10: Applying French cross-reference improvements..."
	python3 code/apply_crossref_improvements.py build/fr
	@echo "Step 11: Cleaning all temporary files..."
	./code/clean_tmpsource.sh --force --all
	@echo "All language versions built successfully!"
	@echo "Note: Figure/table numbering (X.Y format) is automatically handled by Sphinx configuration."

# Clean all build artifacts and temporary files
clean-all:
	@echo "Cleaning all build artifacts..."
	rm -rf $(BUILDDIR)
	@echo "Cleaning temporary source files..."
	./code/clean_tmpsource.sh --force --all 2>/dev/null || true
	@echo "All artifacts cleaned!"

# Internationalization targets for Sphinx UI elements
# (Note: Content is already multilingual via separate source directories)
gettext-extract:
	@echo "Extracting translatable strings from Sphinx theme..."
	$(SPHINXBUILD) -b gettext $(SOURCEDIR)/en $(BUILDDIR)/gettext
	@echo "Message templates created in $(BUILDDIR)/gettext/"

update-po:
	@echo "Updating translation files for all languages..."
	@for lang in it fr; do \
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
	@for lang in it fr; do \
		echo "Compiling $$lang translations..."; \
		msgfmt locales/$$lang/LC_MESSAGES/messages.po -o locales/$$lang/LC_MESSAGES/messages.mo; \
	done
	@echo "Translation files compiled!"

update-translations: gettext-extract update-po compile-mo
	@echo "All translation files updated and compiled!"

.PHONY: help Makefile it en fr all clean-all gettext-extract update-po compile-mo update-translations

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

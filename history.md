
1. Create a venv using Python 3.11 in the root directory of the project.
2. Activate the venv via `source .venv/bin/activate`
3. Properly install all Python libraries via `bash setup.py`.
4. Create the project structure running `sphinx-quickstart`.
5. In the `source` directory, create the subdirs for each language.
6. Put a copy of `conf.py` and `index.md` in each language dir, then remove
   these two files in the `source` directory.
7. Modify the `conf.py` files in each language dir:
   - change the `language` field accordingly,
   - let the `html_static_path` and `templates_path` options point to the
     corresponding directories in the parent dir (that is, prepend `../` to
     the current values of the options),
   - set `html_theme` to `'sphinx_book_theme'`,
   - add the line `html_theme_options = { }`, in case you need to further
     customize the theme,
   - add the line `html_context = { }`, in case you need to pass information to
     the templates,
   - add `'myst_parser'`, `'sphinx_book_theme'` and `'sphinx_external_toc'` to
     the list in the `extensions` option,
   - add the line `myst_enable_extensions = [ 'html_admonition', 'html_image', 'colon_fence' ]`,
   - add the line `source_suffix = { '.rst': 'restructuredtext', '.md': 'markdown', }`

   - add the `locale_dirs = ['../locales/']` and `gettext_compact = False`
     lines,
   - add the line `html_css_files = ['custom.css']` to specify a custom CSS,
   - add the lines `external_toc_path = '_toc.yml'` and
     `external_toc_exclude_missing = False` in `conf.py`.
8. Extract translatable strings: in the `source` dir, and for all the
   non-default languages, run (replacing `en' with the correct idetifier)
   - `sphinx-build -b gettext en ../locales`
   - `pybabel init -l en -d ../locales -i ../locales/index.pot`
   then run `pybabel compile -d ../locales`
9. In the `_static` directory, copy or create the `custom.css` file, then
   create an `img` directory for all images.
10. In the `source` dir, run `sphinx-build -b html en ../build/en` for each
    different language (replacing `en' with the correct idetifier)

# INTERNATIONALIZATION WORKFLOW
# Extract new translatable strings from Sphinx theme
make gettext-extract

# Update translation files for it/fr (creates/updates messages.po files)  
make update-translations

# Edit locales/[lang]/LC_MESSAGES/messages.po to add translations
# Note: English (en) uses Sphinx built-in translations, no custom .po needed

# Compile translation files
make compile-mo

# Test individual language builds
make it    # Italian with custom UI translations
make en    # English with built-in Sphinx translations  
make fr    # French with custom UI translations
make all   # Build all languages

# Process for adding new translations!

# Extract current available strings
make gettext-extract

# Check if new strings appeared
diff <(grep "^msgid " build/gettext/sphinx.pot | sort) <(grep "^msgid " locales/fr/LC_MESSAGES/messages.po | sort)

# If differences exist, run the full workflow
make update-translations
# Edit .po files
make compile-mo
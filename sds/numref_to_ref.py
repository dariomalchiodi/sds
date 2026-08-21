# ### This works!

# from sphinx.domains.std import StandardDomain

# def setup(app):
#     """Setup function for the Sphinx extension."""
    
#     original_resolve_xref = StandardDomain.resolve_xref
    
#     def enhanced_resolve_xref(self, env, fromdocname, builder, typ, target, node, contnode):
#         if typ == 'numref':
#             section_patterns = ['chap_', 'sec_', 'section:', 'subsec_', 'part:', 'par_']
            
#             if any(target.startswith(pattern) for pattern in section_patterns):
#                 # For section references, resolve as 'ref' instead
#                 result = original_resolve_xref(self, env, fromdocname, builder, 'ref', target, node, contnode)
                
#                 if result is not None:
#                     # Add only-number class
#                     classes = result.get('classes', [])
#                     if 'only-number' not in classes:
#                         classes.append('only-number')
#                         result['classes'] = classes
#                     return result
        
#         # For all other cases, use original method
#         return original_resolve_xref(self, env, fromdocname, builder, typ, target, node, contnode)
    
#     StandardDomain.resolve_xref = enhanced_resolve_xref
    
#     return

import re

from sphinx.domains.std import StandardDomain

# Labels naming a part, chapter, section or sub-section, whatever separator the
# label happens to use ('sec_liste', 'sec-frequenze-cumulate', 'sec:quantili').
# Their numbers are assigned by the HTML post-processing step in sds.py, so both
# {ref} and {numref} to them are resolved as plain 'ref' here and get a class
# telling post-processing what to write in their place.
_SECTION_TARGET_RE = re.compile(
    r'^(?:chap|chapter|sec|section|subsec|subsubsec|part|par|paragraph)[-_:]',
    re.IGNORECASE)


def setup(app):
    """Setup function for the Sphinx extension."""

    # Store the original resolve_xref method
    original_resolve_xref = StandardDomain.resolve_xref

    def _target_figtype(self, env, target):
        """Return the enumerable node type ('table', 'figure', ...) of a
        cross-reference target, or None if it cannot be determined."""
        if target in self.labels:
            docname, labelid, _ = self.labels[target]
        elif target in self.anonlabels:
            docname, labelid = self.anonlabels[target]
        else:
            return None
        if not docname:
            return None
        try:
            target_node = env.get_doctree(docname).ids.get(labelid)
        except Exception:
            return None
        if target_node is None:
            return None
        return self.get_enumerable_node_type(target_node)

    def _add_class(result, class_name):
        """Add a class to a resolved reference node and return it."""
        existing_classes = result.get('classes', [])
        if class_name not in existing_classes:
            existing_classes.append(class_name)
            result['classes'] = existing_classes
        return result

    def enhanced_resolve_xref(self, env, fromdocname, builder, typ, target, node, contnode):
        # Handle numref for sections/chapters
        if typ == 'numref':
            # Check if this is a part/chapter/section/sub-section reference
            if _SECTION_TARGET_RE.match(target):
                # Try to resolve as 'ref' instead of 'numref'
                result = original_resolve_xref(self, env, fromdocname, builder, 'ref', target, node, contnode)

                if result is not None:
                    # Add the only-number class: post-processing then keeps just
                    # the number, dropping the "Paragrafo"/"Capitolo" label.
                    return _add_class(result, 'only-number')

        # Swap {ref}/{numref} behaviour for tables:
        #   {ref}    -> "Tabella X" (the full numfig label, normally numref's job)
        #   {numref} -> "X"         (just the number)
        # An explicit caption (e.g. {ref}`text <label>`) is always left untouched.
        if typ in ('ref', 'numref') and not node.get('refexplicit'):
            if _target_figtype(self, env, target) == 'table':
                if typ == 'ref':
                    # Render the full "Tabella X" label via the numref machinery.
                    return original_resolve_xref(
                        self, env, fromdocname, builder, 'numref', target, node, contnode
                    )
                else:  # typ == 'numref'
                    # Render just the number by temporarily reducing the table
                    # numfig_format to a bare "%s".
                    orig_format = env.config.numfig_format
                    patched_format = dict(orig_format)
                    patched_format['table'] = '%s'
                    env.config.numfig_format = patched_format
                    try:
                        return original_resolve_xref(
                            self, env, fromdocname, builder, 'numref', target, node, contnode
                        )
                    finally:
                        env.config.numfig_format = orig_format

        # Mark {ref} to a part/chapter/section/sub-section written without a
        # caption of its own, so that post-processing can replace its text
        # (the heading title, as Sphinx renders it) with "Paragrafo X.Y.Z".
        # References that do carry a caption — {ref}`text <sec_liste>` or the
        # markdown form [text](sec_liste) — stay untouched.
        if typ == 'ref' and not node.get('refexplicit') \
                and _SECTION_TARGET_RE.match(target):
            result = original_resolve_xref(
                self, env, fromdocname, builder, typ, target, node, contnode
            )
            if result is not None:
                return _add_class(result, 'sds-secref')

        # For all other cases (including figure numref), use original method
        return original_resolve_xref(self, env, fromdocname, builder, typ, target, node, contnode)

    # Replace the resolve_xref method
    StandardDomain.resolve_xref = enhanced_resolve_xref
    
    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
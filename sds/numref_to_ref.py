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

from sphinx.domains.std import StandardDomain

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

    def enhanced_resolve_xref(self, env, fromdocname, builder, typ, target, node, contnode):
        # Handle numref for sections/chapters
        if typ == 'numref':
            # Define section/chapter patterns (using colons as they appear in the original labels)
            section_patterns = [
                'chap_', 'chapter:',
                'sec_', 'section:', 'subsec_', 'subsubsec_',
                'part:', 'par_', 'paragraph:'
            ]

            # Check if this is a section/chapter reference
            if any(target.startswith(pattern) for pattern in section_patterns):
                # Try to resolve as 'ref' instead of 'numref'
                result = original_resolve_xref(self, env, fromdocname, builder, 'ref', target, node, contnode)

                if result is not None:
                    # Add the only-number class
                    existing_classes = result.get('classes', [])
                    if 'only-number' not in existing_classes:
                        existing_classes.append('only-number')
                        result['classes'] = existing_classes
                    return result

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

        # For all other cases (including figure numref), use original method
        return original_resolve_xref(self, env, fromdocname, builder, typ, target, node, contnode)

    # Replace the resolve_xref method
    StandardDomain.resolve_xref = enhanced_resolve_xref
    
    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
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
        
        # For all other cases (including figure/table numref), use original method
        return original_resolve_xref(self, env, fromdocname, builder, typ, target, node, contnode)
    
    # Replace the resolve_xref method
    StandardDomain.resolve_xref = enhanced_resolve_xref
    
    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
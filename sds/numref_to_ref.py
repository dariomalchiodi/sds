from sphinx.transforms import SphinxTransform
from sphinx.addnodes import pending_xref
from docutils import nodes

def setup(app):
    """Setup function for the Sphinx extension."""
    
    # Add a transform that runs BEFORE reference resolution
    app.add_transform(NumrefToRefTransform)
    
    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }

class NumrefToRefTransform(SphinxTransform):
    """Transform that converts numref to ref with only-number class."""
    
    default_priority = 200  # Run BEFORE ReferencesResolver (which is at 210)
    
    def apply(self):
        # Process numref nodes and convert them to ref nodes with only-number class
        for node in self.document.traverse(pending_xref):
            if node.get('reftype') == 'numref':
                # Change reftype to 'ref' so it gets resolved like a ref
                node['reftype'] = 'ref'
                # Add a marker to identify this as a converted numref
                node['converted_numref'] = True
                # Add the only-number class
                existing_classes = node.get('classes', [])
                if 'only-number' not in existing_classes:
                    existing_classes.append('only-number')
                    node['classes'] = existing_classes
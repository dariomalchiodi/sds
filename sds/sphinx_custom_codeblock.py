from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.directives.code import CodeBlock

class CustomCodeBlock(CodeBlock):
    option_spec = CodeBlock.option_spec.copy()
    option_spec['height'] = directives.unchanged
    
    def run(self):
        # Get the height option if specified
        height = self.options.get('height', None)
        
        # Run the parent directive to get the code block
        result = super().run()
        
        # If height is specified, add it as a data attribute or CSS class
        if height and result:
            # Add height as a data attribute to the container
            container = result[0]
            if hasattr(container, 'attributes'):
                container.attributes['data-height'] = height
            
        return result

def setup(app):
    app.add_directive('code-block', CustomCodeBlock, override=True)
    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
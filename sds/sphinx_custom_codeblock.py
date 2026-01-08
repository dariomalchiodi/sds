from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.directives.code import CodeBlock

from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter

# class CustomCodeBlock(CodeBlock):
#     option_spec = CodeBlock.option_spec.copy()
#     option_spec['height'] = directives.unchanged
    
#     def run(self):
#         # Get the height option if specified
#         height = self.options.get('height', None)
        
#         # Run the parent directive to get the code block
#         result = super().run()
        
#         # If height is specified, add it as a data attribute or CSS class
#         if height and result:
#             # Add height as a data attribute to the container
#             container = result[0]
#             if hasattr(container, 'attributes'):
#                 container.attributes['data-height'] = height
            
#         return result

class InteractiveCodeBlock(CodeBlock):
    option_spec = CodeBlock.option_spec.copy()
    option_spec['height'] = directives.unchanged
    option_spec['tags'] = directives.unchanged
    option_spec['class'] = directives.class_option

    id_counter = 0
    current_docname = None
    
    def run(self):
        env = self.state.document.settings.env
        if InteractiveCodeBlock.current_docname != env.docname:
            InteractiveCodeBlock.current_docname = env.docname
            InteractiveCodeBlock.id_counter = 0
            
        height = self.options.get('height', '400px')
        tags_str = self.options.get('tags', '[]').strip()
        custom_classes = self.options.get('class', [])

        if tags_str != '' and tags_str[0] == '[' and tags_str[-1] == ']':
            tags_str = tags_str[1:-1]
            tags = [tag.strip() for tag in tags_str.split(',')]
        else:
            raise ValueError(f"The 'tags' option must be in the format: [tag1, tag2, ...]")
        
        InteractiveCodeBlock.id_counter += 1

        # Get the Python code
        code = '\n'.join(self.content)
        code = code.replace('%this%', str(InteractiveCodeBlock.id_counter))
        code = code.replace(':tags:', '#')

        # Highlight the code using Pygments
        lexer = PythonLexer()
        formatter = HtmlFormatter(nowrap=True)
        highlighted_code = highlight(code, lexer, formatter)

        html = ''

        if 'toggle-code' in tags:
            html = '<div class="toggle-code-wrapper">\n'
            html += '  <button class="toggle-code-button">'
            html += '    <span class="triangle">▶</span>'
            html += '    <span class="button-text"> AAAA</span>'
            html += '  </button>'
            html += '  <div class="toggle-code-content">'

        code_cell_classes = 'cell docutils container'
        if custom_classes:
            code_cell_classes += ' ' + ' '.join(custom_classes)

        html += f'<div class="{code_cell_classes}">\n'
        html += '  <div class="cell_input docutils container">\n'
        html += '    <div class="highlight-ipython3 notranslate">\n'
        html += '      <div class="highlight">\n'
        html += f'        <pre tabindex="-1">\n{highlighted_code}\n</pre>\n'
        html += '      </div>\n    </div>\n  </div>\n</div>\n'

        if 'toggle-code' in tags:
            html += '  </div>\n</div>\n'


        i = InteractiveCodeBlock.id_counter

        if 'no-output' in tags:
            print(f'no-output tag in cell {i}, skipping output divs')
    
        html += f'<div class="cell-div-container">\n'
        html += f'  <div class="splash" id="splash-{i}" ' + \
                f'style="height: {height};"></div>\n'
        html += f'  <div class="cell-out" id="out-{i}"></div>\n'
        html += f'  <div class="cell-stdout" id="stdout-{i}"></div>\n'
        html += f'  <div class="cell-stderr" id="stderr-{i}"></div>\n'
        html += f'  <div class="cell-graph no-mathjax" id="graph-{i}"></div>\n'
        html += '</div>\n'
        result = [nodes.raw('', html, format='html')]
        if height and result:
            # Add height as a data attribute to the container
            container = result[0]
            if hasattr(container, 'attributes'):
                container.attributes['data-height'] = height
        return result

def setup(app):
    app.add_directive('interactive-code', InteractiveCodeBlock, override=True)
    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }







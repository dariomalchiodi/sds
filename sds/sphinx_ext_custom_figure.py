from docutils import nodes
from sphinx.util.docutils import SphinxDirective
from docutils.parsers.rst import directives

class CustomFigureDirective(SphinxDirective):
    has_content = True
    option_spec = {
        'name': lambda x: x,
        'class': directives.class_option,
        'width': directives.length_or_percentage_or_unitless,
    }

    def run(self):
        figure_node = nodes.figure()

        # Handle class option
        if 'class' in self.options:
            figure_node['classes'].extend(self.options['class'])

        # Handle width option
        if 'width' in self.options:
            figure_node['width'] = self.options['width']

        temp_node = nodes.Element()
        self.state.nested_parse(self.content, self.content_offset, temp_node)

        caption_node = None
        caption_text = ""
        if temp_node and isinstance(temp_node[-1], nodes.paragraph):
            caption_paragraph = temp_node.pop()
            caption_text = caption_paragraph.astext()
            caption_node = nodes.caption()
            caption_node.extend(caption_paragraph.children)

        figure_node.extend(temp_node.children)
        if caption_node:
            figure_node += caption_node

        if 'name' in self.options:
            name = self.options['name']
            figure_node['ids'].append(name)
            figure_node['names'].append(name)

            # Only register if not already in domain
            domain = self.env.get_domain('std')
            if name not in domain.labels:
                self.state.document.note_explicit_target(figure_node)
                domain.labels[name] = (self.env.docname, name, caption_text)
                domain.anonlabels[name] = (self.env.docname, name)

        return [figure_node]


def setup(app):
    app.add_directive("customfigure", CustomFigureDirective)
    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
from docutils import nodes
from sphinx.util.docutils import SphinxDirective

class CustomFigureDirective(SphinxDirective):
    has_content = True
    optional_arguments = 1  # optional label for HTML ID

    def run(self):
        env = self.state.document.settings.env

        # Standard figure node
        figure_node = nodes.figure()

        # Parse directive content as normal (so your Python blocks still execute)
        container = nodes.Element()
        self.state.nested_parse(self.content, self.content_offset, container)

        # First paragraph = caption
        caption_node = None
        if container and isinstance(container[0], nodes.paragraph):
            caption_node = nodes.caption("", "", *container[0].children)
            container.pop(0)

        # Append the remaining processed content
        for child in container:
            figure_node += child

        # Append caption at the bottom
        if caption_node:
            figure_node += caption_node

        # Number the figure if numfig is enabled
        if env.config.numfig:
            self.add_name(figure_node)
            self.set_source_info(figure_node)

        # Optional HTML ID
        if self.arguments:
            safe_id = self.arguments[0].strip().replace(":", "-").replace(" ", "_")
            figure_node['ids'].append(safe_id)

        return [figure_node]


def setup(app):
    app.add_directive("customfigure", CustomFigureDirective)
    return {
        "version": "1.0",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }

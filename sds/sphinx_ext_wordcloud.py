import json
from docutils import nodes
from sphinx.util.docutils import SphinxDirective


class sds_wordcloud_node(nodes.General, nodes.Element):
    pass


class SdsWordcloudDirective(SphinxDirective):
    has_content = True
    required_arguments = 0
    optional_arguments = 0
    option_spec = {}

    def run(self):
        words = []
        for line in self.content:
            line = line.strip()
            if not line:
                continue
            if ':' in line:
                term, _, raw_weight = line.rpartition(':')
                term = term.strip()
                try:
                    weight = float(raw_weight.strip())
                except ValueError:
                    weight = 1.0
            else:
                term = line
                weight = 1.0
            if term:
                words.append({'term': term, 'weight': weight})

        node = sds_wordcloud_node()
        node['words'] = words
        return [node]


def visit_wordcloud_html(self, node):
    data = json.dumps(node.get('words', []), ensure_ascii=False)
    # Single-quoted attribute: escape & < > and lone apostrophes in the JSON
    data_attr = data.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace("'", '&#39;')
    self.body.append(f"<div class=\"sds-wordcloud\" data-words='{data_attr}'></div>\n")
    raise nodes.SkipNode


def _passthrough(self, node):
    pass


def setup(app):
    app.add_node(
        sds_wordcloud_node,
        html=(visit_wordcloud_html, _passthrough),
        latex=(_passthrough, _passthrough),
    )
    app.add_directive('sds-wordcloud', SdsWordcloudDirective)
    return {'version': '0.1', 'parallel_read_safe': True}

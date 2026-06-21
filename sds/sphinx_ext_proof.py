from docutils import nodes
from sphinx.util.docutils import SphinxDirective

PROOF_LABELS = {
    'it': 'Dimostrazione',
    'en': 'Proof',
    'fr': 'Démonstration',
    'es': 'Demostración',
}


class sds_proof_node(nodes.General, nodes.Element):
    pass


class sds_proof_header_node(nodes.General, nodes.Element):
    pass


class sds_proof_body_node(nodes.General, nodes.Element):
    pass


class SdsProofDirective(SphinxDirective):
    has_content = True
    required_arguments = 0
    optional_arguments = 1
    final_argument_whitespace = True
    option_spec = {}

    def run(self):
        lang = getattr(self.env.config, 'language', None) or 'it'
        label = PROOF_LABELS.get(lang[:2], 'Proof')
        extra = self.arguments[0] if self.arguments else None

        container = sds_proof_node()

        header = sds_proof_header_node()
        em = nodes.emphasis()
        em += nodes.Text(label)
        if extra:
            em += nodes.Text(' (')
            inline_nodes, _ = self.state.inline_text(extra, self.lineno)
            em.extend(inline_nodes)
            em += nodes.Text(')')
        header += em
        header += nodes.Text('.')
        container += header

        body = sds_proof_body_node()
        self.state.nested_parse(self.content, self.content_offset, body)
        container += body

        return [container]


def _passthrough(self, node):
    pass


def setup(app):
    app.add_node(
        sds_proof_node,
        html=(
            lambda self, node: self.body.append('<div class="sds-proof">'),
            lambda self, node: self.body.append('</div>\n'),
        ),
        latex=(_passthrough, _passthrough),
    )
    app.add_node(
        sds_proof_header_node,
        html=(
            lambda self, node: self.body.append('<p class="sds-proof-header">'),
            lambda self, node: self.body.append('</p>\n'),
        ),
        latex=(_passthrough, _passthrough),
    )
    app.add_node(
        sds_proof_body_node,
        html=(
            lambda self, node: self.body.append('<div class="sds-proof-body">'),
            lambda self, node: self.body.append('</div>\n'),
        ),
        latex=(_passthrough, _passthrough),
    )
    app.add_directive('sds-proof', SdsProofDirective)
    return {'version': '0.1', 'parallel_read_safe': True}

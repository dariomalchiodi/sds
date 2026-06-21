from docutils import nodes
from docutils.statemachine import StringList
from sphinx.util.docutils import SphinxDirective

SEPARATOR = '+++'


class tf_item_node(nodes.General, nodes.Element):
    pass


class tf_question_node(nodes.General, nodes.Element):
    pass


class tf_verdict_node(nodes.General, nodes.Element):
    pass


def _split_stringlist(content, sep_idx):
    """Split a StringList at sep_idx preserving per-line (source, offset) metadata.

    Plain ViewList slicing (content[a:b]) works in some docutils versions but
    silently drops or misreports the items metadata in others, which causes
    Sphinx's cross-reference resolver to fail to find pending_xref nodes inside
    the split fragments.  Building new StringLists from the underlying .data and
    .items lists is always safe.
    """
    data  = list(content.data)
    items = list(content.items)
    before = StringList(initlist=data[:sep_idx],  items=items[:sep_idx])
    after  = StringList(initlist=data[sep_idx+1:], items=items[sep_idx+1:])
    return before, after


class TfItemDirective(SphinxDirective):
    has_content = True
    required_arguments = 0
    optional_arguments = 0
    option_spec = {}

    def run(self):
        content = self.content

        sep_idx = next(
            (i for i, line in enumerate(content) if line.strip() == SEPARATOR),
            None,
        )

        container = tf_item_node()

        q_node = tf_question_node()
        a_node = tf_verdict_node()

        if sep_idx is None:
            self.state.nested_parse(content, self.content_offset, q_node)
        else:
            q_content, a_content = _split_stringlist(content, sep_idx)
            self.state.nested_parse(q_content, self.content_offset, q_node)
            self.state.nested_parse(
                a_content, self.content_offset + sep_idx + 1, a_node
            )

        container += q_node
        container += a_node

        return [container]


def _passthrough(self, node):
    pass


def setup(app):
    app.add_node(
        tf_item_node,
        html=(
            lambda self, node: self.body.append('<div class="tf-item">'),
            lambda self, node: self.body.append('</div>\n'),
        ),
        latex=(_passthrough, _passthrough),
    )
    app.add_node(
        tf_question_node,
        html=(
            lambda self, node: self.body.append('<div class="tf-question">'),
            lambda self, node: self.body.append('</div>\n'),
        ),
        latex=(_passthrough, _passthrough),
    )
    app.add_node(
        tf_verdict_node,
        html=(
            lambda self, node: self.body.append('<div class="tf-verdict">'),
            lambda self, node: self.body.append('</div>\n'),
        ),
        latex=(_passthrough, _passthrough),
    )
    app.add_directive('tf-item', TfItemDirective)
    return {'version': '0.1', 'parallel_read_safe': True}

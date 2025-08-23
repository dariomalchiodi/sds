from docutils import nodes
from docutils.parsers.rst import roles

def external_link_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
    # Support syntax: :extlink:`text <url>`
    if '<' in text and text.endswith('>'):
        label, url = text.rsplit('<', 1)
        label = label.rstrip(' `')
        url = url[:-1].strip()
    else:
        # fallback: use text as both label and url
        label = text
        url = text
    node = nodes.reference(rawtext, label, refuri=url, **options)
    node['target'] = '_blank'
    node['classes'].append('external')
    return [node], []

def setup(app):
    roles.register_local_role('extlink', external_link_role)
    return {'version': '0.1', 'parallel_read_safe': True}

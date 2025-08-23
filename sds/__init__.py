
def setup(app):
    # Register the external link role
    from . import external_link_role
    external_link_role.setup(app)
    # ...add other extension setup here if needed...
    return {'version': '0.1', 'parallel_read_safe': True}

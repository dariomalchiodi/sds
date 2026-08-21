"""Add a ``{prf:numref}`` role to sphinx-proof.

``{prf:ref}`teo-lotus``` renders the full label, e.g. "Theorem 25" (localized
to "Teorema 25" by the sds.py post-processing).  ``{prf:numref}`teo-lotus```
renders only the number — "25" — while keeping the hyperlink, mirroring how
``{ref}`` and ``{numref}`` differ for sections, figures and tables.

Implementation: register the role in the ``prf`` domain and wrap
``ProofDomain.resolve_xref`` so that, for ``typ == "numref"``, it emits the bare
number instead of ``"{type} {number}"``.  Everything else is delegated to
sphinx-proof's own resolver — including a reference carrying its own caption
(``{prf:numref}`testo <teo-lotus>```, where there is no label to strip) and one
pointing at a ``:nonumber:`` block, which has no number to show.
"""
from docutils import nodes
from sphinx.util import logging
from sphinx.util.nodes import make_refnode

from sphinx_proof.domain import ProofDomain, ProofXRefRole

logger = logging.getLogger(__name__)

_orig_resolve_xref = ProofDomain.resolve_xref


def _resolve_xref(self, env, fromdocname, builder, typ, target, node, contnode):
    def delegate():
        return _orig_resolve_xref(
            self, env, fromdocname, builder, typ, target, node, contnode
        )

    if (typ != "numref"
            or node.attributes.get("refdomain", "") != self.name
            or node.attributes.get("refexplicit")):
        return delegate()

    try:
        match = env.proof_list[target]
    except Exception:
        logger.warning(
            "label '%s' not found." % target,
            location=self.env.doc2path(fromdocname)[:-3],
            color="red",
        )
        return None

    todocname = match["docname"]
    if match["nonumber"]:
        # Nothing to show: leave sphinx-proof's own text in place rather than
        # emit an empty, invisible link.
        return delegate()

    # The counter the block is numbered under ('example', 'theorem', …).
    # sphinx-proof calls this field 'countertype', older releases 'type'.
    countertype = match.get("countertype") or match.get("type")
    try:
        number = ".".join(
            map(str, env.toc_fignumbers[todocname][countertype][target])
        )
    except (KeyError, TypeError):
        # Falling back silently here would make {prf:numref} look exactly like
        # {prf:ref}, so make the failure audible instead.
        logger.warning(
            "no number found for label '%s' (counter %r): {prf:numref} falls "
            "back to the full label." % (target, countertype),
            location=self.env.doc2path(fromdocname)[:-3],
            color="red",
        )
        return delegate()
    return make_refnode(
        builder, fromdocname, todocname, target, nodes.Text(number)
    )


def setup(app):
    # Make sure the prf domain is registered before we extend it.
    app.setup_extension("sphinx_proof")

    if getattr(ProofDomain.resolve_xref, "_sds_numref_patched", False) is False:
        _resolve_xref._sds_numref_patched = True
        ProofDomain.resolve_xref = _resolve_xref

    # Register {prf:numref} alongside the existing {prf:ref}.
    app.add_role_to_domain("prf", "numref", ProofXRefRole())

    return {
        "version": "0.1",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }

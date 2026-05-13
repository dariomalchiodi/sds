---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  name: python3
  display_name: Python 3
---

(chap_set-theory)=
# Set theory

In 1895, Georg Cantor proposed a definition capable of capturing the intuitive
idea of a set with remarkable precision: «by a manifold or set I mean any
_many_ which can be thought of as _one_» [^cantor-quote]. In this view, a set
is a grouping of distinct objects sharing some common property. Shortly
afterwards, Cantor refined his definition: «by a "set" we mean any collection
$M$ of definite, distinct objects $m$ of our intuition or our thought — called
the "elements" of $M$» {cite}`cantor-1895`.

A few years later, the mathematical community discovered that this approach,
now known as _naïve set theory_, harboured logical pitfalls and paradoxes; to
avoid them, it became necessary to refound the subject on a far more rigorous
axiomatic system {cite}`suppes`. Even so, in this book I have chosen to adopt
the naïve perspective: although less formal, it allows me to keep the treatment
simple and focused on the pedagogical aims of this book, without overloading
the discussion. As Rudy Rucker observes, it is telling that the word _set_
holds the longest entry of all terms in the _Oxford English Dictionary_
{cite}`rucker`.

[^cantor-quote]: Translated from the original: "Unter einer 'Mannigfaltigkeit'
oder 'Menge' verstehe ich nämlich allgemein jedes Viele, welches sich als
Eines denken lässt" {cite}`cantor-1883`. The italics in the English translation
have been added by the author to highlight the conceptual contrast between
plurality and unity.

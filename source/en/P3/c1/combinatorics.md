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

(chap_combinatorics)=
# Combinatorics

_Combinatorics_ is the branch of mathematics concerned with determining the
number of ways in which the elements of a finite set can be grouped or ordered.
As one might intuit, this number does not depend on the nature of the objects
considered: whether we are dealing with tangible items (such as fruit or
bicycles) or abstract entities (such as a superhero's powers or the colours for
the walls of an office), the logic needed to count their configurations remains
unchanged.

To approach a counting problem correctly, it is important to answer three
fundamental questions:

- Can the same element be chosen more than once?
- Are all the starting elements distinct, or are some of them
  _indistinguishable_ from one another?
- Does the order in which elements are selected matter, or not?

Once these aspects have been clarified, the number of possible configurations
generally depends on just two parameters: the size $n$ of the starting set and
the number $k$ of elements we intend to select.

A particularly effective metaphor is the following: imagine assigning $n$
_objects_ (tangible or otherwise) to $k$ available _slots_. In the sections
that follow, I will analyse the main modes of grouping and ordering, and for
each of them I will show how to derive the formula for calculating the number
of possible cases.

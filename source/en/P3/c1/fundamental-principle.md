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

(sec_fundamental-principle-combinatorics)=
# Fundamental principle

```{figure} https://static.wikia.nocookie.net/marvel_dc/images/8/8c/Detective_Comics_241.jpg/revision/latest?cb=20081218152007
---
figclass: margin
name: fig_dc-241-en
width: 200px
align: left
---
Cover of _Detective Comics_ issue 241 (March 1957). Trademarks & Copyright © 1935–2026 DC Comics, Inc. Source: [DC Database, Fandom](https://dc.fandom.com/wiki/Detective_Comics_Vol_1_241).
```
It may seem strange, but in some stories Batman has worn costumes far more
colourful than the classic grey of the original comics or the black of the more
recent films. Issue 241 of _Detective Comics_ features a story titled «The
Rainbow Batman». In this version, the Dark Knight alternates orange, green, and
pink outfits, with the goal of drawing attention to himself rather than to a
wound on Robin's arm that might have aroused suspicion because it matched one
sustained by Dick Grayson {cite}`robb`. Let us slightly modify the scenario:
imagine that Batman has in his wardrobe four capes (pink, green, red, and
brown) and three costumes (yellow, light blue, and black). In how many
different ways can he pair a cape with a costume? The
{numref}`fig_fundamental-principle-en` shows the answer: for each of the four
capes there are three possible costumes, so the total pairings are
$4 \times 3 = 12$.

```{figure} ../../../_static/img/superhero-grid.png
:width: 50%
:name: fig_fundamental-principle-en

A simple illustration of the fundamental principle of combinatorics:
with four possible options for a first choice and three options for a second
choice, there are twelve combined choices in total
(image created from scratch by the author using AI (ChatGPT) and graphic
post-production).
```

Generalising, we obtain the so-called _fundamental principle of combinatorics_:
when making $t$ choices, if the first can be made in $s_1$ ways, the second in
$s_2$ ways, the third in $s_3$ ways, and so on, then the total number of choice
sequences is

```{math}
s_1 \cdot \ldots \cdot s_t = \prod_{i=1}^t s_i \enspace.
```

The same result can also be obtained by building a decision tree: the number of
possible ways of making the $t$ choices equals the number of leaves of a tree
of depth $t$ in which the first level has $s_1$ nodes, each with $s_2$
children, where each child in turn has $s_3$ children, and so on, as
highlighted in {numref}`fig_tree-en`.

```{figure} ../../../_static/img/superhero-tree.png
:width: 100%
:name: fig_tree-en

The tree corresponding to the possible choices in
{numref}`fig_fundamental-principle-en` (image created from scratch by the
author using AI (ChatGPT) and graphic post-production).
```

As I emphasised at the beginning of the chapter, the application of the
fundamental principle of combinatorics does not depend on the nature of the
objects considered, whether they be capes, costumes, vegetables, or financial
instruments. If, in the previous example, we had been pairing three colours
with four Batmobile models, we would have obtained the same numerical result.
This is true in general: the results of combinatorics depend on the size of the
objects and, when needed, on the number of slots considered. For this reason we
speak, for example, of the _permutations_ of $n$ objects or the _combinations_
of $n$ objects in $k$ slots, using the terms «object» and «slot» in the
abstract sense. In the sections that follow I will often refer to specific
objects, however, in order to illustrate the concepts presented one by one.


## Exercises

````{exercise} •••
:label: ex-en-disp-justice-society-categories

The [Justice Society of
America](https://dc.fandom.com/wiki/Justice_Society_of_America_(New_Earth))
sends three members on a mission in sequence (the first opens hostilities, the
second intervenes in the thick of the fight, the third covers the retreat),
choosing from four superheroes with supernatural powers (Green Lantern, Flash,
Doctor Fate, and Hourman) and three vigilantes without superpowers (Sandman,
Wildcat, and Starman). How many sequences are possible if the first position
must be filled by a superhero and the last by a vigilante?
````
````{solution} ex-en-disp-justice-society-categories
:class: dropdown

The three slots must be filled respecting the category constraints:

- the first slot goes to one of the four superheroes with supernatural powers;
- the last slot goes to one of the three vigilantes;
- the central position can be occupied by any one of the five remaining heroes.

By the fundamental principle of combinatorics, the number of valid sequences
is $4 \cdot 5 \cdot 3 = 60$.
````

````{exercise} ••
:label: ex-en-fpc-xmen-threat

To classify an X-Men mission, Cerebro assigns:

- a threat level from $6$ possible values;
- a priority from $4$ possible values;
- an operational sector from $5$ possible values.

How many distinct mission codes can it produce?
````
````{solution} ex-en-fpc-xmen-threat
:class: dropdown

Each code is obtained by sequentially choosing one entry for each of the three
categories. By the fundamental principle of combinatorics, the possible codes
are therefore $6 \cdot 4 \cdot 5 = 120$.
````

````{exercise} ••
:label: ex-en-fpc-avengers-shifts

The Avengers must cover three shifts (morning, afternoon, night), always
choosing a different member from eight available. In how many ways can the
daily rota be drawn up?
````
````{solution} ex-en-fpc-avengers-shifts
:class: dropdown

For the morning shift there are eight choices, for the afternoon seven (because
the member chosen in the morning cannot be reused), and for the night six (by
an analogous argument). By the fundamental principle of combinatorics, the
possible ways of assigning the shifts are $8 \cdot 7 \cdot 6 = 336$.
````

````{exercise} •••
:label: ex-en-fpc-defenders-leader-constraint

The [Defenders](https://marvel.fandom.com/wiki/Defenders_(Earth-616)) must
assign three distinct roles: team leader, tactical analyst, and operational
support, from seven candidates. Jessica Jones, if selected, can only serve as
team leader. How many assignments are possible?
````
````{solution} ex-en-fpc-defenders-leader-constraint
:class: dropdown

Consider separately the cases in which Jessica Jones is selected or not. In
the first case, the leader role is fixed, and the two remaining roles can be
assigned to the remaining six candidates. This can be done in $d_{6, 2}$
different ways. In the second case, there are only six candidates for the three
roles, so there are $d_{6, 3}$ ways to proceed. Adding the two results, the
possible assignments are $d_{6, 2} + d_{6, 3} = 6 \cdot 5 + 6 \cdot 5 \cdot 4
= 30 + 120 = 150$.
````

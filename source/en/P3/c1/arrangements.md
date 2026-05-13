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

(sec_arrangements)=
# Arrangements

An arrangement of $n$ distinct objects in $k$ slots is any sequence of $k$
symbols, each representing one of the objects. Therefore, the type of grouping
that corresponds to arrangements depends on the order used, and the objects
must be mutually distinguishable. We speak of arrangements _with repetition_
when a symbol may appear more than once in the sequence, and of _simple
arrangements_ otherwise.

## Arrangements with repetition

In arrangements with repetition, the same object may be used more than once,
as specified by the following definition.

```{margin}
In this case the meaning of _repetition_ differs from that seen for
permutations, in which we were required to insert each object exactly as many
times as it appears in the starting multiset; in arrangements, by contrast, we
can repeat the same object as many times as we wish, or omit it entirely.
```
```{prf:definition} Arrangement with repetition
:label: def-en-arrangements-with-repetition
Given a set of $n$ objects $A = \{ a_1,\dots a_n \}$ and a number
$k \in \mathbb N$, an _arrangement with repetition_ is a sequence
$(a_{i_1}, \dots, a_{i_k})$, where for every $j = 1, \dots, k$ one has
$i_j \in \{1, \dots, n\}$ and $a_{i_j} \in A$. We denote by $D_{n, k}$ the
number of possible arrangements with repetition of $n$ objects in $k$ slots.
```


```{prf:example} An example of arrangement with repetition
:label: ex-en-arrangements-with-repetition-1

[Department H](https://marvel.fandom.com/wiki/Department_H_(Earth-616)) must
plan a sequence of three daily missions — morning, afternoon, and evening. For
each mission, any one of the four members of
[Alpha Flight](https://marvel.fandom.com/wiki/Alpha_Flight_(Earth-616)) can be
sent: Guardian, Sasquatch, Northstar, and Aurora, denoted by their initials $G$,
$S$, $N$, and $A$ respectively. If each member can be deployed on more than one
mission during the same day, each schedule corresponds to an arrangement with
repetition of the $n = 4$ objects in the set $\{G, S, N, A\}$ (the squad
members) in $k = 3$ slots (the daily shifts). For example, the following three
situations describe different schedules (and arrangements):
- $(G, S, N)$ indicates that Guardian, Sasquatch, and Northstar carry out the
  morning, afternoon, and evening shifts respectively;
- $(S, N, G)$ swaps the morning and afternoon shifts compared to the previous
  point;
- $(A, G, G)$ involves Aurora in the morning and Guardian in the two subsequent
  shifts.
```

Calculating the number $D_{n, k}$ of possible arrangements with repetition is
fairly straightforward, by considering the number of possible choices for each
of the $k$ slots:
- the object to place in the first slot can be chosen in $n$ different ways;
- the number of choices remains $n$ for the second slot as well, since it is
  possible to reuse the object selected for the first position;
- clearly, there will be $n$ possible choices for all the remaining slots.

Applying the fundamental principle of combinatorics, we therefore obtain

$$
D_{n, k} = \underbrace{n \cdot n \dots \cdot n}_{k \text{ times}} = n^k \enspace.
$$

The same result follows by noting that the set of all arrangements is the
Cartesian product $A^k$ of $A$ with itself, computed $k$ times, and recalling
that $| A^k | = |A|^k = n^k$.

```{prf:example} An example of arrangement with repetition
:label: ex-en-arrangements-with-repetition-2

Returning to {prf:ref}`ex-en-arrangements-with-repetition-1`, the total number
of distinct daily schedules equals $D_{4,3} = 4^3 = 64$, as shown in
{numref}`tab-en-arrangements-with-repetition`, where columns M, A, and E refer
to the morning, afternoon, and evening shifts respectively.
```

````{table} The possible arrangements with repetition of $4$ objects in $3$ slots, describing Alpha Flight shifts; the corresponding simple arrangements are highlighted in bold.
:name: tab-en-arrangements-with-repetition
:align: center

|  # | M   | A   | E   |  # | M   | A   | E   |  # | M   | A   | E   |
|----|-----|-----|-----|----|-----|-----|-----|----|-----|-----|-----|
|  1 | $G$ | $G$ | $G$ |  2 | $G$ | $G$ | $S$ |  3 | $G$ | $G$ | $N$ |
|  4 | $G$ | $G$ | $A$ |  5 | $G$ | $S$ | $G$ |  6 | $G$ | $S$ | $S$ |
| **7** | $\boldsymbol{G}$ | $\boldsymbol{S}$ | $\boldsymbol{N}$ | **8** | $\boldsymbol{G}$ | $\boldsymbol{S}$ | $\boldsymbol{A}$ |  9 | $G$ | $N$ | $G$ |
| **10** | $\boldsymbol{G}$ | $\boldsymbol{N}$ | $\boldsymbol{S}$ | 11 | $G$ | $N$ | $N$ | **12** | $\boldsymbol{G}$ | $\boldsymbol{N}$ | $\boldsymbol{A}$ |
| 13 | $G$ | $A$ | $G$ | **14** | $\boldsymbol{G}$ | $\boldsymbol{A}$ | $\boldsymbol{S}$ | **15** | $\boldsymbol{G}$ | $\boldsymbol{A}$ | $\boldsymbol{N}$ |
| 16 | $G$ | $A$ | $A$ | 17 | $S$ | $G$ | $G$ | 18 | $S$ | $G$ | $S$ |
| **19** | $\boldsymbol{S}$ | $\boldsymbol{G}$ | $\boldsymbol{N}$ | **20** | $\boldsymbol{S}$ | $\boldsymbol{G}$ | $\boldsymbol{A}$ | 21 | $S$ | $S$ | $G$ |
| 22 | $S$ | $S$ | $S$ | 23 | $S$ | $S$ | $N$ | 24 | $S$ | $S$ | $A$ |
| **25** | $\boldsymbol{S}$ | $\boldsymbol{N}$ | $\boldsymbol{G}$ | 26 | $S$ | $N$ | $S$ | 27 | $S$ | $N$ | $N$ |
| **28** | $\boldsymbol{S}$ | $\boldsymbol{N}$ | $\boldsymbol{A}$ | **29** | $\boldsymbol{S}$ | $\boldsymbol{A}$ | $\boldsymbol{G}$ | 30 | $S$ | $A$ | $S$ |
| **31** | $\boldsymbol{S}$ | $\boldsymbol{A}$ | $\boldsymbol{N}$ | 32 | $S$ | $A$ | $A$ | 33 | $N$ | $G$ | $G$ |
| **34** | $\boldsymbol{N}$ | $\boldsymbol{G}$ | $\boldsymbol{S}$ | 35 | $N$ | $G$ | $N$ | **36** | $\boldsymbol{N}$ | $\boldsymbol{G}$ | $\boldsymbol{A}$ |
| **37** | $\boldsymbol{N}$ | $\boldsymbol{S}$ | $\boldsymbol{G}$ | 38 | $N$ | $S$ | $S$ | 39 | $N$ | $S$ | $N$ |
| **40** | $\boldsymbol{N}$ | $\boldsymbol{S}$ | $\boldsymbol{A}$ | 41 | $N$ | $N$ | $G$ | 42 | $N$ | $N$ | $S$ |
| 43 | $N$ | $N$ | $N$ | 44 | $N$ | $N$ | $A$ | **45** | $\boldsymbol{N}$ | $\boldsymbol{A}$ | $\boldsymbol{G}$ |
| **46** | $\boldsymbol{N}$ | $\boldsymbol{A}$ | $\boldsymbol{S}$ | 47 | $N$ | $A$ | $N$ | 48 | $N$ | $A$ | $A$ |
| 49 | $A$ | $G$ | $G$ | **50** | $\boldsymbol{A}$ | $\boldsymbol{G}$ | $\boldsymbol{S}$ | **51** | $\boldsymbol{A}$ | $\boldsymbol{G}$ | $\boldsymbol{N}$ |
| 52 | $A$ | $G$ | $A$ | **53** | $\boldsymbol{A}$ | $\boldsymbol{S}$ | $\boldsymbol{G}$ | 54 | $A$ | $S$ | $S$ |
| **55** | $\boldsymbol{A}$ | $\boldsymbol{S}$ | $\boldsymbol{N}$ | 56 | $A$ | $S$ | $A$ | **57** | $\boldsymbol{A}$ | $\boldsymbol{N}$ | $\boldsymbol{G}$ |
| **58** | $\boldsymbol{A}$ | $\boldsymbol{N}$ | $\boldsymbol{S}$ | 59 | $A$ | $N$ | $N$ | 60 | $A$ | $N$ | $A$ |
| 61 | $A$ | $A$ | $G$ | 62 | $A$ | $A$ | $S$ | 63 | $A$ | $A$ | $N$ |
| 64 | $A$ | $A$ | $A$ |    |     |     |     |    |     |     |     |

````

## Simple arrangements

In arrangements with repetition, each object may appear more than once in the
sequence. When instead each object can be placed in only one position, we speak
of _simple arrangements_, or _arrangements without repetition_. In this case
we must impose $k \leq n$, because once all $n$ objects have been placed in a
sequence there are no others left to choose from.

```{prf:definition} Simple arrangement
:label: def-en-simple-arrangements

Given a set of $n$ objects $A = \{ a_1,\dots a_n \}$ and a number
$k \in \mathbb N$ with $k \leq n$, a _simple arrangement_ is a sequence
$(a_{i_1}, \dots, a_{i_k})$, where for every $j = 1, \dots, k$ one has
$i_j \in \{1, \dots, n\}$ and $a_{i_j} \in A$, and for every
$j, l = 1, \dots, k$ with $j \neq l$ one has $a_{i_j} \neq a_{i_l}$.
We denote by $d_{n, k}$ the number of possible simple arrangements of $n$
objects in $k$ slots.
```

````{prf:example}
:label: ex-en-simple-arrangements-1

If in {prf:ref}`ex-en-arrangements-with-repetition-1` it were not possible to
assign more than one daily shift to the same person, sequences such as
$(A, G, G)$ would no longer be admitted, and each rota would correspond to one
and only one simple arrangement of four objects in three slots.
````

To calculate the number $d_{n, k}$ of simple arrangements of $n$ objects in
$k$ slots, we can follow an argument analogous to that for simple permutations:

- the object to place in the first slot can be chosen in $n$ different ways;
- the second slot can be filled in $n - 1$ possible ways, since the object
  selected for the first position can no longer be reused;
- the third choice can be made in $n - 2$ ways, and so on until the last slot,
  which can be filled by choosing from $n - k + 1$ objects.

Applying the fundamental principle of combinatorics, we obtain

```{math}
d_{n, k} = n (n-1) \ldots (n-k+1) =
n (n-1) \ldots (n-k+1) \cdot \frac{(n-k)!}{(n-k)!} =
\frac{n!}{(n-k)!} \enspace.
```

````{prf:example}
:label: ex-en-simple-arrangements-2

{numref}`tab-en-arrangements-with-repetition` highlights in bold the schedules
from {prf:ref}`ex-en-simple-arrangements-1`, whose number equals
$d_{4, 3} = 4 \cdot 3 \cdot 2 = 24$.
````

When $k=n$, forming an arrangement requires using all the elements of $A$, so
simple permutations are a special case of simple arrangements. Consistently,
$d_{n, n} = n!/0! = n! = p_n$.

## Exercises

```{exercise} •
:label: ex-en-arr-shield-codes

[S.H.I.E.L.D.](https://marvel.fandom.com/wiki/S.H.I.E.L.D.)'s computer system
generates access codes consisting of five characters, each chosen from eight
special symbols, with repetition allowed. How many distinct codes can be
generated?
```
```{solution} ex-en-arr-shield-codes
:class: dropdown

Each code is an arrangement with repetition of $8$ symbols in $5$ slots, so
the number of distinct codes is $D_{8,5} = 8^5 = 32\,768$.
```

````{exercise} ••
:label: ex-en-arr-wakanda-patrols

The Royal Guard of [Wakanda](https://marvel.fandom.com/wiki/Wakanda) must plan
patrols for the next three days, selecting a different warrior each day from
six available. In how many ways can the calendar be organised?
````
````{solution} ex-en-arr-wakanda-patrols
:class: dropdown

Each calendar is a simple arrangement of the six warriors in the three days,
so the calendar can be organised in $d_{6,3} = 6 \cdot 5 \cdot 4 = 120$
different ways.
````

````{exercise} ••
:label: ex-en-arr-defenders-shifts

The [Defenders](https://marvel.fandom.com/wiki/Defenders_(Earth-616)) must
cover four distinct shifts in a day (dawn, morning, afternoon, night), choosing
a different member each time from nine candidates. In how many ways can the
rota be drawn up?
````
````{solution} ex-en-arr-defenders-shifts
:class: dropdown

This involves simple arrangements of $9$ objects in $4$ slots:

```{math}
d_{9,4} = 9 \cdot 8 \cdot 7 \cdot 6 = 3024.
```
````

````{exercise} ••
:label: ex-en-arr-spokesperson

The members of the [Guardians of the
Galaxy](https://marvel.fandom.com/wiki/Guardians_of_the_Galaxy_(Earth-616))
&mdash; Star-Lord, Gamora, Drax, Rocket, and Groot &mdash; must assign three
distinct roles: spokesperson, deputy spokesperson, and archivist. How many
assignments are possible, given that Groot cannot serve as spokesperson, since
his language is limited to the expression «I am Groot»?
````
````{solution} ex-en-arr-spokesperson
:class: dropdown

Without constraints, each assignment would correspond to one of the
$d_{5, 3} = 5 \cdot 4 \cdot 3 = 60$ simple arrangements of heroes with respect
to the roles. Since fixing one of the roles reduces the number of different
configurations to $d_{4, 2} = 4 \cdot 3 = 12$ &mdash; as two roles and four
people remain &mdash; the assignments in which Groot is not spokesperson will
be $60 - 12 = 48$.
````

````{exercise} ••
:label: ex-en-arr-young-avengers-constraint

For a [Young Avengers](https://marvel.fandom.com/wiki/Young_Avengers_(Earth-616))
mission, three distinct roles (command, reconnaissance, support) must be
assigned to seven heroes. In how many ways can the roles be assigned if
Patriot and Wiccan cannot both be selected?
````
````{solution} ex-en-arr-young-avengers-constraint
:class: dropdown

Without constraints, there would be $d_{7, 3} = 7 \cdot 6 \cdot 5 = 210$
possible ways to proceed. Starting from this number, we can subtract the
disallowed cases, in which both Patriot and Wiccan appear. Since the three
roles are distinct, the two heroes can occupy two of them in $3 \cdot 2 = 6$
different ways (these are the arrangements $d_{3, 2}$ of three roles in two
heroes; alternatively, choose Patriot's role first, then Wiccan's). The third
role can be assigned to one of the remaining $5$ heroes. The cases to exclude
are therefore $6 \cdot 5 = 30$, and the number of valid configurations is
$210 - 30 = 180$.
````

````{exercise} •••
:label: ex-en-arr-avengers-first-last

The [Avengers](https://marvel.fandom.com/wiki/Avengers) must plan a sequence of
four consecutive missions, each time choosing a different member from Iron Man,
Thor, Captain America, Black Widow, and Hawkeye. Iron Man must participate in
either the first or the last mission. How many schedules are possible?
````
````{solution} ex-en-arr-avengers-first-last
:class: dropdown

Count separately the cases in which Iron Man is assigned to the first or last
mission. The two sets are disjoint, because each hero takes part in at most one
mission and therefore cannot occupy both positions.

- When Iron Man is involved in the first mission, the three remaining ones can
  be assigned to the four remaining Avengers in
  $d_{4,3} = 4 \cdot 3 \cdot 2 = 24$ different ways.
- The argument at the previous point does not change when Iron Man is assigned
  to the last mission.

Therefore, the valid schedules total $24 + 24 = 48$.
````

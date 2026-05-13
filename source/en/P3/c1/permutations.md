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

(sec_permutations)=
# Permutations

A _permutation_ of $n$ objects is, in essence, an ordered list containing each
of them exactly once. In this context, the configurations considered depend
strictly on the order of the elements, and reusing the same object is not
permitted. In other words, it amounts to arranging $n$ objects in as many
available slots. This is equivalent to fixing a criterion for ordering the
objects and then listing them from «smallest» to «largest».

To calculate the number of possible permutations we must distinguish between
two situations:

- in the first, all objects are different;
- in the second, there exist different objects that are nonetheless
  indistinguishable from one another.

Depending on the two cases, we speak of _simple_ permutations or permutations
_with repetition_, which we explore below.

## Simple permutations

When the objects to be permuted are the elements of a set, they are by
definition all different, i.e. distinguishable from one another. In this case
we speak of a _simple permutation_ (or more briefly a _permutation_) as
described by the following definition.

````{prf:definition} Simple permutation
:label: def-en-simple-permutation

Consider a set $A = \{ a_1,\dots a_n \}$ containing $n$ objects. We call a
_simple permutation_ (_permutation_) of these objects any ordered sequence

```{math}
(a_{i_1}, \dots, a_{i_n}), \quad
1 \leq i_j \leq n \ \forall j \in \{1, \dots, n \}, \quad
i_h \neq i_k \ \forall h \neq k
```

in which all and only the $n$ elements of $A$ appear. We denote by $p_n$ the
number of such simple permutations.
````

In general, I will describe a permutation by listing its elements in the
corresponding order, separated by commas and enclosing the list in round
brackets. It is worth noting that, starting from a simple permutation, it
suffices to swap any two elements to obtain a new one.

````{prf:example} The Fantastic 4
:label: ex-en-fantastic-4
Consider the set $Q = \{ f, i, t, c \}$ of the Fantastic 4: Mister Fantastic
($f$), the Invisible Woman ($i$), the Human Torch ($t$), and the Thing ($c$):
the possible simple permutations of its elements are listed in
{numref}`permutations-fantastic-four-en`.
````

```{table} Possible simple permutations of the Fantastic 4 members
:name: permutations-fantastic-four-en
:align: center

|  Permutation   |  Permutation   |
| :------------: | :------------: |
| $(f, i, t, c)$ | $(t, f, i, c)$ |
| $(f, i, c, t)$ | $(t, f, c, i)$ |
| $(f, t, i, c)$ | $(t, i, f, c)$ |
| $(f, t, c, i)$ | $(t, i, c, f)$ |
| $(f, c, i, t)$ | $(t, c, f, i)$ |
| $(f, c, t, i)$ | $(t, c, i, f)$ |
| $(i, f, t, c)$ | $(c, f, i, t)$ |
| $(i, f, c, t)$ | $(c, f, t, i)$ |
| $(i, t, f, c)$ | $(c, i, f, t)$ |
| $(i, t, c, f)$ | $(c, i, t, f)$ |
| $(i, c, f, t)$ | $(c, t, f, i)$ |
| $(i, c, t, f)$ | $(c, t, i, f)$ |
```

The fundamental principle of combinatorics helps us easily calculate the number
$p_n$ of different permutations of $n$ objects:

- the object to place in the first position of the list can be selected in $n$
  different ways, since we can choose from all available objects;
- the second position can be occupied by $n-1$ distinct objects, since the one
  used in the previous step cannot be considered again, so there are
  $n \cdot (n-1)$ different ways to choose the first two elements of the
  sequence;
- proceeding analogously for each subsequent position, the number of options
  decreases by one at each step, creating a tree in which level $i$ is
  associated with the $i$-th position; to fill this position, $n-(i-1)$
  elements of $A$ remain to choose from, so there are
  $n\cdot(n-1) \cdot \ldots \cdot(n-(i-1))$ possible ways to list the first
  $i$ elements of the sequence;
- upon reaching the last position, the single remaining element of $A$ must
  obligatorily be chosen.

One can therefore construct a tree of depth $n$ that has a number of leaves
equal to $n(n-1)(n-2)\ldots 1=n!$, each of which corresponds to one of the
possible simple permutations. In summary, the number of permutations of $n$
objects is $p_n = n!$. Looking at
{numref}`permutations-fantastic-four-en`, for example, one can easily verify
that it contains all the possible $4! = 24$ permutations of the four elements
of set $Q$ introduced in {prf:ref}`ex-en-fantastic-4`.


## Permutations with repetition

Consider now the case in which some of the objects to be permuted are
indistinguishable, but remain _distinguishable by groups_. More precisely,

- there are $r \in \mathbb N$ possible versions for the objects, which we can
  denote as $a_1, \ldots, a_r$, and
- for every $j = 1, \dots, r$, version $a_j$ is repeated $n_j$ times (which
  implies $\sum_{j=1}^r n_j = n$).

For each version $a_j$ there is therefore a group of indistinguishable objects
whose size is $n_j$. These objects form a _multiset_ (an unordered collection
in which each element may appear one or more times) containing $n_1$
occurrences of version $a_1$, $n_2$ occurrences of $a_2$, and so on. In
summary, we can write the elements of this multiset one after another, obtaining
the sequence

```{math}
\underbrace{a_1, \ldots, a_1}_{n_1 \text{ times}},
\underbrace{a_2, \ldots, a_2}_{n_2 \text{ times}}, \ldots,
\underbrace{a_r, \ldots, a_r}_{n_r \text{ times}} \enspace.
```

Changing the order of the elements does not always produce a different
sequence: if two indistinguishable objects were swapped, the sequence would
remain unchanged. In these situations only the permutations that produce
genuinely distinguishable sequences are considered, as described by the
following definition.

````{prf:definition} Permutation with repetition
:label: def-en-permutation-repetition

Consider a multiset $A = \{ a_1,\dots a_n \}$ containing $n$ objects
distinguishable by groups of sizes $n_1, \ldots, n_r$. A _permutation of
objects distinguishable by groups_ (more briefly, _permutation with
repetition_) of these objects is any ordered sequence of them that is
distinguishable from the others, and we denote by $P_{n; n_1, \ldots, n_r}$
the number of such configurations.
````

I will denote permutations with repetition using the same syntax as simple
permutations, separating elements with commas and using round brackets as
delimiters.

````{prf:example} Dupli-Kate and Multi-Paul
:label: en-dupli-kate-multi-paul
Consider the twins
[Kate](https://comicvine.gamespot.com/dupli-kate/4005-41136/) and
[Paul Cha](https://comicvine.gamespot.com/multi-paul/4005-48737/) who appear
in [Invincible](https://comicvine.gamespot.com/invincible/4050-150390/).
Both are endowed with the power to self-replicate at will and are known as
Dupli-Kate and Multi-Paul. In particular, each version of Dupli-Kate is
marked with a progressive integer on her costume, so we can denote her clones
present at a given moment as $k_1$, $k_2$, and so on. Imagine the same holds
for Multi-Paul, whose replicas we will denote by $p_1, p_2, \ldots$, and that
in front of us there are two versions of Kate and three of Paul, so that the
resulting quintet is described by the multiset $A= \{ k_1, k_2, p_1, p_2, p_3
\}$.

To calculate in how many ways these five versions of Kate and Paul can be
lined up without taking their progressive number into account, one must find
the number of permutations with repetition of $n = 5$ objects divided into two
distinct groups: one comprising the $n_1 = 2$ copies of Kate and another with
$n_2 = 3$ Paul clones. In this context, $(k_1, k_2, p_1, p_2, p_3)$ and
$(k_2, k_1, p_1, p_2, p_3)$ denote two different simple permutations, yet they
correspond to the same permutation with repetition: in the first two positions
Kate appears, in the last three Paul appears. By contrast, $(k_1, k_2, p_1,
p_2, p_3)$ and $(k_1, p_1, k_2, p_2, p_3)$ denote different permutations with
repetition, because in the first case the second position is occupied by Kate
and the third by Paul, whereas in the second the opposite holds.
````

Before calculating the total number of permutations with repetition of $n$
objects distinguishable by groups of sizes $n_1, n_2,\dots n_r$, let us
first analyse the particular case of {prf:ref}`en-dupli-kate-multi-paul`.
```{margin}
Fixing the positions of Kate's copies determines in this case also those of
Paul's copies.
```
Let us focus on one possible permutation with repetition, establishing the
positions of Kate and those of Paul. For example, suppose the first and last
positions are dedicated to Kate and the remaining ones to Paul:

<p style="text-align: center">Kate Paul Paul Paul Kate</p>

Now, several simple permutations of five objects (the two copies of Kate and
the three of Paul) correspond to this permutation with repetition.
{numref}`permutations-indistinguishable-objects-en` lists all the permutations
in which Kate is at the extremes of the line, i.e. in the permutation with
repetition we have fixed.

```{table} Possible simple permutations of objects in two distinguishable groups containing respectively two duplicates $k_1$ and $k_2$ of Kate and three duplicates $p_1$, $p_2$, and $p_3$ of Paul, such that Kate is in the first and last position.
:name: permutations-indistinguishable-objects-en
:align: center

|         Permutation        |
| :-------------------------: |
| $(k_1, p_1, p_2, p_3, k_2)$ |
| $(k_1, p_3, p_1, p_2, k_2)$ |
| $(k_1, p_2, p_3, p_1, k_2)$ |
| $(k_1, p_3, p_2, p_1, k_2)$ |
| $(k_1, p_2, p_1, p_3, k_2)$ |
| $(k_1, p_1, p_3, p_2, k_2)$ |
| $(k_2, p_1, p_2, p_3, k_1)$ |
| $(k_2, p_3, p_1, p_2, k_1)$ |
| $(k_2, p_2, p_3, p_1, k_1)$ |
| $(k_2, p_3, p_2, p_1, k_1)$ |
| $(k_2, p_2, p_1, p_3, k_1)$ |
| $(k_2, p_1, p_3, p_2, k_1)$ |
```

The rows of {numref}`permutations-indistinguishable-objects-en` were obtained
by permuting the two copies of Kate in the first and last position and the
three copies of Paul in the remaining positions. If we consider Kate, there
are only two possibilities: $k_1$ and $k_2$ in first and last position
respectively, or vice versa, and these two possibilities correspond to the
$2!$ simple permutations of the two versions of Kate. In other words, we could
have considered all the simple permutations of these two versions, and for each
of them taken the first element and placed it in the first column of the table,
then inserted the second element in the last column. In this way we would have
obtained two _templates_ for the rows of the table — respectively for rows one
to six and seven to twelve. In both cases, the rows are completed by an
analogous argument involving the $3!$ possible simple permutations of Paul's
versions. We can therefore apply the fundamental principle of combinatorics:
since there are $2!$ ways to fill the head and tail positions and $3!$ ways to
fill the central positions, the single configuration considered corresponds to
$n_1! \cdot n_2! = 2! \cdot 3! = 12$ simple permutations of the five available
objects.

This argument does not depend on the particular permutation with repetition
analysed: to each of the $P_{5; 2,3}$ permutations with repetition correspond
$2! \cdot 3! = 12$ simple permutations, and if we consider all of them it is
easy to see that together they identify the totality of simple permutations.
Therefore the equality $P_{5; 2,3} \cdot 2! \cdot 3! = 5!$ must hold, which
allows us to derive

```{math}
P_{5; 2,3} = \frac{5!}{2! \cdot 3!} = 10 \enspace.
```

Note that $P_{5; 2,3} = \binom{5}{2}$, and indeed the number of permutations
with repetition coincides with the number of ways in which the two positions
for Kate can be selected from the five available.

In the general case, we have $n$ objects divided into $r$ groups of sizes
$n_1, \ldots, n_r$, and repeating the previous argument yields
$n! = P_{n; n_1,\dots, n_r} \cdot n_1! \cdot n_2! \cdot \ldots \cdot n_r!$,
which implies

```{math}
:label: eq-en-permutations-repetition

P_{n; n_1, \dots, n_r} = \frac{n!}{n_1!\cdot n_2! \cdot \ldots \cdot n_r!}
\enspace.
```

The quantity $P_{n; n_1, \dots, n_r}$ is also called the _multinomial
coefficient_ and denoted

```{math}
P_{n; n_1, \dots, n_r} = \frac{n!}{n_1!\cdot n_2! \cdot \ldots \cdot n_r!}
                       \triangleq \binom{n}{n_1, n_2, \ldots, n_r} \enspace,
```

because it represents a generalisation of the binomial coefficient: indeed,
$\binom{n}{k} = \binom{n}{k, n-k}$ indicates in how many ways it is possible
to divide $n$ objects into two groups containing $k$ and $n-k$ elements
respectively; analogously $\binom{n}{n_1, \ldots, n_r}$ indicates in how many
ways it is possible to divide $n$ objects into $r$ groups in which the first
contains $n_1$ elements, the second contains $n_2$, and so on.

## Exercises

````{exercise} ••
:label: ex-en-perm-xmen-original

The [X-Men](https://marvel.fandom.com/wiki/X-Men) in their original line-up
are five: Cyclops, Marvel Girl, Beast, Angel, and Iceman. In how many ways can
they be lined up so that Cyclops is always at the front (as team leader)?
````
````{solution} ex-en-perm-xmen-original
:class: dropdown

If Cyclops must stand in first position, the remaining four heroes can occupy
the other four positions in $p_4 = 4! = 24$ ways.
````

````{exercise} ••
:label: ex-en-perm-thunderbolts

The original
[Thunderbolts](https://marvel.fandom.com/wiki/Thunderbolts) were formed by
Citizen V, a villain operating under a false identity who had convinced five
other criminals to change their identities and pretend to be heroes. Jolt
later joined the group, unaware of this deception. In how many ways can all the
group's members be lined up so that the five original ex-villains occupy the
first positions?
````
````{solution} ex-en-perm-thunderbolts
:class: dropdown

The five ex-villains can occupy the first positions in $p_5 = 5! = 120$ ways,
and &mdash; for each of these orderings &mdash; the two remaining members can
occupy the last positions in $p_2 = 2! = 2$ ways. By the fundamental
principle, the number of possible configurations is $120 \cdot 2 = 240$.
````

````{exercise} ••
:label: ex-en-perm-sinister-six

In how many ways can the [Sinister Six](https://marvel.fandom.com/wiki/Sinister_Six)
(Doctor Octopus, Vulture, Electro, Mysterio, Kraven the Hunter, and Sandman)
occupy six chairs, so that Doctor Octopus and Electro are never seated next to
each other?
````
````{solution} ex-en-perm-sinister-six
:class: dropdown

Each assignment of characters to chairs corresponds to a particular permutation
of the Sinister Six, but not all permutations are to be considered. To solve
this problem, it is convenient to reason by complementarity, subtracting from
the $p_6 = 6! = 720$ permutations all those in which Doctor Octopus and Electro
are adjacent. The count of the latter is performed by treating the two villains
as a single block, yielding five objects (four characters plus the pair) to be
permuted in $p_5 = 5! = 120$ ways; one must however account for the fact that
swapping the two elements of the pair produces two different permutations among
the original ones, so there are $240$ ways of placing Doctor Octopus and
Electro next to each other. In conclusion, there are $720 - 240 = 480$
acceptable arrangements.
````

````{exercise} ••
:label: ex-en-perm-substitute-legion

The [Legion of Substitute Heroes](https://dc.fandom.com/wiki/Legion_of_Substitute_Heroes_(Earth-Prime))
comprises Polar Boy, Night Girl, Fire Lad, Stone Boy, and Chlorophyll Kid.
Their weekly power rankings are compiled as follows: Night Girl and Polar Boy
are always in the top two positions (in any order), while Stone Boy is always
last. In how many distinct ways can a ranking be compiled?
````
````{solution} ex-en-perm-substitute-legion
:class: dropdown

Stone Boy must always appear in last place, so the number of rankings is
obtained by applying the fundamental principle of combinatorics, multiplying:

- the $p_2 = 2! = 2$ ways in which Night Girl and Polar Boy can occupy the
  first two positions, and
- the $p_2 = 2$ possible ways of distributing Fire Lad and Chlorophyll Kid in
  the remaining central positions.

It is therefore possible to compile the ranking in four distinct ways.
````

````{exercise} ••
:label: ex-en-perm-public-secret-identity

Iron Man, Captain America, and the Invisible Woman have publicly known
identities; conversely, Daredevil, Spider-Man, and Ant-Man operate
anonymously. If we consider superheroes with a public identity as
indistinguishable from one another, and likewise those with a secret identity,
in how many distinct ways is it possible to order them?
````
````{solution} ex-en-perm-public-secret-identity
:class: dropdown

In this case, we must consider the permutations of six objects organised into
two groups of three indistinguishable heroes each. Applying formula
{eq}`eq-en-permutations-repetition`, we obtain

```{math}
P_{6;\,3,3} = \frac{6!}{3!\cdot 3!} = \binom{6}{3} = 20 \enspace.
```
````

````{exercise} ••
:label: ex-en-perm-anagrams-superman

In how many ways can the anagrams of the word SUPERMAN be formed, understanding
by anagram any rearrangement of the letters of the starting word, even when the
result has no meaning?
````
````{solution} ex-en-perm-anagrams-superman
:class: dropdown

SUPERMAN is a word containing eight letters, all different from one another. The
number of anagrams therefore coincides with the number of simple permutations
of $8$ objects, which equals $p_8 = 8! = 40\,320$.
````

````{exercise} ••
:label: ex-en-perm-anagrams-antman

In how many ways can the anagrams of the word ANTMAN be formed, in the same
sense as the previous exercise?
````
````{solution} ex-en-perm-anagrams-antman
:class: dropdown

The word ANTMAN contains six letters, two of which appear in two different
positions. The number of distinct anagrams is therefore a permutation with
repetition: more precisely, T and M each belong to a group with multiplicity
$1$, whereas A and N refer to two groups with multiplicity $2$. Therefore the
number of distinct anagrams is

```{math}
P_{6;\,2,2,1,1} = \frac{6!}{2!\cdot 2!\cdot 1!\cdot 1!} = \frac{720}{4} = 180
\enspace.
```
````

````{exercise} •••
:label: ex-en-perm-justice-society

In its original line-up, the [Justice Society of
America](https://dc.fandom.com/wiki/Justice_Society_of_America_(New_Earth))
fields eight heroes: three with magical or alien powers (Green Lantern, Spectre,
and Doctor Fate), three who use secret technologies (Atom, Hourman, and Flash),
and two who use well-known and easily recognisable technologies (Sandman and
Hawkman). In how many ways can they intervene one after another in battle,
always keeping heroes of the same category consecutive?
````
````{solution} ex-en-perm-justice-society
:class: dropdown

Imagine having all the heroes with magical powers intervene first, then those
using secret technologies, and finally the remaining ones. Since the first two
groups can be permuted in $p_3 = 3!$ ways and the third can be ordered in
$p_2 = 2!$ configurations, by the fundamental principle of combinatorics there
are $6 \cdot 6 \cdot 2 = 72$ ways of intervening in this group order. If we
change the order of the groups, the result is the same. Therefore the final
result is obtained by multiplying $72$ by the number of permutations of the
groups, which is $p_3 = 3!$. In conclusion, there will be $432$ different ways
of deploying the members of the Justice Society, one after another.
````

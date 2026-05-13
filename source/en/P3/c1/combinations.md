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

(sec_combinations)=
# Combinations

Analogously to arrangements, combinations also describe tuples of fixed length
in which objects chosen from a set appear. In this case, however, the tuples
are _unordered_: they are not sequences but rather _subsets_ of the starting
set. Therefore, in the groupings that correspond to combinations order is not
relevant, but it remains possible to decide whether objects may be repeated or
not. The two resulting categories of combinations are described in the sections
below.

## Simple combinations

```{margin}
It is also possible to speak of constructing _sets_ from a _universe_ that
contains the objects under consideration.
```
When an object can be considered at most once, we can effectively say that
there is a correspondence between combinations — called _simple_ — and the
subsets of the starting set.

````{prf:definition}
:label: def-en-combinations
Consider a set $A = \{ a_1, \ldots, a_n \}$ of $n$ objects and fix a natural
number $k \leq n$. A _simple combination_ (or more briefly a _combination_) of
the $n$ objects in $k$ slots is an unordered tuple $\{ a_{i_1}, \dots, a_{i_k}
\}$ such that for every $j = 1, \dots, k$ one has $a_{i_j} \in A$, and
$a_{i_j} \neq a_{i_l}$ for every $j, l = 1, \dots, k$ with $j \neq l$. We
denote the number of possible simple combinations of $n$ objects in $k$ slots
by $c_{n, k}$.
````

I will denote combinations using curly brackets as delimiters of the tuples, to
emphasise that order is not relevant; moreover, this notation is consistent
with the fact that a simple combination identifies a subset
$\{ a_{i_1}, \dots, a_{i_k} \}\subseteq A$, so that the descriptions of the
subset — given in extensional form — and the combination coincide.

````{prf:example} Peter Petrelli
:label: ex-en-peter-petrelli
[Peter Petrelli](https://comicvine.gamespot.com/peter-petrelli/4005-47678/) is
one of the protagonists of
[Heroes](https://comicvine.gamespot.com/heroes/4050-19509/), endowed with an
extraordinary form of _empathy_ that allows him to reproduce the powers of
other superheroes in his vicinity. Suppose this meta-power is limited, and that
Peter can replicate only three superpowers at a time:
$\{ \text{psychokinesis}, \text{telepathy}, \text{invisibility} \}$ and
$\{ \text{telepathy}, \text{invisibility}, \text{psychokinesis} \}$ denote the
same unordered triple, and hence the same subset and the same simple
combination of $k = 3$ superpowers. In this case, the set from which we extract
the objects is the set of all superpowers, and it is of little relevance to
determine its cardinality $n$.
````

To calculate the number $c_{n, k}$ of possible simple combinations of $n$
objects in $k$ slots, we can exploit the link between these and simple
arrangements:
- each simple combination corresponds to multiple arrangements: permuting in
  all possible ways the $k$ objects that compose it yields $k!$ distinct
  arrangements;
- consequently, each combination appears exactly $k!$ times in the set of
  $d_{n, k}$ simple arrangements of $n$ objects in $k$ slots, from which
  $d_{n, k} = c_{n, k} \cdot k!$;
- inverting this relation gives $c_{n, k} = \frac{d_{n, k}}{k!}$.

Applying the formula for calculating $d_{n, k}$ we finally obtain

```{math}
c_{n, k} = \frac{d_{n, k}}{k!} = \frac{n!}{(n-k)!k!} =\binom{n}{k} \enspace.
```

````{prf:example} Peter Petrelli
:label: ex-en-peter-petrelli-2

Imagine there are $n = 477$ possible
superpowers[^superpowers], and that Peter Petrelli (see
{prf:ref}`ex-en-peter-petrelli`) can reproduce all of them. This means that, at
any given moment, he will be able to «remember»
$c_{477, 3} = \binom{477}{3} = \;$
<span style="word-spacing: -0.1rem">17 974 950</span>
different configurations of three superpowers.
````

## Combinations with repetition

When it is possible to insert the same object more than once in a combination,
we say that the latter is a _combination with repetition_. In this case, the
construction of a combination is analogous to that of a _multiset_, a
generalisation of the concept of set in whose extensional description objects
may appear more than once, so that each element in the multiset also has a
_multiplicity_, understood as the number of times it occurs.

````{prf:definition} Combination with repetition
:label: def-en-combination-with-repetition

Consider a set $A = \{ a_1, \ldots, a_n \}$ of $n$ objects and fix a natural
number $k \in \mathbb N$. A _combination with repetition_ of the $n$ objects
in $k$ slots is an unordered tuple $\{ a_{i_1}, \dots, a_{i_k} \}$ such that
for every $j = 1, \dots, k$ one has $a_{i_j} \in A$. We denote the number of
all possible combinations with repetition of $n$ objects in $k$ slots by
$C_{n, k}$.
````

I will describe combinations with repetition using the same notation as simple
ones, with the difference that in this case the tuple in curly brackets may
contain duplicates.

````{prf:example}
:label: ex-en-combinations-with-repetition

Imagine a lift with a capacity of four people, full of Dupli-Kate and
Multi-Paul clones (see {prf:ref}`en-dupli-kate-multi-paul`), without both
twins necessarily being present. {numref}`tab-en-combinations-DK-MP` lists all
the ways in which four clones can enter the lift, where each configuration
corresponds to a combination with repetition of the two objects $k$ and $p$
(Kate and Paul) in four slots.
````

```{table} Possible combinations with repetition of Dupli-Kate and Multi-Paul in four slots
:name: tab-en-combinations-DK-MP
:align: center

|    Combination     |
| :----------------: |
| $\{ k, k, k, k \}$ |
| $\{ k, k, k, p \}$ |
| $\{ k, k, p, p \}$ |
| $\{ k, p, p, p \}$ |
| $\{ p, p, p, p \}$ |
```


One possible way to calculate the number $C_{n, k}$ of combinations with
repetition of $n$ objects from a set $A$ in $k$ slots consists in associating
them uniquely with appropriate subsets of $\mathbb N$. Given a bijective
function $r: A \rightarrow \{ 1, \ldots, n \}$, each possible combination with
repetition $\{ a_{i_1}, \ldots, a_{i_k} \}$ can be transformed into the
numerical set $\{r(a_{i_1}), \ldots, r(a_{i_k}) \}$, replacing each element
with its numerical representation through $r$. If we denote by $\sigma^r$ the
sequence obtained by sorting this set in non-decreasing order, it follows that:

- $\sigma^r$ does not depend on the particular order in which the elements of
  the starting combination are listed;
- the $k$ elements of $\sigma^r$ are integers between $1$ and $n$, extremes
  included, and this sequence may contain adjacent equal values.

Finally, let us denote by $\sigma^r_i$ the $i$-th element of $\sigma^r$ and
construct a last sequence

```{math}
\rho = \{ \sigma^r_1 + 0, \sigma^r_2 + 1, \ldots, \sigma^r_k + k - 1 \}.
```

$\rho$ will also contain $k$ elements, but they will automatically be sorted in
strictly increasing order, because they were obtained by incrementing the
elements of $\sigma^r$ — which is non-decreasing — by an ever-larger quantity.
Moreover, $\rho$ will contain integer values between $1$ and $n + k - 1$, so it
can be put in bijective correspondence with a subset of
$M = \{ 1, \ldots, n + k - 1 \}$ containing $k$ elements. In summary, each
combination with repetition of $n$ objects in $k$ slots can be related to a
subset of $M$ of cardinality $k$.

Conversely, a generic subset of $M$ of cardinality $k$ can be described by
listing its elements in increasing order, obtaining a sequence $\rho$. If we
now decrement the elements of this sequence by subtracting zero from the first
element, one from the second, two from the third, and so on, we obtain a new
sequence $\sigma^r$ sorted in non-decreasing order, whose values (which may be
repeated) lie between $1$ and $n$ (extremes included). Considering the
pre-images of these values through $r$ then yields a combination with
repetition of $k$ objects from $A$. Thus every subset of $M$ of $k$ elements
can be related to a combination with repetition of $n$ objects in $k$ slots.

````{prf:example}
:label: en-combinations-DK-MP-2
Returning to {prf:ref}`ex-en-combinations-with-repetition`, the starting set of
objects $A = \{ k, p \}$, where $k$ and $p$ denote Kate and Paul respectively,
can be put in bijective correspondence with $N = \{ 1, 2 \}$, for example by
setting $r(k) = 2$ and $r(p) = 1$. {numref}`tab-en-combinations-DK-MP-2`
shows the correspondence between all combinations with repetition of the two
objects in $A$ in four positions and the sequences $\sigma^r$ and $\rho$.
````

```{table} Correspondence between the combinations with repetition of Dupli-Kate and Multi-Paul in four slots.
:name: tab-en-combinations-DK-MP-2
:align: center

|    Combination     |     $\sigma^r$     |     $\rho$     |
| :----------------: | :----------------: | :----------------: |
| $\{ k, k, k, k \}$ | $\{ 2, 2, 2, 2 \}$ | $\{ 2, 3, 4, 5 \}$ |
| $\{ k, k, k, p \}$ | $\{ 1, 2, 2, 2 \}$ | $\{ 1, 3, 4, 5 \}$ |
| $\{ k, k, p, p \}$ | $\{ 1, 1, 2, 2 \}$ | $\{ 1, 2, 4, 5 \}$ |
| $\{ k, p, p, p \}$ | $\{ 1, 1, 1, 2 \}$ | $\{ 1, 2, 3, 5 \}$ |
| $\{ p, p, p, p \}$ | $\{ 1, 1, 1, 1 \}$ | $\{ 1, 2, 3, 4 \}$ |
```

Therefore, combinations with repetition of $n$ objects in $k$ slots are in
bijective correspondence with subsets of $M$ of cardinality $k$, and since the
number of these subsets equals the number of simple combinations of $n + k - 1$
objects in $k$ slots, we can conclude that

```{math}
C_{n, k} = c_{n + k - 1, k} = \binom{n+k-1}{k} \enspace.
```


[^superpowers]: As listed for example on
[superherodb](https://www.superherodb.com/powers/).


## Exercises

````{exercise} ••
:label: ex-en-power-set

Given the set $A = \{ a_1,\dots a_n \}$ and denoting by $\mathcal{P}(A)$ the
power set of $A$, calculate the cardinality of $\mathcal{P}(A)$.
````
````{solution} ex-en-power-set
:class: dropdown

Recall that the power set $\mathcal{P}(A)$ is the set of all proper and
improper subsets of $A$: it contains the empty set, all subsets consisting of
a single element of $A$, all subsets consisting of exactly two elements of $A$,
and so on, and it also contains $A$ itself.

Since the number of subsets consisting of $k$ elements is
$c_{n,k}=\binom{n}{k}$, the cardinality of $\mathcal{P}(A)$ is
$|\mathcal{P}(A)| = 1 + \sum_{k=1}^{n} \binom{n}{k}$, where the first addend
accounts for the empty set. Using the properties of the binomial coefficient
we obtain

```{math}
|\mathcal{P}(A)| = \sum_{k=0}^{n} \binom{n}{k}
                 = \sum_{k=0}^{n}\binom{n}{k} 1^k 1^{n-k} = 2^n,
```

where in the last step we have used Newton's binomial formula:
$(a+b)^n = \sum_{k=0}^{n}\binom{n}{k}a^k b^{n-k}$, setting $a=1$ and $b=1$.

This exercise can also be solved as follows: if we represent each subset $S$
of $A$ as an $n$-tuple of binary elements, where position $i$ contains the
symbol $1$ if element $a_i$ belongs to $S$ and $0$ if it does not, then the
power set $\mathcal{P}(A)$ is the set of all $n$-tuples that can be
constructed from the two symbols $0$ and $1$. Therefore

```{math}
|\mathcal{P}(A)| = D_{n,2}=2^n.
```

````

````{exercise} ••
:label: ex-en-comb-justice-league-squad

The [Justice League](https://dc.fandom.com/wiki/Justice_League_(Prime_Earth))
must select a rapid-response squad of four members, choosing from ten
candidates. In how many distinct ways can the squad be formed?
````
````{solution} ex-en-comb-justice-league-squad
:class: dropdown

This amounts to choosing four heroes from ten, without order and without
repetition. This can be done in $c_{10,4} = \binom{10}{4} = 210$ ways.
````

````{exercise} ••
:label: ex-en-comb-xmen-professor-x

The [X-Men](https://marvel.fandom.com/wiki/X-Men) must form a team of five
members from twelve available. Professor X must necessarily be included. How
many different teams are possible?
````
````{solution} ex-en-comb-xmen-professor-x
:class: dropdown

Since Professor X must be included, four members must be chosen from the
remaining eleven. The number of teams is therefore
$c_{11,4} = \binom{11}{4} = 330$.
````

````{exercise} •••
:label: ex-en-comb-defenders-not-together

The [Defenders](https://marvel.fandom.com/wiki/Defenders_(Earth-616)) have nine
candidates for a mission that requires four members. In how many ways can the
squad be formed if Daredevil and Jessica Jones cannot appear together?
````
````{solution} ex-en-comb-defenders-not-together
:class: dropdown

Without constraints, the possible squads would be $c_{9, 4} = \binom{9}{4} =
126$. On the other hand, the squads containing both Daredevil and Jessica Jones
are counted as follows: with the pair fixed, two more members must be chosen
from the remaining seven, which can be done in $c_{7,2} = \binom{7}{2} = 21$
ways. The valid squads are therefore $126 - 21 = 105$.
````

````{exercise} ••
:label: ex-en-comb-guardians-resources

The [Guardians of the
Galaxy](https://marvel.fandom.com/wiki/Guardians_of_the_Galaxy_(Earth-616))
are equipping the
[Milano](https://marvel.fandom.com/wiki/Milano) (their spaceship) for a
mission. On board there are five available bays, each of which can hold one of
four types of device: laser cannons, energy shields, detection sensors, and
life-support modules. Calculate the number of different ways to configure the
Milano, given that each device type can be installed multiple times and only
the count of each device type matters (not in which specific bays they are
installed).
````
````{solution} ex-en-comb-guardians-resources
:class: dropdown

Each configuration corresponds to one and only one combination with repetition
of four objects (the device types) in five slots (the bays), for a total of
$C_{4,5} = \binom{4+5-1}{5} = \binom{8}{5} = 56$ possible configurations.
````

````{exercise} •
:label: ex-en-comb-avengers-gems

The [Avengers](https://marvel.fandom.com/wiki/Avengers_(Earth-616)) wish to
select four [Infinity
Stones](https://marvel.fandom.com/wiki/Infinity_Stones) from the six available
to study their behaviour. However, the Time and Reality Stones must be studied
together, because modifying the sequence of events without updating the state
of reality can generate logical inconsistencies and paradoxes. So these two
stones must either both be selected, or both excluded from the group. Calculate
the number of different stone configurations that can be considered.
````
````{solution} ex-en-comb-avengers-gems
:class: dropdown

Since the Time and Reality Stones must be considered together or completely
excluded, we can consider the two cases separately, calculate the number of
possible choices for each, and then sum.

- There are $c_{4, 2} = \binom{4}{2} = 6$ configurations containing the two
  stones, because once the Time and Reality Stones are fixed, two more must be
  selected from the four remaining stones.
- Intuitively, if those two stones are excluded, exactly four remain, and all
  of them must be selected. Indeed, in this case the combinations of these four
  stones in four slots are $c_{4, 4} = 1$.

In conclusion, there are seven possible ways to select the stones for study.
````

````{exercise} •••
:label: ex-en-comb-batman-gadget-constraint

Batman must prepare his utility belt by choosing four gadgets from a list of
eight, but two gadgets (the flash grenade and the night-vision goggles) are
incompatible and cannot be included together. In how many ways can he choose
his equipment?
````
````{solution} ex-en-comb-batman-gadget-constraint
:class: dropdown

Without the incompatibility constraint, the possible loadouts would be
described by the combinations of eight gadgets in groups of four, for a total
of $c_{8, 4} = \binom{8}{4} = 70$ cases. From these we must subtract the
disallowed configurations. In such configurations two of the four slots are
already occupied by the flash grenade and the night-vision goggles, so their
count equals the number of combinations of the six remaining gadgets in groups
of two, that is $c_{6, 2} = \binom{6}{2} = 15$. The valid total is therefore
$70 - 15 = 55$.
````

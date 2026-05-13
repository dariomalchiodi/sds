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

(sec_combinatorial-enumeration)=
# Combinatorial enumeration

In Python it is fairly easy to generate all the types of groupings seen so
far. In particular, the `itertools` module provides efficient iterators that
allow generating all possible groupings of a given type in sequence, without
ever holding all of them in memory simultaneously.

```{admonition} Iterators and memory
:class: tip
The functions in `itertools` return _iterators_, not lists. Elements are
generated one at a time only when requested, without ever loading the entire
sequence into memory. This is particularly advantageous when $n$ and $k$ are
large: for example, selecting all teams of 5 heroes from the 50 characters of
the Marvel Cinematic Universe would produce $c_{50,5} = $ <span style="word-spacing: -0.1rem">2 118 760</span> combinations. Assuming that
describing a team requires specifying an integer identifier for each member,
materialising all possible teams into a list would likely require several tens
of megabytes of RAM, whereas the iterator-based approach would keep only a
single team in memory at any one time — requiring roughly twenty bytes!

If an application did require saving all descriptions in memory — for example
because some processing of the teams cannot be done sequentially — iterators
can be explicitly converted into lists using `list`.
```

## Simple permutations

Objects of the class `itertools.permutations` are iterators that, when
traversed, generate all simple permutations of the elements contained in the
object used to instantiate the class. For example, executing the following cell
produces a list of the possible permutations of the Fantastic 4, analogous to
{numref}`permutations-fantastic-four-en`:

```{code-cell} python
import itertools as it

fantastic_4 = ['f', 'i', 't', 'c']
for i, p in enumerate(it.permutations(fantastic_4)):
    print(p, end='\n' if (i+1) % 3 == 0 else '  ')
```

In other words, the previous code generates all $p_4 = 24$ permutations of the
four squad members.

## Permutations with repetition

The `itertools` module does not offer the ability to directly generate all
permutations with repetition of a set of objects distinguishable by groups. It
is, however, fairly easy to obtain these permutations starting from simple
ones and filtering out duplicates[^sympy], for example by inserting the
permutations into a set, so as to be able to ignore their subsequent
occurrences. The following cell uses an approach of this kind to produce a list
similar to {numref}`permutations-indistinguishable-objects-en`:

```{code-cell} python

clones = ['k', 'k', 'p', 'p', 'p']
seen = set()
for t in it.permutations(clones):
    if t not in seen:
        print(t, end='\n' if (len(seen)+1) % 3 == 0 else '  ')
        seen.add(t)
```

## Arrangements with repetition

It is easy to see that the arrangements with repetition of the elements of a
set $A$ in $k \in \mathbb N$ slots are exactly the elements of the Cartesian
product

```{math}
A^k = \underbrace{A \times A \times \cdots \times A}_{\text{$k$ times}} \enspace,
```

and that they can therefore be obtained directly by generating the elements of
the iterated Cartesian product, which is easily done using the iterator
returned by `itertools.product`, which when invoked with the optional `repeat`
parameter computes the product of a set with itself a given number of times.
The following cell shows how to reproduce in this way the arrangements with
repetition of {numref}`tab-en-arrangements-with-repetition`.

```{code-cell} python
alpha_flight = ['g', 's', 'n', 'a']
for i, d in enumerate(it.product(alpha_flight, repeat=3)):
    print(d, end='\n' if (i+1) % 4 == 0 else '  ')
    if i == 15:
        break
```

This code does not print all $D_{4, 3} = 64$ arrangements with repetition,
because the for loop is forced to exit after considering $16$ of them, to
avoid unnecessarily long output.

## Simple arrangements

By virtue of the relationship between simple permutations and simple
arrangements, the latter can be generated using `itertools.permutations`,
specifying a second argument indicating the number of slots. For example, in
the following cell all $d_{4, 3} = 24$ simple arrangements highlighted in bold
in {numref}`tab-en-arrangements-with-repetition` are produced.

```{code-cell} python

for i, d in enumerate(it.permutations(alpha_flight, 3)):
    print(d, end='\n' if (i+1) % 4 == 0 else '  ')
```

## Combinations

The `itertools` module contains two classes `combinations` and
`combinations_with_replacement` whose objects are iterators over combinations —
simple and with repetition, respectively. For example, the following cell
prints the simple combinations of three of Peter Petrelli's powers (see
{prf:ref}`ex-en-peter-petrelli`), in the case where these can be selected from
a group of five superpowers.

```{code-cell} python
powers = ['telepathy', 'invisibility', 'psychokinesis',
          'regeneration', 'precognition']
for c in it.combinations(powers, 3):
    print(c)
```

Analogously, the code below generates all the combinations with repetition
considered in {numref}`tab-en-combinations-DK-MP`.

```{code-cell} python
for c in it.combinations_with_replacement(['k','p'], 4):
    print(c)
```



[^sympy]: In principle, a slightly more efficient approach is to iterate over
`dict.fromkeys(it.permutations(clones))`, a dummy dictionary created on the
fly using the tuples describing the permutations as keys, all mapped to `None`.
In this way, duplicates are automatically excluded, because inserting a
key–value pair for an already-present key simply overwrites it. If the Python
implementation in use is, say, written in C, creating the dictionary takes less
time than creating and using the set that collects the distinct tuples. In
practice, both approaches have very low efficiency when the number of objects
is large but there are few distinct objects, because `it.permutations` always
generates _all_ simple permutations before filtering. To work around this
drawback, the `sympy.utilities.iterables` module contains the generator
`multiset_permutations`, which efficiently enumerates only the distinct
permutations.

## Exercises

````{exercise} •
:label: ex-en-gen-titans-shifts

Generate and print all ways in which three patrol shifts can be assigned to
the five [Teen Titans](https://dc.fandom.com/wiki/Teen_Titans) (Robin,
Starfire, Raven, Beast Boy, Cyborg), possibly assigning more than one shift to
the same superhero. Also count and print the total number of possible rotas.
````
````{solution} ex-en-gen-titans-shifts
:class: dropdown

Each assignment corresponds to an arrangement with repetition of the five Teen
Titans in three slots: the same superhero can cover more than one shift (hence
the need to consider repetitions), and the order of the shifts matters —
being assigned the first shift is different from being assigned the second or
third (hence the use of arrangements).

```{code-cell} python
titans = ['Robin', 'Starfire', 'Raven', 'Beast Boy', 'Cyborg']
count = 0
for t in it.product(titans, repeat=3):
    print(t)
    count += 1
print(f'In total there are {count} different ways of assigning the shifts.')
```
````

````{exercise} •
:label: ex-en-gen-titans-count

If in the previous exercise the only requirement had been to count the number
of different rotas without printing them, would there be more efficient ways to
answer the question?
````
````{solution} ex-en-gen-titans-count
:class: dropdown

Since we are considering arrangements with repetition of five objects in three
slots, we know there are exactly $D_{5, 3} = 5^3 = 125$ of them. This argument
allows the question to be answered by computing a single exponentiation.
````

````{exercise} •
:label: ex-en-gen-watchmen-pairs

Generate and print all possible pairs formed from the six members of the
[Watchmen](https://dc.fandom.com/wiki/Watchmen) (Rorschach, Nite Owl, Silk
Spectre, Ozymandias, Doctor Manhattan, Comedian).
````
````{solution} ex-en-gen-watchmen-pairs
:class: dropdown

```{code-cell} python
watchmen = ['Rorschach', 'Nite Owl', 'Silk Spectre',
            'Ozymandias', 'Dr Manhattan', 'Comedian']

for c in it.combinations(watchmen, 2):
    print(c)
```
````

````{exercise} •
:label: ex-en-gen-dk-mp-repetition

Calculate how many of the combinations with repetition of Dupli-Kate and
Multi-Paul in four slots contain at least one Kate clone.
````
````{solution} ex-en-gen-dk-mp-repetition
:class: dropdown

```{code-cell} python
count = 0
for c in it.combinations_with_replacement(['k', 'p'], 4):
    if 'k' in c:
        count += 1
print(f'Exactly {count} combinations contain at least one Kate clone.')
```
````

````{exercise} •
:label: ex-en-gen-dk-mp-repetition-comp

Reconsider the previous exercise, solving it using a _list comprehension_.
````
````{solution} ex-en-gen-dk-mp-repetition-comp
:class: dropdown

```{code-cell} python
count = len([1 for c in it.combinations_with_replacement(['k', 'p'], 4)
               if 'k' in c])
print(f'Exactly {count} combinations contain at least one Kate clone.')
```
````

````{exercise} •
:label: ex-en-gen-iter-vs-list

Count how many arrangements with repetition of the $21$ regular members of the
[Legion of
Super-Heroes](https://dc.fandom.com/wiki/Legion_of_Super-Heroes_(Earth-Prime))
in $3$ slots satisfy the condition that the first and third slots are occupied
by the same hero, without storing the entire list in memory.
````
````{solution} ex-en-gen-iter-vs-list
:class: dropdown

```{code-cell} python
count = sum(1 for d in it.product(range(21), repeat=3) if d[0] == d[2])
print(f'In exactly {count} cases the same hero appears in the first '
      'and last position.')
```

The result is $21^2 = 441$: the first slot has $21$ choices, the second
likewise, whereas the third is constrained to match the first.
````

````{exercise} ••
:label: ex-en-gen-alpha-flight-no-guardian

How many simple arrangements of the four Alpha Flight members (see
{prf:ref}`ex-en-arrangements-with-repetition-1`) in three slots exclude
Guardian? Verify the answer experimentally by generating all arrangements and
counting those that exclude him.
````
````{solution} ex-en-gen-alpha-flight-no-guardian
:class: dropdown

Excluding Guardian is equivalent to not considering one of the possible
objects, and therefore to focusing on the simple arrangements of three objects
in three slots, which number $d_{3, 3} = 6$, as confirmed by the code below.

```{code-cell} python
alpha_flight = ['g', 's', 'n', 'a']
no_g = [d for d in it.permutations(alpha_flight, 3) if 'g' not in d]
print(f'The number of arrangements not including Guardian is {len(no_g)}')
```
````

````{exercise} ••
:label: ex-en-verify-formula

Write a function `compute_combinatorics(n, k)` that, using `itertools`
iterators, counts the number of arrangements with repetition, simple
arrangements, and simple combinations of `n` objects in `k` slots. The
function must return a dictionary whose keys are the strings `'D'`, `'d'`, and
`'c'`, associated respectively with arrangements with repetition, simple
arrangements, and combinations. Verify that the function behaves correctly when
the arguments `n` and `k` are $5$ and $3$ respectively.
````
````{solution} ex-en-verify-formula
:class: dropdown

Although the required values could be calculated directly, the problem
explicitly requires the use of iterators. It is therefore possible to use
generators based on these, producing the constant value $1$ for each grouping
considered. Summing the generated values yields the required counts.

The problem does not specify which objects to consider, only how many. Since
combinatorial indices do not depend on the specific nature of the objects, we
can use integers from $0$ to the value in `n`, which are produced efficiently
by `range`.

```{code-cell} python
def compute_combinatorics(n, k):
    objects = range(n)
    disp_repeat = sum(1 for _ in it.product(objects, repeat=k))
    disp_simple = sum(1 for _ in it.permutations(objects, k))
    comb = sum(1 for _ in it.combinations(objects, k))
    return {'D': disp_repeat, 'd': disp_simple, 'c': comb}
```

Applying the corresponding formulas for the two types of arrangements and for
combinations, it is easy to obtain $D_{5, 3} = 125$, $d_{5, 3} = 60$, and
$c_{5, 3} = 10$, which we can verify via simple assertions.

```{code-cell} python
result = compute_combinatorics(5, 3)

assert result['D'] == 125
assert result['d'] == 60
assert result['c'] == 10
```
````

````{exercise} ••
:label: ex-en-gen-dk-clones-anagrams

Generate all permutations of the objects in the multiset containing two
Dupli-Kate clones and three Multi-Paul clones, inserting all simple
permutations into a set.
````
````{solution} ex-en-gen-dk-clones-anagrams
:class: dropdown

In the section on permutations with repetition, permutations were inserted into
a set _after_ being used, to avoid reconsidering them later. Here, instead, we
are asked to use it to aggregate the permutations, perhaps for future use. The
most straightforward approach is to enumerate the simple permutations, inserting
them all into the set: this operation handles duplicates automatically, because
inserting an element that is already in a set has no effect.

```{code-cell} python
clones = ['k', 'k', 'p', 'p', 'p']
distinct = set()
for p in it.permutations(clones):
    distinct.add(p)
print(distinct)
```

In fact, it is possible to rewrite this code much more concisely. The
constructors of almost all structured data types we have considered accept
iterators as arguments, which are automatically traversed, progressively
inserting the generated elements into the structure. In our case this allows
the previous cell to be rewritten as shown below.

```{code-cell} python
clones = ['k', 'k', 'p', 'p', 'p']
distinct = set(it.permutations(clones))

print(distinct)
```
````

````{exercise} ••
:label: ex-en-gen-doom-patrol-islice

Read the
[documentation](https://docs.python.org/3/library/itertools.html#itertools.islice)
of the class `itertools.islice`, and use it to generate and print only ten
simple permutations of the five members of the
[Doom Patrol](https://dc.fandom.com/wiki/Doom_Patrol) (Robotman, Negative Man,
Elasti-Girl, Crazy Jane, Flex Mentallo), without generating or traversing the
remaining $5! - 10 = 110$ permutations.
````
````{solution} ex-en-gen-doom-patrol-islice
:class: dropdown

The class `islice` constructs an iterator from another iterator, extracting a
sub-sequence. In its simplest form, the constructor takes the source iterator
and an integer $n$: the returned iterator will produce only the first $n$
elements of the original one.

```{code-cell} python
doom_patrol = ['Robotman', 'Negative Man', 'Elasti-Girl',
               'Crazy Jane', 'Flex Mentallo']
for p in it.islice(it.permutations(doom_patrol), 10):
    print(p)
```
````

````{exercise} ••
:label: ex-en-gen-peter-incompatible-powers

Print all combinations of three superpowers, chosen from telepathy,
invisibility, psychokinesis, regeneration, and precognition, excluding those
that simultaneously contain telepathy and psychokinesis. How many such
combinations are there?
````
````{solution} ex-en-gen-peter-incompatible-powers
:class: dropdown

```{code-cell} python
powers = ['telepathy', 'invisibility', 'psychokinesis',
          'regeneration', 'precognition']
valid = [c for c in it.combinations(powers, 3)
          if not ('telepathy' in c and 'psychokinesis' in c)]
print(f'There are {len(valid)} valid combinations.')
```

The number of valid combinations can also be obtained by reasoning as follows:
starting from the $c_{5, 3} = 10$ total combinations, subtract all those in
which two of the three slots are occupied by telepathy and psychokinesis; since
the one remaining slot can contain any of the other superpowers, there are
exactly three combinations to remove. Therefore, there will be seven valid
combinations.

````

````{exercise} •••
:label: ex-en-gen-young-avengers-teams

Write a Python generator that, given a list of heroes and an integer $k$,
produces all pairs of disjoint teams of $k$ heroes each. Verify the behaviour
of the generator using the nine
[Young Avengers](https://marvel.fandom.com/wiki/Young_Avengers) (Patriot,
Hulkling, Wiccan, Speed, Stature, Vision, Kate Bishop, Noh-Varr, and Jonas)
and $k = 2$, bearing in mind that the number of team pairs — in this case —
must equal $c_{9,2} \cdot c_{7,2} = 36 \cdot 21 = 756$.
````
````{solution} ex-en-gen-young-avengers-teams
:class: dropdown

```{code-cell} python
def disjoint_teams(heroes, k):
    for team_1 in it.combinations(heroes, k):
        remaining = [e for e in heroes if e not in team_1]
        for team_2 in it.combinations(remaining, k):
            yield team_1, team_2

young_avengers = ['Patriot', 'Hulkling', 'Wiccan', 'Speed',
                  'Stature', 'Vision', 'Kate Bishop', 'Noh-Varr', 'Jonas']
num_pairs = sum(1 for _ in disjoint_teams(young_avengers, 2))
assert num_pairs == 756
```
````

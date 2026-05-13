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

(sec_finite-infinite-sets)=
# Finite and infinite sets

It is not hard to think of sets containing a finite number of elements, such
as the set of members of the Justice League, the set of days of the week, and
the set of prime numbers less than $100$. We say that such sets are _finite_.
There are, however, also sets that do not contain a finite number of elements,
such as the set of all fractions or the set of points in the plane. For these
_infinite_ sets two cases are distinguished:

```{margin}
In mathematics, a set is simply called _countable_ if its elements can be
listed in a finite or infinite sequence; finite sets are therefore countable
as well.
```
- a set is said to be _countably infinite_ when it is possible to construct
  an (infinite) sequence $x_1, x_2, \dots$ that contains each of its elements
  at some position: the set $D$ of odd numbers, which I will introduce shortly,
  is an example of a countably infinite set;
- in all other cases the set is said to be _uncountably infinite_: the set of
  points on a line and the set of real numbers are both infinite and
  uncountable.

The extensive description is not, strictly speaking, applicable to infinite
sets, since by definition it is impossible to list all their elements. However,
when a countably infinite set can be associated with a sequence that one can
intuitively continue after seeing only a few of its initial elements, it is
acceptable to extend the extensive description by listing only those elements
and then adding ellipsis to emphasise the infinite nature of the set. For
example, although the intensive description

```{math}
D = \{ 2n+1 \mid n \in \mathbb N \}
```

is the most precise way to denote the set of odd numbers, in many contexts the
extensive formulation $D = \{1, 3, 5, 7, 9, \dots \}$ is also used. It should
be kept in mind, however, that a partial sequence cannot identify a set
uniquely: in the previous case, the initial terms $1, 3, 5, 7, 9$ could in
principle refer also to the set of odd numbers less than $100$, or to any
other sequence that coincides with the odd numbers on the first few elements
but then diverges. The ellipsis suggests what the remaining elements are, but
does not define them rigorously, which is why the intensive description remains
the formally correct one. All the more so, extensive descriptions fail to
capture the complexity of uncountably infinite sets, for which only intensive
descriptions are generally usable.

## Exercises

````{exercise}
:label: ex-en-suicide-squad

The [Suicide Squad](https://dc.fandom.com/wiki/Suicide_Squad_(Prime_Earth))
consists of six members: Emerald Empress, Doctor Polaris, Johnny Sorrow, Lobo,
Rustam, and Cyclotron, each of whom can be either operational or out of action.
The state of the group is described by a vector
$(x_1, x_2, x_3, x_4, x_5, x_6)$, where for each $i = 1, \dots 6$, $x_i$
equals $1$ if the $i$-th member (in the order above) is operational, and $0$
otherwise. Answer the following questions.

1. How many elements does the set of all possible states of the group contain?
2. Let $A$ be the set of states in which at least one of members $1$ and $2$
   is operational, and at least one of members $3$ and $4$ is operational.
   Write Python code that lists all elements of $A$.
3. Let $B$ be the set of states in which members $1$ and $3$ are both out of
   action. How many elements does $B$ contain?
````
````{solution} ex-en-suicide-squad
:class: dropdown

1. Regardless of $i$, each component $x_i$ can take two distinct values, so
   the fundamental principle of combinatorics tells us that the set of all
   states has $2^6 = 64$ elements.

2. The conditions required are $(x_1=1 \vee x_2=1)$ and $(x_3=1 \vee x_4=1)$.
   The pairs $(x_1, x_2)$ satisfying the first condition are three:
   $(1,0),(0,1),(1,1)$. Analogously, there are three configurations for
   $(x_3, x_4)$. In contrast, $(x_5, x_6)$ can take all four possible
   configurations. By the fundamental principle of combinatorics, we have
   $|A| = 3 \times 3 \times 4 = 36$, and the elements of $A$ are exactly the
   vectors with $(x_1, x_2) \neq (0,0)$ and $(x_3, x_4) \neq (0,0)$, as
   confirmed by the output of the following code.

```{code-cell} python
import itertools as it

v = (0, 1)
teams = [t for t in it.product(v, repeat=6)
           if (t[0] or t[1]) and (t[2] or t[3])]
for t in teams:
    print(t)
```

3. With $x_1=0$ and $x_3=0$ fixed, the remaining components $x_2$, $x_4$,
   $x_5$, and $x_6$ are free, so $|B| = 2^4 = 16$.
````

````{exercise}
:label: ex-en-new-warriors

The [New Warriors](https://marvel.fandom.com/wiki/New_Warriors_(Earth-616))
are a Marvel superhero group that, in one of their line-ups, consists of six
members: Night Thrasher, Firestar, Justice, Namorita, Speedball, and Nova.
For each of the following sets, determine whether it is finite, countably
infinite, or uncountably infinite, justifying your answer.

1. The set $W$ of the six New Warriors members.
2. The set $M$ of possible mission numbers assigned progressively to the group
   starting from $1$, that is $M = \{1, 2, 3, 4, \dots\}$.
3. The set $C$ of all pairs $(i, n)$ where
   $i \in [1 .. 6]$ identifies one of the six members and $n \in \mathbb{N}$
   is the number of the mission they lead.
4. The set $V$ of all possible real values (in km/h) of the speed at which
   Nova can fly, given that his speed lies in the interval $[0, 10^6]$.
````
````{solution} ex-en-new-warriors
:class: dropdown

1. $W$ is finite: it contains exactly $6$ elements, one for each listed member.
2. $M$ is countably infinite: since the total number of missions the New
   Warriors will undertake is not known in advance, every natural number is a
   possible mission number. Hence $M = \mathbb{N}$, which is by definition
   countable.
3. $C$ is countably infinite. For each fixed $i$ there are infinitely many
   values of $n$, so $C$ is infinite. To show countability, construct the
   sequence $(1,1), (1,2), (1,3), \dots, (2,1), (2,2), \dots$, which, after
   exhausting all elements with $i = j$, moves on to $i = j+1$. Since six
   countable sequences are concatenated, the result is still a countable
   sequence that lists every element of $C$.
4. $V$ is uncountably infinite: the possible real values of speed belong to
   the interval $[0, 10^6]$, which is a subset of $\mathbb{R}$, and every
   interval of real numbers is uncountable.
````

````{exercise}
:label: ex-en-great-lakes-avengers

The [Great Lakes
Avengers](https://marvel.fandom.com/wiki/Great_Lakes_Avengers_(Earth-616))
are an eccentric Marvel group consisting of six members: Big Bertha, Doorman,
Flatman, Mr. Immortal, Dinah Soar, and Grasshopper. Before each mission, the
group assigns three distinct roles — leader, tactician, and scout — to three
distinct members. The order of the roles is significant (being the leader is
different from being the tactician). Let $R$ be the set of all possible role
assignments.

1. How many elements does $R$ contain?
2. Let $D$ be the set of assignments in which Doorman fills one of the three
   roles. How many elements does $D$ contain?
3. Write Python code that lists all elements of $R$ and verify the results
   from parts 1 and 2.
````
````{solution} ex-en-great-lakes-avengers
:class: dropdown

1. We must choose, in order, three distinct members from six, so we are
   counting the simple arrangements of six objects (the heroes) in three
   slots (the roles). Hence $|R| = d_{6, 3} = 6 \times 5 \times 4 = 120$.

2. Doorman can fill any of the three roles. Once Doorman's role is chosen,
   the two remaining roles are assigned by selecting two different members
   from the five remaining ones, which can be done in
   $d_{5, 2} = 5 \times 4 = 20$ ways. Therefore $|D| = 3 \times d_{5, 2} = 60$.

3. In the cell below, for brevity, the superheroes are denoted BB (Big Bertha),
   DM (Doorman), FM (Flatman), MI (Mr. Immortal), DS (Dinah Soar), and GH
   (Grasshopper). Using `it.permutations` we can generate all arrangements
   corresponding to elements of $R$, select those that belong to $D$, print
   them, and count them.

```{code-cell} python
import itertools as it

members = ['BB', 'DM', 'FM', 'MI', 'DS', 'GH']
roles = ['leader', 'tactician', 'scout']

R = it.permutations(members, 3)

D = [t for t in R if 'DM' in t]

print('Elements of D:')
for i, a in enumerate(D):
    print('-'.join(a), end=', ' if (i+1) % 6 else '\n')

print(f"\n|D| = {len(D)}")
```
````

````{exercise}
:label: ex-en-doom-patrol

The [Doom Patrol](https://dc.fandom.com/wiki/Doom_Patrol_(New_Earth)) is a
team of outcast superheroes, including Robotman, Negative Man, Elasti-Girl,
and Crazy Jane. Their historical archive labels every encounter with a pair of
positive natural numbers $(v, s)$, where $v$ is the issue number of a comic
and $s$ is the number of the encounter within that issue. Let
$A = \{ (v, s) : v, s \in \mathbb{N} \}$ be the set of all possible encounter
labels.

1. Prove that $A$ is infinite.
2. Prove that $A$ is countable by explicitly constructing a sequence
   $a_1, a_2, a_3, \dots$ that lists every element of $A$ at some position,
   and derive the formula for the position of a generic element $(v, s)$.
3. At what position does $(3, 2)$ appear in the sequence from part 2?
````
````{solution} ex-en-doom-patrol
:class: dropdown

1. There is no «last» issue number in principle, so $A$ contains all pairs
   $(v, i)$ for $v \in \mathbb N$ and is therefore infinite.

2. We use the classical _diagonal enumeration_: consider the decomposition
   $A = \cup_{k=2}^{+\infty} D_k$, where
   $D_k = \{ (v,s) \in A : v + s = k \}$ denotes a _diagonal_ containing
   exactly $k-1$ pairs, ordered as $(1, k-1), (2, k-2), \dots, (k-1, 1)$.
   Every pair $(v, s)$ belongs to exactly one diagonal, so by considering all
   diagonals in order and enumerating their elements, after a finite number of
   steps we must reach $(v, s)$. Hence $A$ is countable.

3. For $(3, 2)$ we have $k = 3 + 2 = 5$, so the pair belongs to $D_5$.
   Generating the sequence elements corresponding to the first four diagonals
   shows that $(3, 2)$ occurs in ninth position:

   ```{math}
   \underbrace{(1,1)}_{D_2},
   \underbrace{(1,2), (2,1)}_{D_3},
   \underbrace{(1,3), (2,2), (3,1)}_{D_4},
   \underbrace{(1,4), (2,3), (3,2), (4, 1)}_{D_5} \enspace.
   ```

````

````{exercise}
:label: ex-en-extensive-intensive

For each of the following sets, expressed in intensive form, write — where
possible — the corresponding extensive description, and state whether it is
exact or only partial.

1. $A = \{ n \in \mathbb{N} \mid n^2 \leq 25 \}$.
2. $B = \{ n \in \mathbb{Z} \mid -3 \leq n \leq 3 \}$.
3. $C = \{ n \in \mathbb{N} \mid n \text{ is a multiple of } 3 \}$.
4. $D = \{ x \in \mathbb{R} \mid 1 \leq x \leq 2 \}$.
````
````{solution} ex-en-extensive-intensive
:class: dropdown

1. $A = \{ 1, 2, 3, 4, 5 \}$. The set is finite, so the extensive description
   is exact: it lists precisely all and only the elements of $A$.

2. $B = \{ -3, -2, -1, 0, 1, 2, 3 \}$. Again the set is finite and the
   extensive description is exact.

3. One possible extensive description is $C = \{0, 3, 6, 9, \dots\}$. $C$
   is countably infinite, so the extensive description is only partial: the
   ellipsis suggests the pattern but does not define it rigorously. In this
   case, for example, the four values shown also mark the beginning of the
   sequence of numbers whose digits all belong to $\{ 0, 3, 6, 9 \}$, which
   would continue with $30, 33, 36, 39, 60$, and so on.

4. $D$ is an interval of real numbers and is therefore uncountably infinite;
   an extensive description is not applicable. There is no partial listing of
   its elements that would be meaningful.
````

````{exercise}
:label: ex-en-intensive-extensive

For each of the following sets, expressed in extensive form, write an
equivalent intensive description.

1. $A = \{ \text{Thor}, \text{Iron Man}, \text{Captain America},
   \text{Hulk}, \text{Black Widow}, \text{Hawkeye} \}$.
2. $B = \{ 2, 4, 6, 8, \dots \}$.
3. $C = \{ 1, 4, 9, 16, 25, \dots \}$.
4. $D = \{ 0, 1 \}$.
````
````{solution} ex-en-intensive-extensive
:class: dropdown

1. One possible intensive description is
   $A = \{ x \mid x \text{ is an original Avenger} \}$.

2. The sequence shown suggests that the set contains the even numbers. In that
   case two possible intensive descriptions are
   $B = \{ n \in \mathbb N \mid n \text{ is even} \}$ and
   $B = \{ 2k \mid k \in \mathbb N \}$ (though the same sequence could in
   principle continue in different ways, for example listing all even numbers
   whose digits are all equal).

3. The simplest interpretation suggests the extensive description lists the
   first perfect squares (though again, other interpretations are possible).
   In that case, the intensive formulation $C = \{ n^2 \mid n \in \mathbb N \}$
   can be used, or equivalently $C = \{ n \in \mathbb N \mid \sqrt{n} \in \mathbb{N} \}$.

4. $D = \{ n \in \mathbb Z \mid 0 \leq n \leq 1 \}$, or
   $D = \{ x \in \mathbb R \mid x^2 = x \}$, or more simply
   $D = \{ x \in \mathbb R \mid x = 0 \vee x = 1 \}$.
````

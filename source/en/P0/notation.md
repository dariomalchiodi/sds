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

(sec:notation)=
# Notation

The {numref}`tab-notation` lists the main notations I will use in the
mathematical formulas.

```{table} Notation used in the text for mathematical formulas.
:name: tab-notation
:align: center
:class: [full-width]

|  Symbol                      | Meaning                                                                 |
|:-----------------------------|:------------------------------------------------------------------------|
| $\mathbb N$                  | set of natural numbers                                                  |
| $\mathbb Z$                  | set of integers                                                         |
| $[a..b]$                     | discrete interval of integers between $a$ and $b$ (inclusive)           |
| $\mathbb R$                  | set of real numbers                                                     |
| $[a, b]$                     | closed interval of real numbers between $a$ and $b$                     |
| $(a, b)$                     | open interval of real numbers between $a$ and $b$                       |
| $[a, b)$, $(a, b]$           | half-open intervals of real numbers between $a$ and $b$                 |
| $A = \\{ a_1, \dots a_n \\}$ | set/event composed of the elements/outcomes $a_1, \dots, a_n$           |
| $a \in A$                    | element $a$ of the set $A$                                              |
| $(a_1, \dots, a_n)$          | arrangement/permutation of the elements $a_1, \dots, a_n$               |
| $n!$                         | factorial of the integer $n$                                            |
| $\binom{n}{k}$               | binomial coefficient («$n$ choose $k$») of $n$ objects in $k$ positions |
| $p_n$                        | number of simple permutations of $n$ elements                           |
| $P_{n; n_1, \dots, n_k}$     | number of permutations with repetition of $n$ distinguishable elements grouped into $n_1, \dots, n_k$ objects |
| $\\{ a_1, \dots, a_n \\}$    | combination composed of the elements $a_1, \dots, a_n$                  |
| $D_{n, k}$                   | arrangements with repetition of $n$ objects in $k$ positions            |
| $d_{n, k}$                   | arrangements without repetition of $n$ objects in $k$ positions         |
| $c_{n, k}$                   | simple combinations of $n$ objects in $k$ positions                     |
| $C_{n, k}$                   | combinations with repetition of $n$ objects in $k$ positions            |
| $S \subseteq T$              | subset/sub-event $S$ of a set/event $T$                                 |
| $\Omega$                     | universal set / sample space                                            |
| $A \rightarrow B$            | event/proposition $A$ implies event/proposition $B$                     |
| $A \leftrightarrow B$        | event/proposition $A$ is logically equivalent to event/proposition $B$  |
| $S \cup T$                   | union of sets/events $S$ and $T$                                        |
| $S \cap T$                   | intersection of sets/events $S$ and $T$                                 |
| $S \backslash T$             | difference between set/event $S$ and set/event $T$                      |
| $S \ominus T$                | symmetric difference between sets/events $S$ and $T$                    |
| $A \vee B$                   | logical disjunction between propositions $A$ and $B$                    |
| $A \wedge B$                 | logical conjunction between propositions $A$ and $B$                    |
| $\mathscr E$                 | random experiment                                                       |
| $\omega \in \Omega$          | outcome of a random experiment                                          |
| $\\{ \omega \\}$             | elementary event                                                        |
| $\mathsf A$                  | event algebra                                                           |
| $2^A$                        | power set of set $A$                                                    |
| $\mathbb P$                  | probability function                                                    |
| $\mathbb P(E)$               | probability of event $E$                                                |
| $\mathbb P(E\|F)$            | conditional probability of event $E$ given event $F$                    |
| $\mathbb E(X)$               | expected value of the random variable $X$                               |
| $\mathbb E(g(X))$            | expected value of the function $g$ of the random variable $X$           |
| $\mathbb E(g(X, Y))$         | expected value of the function $g$ of the random variables $X$ and $Y$  |
| $a \triangleq b$             | $a$ is defined as equal to $b$                                          |
```

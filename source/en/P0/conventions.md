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
(sec_conventions)=
# Conventions and notation

As mentioned in the previous section, I will often accompany the text with
code examples. It will not always be meant to be executed: sometimes I will use it for
illustrative purposes, for example to indicate `True` and `False` as the only
possible literals for the `bool` data type. In those cases, I will use a
monospaced font with a color that differs from the main text. When it becomes
necessary to present code that is meant to be executed, I will place it inside
a box that resembles a _code cell_ in a _notebook_. Here too I will use a
monospaced font, highlighting elements such as variables, literals, and
keywords with different colors, much as modern IDEs do. To improve readability,
the code will be visually separated from the main text. Whenever there is
output, I will show it inside a dedicated _output cell_ placed immediately
after the code cell, as in the following example, so that the connection
between instructions and results is clear.

```{margin}
It is common practice to use a monospaced font, in which every glyph has the
same width, to display code, input, and output. This improves readability,
making indentation easier to follow and reducing the risk of confusing similar
characters such as 1 and l, or O and 0.
```

```{code-cell}
age = 24
print(age <= 42)
```

To highlight specific components inside the text, I will use dedicated blocks,
each with its own style.

```{admonition} _
:class: naming
Areas of this kind contain explanations of the terms used, or of alternative
wording.
```

```{prf:definition}
:label: placeholder-definition
:class: no-number
This area introduces one or more concepts rigorously.
```
```{margin}
Definitions, examples, and so on will typically be numbered, and often
accompanied by a specific name enclosed in parentheses.
```

```{prf:example}
:label: placeholder-example
:class: no-number
Examples will appear inside boxes of this kind.
```

````{prf:theorem}
:label: placeholder-theorem
:nonumber:
:class: no-number
This type of block contains the statement of a theorem.
````

```{prf:corollary}
:label: placeholder-corollary
:class: no-number
Corollaries will be presented in areas like this.
```

```{prf:lemma}
:class: no-number
:label: placeholder-lemma
This area contains the statement of a lemma.
```

```{admonition} _
:class: myproof
This block contains proofs of theorems, corollaries, or lemmas. I will omit
them whenever it is important to introduce a theoretical result whose proof
would require advanced mathematical knowledge.
```

```{note}
This type of box contains secondary aspects that I prefer to emphasize in the
main text, rather than describe in footnotes.
```

(sec_notation)=
Finally, {numref}`tab-notation` lists the main notations I will use in
mathematical formulas.

```{table} Notation used in the text for mathematical formulas.
:name: tab-notation
:align: center
:class: [full-width]

| Symbol                        | Meaning                                                                 |
|:------------------------------|:------------------------------------------------------------------------|
| $\mathbb N$                  | set of natural numbers                                                  |
| $\mathbb Z$                  | set of integers                                                         |
| $[a..b]$                      | discrete interval of integers between $a$ and $b$ (inclusive)           |
| $\mathbb R$                  | set of real numbers                                                     |
| $[a, b]$                      | closed interval of real numbers between $a$ and $b$                     |
| $(a, b)$                      | open interval of real numbers between $a$ and $b$                       |
| $[a, b)$, $(a, b]$            | half-open intervals of real numbers between $a$ and $b$                 |
| $A = \\{ a_1, \dots a_n \\}$ | set/event composed of the elements/outcomes $a_1, \dots, a_n$          |
| $a \in A$                    | element $a$ of the set $A$                                              |
| $(a_1, \dots, a_n)$          | arrangement or permutation of the elements $a_1, \dots, a_n$           |
| $n!$                          | factorial of the integer $n$                                            |
| $\binom{n}{k}$               | binomial coefficient ("$n$ choose $k$") of $n$ objects in $k$ places   |
| $p_n$                         | number of simple permutations of $n$ elements                           |
| $P_{n; n_1, \dots, n_k}$     | number of permutations with repetition of $n$ distinguishable elements grouped into $n_1, \dots, n_k$ objects |
| $\{ a_1, \dots, a_n \}$     | combination composed of the elements $a_1, \dots, a_n$                 |
| $D_{n, k}$                    | arrangements with repetition of $n$ objects in $k$ positions            |
| $d_{n, k}$                    | arrangements without repetition of $n$ objects in $k$ positions         |
| $c_{n, k}$                    | simple combinations of $n$ objects in $k$ positions                     |
| $C_{n, k}$                    | combinations with repetition of $n$ objects in $k$ positions            |
| $S \subseteq T$              | subset/sub-event $S$ of a set/event $T$                                 |
| $\Omega$                     | universal set / sample space / certain event                            |
| $\varnothing$                | empty set / impossible event                                            |
| $A \rightarrow B$            | event/proposition $A$ implies event/proposition $B$                     |
| $A \leftrightarrow B$        | event/proposition $A$ is logically equivalent to event/proposition $B$  |
| $S \cup T$                   | union of sets/events $S$ and $T$                                        |
| $S \cap T$                   | intersection of sets/events $S$ and $T$                                 |
| $S \backslash T$             | difference between set/event $S$ and set/event $T$                      |
| $S \Delta T$                 | symmetric difference between sets/events $S$ and $T$                    |
| $A \vee B$                   | logical disjunction between propositions $A$ and $B$                    |
| $A \wedge B$                 | logical conjunction between propositions $A$ and $B$                    |
| $\mathscr E$                 | random experiment                                                       |
| $\omega \in \Omega$        | outcome of a random experiment                                          |
| $\\{ \omega \\}$           | elementary event                                                        |
| $\mathsf A$                  | event algebra                                                           |
| $2^A$                         | power set of set $A$                                                    |
| $\mathcal P$                 | partition of a set                                                      |
| $\mathbb P$                  | probability function                                                    |
| $\mathbb P(E)$               | probability of event $E$                                                |
| $\mathbb P(E\|F)$           | conditional probability of event $E$ given event $F$                    |
| $\mathbb E(X)$               | expected value of the random variable $X$                               |
| $\mathbb E(g(X))$            | expected value of the function $g$ of the random variable $X$           |
| $\mathbb E(g(X, Y))$         | expected value of the function $g$ of the random variables $X$ and $Y$  |
| $a \triangleq b$             | $a$ is defined to be equal to $b$                                       |
```
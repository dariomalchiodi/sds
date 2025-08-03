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


(sec:notazione)=
# Notation

La {numref}`tab-notation` répertorie les principales notations que
j’utiliserai dans les formules mathématiques.

```{table} Notation utilisée dans le texte pour les formules mathématiques.
:name: tab-notation
:align: center
:class: [full-width]

|  Symbole                   | Signification                                                                  |
|:---------------------------|:-------------------------------------------------------------------------------|
| $\mathbb N$                | ensemble des nombres naturels                                                  |
| $\mathbb Z$                | ensemble des nombres entiers                                                   |
| $[a..b]$                   | intervalle discret des entiers entre $a$ et $b$ (bornes incluses)              |
| $\mathbb R$                | ensemble des nombres réels                                                     |
| $[a, b]$                   | intervalle fermé des réels entre $a$ et $b$                                    |
| $(a, b)$                   | intervalle ouvert des réels entre $a$ et $b$                                   |
| $[a, b)$, $(a, b]$         | intervalles semi-ouverts des réels entre $a$ et $b$                            |
| $A = \\{ a_1, \dots a_n \\}$ | ensemble/événement composé des éléments/résultats $a_1, \dots, a_n$            |
| $a \in A$                  | élément $a$ de l’ensemble $A$                                                 |
| $(a_1, \dots, a_n)$        | arrangement ou permutation des éléments $a_1, \dots, a_n$                      |
| $n!$                       | factorielle de l’entier $n$                                                   |
| $\binom{n}{k}$             | coefficient binomial («$n$ parmi $k$») de $n$ objets dans $k$ positions        |
| $p_n$                      | nombre de permutations simples de $n$ éléments                                |
| $P_{n; n_1, \dots, n_k}$   | nombre de permutations avec répétition de $n$ éléments divisés en groupes de $n_1, \dots, n_k$ objets |
| $\\{ a_1, \dots, a_n \\}$    | combinaison des éléments $a_1, \dots, a_n$                                    |
| $D_{n, k}$                 | arrangements avec répétition de $n$ objets dans $k$ positions                  |
| $d_{n, k}$                 | arrangements sans répétition de $n$ objets dans $k$ positions                  |
| $c_{n, k}$                 | combinaisons simples de $n$ objets dans $k$ positions                          |
| $C_{n, k}$                 | combinaisons avec répétition de $n$ objets dans $k$ positions                  |
| $S \subseteq T$            | sous-ensemble/sous-événement $S$ d’un ensemble/événement $T$                  |
| $\Omega$                   | univers / espace des résultats                                                 |
| $A \rightarrow B$          | événement/proposition $A$ implique événement/proposition $B$                  |
| $A \leftrightarrow B$      | événement/proposition $A$ équivaut à événement/proposition $B$                |
| $S \cup T$                 | union des ensembles/événements $S$ et $T$                                     |
| $S \cap T$                 | intersection des ensembles/événements $S$ et $T$                              |
| $S \backslash T$           | différence entre l’ensemble/événement $S$ et l’ensemble/événement $T$        |
| $S \ominus T$              | différence symétrique entre les ensembles/événements $S$ et $T$               |
| $A \vee B$                 | disjonction logique des propositions $A$ et $B$                               |
| $A \wedge B$               | conjonction logique des propositions $A$ et $B$                               |
| $\mathscr E$               | expérience aléatoire                                                          |
| $\omega \in \Omega$        | issue d’une expérience aléatoire                                              |
| $\\{ \omega \\}$           | événement élémentaire                                                         |
| $\mathsf A$                | algèbre des événements                                                        |
| $2^A$                      | ensemble des parties de l’ensemble $A$                                        |
| $\mathbb P$                | fonction de probabilité                                                       |
| $\mathbb P(E)$             | probabilité de l’événement $E$                                                |
| $\mathbb P(E\|F)$          | probabilité conditionnelle de l’événement $E$ sachant $F$                     |
| $\mathbb E(X)$             | espérance de la variable aléatoire $X$                                        |
| $\mathbb E(g(X))$          | espérance de la fonction $g$ de la variable aléatoire $X$                     |
| $\mathbb E(g(X, Y))$       | espérance de la fonction $g$ des variables aléatoires $X$ et $Y$              |
| $a \triangleq b$           | $a$ est défini comme étant égal à $b$                                         |

```

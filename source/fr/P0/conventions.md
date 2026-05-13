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
# Conventions et notation

Comme indiqué dans la section précédente, j’accompagnerai souvent le texte
d’exemples de code. Ils ne seront pas toujours destinés à être exécutés : je
les utiliserai parfois à des fins illustratives, par exemple pour indiquer que
`True` et `False` sont les seuls littéraux possibles du type de données
`bool`. Dans ces cas, j’emploierai une police à chasse fixe avec une couleur
différente de celle du texte principal. Lorsqu’il deviendra nécessaire de
présenter du code destiné à être exécuté, je l’insérerai dans un encadré qui
rappelle une _cellule de code_ dans un _notebook_. Là encore, j’utiliserai une
police à chasse fixe, en mettant en évidence avec des couleurs différentes des
éléments comme les variables, les littéraux et les mots-clés, un peu à la
manière des IDE modernes. Pour améliorer la lisibilité, le code sera
visuellement séparé du texte principal. Lorsqu’il y aura un résultat, je
l’afficherai dans une _cellule de sortie_ dédiée, placée immédiatement après la
cellule de code, comme dans l’exemple suivant, afin que le lien entre les
instructions et les résultats soit clair.

```{margin}
Il est courant d’utiliser une police à chasse fixe, dans laquelle chaque glyphe
a la même largeur, pour afficher le code, les entrées et les sorties. Cela en
améliore la lisibilité, facilite l’indentation et réduit le risque de
confondre des caractères similaires comme 1 et l, ou O et 0.
```

```{code-cell}
age = 24
print(age <= 42)
```

Pour mettre en évidence certains éléments du texte, j’utiliserai des encadrés
spécifiques, chacun avec son propre style.

```{admonition} _
:class: naming
Ce type d’encadré contient des explications sur les termes employés, ou sur des
formulations alternatives.
```

```{prf:definition}
:label: placeholder-definition
:class: no-number
Cet encadré introduit un ou plusieurs concepts de manière rigoureuse.
```
```{margin}
Les définitions, exemples, etc. seront généralement numérotés, et souvent
accompagnés d’un nom spécifique entre parenthèses.
```

```{prf:example}
:label: placeholder-example
:class: no-number
Les exemples apparaîtront dans des encadrés de ce type.
```

````{prf:theorem}
:label: placeholder-theorem
:nonumber:
:class: no-number
Ce type d’encadré contient l’énoncé d’un théorème.
````

```{prf:corollary}
:label: placeholder-corollary
:class: no-number
Les corollaires seront présentés dans des encadrés comme celui-ci.
```

```{prf:lemma}
:class: no-number
:label: placeholder-lemma
Cet encadré contient l’énoncé d’un lemme.
```

```{admonition} _
:class: myproof
Cet encadré contient les démonstrations des théorèmes, corollaires ou lemmes.
Je les omettrai lorsqu’il sera important d’introduire un résultat théorique
dont la preuve exigerait des connaissances mathématiques avancées.
```

```{note}
Ce type d’encadré contient des aspects secondaires que je préfère mettre en
évidence dans le texte plutôt que dans des notes de bas de page.
```

(sec_notation)=
Enfin, la {numref}`tab-notation` répertorie les principales notations que
j’utiliserai dans les formules mathématiques.

```{table} Notation utilisée dans le texte pour les formules mathématiques.
:name: tab-notation
:align: center
:class: [full-width]

| Symbole                        | Signification                                                               |
|:-------------------------------|:----------------------------------------------------------------------------|
| $\mathbb N$                   | ensemble des nombres naturels                                               |
| $\mathbb Z$                   | ensemble des nombres entiers                                                |
| $[a..b]$                       | intervalle discret des entiers entre $a$ et $b$ (bornes incluses)          |
| $\mathbb R$                   | ensemble des nombres réels                                                  |
| $[a, b]$                       | intervalle fermé des réels entre $a$ et $b$                                 |
| $(a, b)$                       | intervalle ouvert des réels entre $a$ et $b$                                |
| $[a, b)$, $(a, b]$             | intervalles semi-ouverts des réels entre $a$ et $b$                         |
| $A = \\{ a_1, \dots a_n \\}$ | ensemble/événement composé des éléments/résultats $a_1, \dots, a_n$        |
| $a \in A$                     | élément $a$ de l’ensemble $A$                                               |
| $(a_1, \dots, a_n)$           | arrangement ou permutation des éléments $a_1, \dots, a_n$                  |
| $n!$                           | factorielle de l’entier $n$                                                 |
| $\binom{n}{k}$                | coefficient binomial (« $n$ parmi $k$ ») de $n$ objets dans $k$ positions   |
| $p_n$                          | nombre de permutations simples de $n$ éléments                              |
| $P_{n; n_1, \dots, n_k}$      | nombre de permutations avec répétition de $n$ éléments distinguables regroupés en $n_1, \dots, n_k$ objets |
| $\{ a_1, \dots, a_n \}$      | combinaison composée des éléments $a_1, \dots, a_n$                        |
| $D_{n, k}$                     | arrangements avec répétition de $n$ objets dans $k$ positions               |
| $d_{n, k}$                     | arrangements sans répétition de $n$ objets dans $k$ positions               |
| $c_{n, k}$                     | combinaisons simples de $n$ objets dans $k$ positions                       |
| $C_{n, k}$                     | combinaisons avec répétition de $n$ objets dans $k$ positions               |
| $S \subseteq T$               | sous-ensemble/sous-événement $S$ d’un ensemble/événement $T$                |
| $\Omega$                      | univers / espace des résultats / événement certain                          |
| $\varnothing$                 | ensemble vide / événement impossible                                        |
| $A \rightarrow B$             | événement/proposition $A$ implique événement/proposition $B$                |
| $A \leftrightarrow B$         | événement/proposition $A$ est logiquement équivalent à événement/proposition $B$ |
| $S \cup T$                    | union des ensembles/événements $S$ et $T$                                   |
| $S \cap T$                    | intersection des ensembles/événements $S$ et $T$                            |
| $S \backslash T$              | différence entre l’ensemble/événement $S$ et l’ensemble/événement $T$       |
| $S \Delta T$                  | différence symétrique entre les ensembles/événements $S$ et $T$             |
| $A \vee B$                    | disjonction logique des propositions $A$ et $B$                             |
| $A \wedge B$                  | conjonction logique des propositions $A$ et $B$                             |
| $\mathscr E$                  | expérience aléatoire                                                        |
| $\omega \in \Omega$         | issue d’une expérience aléatoire                                            |
| $\\{ \omega \\}$            | événement élémentaire                                                       |
| $\mathsf A$                   | algèbre des événements                                                      |
| $2^A$                          | ensemble des parties de l’ensemble $A$                                      |
| $\mathcal P$                  | partition d’un ensemble                                                     |
| $\mathbb P$                   | fonction de probabilité                                                     |
| $\mathbb P(E)$                | probabilité de l’événement $E$                                              |
| $\mathbb P(E\|F)$            | probabilité conditionnelle de l’événement $E$ sachant l’événement $F$       |
| $\mathbb E(X)$                | espérance de la variable aléatoire $X$                                      |
| $\mathbb E(g(X))$             | espérance de la fonction $g$ de la variable aléatoire $X$                   |
| $\mathbb E(g(X, Y))$          | espérance de la fonction $g$ des variables aléatoires $X$ et $Y$            |
| $a \triangleq b$              | $a$ est défini comme égal à $b$                                             |
```

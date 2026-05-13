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

(sec_arrangements-fr)=
# Arrangements

Un arrangement de $n$ objets distincts en $k$ cases est toute suite de $k$
symboles, chacun représentant l'un des objets. Ainsi, le type de groupement
correspondant aux arrangements dépend de l'ordre utilisé, et les objets doivent
être mutuellement discernables. On parle d'arrangements _avec répétition_ lorsqu'
un symbole peut apparaître plus d'une fois dans la suite, et d'_arrangements
simples_ dans le cas contraire.

## Arrangements avec répétition

Dans les arrangements avec répétition, le même objet peut être utilisé plus
d'une fois, comme le précise la définition suivante.

```{margin}
Ici le sens de _répétition_ diffère de celui vu pour les permutations, où il
fallait insérer chaque objet exactement autant de fois qu'il apparaît dans le
multiensemble de départ ; dans les arrangements, en revanche, on peut répéter le
même objet autant de fois qu'on le souhaite, ou l'omettre entièrement.
```
```{prf:definition} Arrangement avec répétition
:label: def-fr-arrangements-avec-repetition
Étant donné un ensemble de $n$ objets $A = \{ a_1,\dots a_n \}$ et un entier
$k \in \mathbb N$, un _arrangement avec répétition_ est une suite
$(a_{i_1}, \dots, a_{i_k})$, où pour tout $j = 1, \dots, k$ on a
$i_j \in \{1, \dots, n\}$ et $a_{i_j} \in A$. On note $D_{n, k}$ le nombre
d'arrangements avec répétition possibles de $n$ objets en $k$ cases.
```


```{prf:example} Un exemple d'arrangement avec répétition
:label: ex-fr-arrangements-avec-repetition-1

Le [Département H](https://marvel.fandom.com/wiki/Department_H_(Earth-616)) doit
planifier une séquence de trois missions quotidiennes — matin, après-midi et
soir. Pour chaque mission, n'importe lequel des quatre membres d'
[Alpha Flight](https://marvel.fandom.com/wiki/Alpha_Flight_(Earth-616)) peut être
envoyé : Guardian, Sasquatch, Northstar et Aurora, désignés par leurs initiales
$G$, $S$, $N$ et $A$ respectivement. Si chaque membre peut être déployé sur plus
d'une mission au cours de la même journée, chaque planning correspond à un
arrangement avec répétition des $n = 4$ objets de l'ensemble $\{G, S, N, A\}$
(les membres de l'équipe) en $k = 3$ cases (les gardes journalières). Par
exemple, les trois situations suivantes décrivent des plannings différents (et
des arrangements différents) :
- $(G, S, N)$ indique que Guardian, Sasquatch et Northstar assurent
  respectivement les gardes du matin, de l'après-midi et du soir ;
- $(S, N, G)$ inverse les gardes du matin et de l'après-midi par rapport au
  point précédent ;
- $(A, G, G)$ implique Aurora le matin et Guardian lors des deux gardes suivantes.
```

Calculer le nombre $D_{n, k}$ d'arrangements avec répétition possibles est assez
simple, en considérant le nombre de choix possibles pour chacune des $k$ cases :
- l'objet à placer dans la première case peut être choisi de $n$ façons
  différentes ;
- le nombre de choix reste $n$ pour la deuxième case également, car il est
  possible de réutiliser l'objet sélectionné pour la première position ;
- clairement, il y aura $n$ choix possibles pour toutes les cases restantes.

En appliquant le principe fondamental de la combinatoire, on obtient donc

$$
D_{n, k} = \underbrace{n \cdot n \dots \cdot n}_{k \text{ fois}} = n^k \enspace.
$$

On obtient le même résultat en notant que l'ensemble de tous les arrangements
est le produit cartésien $A^k$ de $A$ avec lui-même, calculé $k$ fois, et en
rappelant que $|A^k| = |A|^k = n^k$.

```{prf:example} Un exemple d'arrangement avec répétition
:label: ex-fr-arrangements-avec-repetition-2

En revenant à {prf:ref}`ex-fr-arrangements-avec-repetition-1`, le nombre total
de plannings quotidiens distincts est égal à $D_{4,3} = 4^3 = 64$, comme le
montre le {numref}`tab-fr-arrangements-avec-repetition`, où les colonnes M, A et
S désignent respectivement les gardes du matin, de l'après-midi et du soir.
```

````{table} Les arrangements avec répétition possibles de $4$ objets en $3$ cases, décrivant les gardes d'Alpha Flight ; les arrangements simples correspondants sont mis en évidence en gras.
:name: tab-fr-arrangements-avec-repetition
:align: center

|  # | M   | A   | S   |  # | M   | A   | S   |  # | M   | A   | S   |
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

## Arrangements simples

Dans les arrangements avec répétition, chaque objet peut apparaître plus d'une
fois dans la suite. Lorsque au contraire chaque objet ne peut être placé qu'en
une seule position, on parle d'_arrangements simples_, ou _arrangements sans
répétition_. Dans ce cas, on doit imposer $k \leq n$, car une fois que tous les
$n$ objets ont été placés dans une suite, il n'en reste plus à choisir.

```{prf:definition} Arrangement simple
:label: def-fr-arrangements-simples

Étant donné un ensemble de $n$ objets $A = \{ a_1,\dots a_n \}$ et un entier
$k \in \mathbb N$ avec $k \leq n$, un _arrangement simple_ est une suite
$(a_{i_1}, \dots, a_{i_k})$, où pour tout $j = 1, \dots, k$ on a
$i_j \in \{1, \dots, n\}$ et $a_{i_j} \in A$, et pour tout
$j, l = 1, \dots, k$ avec $j \neq l$ on a $a_{i_j} \neq a_{i_l}$.
On note $d_{n, k}$ le nombre d'arrangements simples possibles de $n$ objets en
$k$ cases.
```

````{prf:example}
:label: ex-fr-arrangements-simples-1

Si dans {prf:ref}`ex-fr-arrangements-avec-repetition-1` il n'était pas possible
d'attribuer plus d'une garde quotidienne à la même personne, des suites comme
$(A, G, G)$ ne seraient plus admises, et chaque planning correspondrait à un et
un seul arrangement simple de quatre objets en trois cases.
````

Pour calculer le nombre $d_{n, k}$ d'arrangements simples de $n$ objets en $k$
cases, on peut suivre un raisonnement analogue à celui des permutations simples :

- l'objet à placer dans la première case peut être choisi de $n$ façons
  différentes ;
- la deuxième case peut être remplie de $n - 1$ façons possibles, car l'objet
  sélectionné pour la première position ne peut plus être réutilisé ;
- le troisième choix peut être fait de $n - 2$ façons, et ainsi de suite
  jusqu'à la dernière case, qui peut être remplie en choisissant parmi
  $n - k + 1$ objets.

En appliquant le principe fondamental de la combinatoire, on obtient

```{math}
d_{n, k} = n (n-1) \ldots (n-k+1) =
n (n-1) \ldots (n-k+1) \cdot \frac{(n-k)!}{(n-k)!} =
\frac{n!}{(n-k)!} \enspace.
```

````{prf:example}
:label: ex-fr-arrangements-simples-2

Le {numref}`tab-fr-arrangements-avec-repetition` met en évidence en gras les
plannings de {prf:ref}`ex-fr-arrangements-simples-1`, dont le nombre est égal
à $d_{4, 3} = 4 \cdot 3 \cdot 2 = 24$.
````

Lorsque $k=n$, former un arrangement nécessite d'utiliser tous les éléments de
$A$, de sorte que les permutations simples sont un cas particulier des
arrangements simples. De manière cohérente, $d_{n, n} = n!/0! = n! = p_n$.

## Exercices

```{exercise} •
:label: ex-fr-arr-shield-codes

Le système informatique du [S.H.I.E.L.D.](https://marvel.fandom.com/wiki/S.H.I.E.L.D.)
génère des codes d'accès composés de cinq caractères, chacun choisi parmi huit
symboles spéciaux, avec répétition autorisée. Combien de codes distincts
peuvent être générés ?
```
```{solution} ex-fr-arr-shield-codes
:class: dropdown

Chaque code est un arrangement avec répétition de $8$ symboles en $5$ cases,
donc le nombre de codes distincts est $D_{8,5} = 8^5 = 32\,768$.
```

````{exercise} ••
:label: ex-fr-arr-wakanda-patrouilles

La Garde Royale du [Wakanda](https://marvel.fandom.com/wiki/Wakanda) doit
planifier des patrouilles pour les trois prochains jours, en sélectionnant un
guerrier différent chaque jour parmi six disponibles. De combien de façons
peut-on organiser le calendrier ?
````
````{solution} ex-fr-arr-wakanda-patrouilles
:class: dropdown

Chaque calendrier est un arrangement simple des six guerriers en trois jours,
donc le calendrier peut être organisé de $d_{6,3} = 6 \cdot 5 \cdot 4 = 120$
façons différentes.
````

````{exercise} ••
:label: ex-fr-arr-defenders-gardes

Les [Defenders](https://marvel.fandom.com/wiki/Defenders_(Earth-616)) doivent
assurer quatre gardes distinctes dans une journée (aube, matin, après-midi,
nuit), en choisissant à chaque fois un membre différent parmi neuf candidats. De
combien de façons peut-on établir le planning ?
````
````{solution} ex-fr-arr-defenders-gardes
:class: dropdown

Il s'agit d'arrangements simples de $9$ objets en $4$ cases :

```{math}
d_{9,4} = 9 \cdot 8 \cdot 7 \cdot 6 = 3024.
```
````

````{exercise} ••
:label: ex-fr-arr-porte-parole

Les membres des [Gardiens de la
Galaxie](https://marvel.fandom.com/wiki/Guardians_of_the_Galaxy_(Earth-616))
&mdash; Star-Lord, Gamora, Drax, Rocket et Groot &mdash; doivent attribuer trois
rôles distincts : porte-parole, porte-parole adjoint et archiviste. Combien
d'attributions sont possibles, sachant que Groot ne peut pas être porte-parole,
son langage étant limité à l'expression « Je s'appelle Groot » ?
````
````{solution} ex-fr-arr-porte-parole
:class: dropdown

Sans contraintes, chaque attribution correspondrait à l'un des $d_{5, 3} =
5 \cdot 4 \cdot 3 = 60$ arrangements simples des héros par rapport aux rôles.
Comme fixer l'un des rôles réduit le nombre de configurations différentes à
$d_{4, 2} = 4 \cdot 3 = 12$ &mdash; puisqu'il reste deux rôles et quatre
personnes &mdash; les attributions dans lesquelles Groot n'est pas porte-parole
seront $60 - 12 = 48$.
````

````{exercise} ••
:label: ex-fr-arr-young-avengers-contrainte

Pour une mission des [Young Avengers](https://marvel.fandom.com/wiki/Young_Avengers_(Earth-616)),
trois rôles distincts (commandement, reconnaissance, soutien) doivent être
attribués à sept héros. De combien de façons peut-on attribuer les rôles si
Patriot et Wiccan ne peuvent pas être sélectionnés ensemble ?
````
````{solution} ex-fr-arr-young-avengers-contrainte
:class: dropdown

Sans contraintes, il y aurait $d_{7, 3} = 7 \cdot 6 \cdot 5 = 210$ façons
possibles de procéder. À partir de ce nombre, on peut soustraire les cas
interdits, dans lesquels Patriot et Wiccan apparaissent tous les deux. Comme les
trois rôles sont distincts, les deux héros peuvent occuper deux d'entre eux de
$3 \cdot 2 = 6$ façons différentes (ce sont les arrangements $d_{3, 2}$ de trois
rôles en deux héros ; alternativement, choisir d'abord le rôle de Patriot, puis
celui de Wiccan). Le troisième rôle peut être attribué à l'un des $5$ héros
restants. Les cas à exclure sont donc $6 \cdot 5 = 30$, et le nombre de
configurations valides est $210 - 30 = 180$.
````

````{exercise} •••
:label: ex-fr-arr-avengers-premier-dernier

Les [Avengers](https://marvel.fandom.com/wiki/Avengers) doivent planifier une
séquence de quatre missions consécutives, en choisissant à chaque fois un membre
différent parmi Iron Man, Thor, Captain America, Black Widow et Hawkeye. Iron Man
doit participer soit à la première, soit à la dernière mission. Combien de
plannings sont possibles ?
````
````{solution} ex-fr-arr-avengers-premier-dernier
:class: dropdown

Comptons séparément les cas où Iron Man est assigné à la première ou à la
dernière mission. Les deux ensembles sont disjoints, car chaque héros participe
à une seule mission et ne peut donc pas occuper les deux positions.

- Quand Iron Man est impliqué dans la première mission, les trois restantes
  peuvent être attribuées aux quatre Avengers restants de
  $d_{4,3} = 4 \cdot 3 \cdot 2 = 24$ façons différentes.
- L'argument du point précédent ne change pas lorsque Iron Man est assigné à la
  dernière mission.

Les plannings valides sont donc au nombre de $24 + 24 = 48$.
````

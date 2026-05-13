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

(sec_permutations-fr)=
# Permutations

Une _permutation_ de $n$ objets est, en substance, une liste ordonnée contenant
chacun d'eux exactement une fois. Dans ce contexte, les configurations
considérées dépendent strictement de l'ordre des éléments, et réutiliser le même
objet n'est pas autorisé. Autrement dit, il s'agit de disposer $n$ objets dans
autant de cases disponibles, ce qui revient à fixer un critère d'ordre puis à
les lister du « plus petit » au « plus grand ».

Pour calculer le nombre de permutations possibles, on doit distinguer deux
situations :

- dans la première, tous les objets sont différents ;
- dans la seconde, il existe des objets différents qui sont néanmoins
  indiscernables les uns des autres.

Selon les deux cas, on parle de permutations _simples_ ou de permutations _avec
répétition_, que nous étudions ci-après.

## Permutations simples

Lorsque les objets à permuter sont les éléments d'un ensemble, ils sont par
définition tous différents, c'est-à-dire discernables les uns des autres. Dans
ce cas, on parle de _permutation simple_ (ou plus brièvement de _permutation_),
telle que décrite par la définition suivante.

````{prf:definition} Permutation simple
:label: def-fr-permutation-simple

Considérons un ensemble $A = \{ a_1,\dots a_n \}$ contenant $n$ objets. On
appelle _permutation simple_ (_permutation_) de ces objets toute suite ordonnée

```{math}
(a_{i_1}, \dots, a_{i_n}), \quad
1 \leq i_j \leq n \ \forall j \in \{1, \dots, n \}, \quad
i_h \neq i_k \ \forall h \neq k
```

dans laquelle figurent tous les $n$ éléments de $A$ et uniquement eux. On note
$p_n$ le nombre de telles permutations simples.
````

En général, je décrirai une permutation en listant ses éléments dans l'ordre
correspondant, séparés par des virgules et enfermés dans des parenthèses. Il
convient de noter que, à partir d'une permutation simple, il suffit d'échanger
deux éléments quelconques pour en obtenir une nouvelle.

````{prf:example} Les Quatre Fantastiques
:label: ex-fr-fantastic-4
Considérons l'ensemble $Q = \{ f, i, t, c \}$ des Quatre Fantastiques :
Mister Fantastic ($f$), la Femme Invisible ($i$), la Torche Humaine ($t$) et la
Chose ($c$) : les permutations simples possibles de ses éléments sont listées
dans le {numref}`permutations-quatre-fantastiques-fr`.
````

```{table} Permutations simples possibles des membres des Quatre Fantastiques
:name: permutations-quatre-fantastiques-fr
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

Le principe fondamental de la combinatoire nous permet de calculer facilement le
nombre $p_n$ de permutations différentes de $n$ objets :

- l'objet à placer en première position de la liste peut être choisi de $n$
  façons différentes, puisqu'on peut choisir parmi tous les objets disponibles ;
- la deuxième position peut être occupée par $n-1$ objets distincts, car celui
  utilisé à l'étape précédente ne peut plus être considéré, si bien qu'il y a
  $n \cdot (n-1)$ façons différentes de choisir les deux premiers éléments de
  la suite ;
- en procédant de même pour chaque position suivante, le nombre de choix
  diminue d'une unité à chaque étape, créant un arbre dont le niveau $i$
  correspond à la $i$-ème position ; pour remplir cette position, il reste
  $n-(i-1)$ éléments de $A$ parmi lesquels choisir, d'où
  $n\cdot(n-1) \cdot \ldots \cdot(n-(i-1))$ façons possibles de lister les
  premiers $i$ éléments de la suite ;
- arrivé à la dernière position, le seul élément restant de $A$ doit
  obligatoirement être choisi.

On peut donc construire un arbre de profondeur $n$ ayant un nombre de feuilles
égal à $n(n-1)(n-2)\ldots 1=n!$, chacune correspondant à une des permutations
simples possibles. En résumé, le nombre de permutations de $n$ objets est
$p_n = n!$. En regardant le {numref}`permutations-quatre-fantastiques-fr`, par
exemple, on peut facilement vérifier qu'il contient toutes les $4! = 24$
permutations possibles des quatre éléments de l'ensemble $Q$ introduit dans
{prf:ref}`ex-fr-fantastic-4`.


## Permutations avec répétition

Considérons maintenant le cas où certains des objets à permuter sont
indiscernables, mais restent _discernables par groupes_. Plus précisément,

- il y a $r \in \mathbb N$ versions possibles pour les objets, que l'on peut
  noter $a_1, \ldots, a_r$, et
- pour chaque $j = 1, \dots, r$, la version $a_j$ est répétée $n_j$ fois (ce
  qui implique $\sum_{j=1}^r n_j = n$).

Pour chaque version $a_j$, il y a donc un groupe d'objets indiscernables de
taille $n_j$. Ces objets forment un _multiensemble_ (une collection non ordonnée
dans laquelle chaque élément peut apparaître une ou plusieurs fois) contenant
$n_1$ occurrences de la version $a_1$, $n_2$ occurrences de $a_2$, et ainsi de
suite. En résumé, on peut écrire les éléments de ce multiensemble les uns après
les autres, obtenant la suite

```{math}
\underbrace{a_1, \ldots, a_1}_{n_1 \text{ fois}},
\underbrace{a_2, \ldots, a_2}_{n_2 \text{ fois}}, \ldots,
\underbrace{a_r, \ldots, a_r}_{n_r \text{ fois}} \enspace.
```

Changer l'ordre des éléments ne produit pas toujours une suite différente : si
deux objets indiscernables étaient échangés, la suite resterait inchangée. Dans
ces situations, on ne considère que les permutations qui produisent des suites
véritablement distinctes, telles que décrites par la définition suivante.

````{prf:definition} Permutation avec répétition
:label: def-fr-permutation-repetition

Considérons un multiensemble $A = \{ a_1,\dots a_n \}$ contenant $n$ objets
discernables par groupes de tailles $n_1, \ldots, n_r$. Une _permutation
d'objets discernables par groupes_ (plus brièvement, _permutation avec
répétition_) de ces objets est toute suite ordonnée de ceux-ci qui est
distinguable des autres, et on note $P_{n; n_1, \ldots, n_r}$ le nombre de
telles configurations.
````

Je noterai les permutations avec répétition en utilisant la même syntaxe que
pour les permutations simples, en séparant les éléments par des virgules et en
utilisant des parenthèses comme délimiteurs.

````{prf:example} Dupli-Kate et Multi-Paul
:label: fr-dupli-kate-multi-paul
Considérons les jumeaux
[Kate](https://comicvine.gamespot.com/dupli-kate/4005-41136/) et
[Paul Cha](https://comicvine.gamespot.com/multi-paul/4005-48737/) qui
apparaissent dans
[Invincible](https://comicvine.gamespot.com/invincible/4050-150390/).
Tous deux sont dotés du pouvoir de se répliquer à volonté et sont connus sous
les noms de Dupli-Kate et Multi-Paul. En particulier, chaque version de
Dupli-Kate est marquée d'un entier progressif sur son costume, de sorte qu'on
peut noter ses clones présents à un instant donné $k_1$, $k_2$, etc. Imaginons
que la même convention s'applique à Multi-Paul, dont les répliques seront notées
$p_1, p_2, \ldots$, et qu'il y ait devant nous deux versions de Kate et trois de
Paul, de sorte que le quintette résultant est décrit par le multiensemble
$A = \{ k_1, k_2, p_1, p_2, p_3 \}$.

Pour calculer de combien de façons ces cinq versions de Kate et Paul peuvent se
mettre en rang sans tenir compte de leur numéro progressif, on doit trouver le
nombre de permutations avec répétition de $n = 5$ objets divisés en deux groupes
distincts : l'un comprenant les $n_1 = 2$ copies de Kate et l'autre avec $n_2 =
3$ clones de Paul. Dans ce contexte, $(k_1, k_2, p_1, p_2, p_3)$ et $(k_2, k_1,
p_1, p_2, p_3)$ désignent deux permutations simples différentes, mais elles
correspondent à la même permutation avec répétition : dans les deux premières
positions apparaît Kate, dans les trois dernières apparaît Paul. En revanche,
$(k_1, k_2, p_1, p_2, p_3)$ et $(k_1, p_1, k_2, p_2, p_3)$ désignent des
permutations avec répétition différentes, car dans le premier cas la deuxième
position est occupée par Kate et la troisième par Paul, alors que dans le second
c'est l'inverse.
````

Avant de calculer le nombre total de permutations avec répétition de $n$ objets
discernables par groupes de tailles $n_1, n_2,\dots n_r$, analysons d'abord le
cas particulier de {prf:ref}`fr-dupli-kate-multi-paul`.
```{margin}
Fixer les positions des copies de Kate détermine dans ce cas également celles
des copies de Paul.
```
Concentrons-nous sur une permutation avec répétition possible, en fixant les
positions de Kate et celles de Paul. Par exemple, supposons que les première et
dernière positions soient réservées à Kate et les autres à Paul :

<p style="text-align: center">Kate Paul Paul Paul Kate</p>

Plusieurs permutations simples de cinq objets (les deux copies de Kate et les
trois de Paul) correspondent alors à cette permutation avec répétition.
Le {numref}`permutations-objets-indiscernables-fr` liste toutes les permutations
dans lesquelles Kate occupe les extrémités de la file, c'est-à-dire dans la
permutation avec répétition que nous avons fixée.

```{table} Permutations simples possibles d'objets en deux groupes discernables contenant respectivement deux doublons $k_1$ et $k_2$ de Kate et trois doublons $p_1$, $p_2$ et $p_3$ de Paul, tels que Kate occupe la première et la dernière position.
:name: permutations-objets-indiscernables-fr
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

Les lignes du {numref}`permutations-objets-indiscernables-fr` ont été obtenues
en permutant les deux copies de Kate en première et dernière position et les
trois copies de Paul dans les positions restantes. Si l'on considère Kate, il
n'y a que deux possibilités : $k_1$ et $k_2$ en première et dernière position
respectivement, ou vice versa, et ces deux possibilités correspondent aux $2!$
permutations simples des deux versions de Kate. En d'autres termes, on aurait pu
considérer toutes les permutations simples de ces deux versions, prendre le
premier élément et le placer dans la première colonne du tableau, puis insérer
le second élément dans la dernière colonne. On aurait ainsi obtenu deux
_modèles_ pour les lignes du tableau — respectivement pour les lignes un à six
et sept à douze. Dans les deux cas, les lignes sont complétées par un argument
analogue impliquant les $3!$ permutations simples possibles des versions de Paul.
On peut donc appliquer le principe fondamental de la combinatoire : comme il y a
$2!$ façons de remplir les positions de tête et de queue et $3!$ façons de
remplir les positions centrales, la configuration unique considérée correspond à
$n_1! \cdot n_2! = 2! \cdot 3! = 12$ permutations simples des cinq objets
disponibles.

Cet argument ne dépend pas de la permutation avec répétition particulière
analysée : à chacune des $P_{5; 2,3}$ permutations avec répétition correspondent
$2! \cdot 3! = 12$ permutations simples, et si on les considère toutes, on
constate qu'elles identifient conjointement la totalité des permutations simples.
L'égalité $P_{5; 2,3} \cdot 2! \cdot 3! = 5!$ doit donc être vérifiée, ce qui
permet de dériver

```{math}
P_{5; 2,3} = \frac{5!}{2! \cdot 3!} = 10 \enspace.
```

Notons que $P_{5; 2,3} = \binom{5}{2}$, et en effet le nombre de permutations
avec répétition coïncide avec le nombre de façons dont les deux positions pour
Kate peuvent être sélectionnées parmi les cinq disponibles.

Dans le cas général, on a $n$ objets divisés en $r$ groupes de tailles
$n_1, \ldots, n_r$, et en répétant l'argument précédent on obtient
$n! = P_{n; n_1,\dots, n_r} \cdot n_1! \cdot n_2! \cdot \ldots \cdot n_r!$,
ce qui implique

```{math}
:label: eq-fr-permutations-repetition

P_{n; n_1, \dots, n_r} = \frac{n!}{n_1!\cdot n_2! \cdot \ldots \cdot n_r!}
\enspace.
```

La quantité $P_{n; n_1, \dots, n_r}$ est aussi appelée _coefficient multinomial_
et notée

```{math}
P_{n; n_1, \dots, n_r} = \frac{n!}{n_1!\cdot n_2! \cdot \ldots \cdot n_r!}
                       \triangleq \binom{n}{n_1, n_2, \ldots, n_r} \enspace,
```

car elle représente une généralisation du coefficient binomial : en effet,
$\binom{n}{k} = \binom{n}{k, n-k}$ indique de combien de façons il est possible
de diviser $n$ objets en deux groupes contenant respectivement $k$ et $n-k$
éléments ; de manière analogue, $\binom{n}{n_1, \ldots, n_r}$ indique de combien
de façons il est possible de diviser $n$ objets en $r$ groupes dont le premier
contient $n_1$ éléments, le second $n_2$, et ainsi de suite.

## Exercices

````{exercise} ••
:label: ex-fr-perm-xmen-original

Les [X-Men](https://marvel.fandom.com/wiki/X-Men) dans leur formation originale
sont cinq : Cyclope, Marvel Girl, la Bête, Ange et Iceberg. De combien de façons
peut-on les aligner pour que Cyclope soit toujours en tête (en tant que chef
d'équipe) ?
````
````{solution} ex-fr-perm-xmen-original
:class: dropdown

Si Cyclope doit occuper la première position, les quatre autres héros peuvent
occuper les quatre autres positions de $p_4 = 4! = 24$ façons.
````

````{exercise} ••
:label: ex-fr-perm-thunderbolts

Les [Thunderbolts](https://marvel.fandom.com/wiki/Thunderbolts) originaux
étaient formés de Citizen V, un vilain opérant sous une fausse identité qui
avait convaincu cinq autres criminels de changer d'identité et de prétendre être
des héros. Jolt rejoignit ensuite le groupe sans connaître cette supercherie. De
combien de façons peut-on aligner tous les membres du groupe pour que les cinq
ex-vilains originaux occupent les premières positions ?
````
````{solution} ex-fr-perm-thunderbolts
:class: dropdown

Les cinq ex-vilains peuvent occuper les premières positions de $p_5 = 5! = 120$
façons, et — pour chacun de ces ordres — les deux membres restants peuvent
occuper les dernières positions de $p_2 = 2! = 2$ façons. Par le principe
fondamental, le nombre de configurations possibles est $120 \cdot 2 = 240$.
````

````{exercise} ••
:label: ex-fr-perm-sinister-six

De combien de façons les [Sinister Six](https://marvel.fandom.com/wiki/Sinister_Six)
(Doctor Octopus, Vautour, Électro, Mystério, Kraven le Chasseur et Sablier)
peuvent-ils occuper six chaises, de sorte que Doctor Octopus et Électro ne
soient jamais assis l'un à côté de l'autre ?
````
````{solution} ex-fr-perm-sinister-six
:class: dropdown

Chaque attribution de personnages aux chaises correspond à une permutation
particulière des Sinister Six, mais toutes les permutations ne sont pas à
considérer. Pour résoudre ce problème, il est commode de raisonner par
complémentarité, en soustrayant des $p_6 = 6! = 720$ permutations toutes celles
dans lesquelles Doctor Octopus et Électro sont adjacents. Le dénombrement de ces
dernières se fait en traitant les deux vilains comme un seul bloc, ce qui donne
cinq objets (quatre personnages plus la paire) à permuter de $p_5 = 5! = 120$
façons ; il faut cependant tenir compte du fait qu'échanger les deux éléments de
la paire produit deux permutations différentes parmi les originales, donc il y a
$240$ façons de placer Doctor Octopus et Électro côte à côte. En conclusion, il
y a $720 - 240 = 480$ arrangements acceptables.
````

````{exercise} ••
:label: ex-fr-perm-substitute-legion

La [Légion des Héros de Substitution](https://dc.fandom.com/wiki/Legion_of_Substitute_Heroes_(Earth-Prime))
comprend Polar Boy, Night Girl, Fire Lad, Stone Boy et Chlorophyll Kid. Leur
classement hebdomadaire de pouvoirs est établi comme suit : Night Girl et Polar
Boy sont toujours dans les deux premières positions (dans n'importe quel ordre),
tandis que Stone Boy est toujours le dernier. De combien de façons distinctes
peut-on établir un classement ?
````
````{solution} ex-fr-perm-substitute-legion
:class: dropdown

Stone Boy devant toujours apparaître en dernière place, le nombre de classements
s'obtient en appliquant le principe fondamental de la combinatoire, en
multipliant :

- les $p_2 = 2! = 2$ façons dont Night Girl et Polar Boy peuvent occuper les
  deux premières positions, et
- les $p_2 = 2$ façons possibles de distribuer Fire Lad et Chlorophyll Kid dans
  les positions centrales restantes.

Il est donc possible d'établir le classement de quatre façons distinctes.
````

````{exercise} ••
:label: ex-fr-perm-identite-publique-secrete

Iron Man, Captain America et la Femme Invisible ont des identités publiquement
connues ; à l'inverse, Daredevil, Spider-Man et Ant-Man opèrent anonymement. Si
l'on considère les super-héros à identité publique comme indiscernables les uns
des autres, et de même ceux à identité secrète, de combien de façons distinctes
est-il possible de les ordonner ?
````
````{solution} ex-fr-perm-identite-publique-secrete
:class: dropdown

Dans ce cas, on doit considérer les permutations de six objets organisés en deux
groupes de trois héros indiscernables chacun. En appliquant la formule
{eq}`eq-fr-permutations-repetition`, on obtient

```{math}
P_{6;\,3,3} = \frac{6!}{3!\cdot 3!} = \binom{6}{3} = 20 \enspace.
```
````

````{exercise} ••
:label: ex-fr-perm-anagrammes-superman

De combien de façons peut-on former les anagrammes du mot SUPERMAN, en
entendant par anagramme tout réarrangement des lettres du mot de départ, même
lorsque le résultat n'a pas de sens ?
````
````{solution} ex-fr-perm-anagrammes-superman
:class: dropdown

SUPERMAN est un mot contenant huit lettres, toutes différentes les unes des
autres. Le nombre d'anagrammes coïncide donc avec le nombre de permutations
simples de $8$ objets, qui est égal à $p_8 = 8! = 40\,320$.
````

````{exercise} ••
:label: ex-fr-perm-anagrammes-antman

De combien de façons peut-on former les anagrammes du mot ANTMAN, dans le même
sens que l'exercice précédent ?
````
````{solution} ex-fr-perm-anagrammes-antman
:class: dropdown

Le mot ANTMAN contient six lettres, dont deux apparaissent chacune en deux
positions différentes. Le nombre d'anagrammes distincts est donc une permutation
avec répétition : plus précisément, T et M appartiennent chacun à un groupe de
multiplicité $1$, tandis que A et N renvoient à deux groupes de multiplicité
$2$. Le nombre d'anagrammes distincts est donc

```{math}
P_{6;\,2,2,1,1} = \frac{6!}{2!\cdot 2!\cdot 1!\cdot 1!} = \frac{720}{4} = 180
\enspace.
```
````

````{exercise} •••
:label: ex-fr-perm-justice-society

Dans sa formation originale, la [Justice Society of
America](https://dc.fandom.com/wiki/Justice_Society_of_America_(New_Earth))
aligne huit héros : trois dotés de pouvoirs magiques ou extraterrestres (Green
Lantern, Spectre et Doctor Fate), trois qui utilisent des technologies secrètes
(Atom, Hourman et Flash) et deux qui utilisent des technologies bien connues et
facilement reconnaissables (Sandman et Hawkman). De combien de façons peuvent-ils
intervenir l'un après l'autre dans la bataille, en maintenant toujours les héros
de la même catégorie consécutifs ?
````
````{solution} ex-fr-perm-justice-society
:class: dropdown

Imaginons que tous les héros dotés de pouvoirs magiques interviennent en
premier, puis ceux utilisant des technologies secrètes, et enfin les restants.
Comme les deux premiers groupes peuvent être permutés de $p_3 = 3!$ façons et
le troisième peut être ordonné de $p_2 = 2!$ configurations, par le principe
fondamental de la combinatoire il y a $6 \cdot 6 \cdot 2 = 72$ façons
d'intervenir dans cet ordre de groupes. Si l'on change l'ordre des groupes, le
résultat est le même. Le résultat final s'obtient donc en multipliant $72$ par
le nombre de permutations des groupes, qui est $p_3 = 3!$. En conclusion, il y
aura $432$ façons différentes de déployer les membres de la Justice Society,
l'un après l'autre.
````

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

(sec_combinaisons-fr)=
# Combinaisons

De manière analogue aux arrangements, les combinaisons décrivent également des
tuples de longueur fixe dans lesquels apparaissent des objets choisis dans un
ensemble. Dans ce cas, cependant, les tuples sont _non ordonnés_ : ce ne sont
pas des suites mais plutôt des _sous-ensembles_ de l'ensemble de départ. Ainsi,
dans les groupements correspondant aux combinaisons l'ordre n'est pas pertinent,
mais il reste possible de décider si les objets peuvent être répétés ou non. Les
deux catégories de combinaisons qui en résultent sont décrites dans les sections
ci-dessous.

## Combinaisons simples

```{margin}
On peut aussi parler de construction de _sous-ensembles_ à partir d'un
_univers_ contenant les objets considérés.
```
Lorsqu'un objet peut être considéré au plus une fois, on peut effectivement dire
qu'il existe une correspondance entre les combinaisons — dites _simples_ — et les
sous-ensembles de l'ensemble de départ.

````{prf:definition}
:label: def-fr-combinaisons
Considérons un ensemble $A = \{ a_1, \ldots, a_n \}$ de $n$ objets et fixons un
entier $k \leq n$. Une _combinaison simple_ (ou plus brièvement une
_combinaison_) des $n$ objets en $k$ cases est un tuple non ordonné
$\{ a_{i_1}, \dots, a_{i_k} \}$ tel que pour tout $j = 1, \dots, k$ on a
$a_{i_j} \in A$, et $a_{i_j} \neq a_{i_l}$ pour tout $j, l = 1, \dots, k$ avec
$j \neq l$. On note le nombre de combinaisons simples possibles de $n$ objets en
$k$ cases par $c_{n, k}$.
````

Je noterai les combinaisons en utilisant des accolades comme délimiteurs des
tuples, pour souligner que l'ordre n'est pas pertinent ; de plus, cette notation
est cohérente avec le fait qu'une combinaison simple identifie un sous-ensemble
$\{ a_{i_1}, \dots, a_{i_k} \}\subseteq A$, de sorte que les descriptions du
sous-ensemble — données en forme extensionnelle — et de la combinaison coïncident.

````{prf:example} Peter Petrelli
:label: ex-fr-peter-petrelli
[Peter Petrelli](https://comicvine.gamespot.com/peter-petrelli/4005-47678/) est
l'un des protagonistes de
[Heroes](https://comicvine.gamespot.com/heroes/4050-19509/), doté d'une forme
extraordinaire d'_empathie_ lui permettant de reproduire les pouvoirs des autres
super-héros à sa proximité. Supposons que ce méta-pouvoir soit limité et que
Peter ne puisse répliquer que trois super-pouvoirs à la fois :
$\{ \text{télékinésie}, \text{télépathie}, \text{invisibilité} \}$ et
$\{ \text{télépathie}, \text{invisibilité}, \text{télékinésie} \}$ désignent le
même triple non ordonné, donc le même sous-ensemble et la même combinaison
simple de $k = 3$ super-pouvoirs. Dans ce cas, l'ensemble à partir duquel on
extrait les objets est l'ensemble de tous les super-pouvoirs, et il importe peu
de déterminer sa cardinalité $n$.
````

Pour calculer le nombre $c_{n, k}$ de combinaisons simples possibles de $n$
objets en $k$ cases, on peut exploiter le lien entre celles-ci et les
arrangements simples :
- chaque combinaison simple correspond à plusieurs arrangements : permuter de
  toutes les façons possibles les $k$ objets qui la composent donne $k!$
  arrangements distincts ;
- par conséquent, chaque combinaison apparaît exactement $k!$ fois dans
  l'ensemble des $d_{n, k}$ arrangements simples de $n$ objets en $k$ cases,
  d'où $d_{n, k} = c_{n, k} \cdot k!$ ;
- en inversant cette relation, on obtient $c_{n, k} = \frac{d_{n, k}}{k!}$.

En appliquant la formule de calcul de $d_{n, k}$, on obtient finalement

```{math}
c_{n, k} = \frac{d_{n, k}}{k!} = \frac{n!}{(n-k)!k!} =\binom{n}{k} \enspace.
```

````{prf:example} Peter Petrelli
:label: ex-fr-peter-petrelli-2

Imaginons qu'il y ait $n = 477$ super-pouvoirs
possibles[^superpouvoirs], et que Peter Petrelli (voir
{prf:ref}`ex-fr-peter-petrelli`) puisse tous les reproduire. Cela signifie qu'à
tout moment donné, il sera en mesure de « mémoriser »
$c_{477, 3} = \binom{477}{3} = \;$
<span style="word-spacing: -0.1rem">17 974 950</span>
configurations différentes de trois super-pouvoirs.
````

## Combinaisons avec répétition

Lorsqu'il est possible d'insérer le même objet plus d'une fois dans une
combinaison, on dit que celle-ci est une _combinaison avec répétition_. Dans ce
cas, la construction d'une combinaison est analogue à celle d'un _multiensemble_,
une généralisation du concept d'ensemble dans la description extensionnelle
duquel les objets peuvent apparaître plus d'une fois, de sorte que chaque
élément du multiensemble a également une _multiplicité_, comprise comme le
nombre de fois où il apparaît.

````{prf:definition} Combinaison avec répétition
:label: def-fr-combinaison-avec-repetition

Considérons un ensemble $A = \{ a_1, \ldots, a_n \}$ de $n$ objets et fixons un
entier $k \in \mathbb N$. Une _combinaison avec répétition_ des $n$ objets en
$k$ cases est un tuple non ordonné $\{ a_{i_1}, \dots, a_{i_k} \}$ tel que pour
tout $j = 1, \dots, k$ on a $a_{i_j} \in A$. On note le nombre de toutes les
combinaisons avec répétition possibles de $n$ objets en $k$ cases par $C_{n, k}$.
````

Je décrirai les combinaisons avec répétition en utilisant la même notation que
les combinaisons simples, à la différence que dans ce cas le tuple entre accolades
peut contenir des doublons.

````{prf:example}
:label: ex-fr-combinaisons-avec-repetition

Imaginons un ascenseur d'une capacité de quatre personnes, rempli de clones de
Dupli-Kate et Multi-Paul (voir {prf:ref}`fr-dupli-kate-multi-paul`), sans que les
deux jumeaux soient nécessairement tous les deux présents. Le
{numref}`tab-fr-combinaisons-DK-MP` liste toutes les façons dont quatre clones
peuvent entrer dans l'ascenseur, où chaque configuration correspond à une
combinaison avec répétition des deux objets $k$ et $p$ (Kate et Paul) en quatre
cases.
````

```{table} Combinaisons avec répétition possibles de Dupli-Kate et Multi-Paul en quatre cases
:name: tab-fr-combinaisons-DK-MP
:align: center

|    Combinaison     |
| :----------------: |
| $\{ k, k, k, k \}$ |
| $\{ k, k, k, p \}$ |
| $\{ k, k, p, p \}$ |
| $\{ k, p, p, p \}$ |
| $\{ p, p, p, p \}$ |
```


Une façon possible de calculer le nombre $C_{n, k}$ de combinaisons avec
répétition de $n$ objets d'un ensemble $A$ en $k$ cases consiste à les associer
de manière unique à des sous-ensembles appropriés de $\mathbb N$. Étant donnée
une fonction bijective $r: A \rightarrow \{ 1, \ldots, n \}$, chaque combinaison
avec répétition possible $\{ a_{i_1}, \ldots, a_{i_k} \}$ peut être transformée
en l'ensemble numérique $\{r(a_{i_1}), \ldots, r(a_{i_k}) \}$, en remplaçant
chaque élément par sa représentation numérique via $r$. Si l'on note $\sigma^r$
la suite obtenue en triant cet ensemble par ordre croissant, il s'ensuit que :

- $\sigma^r$ ne dépend pas de l'ordre particulier dans lequel les éléments de la
  combinaison de départ sont listés ;
- les $k$ éléments de $\sigma^r$ sont des entiers compris entre $1$ et $n$,
  bornes incluses, et cette suite peut contenir des valeurs adjacentes égales.

Enfin, notons $\sigma^r_i$ le $i$-ème élément de $\sigma^r$ et construisons une
dernière suite

```{math}
\rho = \{ \sigma^r_1 + 0, \sigma^r_2 + 1, \ldots, \sigma^r_k + k - 1 \}.
```

$\rho$ contiendra également $k$ éléments, mais ils seront automatiquement triés
par ordre strictement croissant, car ils ont été obtenus en incrémentant les
éléments de $\sigma^r$ — qui est non décroissant — d'une quantité de plus en
plus grande. De plus, $\rho$ contiendra des valeurs entières comprises entre $1$
et $n + k - 1$, et peut donc être mise en correspondance bijective avec un
sous-ensemble de $M = \{ 1, \ldots, n + k - 1 \}$ contenant $k$ éléments. En
résumé, chaque combinaison avec répétition de $n$ objets en $k$ cases peut être
associée à un sous-ensemble de $M$ de cardinalité $k$.

Réciproquement, un sous-ensemble générique de $M$ de cardinalité $k$ peut être
décrit en listant ses éléments par ordre croissant, obtenant une suite $\rho$. Si
l'on décrémente maintenant les éléments de cette suite en soustrayant zéro du
premier élément, un du second, deux du troisième, et ainsi de suite, on obtient
une nouvelle suite $\sigma^r$ triée par ordre non décroissant, dont les valeurs
(qui peuvent être répétées) sont comprises entre $1$ et $n$ (bornes incluses).
Considérer ensuite les préimages de ces valeurs par $r$ donne une combinaison
avec répétition de $k$ objets de $A$. Ainsi, tout sous-ensemble de $M$ de $k$
éléments peut être associé à une combinaison avec répétition de $n$ objets en
$k$ cases.

````{prf:example}
:label: fr-combinaisons-DK-MP-2
En revenant à {prf:ref}`ex-fr-combinaisons-avec-repetition`, l'ensemble de
départ d'objets $A = \{ k, p \}$, où $k$ et $p$ désignent Kate et Paul
respectivement, peut être mis en correspondance bijective avec $N = \{ 1, 2 \}$,
par exemple en posant $r(k) = 2$ et $r(p) = 1$. Le
{numref}`tab-fr-combinaisons-DK-MP-2` montre la correspondance entre toutes les
combinaisons avec répétition des deux objets de $A$ en quatre positions et les
suites $\sigma^r$ et $\rho$.
````

```{table} Correspondance entre les combinaisons avec répétition de Dupli-Kate et Multi-Paul en quatre cases.
:name: tab-fr-combinaisons-DK-MP-2
:align: center

|    Combinaison     |     $\sigma^r$     |     $\rho$     |
| :----------------: | :----------------: | :----------------: |
| $\{ k, k, k, k \}$ | $\{ 2, 2, 2, 2 \}$ | $\{ 2, 3, 4, 5 \}$ |
| $\{ k, k, k, p \}$ | $\{ 1, 2, 2, 2 \}$ | $\{ 1, 3, 4, 5 \}$ |
| $\{ k, k, p, p \}$ | $\{ 1, 1, 2, 2 \}$ | $\{ 1, 2, 4, 5 \}$ |
| $\{ k, p, p, p \}$ | $\{ 1, 1, 1, 2 \}$ | $\{ 1, 2, 3, 5 \}$ |
| $\{ p, p, p, p \}$ | $\{ 1, 1, 1, 1 \}$ | $\{ 1, 2, 3, 4 \}$ |
```

Par conséquent, les combinaisons avec répétition de $n$ objets en $k$ cases sont
en correspondance bijective avec les sous-ensembles de $M$ de cardinalité $k$,
et comme le nombre de ces sous-ensembles est égal au nombre de combinaisons
simples de $n + k - 1$ objets en $k$ cases, on peut conclure que

```{math}
C_{n, k} = c_{n + k - 1, k} = \binom{n+k-1}{k} \enspace.
```


[^superpouvoirs]: Tels que listés par exemple sur
[superherodb](https://www.superherodb.com/powers/).


## Exercices

````{exercise} ••
:label: ex-fr-ensemble-parties

Étant donné l'ensemble $A = \{ a_1,\dots a_n \}$ et notant par $\mathcal{P}(A)$
l'ensemble des parties de $A$, calculez la cardinalité de $\mathcal{P}(A)$.
````
````{solution} ex-fr-ensemble-parties
:class: dropdown

Rappelons que l'ensemble des parties $\mathcal{P}(A)$ est l'ensemble de tous
les sous-ensembles propres et impropres de $A$ : il contient l'ensemble vide,
tous les sous-ensembles composés d'un seul élément de $A$, tous les
sous-ensembles composés d'exactement deux éléments de $A$, et ainsi de suite,
et il contient aussi $A$ lui-même.

Comme le nombre de sous-ensembles composés de $k$ éléments est
$c_{n,k}=\binom{n}{k}$, la cardinalité de $\mathcal{P}(A)$ est
$|\mathcal{P}(A)| = 1 + \sum_{k=1}^{n} \binom{n}{k}$, où le premier terme
correspond à l'ensemble vide. En utilisant les propriétés du coefficient
binomial, on obtient

```{math}
|\mathcal{P}(A)| = \sum_{k=0}^{n} \binom{n}{k}
                 = \sum_{k=0}^{n}\binom{n}{k} 1^k 1^{n-k} = 2^n,
```

où à la dernière étape on a utilisé la formule du binôme de Newton :
$(a+b)^n = \sum_{k=0}^{n}\binom{n}{k}a^k b^{n-k}$, en posant $a=1$ et $b=1$.

Cet exercice peut aussi se résoudre comme suit : si l'on représente chaque
sous-ensemble $S$ de $A$ comme un $n$-uplet d'éléments binaires, où la position
$i$ contient le symbole $1$ si l'élément $a_i$ appartient à $S$ et $0$ s'il
n'y appartient pas, alors l'ensemble des parties $\mathcal{P}(A)$ est
l'ensemble de tous les $n$-uplets pouvant être construits à partir des deux
symboles $0$ et $1$. Par conséquent

```{math}
|\mathcal{P}(A)| = D_{n,2}=2^n.
```

````

````{exercise} ••
:label: ex-fr-comb-justice-league-equipe

La [Justice League](https://dc.fandom.com/wiki/Justice_League_(Prime_Earth)) doit
sélectionner une équipe d'intervention rapide de quatre membres, parmi dix
candidats. De combien de façons distinctes peut-on former l'équipe ?
````
````{solution} ex-fr-comb-justice-league-equipe
:class: dropdown

Il s'agit de choisir quatre héros parmi dix, sans ordre et sans répétition.
Cela peut se faire de $c_{10,4} = \binom{10}{4} = 210$ façons.
````

````{exercise} ••
:label: ex-fr-comb-xmen-professeur-x

Les [X-Men](https://marvel.fandom.com/wiki/X-Men) doivent former une équipe de
cinq membres parmi douze disponibles. Le Professeur X doit nécessairement en
faire partie. Combien d'équipes différentes sont possibles ?
````
````{solution} ex-fr-comb-xmen-professeur-x
:class: dropdown

Comme le Professeur X doit être inclus, quatre membres doivent être choisis
parmi les onze restants. Le nombre d'équipes est donc
$c_{11,4} = \binom{11}{4} = 330$.
````

````{exercise} •••
:label: ex-fr-comb-defenders-pas-ensemble

Les [Defenders](https://marvel.fandom.com/wiki/Defenders_(Earth-616)) ont neuf
candidats pour une mission nécessitant quatre membres. De combien de façons
peut-on former l'équipe si Daredevil et Jessica Jones ne peuvent pas apparaître
ensemble ?
````
````{solution} ex-fr-comb-defenders-pas-ensemble
:class: dropdown

Sans contraintes, les équipes possibles seraient $c_{9, 4} = \binom{9}{4} =
126$. D'autre part, les équipes contenant à la fois Daredevil et Jessica Jones
se comptent comme suit : la paire étant fixée, deux autres membres doivent être
choisis parmi les sept restants, ce qui peut se faire de $c_{7,2} = \binom{7}{2}
= 21$ façons. Les équipes valides sont donc $126 - 21 = 105$.
````

````{exercise} ••
:label: ex-fr-comb-gardiens-ressources

Les [Gardiens de la
Galaxie](https://marvel.fandom.com/wiki/Guardians_of_the_Galaxy_(Earth-616))
équipent le
[Milano](https://marvel.fandom.com/wiki/Milano) (leur vaisseau spatial) pour
une mission. À bord, cinq baies sont disponibles, chacune pouvant accueillir
l'un de quatre types d'appareils : canons laser, boucliers énergétiques,
capteurs de détection et modules de survie. Calculez le nombre de façons
différentes de configurer le Milano, sachant que chaque type d'appareil peut
être installé plusieurs fois et que seul le nombre de chaque type d'appareil
importe (pas dans quelle baie spécifique ils sont installés).
````
````{solution} ex-fr-comb-gardiens-ressources
:class: dropdown

Chaque configuration correspond à une et une seule combinaison avec répétition
de quatre objets (les types d'appareils) en cinq cases (les baies), pour un
total de $C_{4,5} = \binom{4+5-1}{5} = \binom{8}{5} = 56$ configurations
possibles.
````

````{exercise} •
:label: ex-fr-comb-avengers-pierres

Les [Avengers](https://marvel.fandom.com/wiki/Avengers_(Earth-616)) souhaitent
sélectionner quatre [Pierres de
l'Infini](https://marvel.fandom.com/wiki/Infinity_Stones) parmi les six
disponibles pour étudier leur comportement. Cependant, les Pierres du Temps et
de la Réalité doivent être étudiées ensemble, car modifier la séquence des
événements sans mettre à jour l'état de la réalité peut générer des
incohérences logiques et des paradoxes. Ces deux pierres doivent donc soit être
toutes les deux sélectionnées, soit être toutes les deux exclues du groupe.
Calculez le nombre de configurations de pierres différentes pouvant être
considérées.
````
````{solution} ex-fr-comb-avengers-pierres
:class: dropdown

Comme les Pierres du Temps et de la Réalité doivent être considérées ensemble
ou complètement exclues, on peut examiner les deux cas séparément, calculer le
nombre de choix possibles pour chacun, puis additionner.

- Il y a $c_{4, 2} = \binom{4}{2} = 6$ configurations contenant les deux
  pierres, car une fois les Pierres du Temps et de la Réalité fixées, deux
  autres doivent être sélectionnées parmi les quatre pierres restantes.
- Intuitivement, si ces deux pierres sont exclues, il en reste exactement
  quatre, et elles doivent toutes être sélectionnées. En effet, dans ce cas
  les combinaisons de ces quatre pierres en quatre cases sont $c_{4, 4} = 1$.

En conclusion, il y a sept façons possibles de sélectionner les pierres à
étudier.
````

````{exercise} •••
:label: ex-fr-comb-batman-gadgets-contrainte

Batman doit préparer sa ceinture utilitaire en choisissant quatre gadgets parmi
une liste de huit, mais deux gadgets (la grenade flash et les lunettes de vision
nocturne) sont incompatibles et ne peuvent pas être inclus ensemble. De combien
de façons peut-il choisir son équipement ?
````
````{solution} ex-fr-comb-batman-gadgets-contrainte
:class: dropdown

Sans la contrainte d'incompatibilité, les chargements possibles seraient décrits
par les combinaisons de huit gadgets en groupes de quatre, pour un total de
$c_{8, 4} = \binom{8}{4} = 70$ cas. On doit en soustraire les configurations
interdites. Dans ces configurations, deux des quatre cases sont déjà occupées
par la grenade flash et les lunettes de vision nocturne, donc leur nombre est
égal au nombre de combinaisons des six gadgets restants en groupes de deux, soit
$c_{6, 2} = \binom{6}{2} = 15$. Le total valide est donc $70 - 15 = 55$.
````

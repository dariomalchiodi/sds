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

(sec_ensembles-finis-infinis)=
# Ensembles finis et infinis

Il n'est pas difficile de penser à des ensembles contenant un nombre fini
d'éléments, comme l'ensemble des membres de la Justice League, l'ensemble
des jours de la semaine ou l'ensemble des nombres premiers inférieurs à
$100$. On dit que de tels ensembles sont _finis_. Il existe cependant aussi
des ensembles qui ne contiennent pas un nombre fini d'éléments, comme
l'ensemble de toutes les fractions ou l'ensemble des points du plan. Pour
ces ensembles _infinis_, on distingue deux cas :

```{margin}
En mathématiques, on dit simplement qu'un ensemble est _dénombrable_ si ses
éléments peuvent être listés dans une suite finie ou infinie ; les ensembles
finis sont donc également dénombrables.
```
- un ensemble est dit _infiniment dénombrable_ lorsqu'il est possible de
  construire une suite (infinie) $x_1, x_2, \dots$ qui contient chacun de
  ses éléments à une certaine position : l'ensemble $D$ des nombres impairs,
  que j'introduirai bientôt, est un exemple d'ensemble infiniment
  dénombrable ;
- dans tous les autres cas, on dit que l'ensemble est _infiniment non
  dénombrable_ : l'ensemble des points d'une droite et l'ensemble des
  nombres réels sont tous deux infinis et non dénombrables.

La description extensive n'est, à proprement parler, pas applicable aux
ensembles infinis, puisque par définition il est impossible d'en lister
tous les éléments. Cependant, lorsqu'un ensemble infiniment dénombrable
peut être associé à une suite que l'on peut intuitivement prolonger après
n'avoir vu que quelques-uns de ses termes initiaux, il est acceptable
d'étendre la description extensive en listant seulement ces éléments, puis
en ajoutant des points de suspension pour souligner le caractère infini de
l'ensemble. Par exemple, bien que la description intensive

```{math}
D = \{ 2n+1 \mid n \in \mathbb N \}
```

soit la plus précise pour désigner l'ensemble des nombres impairs, on
utilise aussi souvent la formulation extensive $D = \{1, 3, 5, 7, 9, \dots \}$.
Il faut cependant garder à l'esprit qu'une suite partielle ne peut pas
identifier un ensemble de façon univoque : dans le cas précédent, les
premiers termes $1, 3, 5, 7, 9$ pourraient en principe se référer à
l'ensemble des nombres impairs inférieurs à $100$, ou à toute autre suite
qui coïncide avec celle des impairs sur les premiers éléments mais diverge
ensuite. Les points de suspension suggèrent quels sont les éléments
restants, mais ne les définissent pas rigoureusement, c'est pourquoi la
description intensive reste formellement correcte. À plus forte raison, les
descriptions extensives ne parviennent pas à saisir la complexité des
ensembles infiniment non dénombrables, pour lesquels seules des
descriptions intensives sont généralement utilisables.

## Exercices

````{exercise}
:label: ex-fr-suicide-squad

La [Suicide Squad](https://dc.fandom.com/wiki/Suicide_Squad_(Prime_Earth))
est composée de six membres : Emerald Empress, Doctor Polaris, Johnny
Sorrow, Lobo, Rustam et Cyclotron, chacun pouvant être soit opérationnel
soit hors combat. L'état du groupe est décrit par un vecteur
$(x_1, x_2, x_3, x_4, x_5, x_6)$, où pour chaque $i = 1, \dots 6$, $x_i$
vaut $1$ si le $i$-ème membre (dans l'ordre ci-dessus) est opérationnel,
et $0$ sinon. Répondez aux questions suivantes.

1. Combien d'éléments contient l'ensemble de tous les états possibles du
   groupe ?
2. Soit $A$ l'ensemble des états dans lesquels au moins un des membres
   $1$ et $2$ est opérationnel, et au moins un des membres $3$ et $4$ est
   opérationnel. Écrivez du code Python qui liste tous les éléments de $A$.
3. Soit $B$ l'ensemble des états dans lesquels les membres $1$ et $3$ sont
   tous les deux hors combat. Combien d'éléments contient $B$ ?
````
````{solution} ex-fr-suicide-squad
:class: dropdown

1. Quelle que soit la valeur de $i$, chaque composante $x_i$ peut prendre
   deux valeurs distinctes, donc le principe fondamental du calcul
   combinatoire nous dit que l'ensemble de tous les états a $2^6 = 64$
   éléments.

2. Les conditions requises sont $(x_1=1 \vee x_2=1)$ et $(x_3=1 \vee x_4=1)$.
   Les paires $(x_1, x_2)$ satisfaisant la première condition sont au nombre
   de trois : $(1,0),(0,1),(1,1)$. De même, il existe trois configurations
   pour $(x_3, x_4)$. En revanche, $(x_5, x_6)$ peut prendre toutes les
   quatre configurations possibles. Par le principe fondamental du calcul
   combinatoire, on a $|A| = 3 \times 3 \times 4 = 36$, et les éléments de
   $A$ sont exactement les vecteurs avec $(x_1, x_2) \neq (0,0)$ et
   $(x_3, x_4) \neq (0,0)$, comme le confirme la sortie du code suivant.

```{code-cell} python
import itertools as it

v = (0, 1)
teams = [t for t in it.product(v, repeat=6)
           if (t[0] or t[1]) and (t[2] or t[3])]
for t in teams:
    print(t)
```

3. Avec $x_1=0$ et $x_3=0$ fixés, les composantes restantes $x_2$, $x_4$,
   $x_5$ et $x_6$ sont libres, donc $|B| = 2^4 = 16$.
````

````{exercise}
:label: ex-fr-new-warriors

Les [New Warriors](https://marvel.fandom.com/wiki/New_Warriors_(Earth-616))
sont un groupe de super-héros Marvel qui, dans l'une de leurs formations,
compte six membres : Night Thrasher, Firestar, Justice, Namorita, Speedball
et Nova. Pour chacun des ensembles suivants, déterminez s'il est fini,
infiniment dénombrable ou infiniment non dénombrable, en justifiant votre
réponse.

1. L'ensemble $W$ des six membres des New Warriors.
2. L'ensemble $M$ des numéros de mission possibles attribués
   progressivement au groupe à partir de $1$, c'est-à-dire
   $M = \{1, 2, 3, 4, \dots\}$.
3. L'ensemble $C$ de toutes les paires $(i, n)$ où
   $i \in [1 .. 6]$ identifie l'un des six membres et $n \in \mathbb{N}$
   est le numéro de la mission qu'il dirige.
4. L'ensemble $V$ de toutes les valeurs réelles possibles (en km/h) de la
   vitesse à laquelle Nova peut voler, sachant que sa vitesse est dans
   l'intervalle $[0, 10^6]$.
````
````{solution} ex-fr-new-warriors
:class: dropdown

1. $W$ est fini : il contient exactement $6$ éléments, un pour chaque
   membre listé.
2. $M$ est infiniment dénombrable : comme le nombre total de missions que
   les New Warriors entreprendront n'est pas connu à l'avance, tout
   nombre naturel est un numéro de mission possible. Donc $M = \mathbb{N}$,
   qui est par définition dénombrable.
3. $C$ est infiniment dénombrable. Pour chaque $i$ fixé, il existe une
   infinité de valeurs de $n$, donc $C$ est infini. Pour montrer la
   dénombrabilité, on construit la suite
   $(1,1), (1,2), (1,3), \dots, (2,1), (2,2), \dots$ qui, après avoir
   épuisé les éléments avec $i = j$, passe à $i = j+1$. Comme six suites
   dénombrables sont concaténées, le résultat est encore une suite
   dénombrable qui liste tous les éléments de $C$.
4. $V$ est infiniment non dénombrable : les valeurs réelles possibles de
   vitesse appartiennent à l'intervalle $[0, 10^6]$, qui est un
   sous-ensemble de $\mathbb{R}$, et tout intervalle de nombres réels est
   non dénombrable.
````

````{exercise}
:label: ex-fr-great-lakes-avengers

Les [Great Lakes
Avengers](https://marvel.fandom.com/wiki/Great_Lakes_Avengers_(Earth-616))
sont un groupe Marvel excentrique composé de six membres : Big Bertha,
Doorman, Flatman, Mr. Immortal, Dinah Soar et Grasshopper. Avant chaque
mission, le groupe attribue trois rôles distincts — chef, tacticien et
éclaireur — à trois membres distincts. L'ordre des rôles est significatif
(être chef est différent d'être tacticien). Soit $R$ l'ensemble de toutes
les affectations de rôles possibles.

1. Combien d'éléments contient $R$ ?
2. Soit $D$ l'ensemble des affectations dans lesquelles Doorman remplit
   l'un des trois rôles. Combien d'éléments contient $D$ ?
3. Écrivez du code Python qui liste tous les éléments de $R$ et vérifiez
   les résultats des points 1 et 2.
````
````{solution} ex-fr-great-lakes-avengers
:class: dropdown

1. Nous devons choisir, dans l'ordre, trois membres distincts parmi six,
   donc nous comptons les arrangements simples de six objets (les héros)
   dans trois emplacements (les rôles). Ainsi
   $|R| = d_{6, 3} = 6 \times 5 \times 4 = 120$.

2. Doorman peut remplir l'un quelconque des trois rôles. Une fois le rôle
   de Doorman choisi, les deux rôles restants sont attribués en
   sélectionnant deux membres différents parmi les cinq restants, ce qui
   peut se faire de $d_{5, 2} = 5 \times 4 = 20$ façons. Donc
   $|D| = 3 \times d_{5, 2} = 60$.

3. Dans la cellule ci-dessous, par souci de brièveté, les super-héros sont
   désignés BB (Big Bertha), DM (Doorman), FM (Flatman), MI (Mr. Immortal),
   DS (Dinah Soar) et GH (Grasshopper). En utilisant `it.permutations` on
   peut générer tous les arrangements correspondant aux éléments de $R$,
   sélectionner ceux qui appartiennent à $D$, les afficher et les compter.

```{code-cell} python
import itertools as it

members = ['BB', 'DM', 'FM', 'MI', 'DS', 'GH']
roles = ['chef', 'tacticien', 'eclaireur']

R = it.permutations(members, 3)

D = [t for t in R if 'DM' in t]

print('Elements de D:')
for i, a in enumerate(D):
    print('-'.join(a), end=', ' if (i+1) % 6 else '\n')

print(f"\n|D| = {len(D)}")
```
````

````{exercise}
:label: ex-fr-doom-patrol

La [Doom Patrol](https://dc.fandom.com/wiki/Doom_Patrol_(New_Earth)) est
une équipe de super-héros marginaux, dont Robotman, Negative Man,
Elasti-Girl et Crazy Jane. Leurs archives historiques étiquettent chaque
affrontement avec une paire de nombres naturels positifs $(v, s)$, où $v$
est le numéro d'un comic et $s$ le numéro de l'affrontement dans ce comic.
Soit $A = \{ (v, s) : v, s \in \mathbb{N} \}$ l'ensemble de toutes les
étiquettes d'affrontement possibles.

1. Démontrez que $A$ est infini.
2. Démontrez que $A$ est dénombrable en construisant explicitement une
   suite $a_1, a_2, a_3, \dots$ qui liste chaque élément de $A$ à une
   certaine position, et établissez la formule pour la position d'un
   élément générique $(v, s)$.
3. À quelle position se trouve $(3, 2)$ dans la suite du point précédent ?
````
````{solution} ex-fr-doom-patrol
:class: dropdown

1. Il n'y a pas de «dernier» numéro de comic en principe, donc $A$
   contient toutes les paires $(v, i)$ pour $v \in \mathbb N$ et est
   donc un ensemble infini.

2. On adopte la classique _énumération diagonale_ : on considère la
   décomposition $A = \cup_{k=2}^{+\infty} D_k$, où
   $D_k = \{ (v,s) \in A : v + s = k \}$ désigne une _diagonale_
   contenant exactement $k-1$ paires, ordonnées comme
   $(1, k-1), (2, k-2), \dots, (k-1, 1)$. Chaque paire $(v, s)$
   appartient à une et une seule diagonale, donc en considérant toutes
   les diagonales dans l'ordre et en énumérant leurs éléments, après un
   nombre fini d'étapes on doit atteindre $(v, s)$. Donc $A$ est
   dénombrable.

3. Pour $(3, 2)$ on a $k = 3 + 2 = 5$, donc la paire appartient à $D_5$.
   En générant les éléments de la suite correspondant aux quatre premières
   diagonales, on voit que $(3, 2)$ apparaît en neuvième position :

   ```{math}
   \underbrace{(1,1)}_{D_2},
   \underbrace{(1,2), (2,1)}_{D_3},
   \underbrace{(1,3), (2,2), (3,1)}_{D_4},
   \underbrace{(1,4), (2,3), (3,2), (4, 1)}_{D_5} \enspace.
   ```

````

````{exercise}
:label: ex-fr-extensive-intensive

Pour chacun des ensembles suivants, exprimés en forme intensive, écrivez —
lorsque c'est possible — la description extensive correspondante, et
indiquez si elle est exacte ou seulement partielle.

1. $A = \{ n \in \mathbb{N} \mid n^2 \leq 25 \}$.
2. $B = \{ n \in \mathbb{Z} \mid -3 \leq n \leq 3 \}$.
3. $C = \{ n \in \mathbb{N} \mid n \text{ est un multiple de } 3 \}$.
4. $D = \{ x \in \mathbb{R} \mid 1 \leq x \leq 2 \}$.
````
````{solution} ex-fr-extensive-intensive
:class: dropdown

1. $A = \{ 1, 2, 3, 4, 5 \}$. L'ensemble est fini, donc la description
   extensive est exacte : elle liste précisément tous les éléments de $A$
   et uniquement ceux-ci.

2. $B = \{ -3, -2, -1, 0, 1, 2, 3 \}$. Là encore l'ensemble est fini et
   la description extensive est exacte.

3. Une description extensive possible est $C = \{0, 3, 6, 9, \dots\}$.
   $C$ est infiniment dénombrable, donc la description extensive est
   seulement partielle : les points de suspension suggèrent le motif mais
   ne le définissent pas rigoureusement. Dans ce cas, par exemple, les
   quatre valeurs indiquées marquent aussi le début de la suite des nombres
   dont les chiffres appartiennent tous à $\{ 0, 3, 6, 9 \}$, qui
   continuerait par $30, 33, 36, 39, 60$, etc.

4. $D$ est un intervalle de nombres réels et est donc infiniment non
   dénombrable ; une description extensive n'est pas applicable. Il n'est
   pas possible d'établir une liste partielle de ses éléments qui soit
   significative.
````

````{exercise}
:label: ex-fr-intensive-extensive

Pour chacun des ensembles suivants, exprimés en forme extensive, écrivez
une description intensive équivalente.

1. $A = \{ \text{Thor}, \text{Iron Man}, \text{Captain America},
   \text{Hulk}, \text{Black Widow}, \text{Hawkeye} \}$.
2. $B = \{ 2, 4, 6, 8, \dots \}$.
3. $C = \{ 1, 4, 9, 16, 25, \dots \}$.
4. $D = \{ 0, 1 \}$.
````
````{solution} ex-fr-intensive-extensive
:class: dropdown

1. Une description intensive possible est
   $A = \{ x \mid x \text{ est un Avenger de la formation originale} \}$.

2. La suite indiquée suggère que l'ensemble contient les nombres pairs.
   Dans ce cas, deux descriptions intensives possibles sont
   $B = \{ n \in \mathbb N \mid n \text{ est pair} \}$ et
   $B = \{ 2k \mid k \in \mathbb N \}$ (bien que la même suite puisse
   continuer de différentes façons, par exemple en listant tous les
   nombres pairs dont les chiffres sont tous égaux).

3. L'interprétation la plus simple suggère que la description extensive
   liste les premiers carrés parfaits (bien que d'autres interprétations
   soient possibles). Dans ce cas, on peut utiliser la formulation
   intensive $C = \{ n^2 \mid n \in \mathbb N \}$, ou de manière
   équivalente $C = \{ n \in \mathbb N \mid \sqrt{n} \in \mathbb{N} \}$.

4. $D = \{ n \in \mathbb Z \mid 0 \leq n \leq 1 \}$, ou
   $D = \{ x \in \mathbb R \mid x^2 = x \}$, ou plus simplement
   $D = \{ x \in \mathbb R \mid x = 0 \vee x = 1 \}$.
````

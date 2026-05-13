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

(sec_principe-fondamental-combinatoire)=
# Principe fondamental

```{figure} https://static.wikia.nocookie.net/marvel_dc/images/8/8c/Detective_Comics_241.jpg/revision/latest?cb=20081218152007
---
figclass: margin
name: fig_dc-241-fr
width: 200px
align: left
---
Couverture de _Detective Comics_ numéro 241 (mars 1957). Marques déposées &
Copyright © 1935–2026 DC Comics, Inc. Source : [DC Database, Fandom](https://dc.fandom.com/wiki/Detective_Comics_Vol_1_241).
```
Cela peut sembler étrange, mais dans certaines histoires Batman a porté des
costumes bien plus colorés que le gris classique des bandes dessinées originales
ou le noir des films récents. Le numéro 241 de _Detective Comics_ présente une
histoire intitulée « The Rainbow Batman ». Dans cette version, le Chevalier Noir
alterne des tenues orange, verte et rose, dans le but d'attirer l'attention sur
lui plutôt que sur une blessure au bras de Robin qui aurait pu éveiller des
soupçons en raison de sa ressemblance avec celle de Dick Grayson {cite}`robb`.
Modifions légèrement le scénario : imaginez que Batman dispose dans sa garde-robe
de quatre capes (rose, verte, rouge et marron) et de trois costumes (jaune, bleu
ciel et noir). De combien de façons différentes peut-il associer une cape à un
costume ? La {numref}`fig_principe-fondamental-fr` montre la réponse : pour
chacune des quatre capes il existe trois costumes possibles, de sorte que le
nombre total d'associations est $4 \times 3 = 12$.

```{figure} ../../../_static/img/superhero-grid.png
:width: 50%
:name: fig_principe-fondamental-fr

Une illustration simple du principe fondamental de la combinatoire : avec quatre
options possibles pour un premier choix et trois options pour un second choix,
il y a en tout douze choix combinés (image créée à partir de zéro par l'auteur
à l'aide de l'IA (ChatGPT) et d'une post-production graphique).
```

En généralisant, on obtient le _principe fondamental de la combinatoire_ : lors
de $t$ choix successifs, si le premier peut être effectué de $s_1$ façons, le
second de $s_2$ façons, le troisième de $s_3$ façons, etc., alors le nombre
total de suites de choix est

```{math}
s_1 \cdot \ldots \cdot s_t = \prod_{i=1}^t s_i \enspace.
```

On peut obtenir le même résultat en construisant un arbre de décision : le
nombre de façons d'effectuer les $t$ choix est égal au nombre de feuilles d'un
arbre de profondeur $t$ dans lequel le premier niveau comporte $s_1$ nœuds,
chacun ayant $s_2$ enfants, chaque enfant ayant à son tour $s_3$ enfants, et
ainsi de suite, comme illustré dans la {numref}`fig_arbre-fr`.

```{figure} ../../../_static/img/superhero-tree.png
:width: 100%
:name: fig_arbre-fr

L'arbre correspondant aux choix possibles dans la
{numref}`fig_principe-fondamental-fr` (image créée à partir de zéro par
l'auteur à l'aide de l'IA (ChatGPT) et d'une post-production graphique).
```

Comme je l'ai souligné au début du chapitre, l'application du principe
fondamental de la combinatoire ne dépend pas de la nature des objets considérés,
qu'il s'agisse de capes, de costumes, de légumes ou d'instruments financiers. Si
dans l'exemple précédent nous avions associé trois couleurs à quatre modèles de
Batmobile, nous aurions obtenu le même résultat numérique. C'est vrai en général :
les résultats de la combinatoire dépendent de la taille des objets et, le cas
échéant, du nombre de cases considérées. C'est pourquoi on parle, par exemple,
des _permutations_ de $n$ objets ou des _combinaisons_ de $n$ objets en $k$
cases, en utilisant les termes « objet » et « case » dans un sens abstrait. Dans
les sections qui suivent, je ferai souvent référence à des objets spécifiques
afin d'illustrer les concepts présentés.


## Exercices

````{exercise} •••
:label: ex-fr-disp-justice-society-categories

La [Justice Society of
America](https://dc.fandom.com/wiki/Justice_Society_of_America_(New_Earth))
envoie trois membres en mission dans un ordre précis (le premier engage les
hostilités, le second intervient au cœur de la bataille, le troisième couvre la
retraite), en choisissant parmi quatre super-héros dotés de pouvoirs surnaturels
(Green Lantern, Flash, Doctor Fate et Hourman) et trois justiciers sans
super-pouvoirs (Sandman, Wildcat et Starman). Combien de suites sont possibles
si la première position doit être occupée par un super-héros et la dernière par
un justicier ?
````
````{solution} ex-fr-disp-justice-society-categories
:class: dropdown

Les trois cases doivent être remplies en respectant les contraintes de catégorie :

- la première case revient à l'un des quatre super-héros dotés de pouvoirs
  surnaturels ;
- la dernière case revient à l'un des trois justiciers ;
- la position centrale peut être occupée par n'importe lequel des cinq héros
  restants.

Par le principe fondamental de la combinatoire, le nombre de suites valides est
$4 \cdot 5 \cdot 3 = 60$.
````

````{exercise} ••
:label: ex-fr-fpc-xmen-menace

Pour classer une mission des X-Men, Cérébro attribue :

- un niveau de menace parmi $6$ valeurs possibles ;
- une priorité parmi $4$ valeurs possibles ;
- un secteur opérationnel parmi $5$ valeurs possibles.

Combien de codes de mission distincts peut-il produire ?
````
````{solution} ex-fr-fpc-xmen-menace
:class: dropdown

Chaque code est obtenu en choisissant successivement une valeur pour chacune des
trois catégories. Par le principe fondamental de la combinatoire, le nombre de
codes possibles est donc $6 \cdot 4 \cdot 5 = 120$.
````

````{exercise} ••
:label: ex-fr-fpc-avengers-gardes

Les Avengers doivent assurer trois gardes (matin, après-midi, nuit), en
choisissant à chaque fois un membre différent parmi huit disponibles. De combien
de façons peut-on établir le planning journalier ?
````
````{solution} ex-fr-fpc-avengers-gardes
:class: dropdown

Pour la garde du matin il y a huit choix, pour l'après-midi sept (car le membre
choisi le matin ne peut pas être réutilisé), et pour la nuit six (par un
raisonnement analogue). Par le principe fondamental de la combinatoire, le nombre
de façons d'attribuer les gardes est $8 \cdot 7 \cdot 6 = 336$.
````

````{exercise} •••
:label: ex-fr-fpc-defenders-contrainte-chef

Les [Defenders](https://marvel.fandom.com/wiki/Defenders_(Earth-616)) doivent
attribuer trois rôles distincts : chef d'équipe, analyste tactique et soutien
opérationnel, parmi sept candidats. Jessica Jones, si elle est sélectionnée, ne
peut occuper que le rôle de chef d'équipe. Combien d'attributions sont possibles ?
````
````{solution} ex-fr-fpc-defenders-contrainte-chef
:class: dropdown

Considérons séparément les cas où Jessica Jones est sélectionnée ou non. Dans
le premier cas, le rôle de chef est fixé, et les deux rôles restants peuvent
être attribués aux six autres candidats, ce qui peut se faire de $d_{6, 2}$
façons différentes. Dans le second cas, il n'y a que six candidats pour les
trois rôles, donc il y a $d_{6, 3}$ façons de procéder. En additionnant les
deux résultats, le nombre d'attributions possibles est
$d_{6, 2} + d_{6, 3} = 6 \cdot 5 + 6 \cdot 5 \cdot 4 = 30 + 120 = 150$.
````

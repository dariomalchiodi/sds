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

(par:franklin-law)=
# Présentation

> En ce monde, rien n’est certain<br/>
> à part la mort et les impôts
>
> -- Benjamin Franklin

La citation qui ouvre ce paragraphe est une traduction d’une lettre écrite en
1789 par Benjamin Franklin (voir {numref}`benjamin-franklin`), l’un des pères
fondateurs des États-Unis d’Amérique. Si l’on accepte cet adage, souvent
référencé comme la _loi de Franklin_ [^citation-franklin], cela vaut la peine
d’étudier l’incertitude, car pratiquement tout est incertain (ironiquement, la
validité même de la loi de Franklin ne va pas de soi : pensons par exemple au
phénomène de l’évasion fiscale, ou au fait que les résidents de la Principauté
de Monaco ne paient pas d’impôts).

```{figure} https://live.staticflickr.com/2869/9544834557_b844c48e78_b.jpg
:width: 70%
:name: benjamin-franklin

Représentation de Benjamin Franklin sur les billets de 100 dollars américains
(image de E. Strauhmanis, distribuée sous licence
  [CC BY 2.0](https://creativecommons.org/licenses/by/2.0/))
```

En réalité, le concept d’_incertitude_ est particulièrement difficile à définir,
car il est très nuancé et prend des significations différentes selon le
contexte. Dans ce livre, nous allons nous concentrer sur une incarnation
particulière de ce concept, que nous appellerons _aléa_.
De manière simple (et donc certainement perfectible), on peut identifier
l’aléa comme la propriété qui caractérise toute expérience dont, même répétée
dans les mêmes conditions, le résultat ne peut être déterminé à l’avance.
De façon (pour l’instant) informelle, nous appellerons _événements_ les
affirmations concernant les résultats de ces expériences. La valeur de vérité
de ces affirmations sera donc incertaine.
Un exemple classique d’événement est celui du résultat du lancer de dés
lorsqu’on joue au Monopoly. Un autre exemple, tout aussi classique mais plus
moderne, concerne la valeur de clôture d’un indice boursier. Si nous y
réfléchissons davantage, de nombreux autres exemples nous viennent à l’esprit :
en observant le ciel le matin, y aura-t-il de la pluie aujourd’hui ? Combien de
petits-enfants aura la sœur de mon voisin ? L’année prochaine, parviendrai-je à
passer l’hiver en n’attrapant la grippe qu’une seule fois au plus ? En effet,
il n’est pas difficile de se convaincre que l’aléa (ou, si vous préférez,
le non-déterminisme) traverse notre existence, au point de jouer un rôle
essentiel dans la description de certains aspects fondamentaux de la Nature,
comme la théorie de l’évolution ou la mécanique quantique.

Malgré cela, les gens apprennent plus ou moins rapidement à cohabiter
raisonnablement bien avec l’incertitude : en sortant de chez soi, la plupart
du temps, on sait s’il est judicieux de prendre un parapluie, et certaines
personnes parviennent même à spéculer avec succès en bourse. Cela se produit
parce que nous sommes capables d’_évaluer_ l’incertitude de nombreux événements,
en acceptant le _risque_ que comporte cette évaluation (pour reprendre
l’exemple du ciel nuageux, le risque est d’emporter un parapluie inutilement,
ou de ne pas l’emporter et de se retrouver sous la pluie). Presque toujours,
nous faisons tout cela de manière largement subjective, en nous fondant sur
notre _expérience_. Les mathématiques nous fournissent cependant des outils
qualitatifs et quantitatifs pour aborder ce problème de manière rigoureuse.
En particulier, en combinant le _calcul des probabilités_ et la _statistique_,
nous pouvons modéliser l’incertitude des événements et l’évaluer à l’aide de
l’expérience que nous avons acquise.

Ce livre a justement pour objectif de fournir les bases de ces deux branches
des mathématiques, à travers une approche interactive et centrée sur
l’analyse des données, particulièrement adaptée aux étudiants ayant déjà acquis
des compétences en programmation informatique. Le contenu a notamment été
conçu pour les étudiants en licence d'informatique, mais il s'adapte également
à tout contexte éducatif comportant au moins un enseignement obligatoire en
programmation.

Le travail est organisé en quatre parties :

- la première introduit le langage de programmation Python et les principales
  bibliothèques actuellement utilisées pour l’analyse de données (ce que l’on
  appelle le _Python data science stack_) ;
- la deuxième aborde le thème de la _statistique descriptive_, que l’on peut
  relier de manière informelle au problème d’organiser les observations d’un
  phénomène, puis de les analyser afin d’en extraire de l’_information_
  (la base de l’expérience évoquée plus haut) ;
- la troisième introduit les fondements du _calcul des probabilités_, entendu
  comme une discipline permettant d’évaluer de manière quantitative
  l’incertitude des événements ;
- la quatrième se concentre enfin sur les bases de la _statistique
  inférentielle_, afin de fournir des outils permettant de prendre des décisions
  en condition d’incertitude, à l’aide des outils introduits dans les chapitres
  précédents.

Chacune de ces parties, prise isolément, remplirait un livre entier —
voire plusieurs ! Par conséquent, bien que le matériel soit exploitable sans
avoir à recourir à des sources externes, le livre permet très souvent
d’aborder uniquement les concepts fondamentaux des disciplines concernées.
Cependant, lorsque c’est possible, certains outils avancés, typiques du
_machine learning_, sont brièvement décrits : ils reposent sur l’application
des concepts et outils présentés dans cet ouvrage.

[^citation-franklin]: Dans la source originale (une lettre de B. Franklin au
physicien français Jean-Baptiste Le Roy), cette affirmation apparaît en réalité
comme la fin de la phrase : «... in this world nothing can be said to be
certain, except death and taxes». Il convient toutefois de souligner que,
bien que cette maxime soit attribuée à Benjamin Franklin, il existe des
[sources antérieures]([wiki:Death_and_taxes_(idiom)](https://en.wikipedia.org/wiki/Death_and_taxes_(idiom)))
qui en rapportent certaines variantes.


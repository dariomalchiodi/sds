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

(chap_introduction)=
(par_franklin-law)=
(sec_franklin-law)=
# Introduction

> En ce monde, rien ne peut être tenu pour certain,<br/>
> sauf la mort et les impôts
>
> -- Benjamin Franklin

La citation qui ouvre cette section provient d’une lettre écrite en 1789 par
Benjamin Franklin (voir {numref}`benjamin-franklin`), l’un des Pères
fondateurs des États-Unis d’Amérique. Si l’on accepte ce principe, souvent
appelé _loi de Franklin_ [^citation-franklin], alors il vaut la peine
d’étudier l’incertitude, car pratiquement tout est incertain. Ironiquement,
même la loi de Franklin n’est pas entièrement au-dessus de tout doute : il
suffit de penser, par exemple, à l’évasion fiscale, ou au fait que les
résidents de la Principauté de Monaco ne paient pas d’impôt sur le revenu.

```{figure} https://live.staticflickr.com/2869/9544834557_b844c48e78_b.jpg
:width: 70%
:name: benjamin-franklin

Portrait de Benjamin Franklin sur les billets de 100 dollars américains
(image d’E. Strauhmanis, distribuée sous licence
{extlink}`CC BY 2.0 <https://creativecommons.org/licenses/by/2.0/>`)
```

En réalité, le concept d’_incertitude_ est difficile à définir, car il possède
de multiples facettes et prend des sens différents selon le contexte. Dans ce
livre, je me concentrerai sur une acception particulière du terme, souvent
désignée par le mot _hasard_. En termes simples &mdash; et donc forcément
imparfaits &mdash;, on peut identifier le hasard comme la propriété qui
caractérise une expérience qui, même répétée dans les mêmes conditions,
produit un résultat impossible à prévoir a priori. De manière pour l’instant
informelle, j'appellerai _événements_ les énoncés portant sur les résultats de
ces expériences. Leur valeur de vérité est donc incertaine. Un exemple
classique d’événement est l’issue d’un lancer de dé lors d’une partie de
Monopoly. Un autre exemple, tout aussi classique mais plus moderne, concerne la
valeur de clôture d’un indice boursier. Mais on pourrait en ajouter bien
d’autres : pleuvra-t-il aujourd’hui si, en regardant le ciel le matin, nous
voyons des nuages à l’horizon ? Combien de petits-enfants la sœur de mon voisin
de palier aura-t-elle ? L’an prochain, réussirai-je à traverser la saison de la
grippe en tombant malade au plus une fois ? En réalité, il n’est pas difficile
de constater que le hasard &mdash; ou, si vous préférez, le non-déterminisme
&mdash; imprègne la vie quotidienne. Il joue aussi un rôle essentiel dans la
description de certains aspects fondamentaux de la Nature, comme la théorie de
l’évolution ou la mécanique quantique.

Malgré cela, nous apprenons assez vite à vivre raisonnablement bien avec
l’incertitude : lorsque nous sortons de chez nous, nous savons presque toujours
s’il vaut la peine d’emporter un parapluie, et certaines personnes parviennent
même à spéculer avec succès sur les marchés financiers. Cela tient au fait que
nous sommes capables d’_évaluer_ l’incertitude de nombreux événements, en
acceptant le _risque_ que cette évaluation implique. Pour reprendre l’exemple
du ciel nuageux, le risque est soit d’emporter inutilement un parapluie, soit
de finir sous la pluie sans en avoir pris un. En général, les décisions que
nous prenons reposent sur des critères largement subjectifs fondés sur notre
_expérience_. Les mathématiques fournissent toutefois des outils permettant
d’aborder ce problème avec rigueur. En particulier, en combinant la _théorie
des probabilités_ et la _statistique_, nous pouvons modéliser l’incertitude des
événements et l’évaluer à partir de l’expérience acquise.

Le but de ce livre est précisément de fournir les bases de ces deux branches
des mathématiques, en adoptant une approche interactive centrée sur l’analyse
de données et destinée à un public ayant déjà acquis des
compétences en programmation informatique. Le contenu a été conçu pour les
étudiantes et étudiants des cursus d’informatique, mais il convient tout à fait
à tout parcours d’études comportant au moins un cours obligatoire de
programmation.

Le travail est organisé en quatre parties :

- la première présente le langage de programmation Python et son _data science
  stack_, c’est-à-dire les principales bibliothèques utilisées pour l’analyse
  des données ;
- la deuxième traite de _statistique descriptive_, qui fournit des outils pour
  organiser et analyser les observations d’un phénomène afin d’en extraire de
  l’_information_ (la base de l’expérience mentionnée plus haut) ;
- la troisième décrit les fondements de la _théorie des probabilités_, comprise
  comme une discipline permettant de quantifier l’incertitude des événements ;
- la quatrième et dernière partie est consacrée aux fondements de la
  _statistique inférentielle_, en fournissant des outils qui aident à prendre
  des décisions en situation d’incertitude à l’aide des méthodes introduites
  dans les parties précédentes.

Chacune de ces parties, prise isolément, remplirait un manuel entier &mdash;
voire davantage. Pour cette raison, je me limiterai aux concepts fondamentaux
des disciplines considérées, tout en essayant de rendre le livre utilisable
sans devoir recourir à des sources extérieures. Lorsque cela sera possible,
j’introduirai aussi certains aspects plus avancés, typiques du _machine
learning_, fondés sur les concepts et les outils présentés dans les chapitres
précédents.

[^citation-franklin]: Cet aphorisme est généralement attribué à une phrase
contenue dans une lettre de B. Franklin au physicien français Jean-Baptiste Le
Roy: « ... in this word nothing can be said to be certain, except death and
taxes ». Il convient toutefois de souligner que, bien que cette formule soit
attribuée à Benjamin Franklin, il existe des {extlink}`sources antérieures
<https://en.wikipedia.org/wiki/Death_and_taxes_(idiom)>` qui en donnent
plusieurs variantes.


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

(sec:apprendre-et-programmer)=
# Apprendre <span class="ast">\*</span>et<span class="ast">\*</span> programmer

Comme décrit dans le paragraphe précédent, j’introduirai les concepts en les
accompagnant (ou en les précédant) d’exemples. Lorsque c’est possible, je
montrerai aussi des _implémentations_ en utilisant un langage relativement
moderne : en particulier, je ferai référence à [Python](https://www.python.org)
et à l’écosystème _data science_ qui lui est associé, composé des paquets
largement utilisées, au moment où j’écris, par la communauté open source dédiée
à l’analyse de données[^paquets]. Il est donc fortement recommandé de posséder
des connaissances de base en programmation.
```{margin}
Ce livre est l’évolution d’une série de notes de cours conçus pour des
étudiants de deuxième année de licence en informatique ; je ferai donc
référence au niveau de programmation que l’on acquiert pendant la première
année dans ces cursus ou dans des cursus similaires.
```

Le {ref}`chap:intro-python` contient une description de niveau intermédiaire à
avancé des fonctionnalités de Python qui sont utilisées, et peut servir de
remise à niveau pour celles et ceux qui savent déjà programmer mais ne
connaissent pas ce langage. Une lecture de ce chapitre est toutefois
recommandée à tout le monde, afin de se familiariser avec les conventions
adoptées dans le code présenté.

Ce livre a été écrit avec une technologie qui permet d’intégrer du contenu
généré par l’exécution de code Python. Ce code est caché lorsqu’il sert
simplement à produire des tableaux ou des graphiques, tandis qu’il est affiché
de manière explicite quand le lecteur est guidé à travers l’implémentation d’un
ou plusieurs concepts expliqués dans le texte. Dans ces cas, un lien
« Afficher le code » permet au lecteur d’afficher ou masquer le code caché.
Je vous encourage vivement à profiter de cette possibilité : lire un texte de
manière passive apporte peu de bénéfices, et exécuter du code sans y réfléchir
n’a pas beaucoup de sens non plus ; ce qui compte, c’est de l’analyser, le
comprendre et le modifier (même des changements faits uniquement pour mieux en
saisir le fonctionnement sont utiles). En bref, _jouez avec_, dans le véritable
esprit _hacker_ &mdash; entendu dans le sens original du terme[^hacker]. En
réalité, on peut aussi explorer le livre sans forcément tout comprendre du code
ni devoir l’exécuter : comme montré dans {ref}`sec:apercu-general`, certaines
paragraphes incluent des éléments interactifs spécialement conçus pour aider à
mieux saisir les concepts abordés.

```{margin}
Les parties interactives s’appuient sur [PyScript](https://pyscript.net/), une
technologie qui permet d’exécuter du code Python dans les navigateurs web
modernes. Elle ne nécessite ni installation ni configuration manuelle, mais
demande une connexion internet active et un navigateur compatible avec
WebAssembly (comme Chrome, Firefox, Edge, Safari, ou tout navigateur basé sur
Chromium, à condition qu'ils soient à jour).
```

Très souvent, j’essaie de guider le lecteur dans une implémentation effective
des outils fondamentaux, surtout dans la première partie, portant sur les
statistiques descriptives. Le résultat obtenu ne doit pas être considéré comme
équivalent à celui des paquets professionnelles : d’un côté, l’objectif est de
se concentrer sur les aspects fondamentaux pour faciliter la compréhension d’un
ou plusieurs concepts ; de l’autre, ces implémentations ne sont pas destinées à
un usage professionnel. C’est un peu comme un développeur qui apprend à coder
les principaux algorithmes de tri à la main (et qui serait capable de le faire
en cas de besoin), mais qui utilise ensuite des paquets fiables, optimisées et
bien testées, car cela dépasse ce qu’une personne seule peut raisonnablement
produire. Dans cet esprit, juste après les implémentations « faites maison »,
les lecteurs sont orientés vers l’utilisation de paquets à l’état de l’art.

En principe, même ceux qui ne savent pas programmer peuvent lire ce livre, en
sautant simplement les parties contenant, décrivant ou discutant du code. Mais
dans ce cas, il faut bien peser le risque de ne pas assimiler les contenus de
manière optimale, étant donné que le livre mêle texte et code dans une large
mesure. À ces lecteurs, je conseille d’envisager des ouvrages plus classiques,
comme :

- Statistique et probabilités, de Jean-Pierre Lecoutre {cite:p}`lecoutre`,
- Mini Manuel de probabilités et statistique : Cours + QCM, de Françoise
  Couty-Fredon, Jean Debord etand Daniel Fredon {cite:p}`coutyfredon`.

J’adresse également un avertissement à ceux qui ne savent pas programmer et
seraient tentés de lire ce livre pour apprendre à le faire, tout en découvrant
en même temps l’analyse de données. Ce livre __n’est pas__ un manuel pour
apprendre à programmer, mais plutôt un livre pour apprendre _en programmant_, 
car il utilise la programmation comme outil pour enrichir l’apprentissage d’une
autre matière. On dit qu’on ne comprend vraiment quelque chose que lorsqu’on
est capable de l’expliquer à sa grand-mère[^cite-granny] : je fais mienne cette
maxime, en espérant ne pas trop la détourner, en disant qu’on ne comprend
vraiment un concept technique que si on est capable de l’implémenter par un
programme. Mais pour suivre cette approche, il faut déjà savoir écrire du
logiciel, ce qui demande du temps, de l’énergie et du matériel dédié. Là encore,
plusieurs ouvrages peuvent être utiles, comme :

- Python 3 &mdash; Les fondamentaux du langage, de Sébastien Chazallet
  {cite:p}`chazallet`,
- Programmer en langage C : Cours et exercices corrigés, de Claude Delannoy
  {cite:p}`delannoy`.

J’ai délibérément inclus ici deux livres assez récents, chacun dédié à un
langage différent : l’idée est bien d’apprendre les bases de la programmation,
pas les subtilités d’un langage en particulier. Enfin, ce paragraphe ne
mentionne que des livres écrits en français, mais il ne faut pas négliger la
possibilité d’étudier à partir de la version originale d’un ouvrage, si
celle-ci est en anglais, ou s’il en existe une version en anglais pensée pour
des étudiants non natifs anglophones.

````{margin}
```{figure} ../../_static/img/whistle.jpg
---
name: fig-whistle
height: 100px
---
Un sifflet Cap’n Crunch Bo’sun (image du Heinz Nixdorf MuseumsForum, distribuée sous licence [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/))
```
````


[^paquets]: Le dépôt associé à ce livre contient un
[fichier](https://github.com/dariomalchiodi/sds/blob/main/requirements.in)
qui liste toutes les paquets utilisées pour générer les contenus, y compris
celles nécessaires à l’exécution du code.

[^hacker]: Le terme _hacker_ est aujourd’hui souvent utilisé dans le langage
courant avec une connotation négative, le rapprochant de quelqu’un qui poursuit
des objectifs malveillants en écrivant ou en modifiant du logiciel, ou plus
généralement en exploitant des failles de sécurité pour détourner des
technologies informatiques existantes. En réalité, l’usage moderne du terme en
anglais remonte aux alentours de 1960, avec une connotation plus neutre, et pas
forcément liée à l’informatique : il désignait une personne ayant le talent de
comprendre en profondeur le fonctionnement d’un système, au point de pouvoir le
contrôler et l’utiliser d’une manière différente de celle pour laquelle il
avait été conçu. Pour donner un exemple célèbre, l’un des premiers hacks connus 
&mdash; bien qu’illégal &mdash; consistait à utiliser un « Cap’n Crunch Bo’sun
Whistle » (un sifflet offert dans les boîtes de céréales d’une marque connue,
illustré en {numref}`fig-whistle`) pour passer des appels interurbains ou
internationaux gratuits depuis certains téléphones publics aux États-Unis. L’un
des premiers foyers de la contre-culture hacker fut le Massachusetts Institute
of Technology (MIT) : la première trace écrite du terme « hacking » se trouve
dans le compte rendu d’une réunion de 1955 du
[Tech Model Railroad Club](http://tmrc.mit.edu/), un club d’étudiants
passionnés de modélisme ferroviaire. Ce n’est que plus récemment que le terme a
été pleinement associé au monde de l’informatique.

[^cite-granny]: Il est difficile de retracer l’auteur exact de cette maxime :
certains l’attribuent à Einstein, d’autres à Feynman ou à Rutherford (on dirait
donc qu’il y a consensus sur le contexte des sciences physiques) ; il existe
aussi des variantes où la grand-mère est remplacée par un enfant, ou &mdash;
pour une raison inconnue &mdash; même par un barman.


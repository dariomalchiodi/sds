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

(sec_apprendre-et-programmer)=
# Apprendre <span class="ast">\*</span>et<span class="ast">\*</span> programmer

Comme indiqué dans la section précédente, j’introduirai les concepts en les
accompagnant, ou parfois même en les faisant suivre, d’exemples concrets.
Lorsque cela sera possible, je montrerai aussi des _implémentations_ écrites
dans un langage relativement moderne. J’utiliserai {extlink}`Python
<https://www.python.org>` et son _data science stack_, constitué des
bibliothèques principalement utilisées par la communauté open source qui se
consacre à l’analyse de données[^paquets] (au moment où ce livre est écrit).
Pour suivre le livre efficacement, une connaissance de base de la programmation
est donc vivement recommandée.

```{margin}
Ce livre est l’évolution d’une série de notes de cours conçues pour des
étudiantes et étudiants de deuxième année de licence en informatique. Il
suppose donc les compétences en programmation que l’on acquiert généralement en
première année dans ces cursus, ou dans des parcours similaires.
```

Le {ref}`chap_introduction-python` fournit une présentation de niveau
intermédiaire à avancé des fonctionnalités de Python que j’utilise dans le
livre. Il est conçu pour permettre à celles et ceux qui savent déjà
programmer, mais ne connaissent pas encore ce langage, de se mettre à niveau.
La lecture de ce chapitre est de toute façon recommandée, car elle permet de
se familiariser dès le départ avec les conventions que j’emploie dans le code.

```{margin}
Les composants interactifs reposent sur {extlink}`PyScript
<https://pyscript.net/>`, une technologie qui permet d’exécuter du code Python
dans les navigateurs web modernes. Elle a l’avantage de ne nécessiter aucune
installation ni configuration manuelle, mais elle requiert une connexion
internet active et un navigateur compatible avec WebAssembly (comme Chrome,
Firefox, Edge, Safari et les navigateurs fondés sur Chromium).
```

Ce livre a été écrit avec une technologie qui permet d’intégrer du contenu
généré par l’exécution de code Python. Lorsque je guide les lectrices et
lecteurs dans l’implémentation d’un ou plusieurs concepts, le code est montré
explicitement. En revanche, lorsqu’il sert seulement à produire des éléments
comme des tableaux ou des graphiques, il est masqué, mais un lien « Afficher le
code » permet de l’afficher[^hidden-code]. J’encourage fortement à profiter de
cette possibilité : tout comme lire passivement un texte a peu de sens,
exécuter du code sans y réfléchir présente un intérêt limité. Ce qui compte,
c’est de l’analyser, de le comprendre et de le modifier afin d’en saisir plus
profondément le fonctionnement &mdash; en bref, de _jouer avec_, dans le sens
originel du terme _hacker_[^hacker]. En tout cas, une partie du contenu est
interactive, comme on le voit par exemple dans {ref}`sec_apercu-general` :
manipuler ces éléments, sans même lire le code, est précisément destiné à
faciliter la compréhension des concepts introduits.

Très souvent, je guiderai les lectrices et lecteurs dans l’implémentation
pratique des outils fondamentaux, en particulier dans la première partie
consacrée à la statistique descriptive. Il est important de souligner que ces
implémentations ne sont pas destinées à remplacer des bibliothèques
professionnelles. Leur rôle est plutôt d’attirer l’attention sur les aspects
essentiels d’un ou de plusieurs concepts afin d’en faciliter la compréhension.
Le raisonnement qui sous-tend cette approche est analogue à l’idée selon
laquelle les développeuses et développeurs de logiciels devraient avoir appris
à écrire eux-mêmes les principaux algorithmes de tri (et, si besoin, être
encore capables de le faire), tout en utilisant dans la pratique
professionnelle les implémentations disponibles dans des bibliothèques
optimisées et soigneusement validées, à un niveau qu’il serait difficile
d’atteindre seul. Dans cet esprit, les implémentations « maison » seront
immédiatement suivies de l’utilisation de bibliothèques à l’état de l’art.

Les personnes qui n’ont aucune expérience de la programmation peuvent malgré
tout lire ce livre, en sautant simplement les parties qui contiennent,
décrivent ou discutent du code. Dans ce cas, cependant, elles doivent être
conscientes du risque de ne pas assimiler pleinement le contenu, puisque une
grande partie de l’exposé alterne entre texte et code. Dans une telle
situation, je recommande d’envisager des ouvrages adoptant une approche plus
traditionnelle, comme :

- Statistique et probabilités, de Jean-Pierre Lecoutre {cite:p}`lecoutre`,
- Mini Manuel de probabilités et statistique : Cours + QCM, de Françoise
  Couty-Fredon, Jean Debord etand Daniel Fredon {cite:p}`coutyfredon`.

- Probability and Statistics for Engineering and the Sciences, de Sheldon Ross
  {cite:p}`ross`,
- Introduction to Statistics, de Marylin K. Pelosi, Theresa M. Sandifer,
  Paola Cerchiello et Paolo Giudici {cite:p}`pelosi`.

Je tiens aussi à mettre en garde celles et ceux qui envisagent d’utiliser ce
livre pour apprendre à programmer tout en découvrant l’analyse de données. Ce
livre _n’est pas_ un manuel pour apprendre à programmer. C’est plutôt un livre
pour apprendre _en utilisant_ la programmation, c’est-à-dire en écrivant du
code afin de rendre plus robuste le processus d’apprentissage d’une autre
matière. On dit parfois que l’on n’a vraiment compris quelque chose que
lorsqu’on est capable de l’expliquer à sa grand-mère[^cite-granny]. J’irai un
pas plus loin en disant qu’on ne maîtrise vraiment un concept technique que si
l’on est capable de l’implémenter en écrivant un programme. Pour suivre cette
philosophie, il faut toutefois déjà savoir écrire du logiciel, et c’est une
compétence qui demande du temps, de l’énergie et des supports pédagogiques
dédiés. Pour les personnes qui partent de zéro, je recommande quelques textes
de référence, plus ou moins récents :

- Python 3 &mdash; Les fondamentaux du langage, de Sébastien Chazallet
  {cite:p}`chazallet`,
- Programmer en langage C : Cours et exercices corrigés, de Claude Delannoy
  {cite:p}`delannoy`.

J’ai délibérément choisi des livres consacrés à des langages différents afin de
souligner que ce qui compte vraiment n’est pas de maîtriser les détails d’un
langage particulier, mais de comprendre les fondements de la programmation en
tant que discipline autonome. Enfin, même lorsqu’il existe des traductions, il
vaut toujours la peine de considérer l’édition originale en anglais : elle est
souvent plus à jour et écrite en pensant aussi aux personnes non anglophones.
Cela aide également à se familiariser avec le vocabulaire technique et à
communiquer plus facilement sur les canaux en ligne consacrés à la
programmation, qui constituent une ressource précieuse pour résoudre des
problèmes.

````{margin}
```{figure} ../../_static/img/whistle.jpg
---
name: fig-whistle
height: 100px
---
Un sifflet Cap’n Crunch Bo’sun (image du Heinz Nixdorf MuseumsForum,
distribuée sous licence {extlink}`CC BY-NC-SA 4.0
<https://creativecommons.org/licenses/by-nc-sa/4.0/>`)
```
````


[^paquets]: Le dépôt associé à ce livre contient un
{extlink}`fichier <https://github.com/dariomalchiodi/sds/blob/main/requirements.in>`
qui répertorie toutes les bibliothèques utilisées pour générer les contenus,
y compris celles qui sont nécessaires à l’exécution du code.

[^hidden-code]: Il est utile de se rappeler que le code caché peut contenir des
détails techniques liés à la génération de contenu destiné à être affiché dans
des pages web (comme des éléments HTML ou des styles CSS). Par conséquent, il
n’est pas écrit de la même manière que du code conçu pour l’analyse de données
dans des environnements de travail traditionnels : sa structure répond à des
besoins de présentation et d’interactivité, plutôt qu’à des objectifs
analytiques.

[^hacker]: Le terme _hacker_ est aujourd’hui souvent utilisé dans le langage
courant avec une connotation négative, le rapprochant de quelqu’un qui poursuit
des objectifs malveillants en écrivant ou en modifiant du logiciel, ou en
exploitant des failles de sécurité pour faire un mauvais usage des technologies
informatiques. À l’origine, pourtant, ce n’était pas le cas. En anglais
moderne, le terme apparaît autour de 1960 avec une connotation plus neutre,
pas nécessairement liée à l’informatique : il désignait une personne capable de
comprendre un système si profondément qu’elle pouvait le contrôler et l’adapter
à des usages différents de ceux prévus par ses concepteurs. L’un des premiers
_hacks_ célèbres &mdash; bien qu’illégal &mdash; consistait à utiliser le « Cap’n
Crunch Bo’sun Whistle » (un sifflet trouvé dans des boîtes d’une célèbre marque
de céréales, illustré en {numref}`fig-whistle`) pour passer gratuitement des
appels interurbains et internationaux depuis certains téléphones publics aux
États-Unis. L’un des lieux où la contre-culture hacker a commencé à se former
fut le Massachusetts Institute of Technology (MIT) : la plus ancienne trace
écrite du mot « hacking » apparaît dans le compte rendu d’une réunion de 1955
du {extlink}`Tech Model Railroad Club <http://tmrc.mit.edu/>`, un groupe
d’étudiantes et d’étudiants passionnés de modélisme ferroviaire. L’association
directe avec l’informatique n’est venue que plus tard.

[^cite-granny]: Il est difficile de retracer l’auteur exact de cette maxime :
certains l’attribuent à Einstein, d’autres à Feynman et d’autres encore à
Rutherford ; il semble donc y avoir au moins un certain consensus quant à son
ancrage dans les sciences physiques. Dans sa version la plus connue,
toutefois, cette formule véhicule une vision assez stéréotypée des
grand-mères, probablement parce qu’elle circule depuis longtemps. Il en existe
en réalité plusieurs variantes : certaines tout aussi discutables, où la
grand-mère est remplacée pour une raison quelconque par un barman, et d’autres
où c’est un enfant qui prend sa place.


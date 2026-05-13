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

(chap_combinatoire)=
# Combinatoire

La _combinatoire_ est la branche des mathématiques qui s'intéresse à déterminer
le nombre de façons dont les éléments d'un ensemble fini peuvent être groupés ou
ordonnés. Comme on peut l'intuiter, ce nombre ne dépend pas de la nature des
objets considérés : qu'il s'agisse d'objets tangibles (comme des fruits ou des
bicyclettes) ou d'entités abstraites (comme les pouvoirs d'un super-héros ou les
couleurs des murs d'un bureau), la logique permettant de dénombrer leurs
configurations reste la même.

Pour aborder correctement un problème de dénombrement, il est important de
répondre à trois questions fondamentales :

- Le même élément peut-il être choisi plus d'une fois ?
- Tous les éléments de départ sont-ils distincts, ou certains sont-ils
  _indiscernables_ les uns des autres ?
- L'ordre dans lequel les éléments sont sélectionnés importe-t-il ou non ?

Une fois ces aspects clarifiés, le nombre de configurations possibles dépend en
général de seulement deux paramètres : la taille $n$ de l'ensemble de départ et
le nombre $k$ d'éléments que l'on souhaite sélectionner.

Une métaphore particulièrement efficace est la suivante : imaginez affecter $n$
_objets_ (tangibles ou non) à $k$ _cases_ disponibles. Dans les sections qui
suivent, j'analyserai les principaux modes de groupement et d'ordonnancement, et
pour chacun d'eux je montrerai comment dériver la formule permettant de calculer
le nombre de cas possibles.

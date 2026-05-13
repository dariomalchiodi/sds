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

(chap_theorie-ensembles)=
# Théorie des ensembles

En 1895, Georg Cantor proposa une définition capable de saisir avec une
précision remarquable l'idée intuitive d'ensemble : «par multiplicité ou
ensemble j'entends tout _multiple_ que l'on peut penser comme _un_»
[^citation-cantor]. Selon cette conception, un ensemble est un regroupement
d'objets distincts partageant une propriété commune. Peu après, Cantor
affina sa définition : «par "ensemble" nous entendons toute collection $M$
d'objets $m$ définis et distincts de notre intuition ou de notre pensée —
appelés "éléments" de $M$» {cite}`cantor-1895`.

Quelques années plus tard, la communauté mathématique découvrit que cette
approche, aujourd'hui connue sous le nom de _théorie naïve des ensembles_,
recèle des pièges logiques et des paradoxes ; pour les éviter, il fut
nécessaire de refonder la matière sur un système axiomatique beaucoup plus
rigoureux {cite}`suppes`. Malgré cela, dans ce livre j'ai choisi d'adopter
la perspective naïve : bien que moins formelle, elle me permet de maintenir
l'exposé simple et centré sur les objectifs pédagogiques de cet ouvrage,
sans alourdir le propos. D'ailleurs, comme le fait remarquer Rudy Rucker,
il est significatif que le mot _set_ (ensemble) détienne l'entrée la plus
longue parmi tous les termes de l'_Oxford English Dictionary_
{cite}`rucker`.

[^citation-cantor]: Traduit de l'original : "Unter einer 'Mannigfaltigkeit'
oder 'Menge' verstehe ich nämlich allgemein jedes Viele, welches sich als
Eines denken lässt" {cite}`cantor-1883`. L'italique dans la traduction
française a été ajouté par l'auteur pour souligner le contraste conceptuel
entre pluralité et unité.

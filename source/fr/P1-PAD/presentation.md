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

# Introduction

La première partie de ce livre présente quelques outils de base pour l'analyse
automatisée de jeux de données de petite à moyenne taille[^big-data], à l'aide
d'un ordinateur. Maîtriser ces outils &mdash;ainsi que la capacité à les
appliquer efficacement dans différents contextes de data science&mdash; est
aujourd'hui essentiel pour analyser et interpréter la grande variété de données disponibles, et les utiliser comme support à la prise de décision.

Parmi les outils essentiels, on trouve :

- un langage de programmation, qui permet d'écrire des instructions pour
  automatiser le traitement des données ;
- une bibliothèque pour la gestion structurée des jeux de données.

Dans ce livre, nous utiliserons Python et Pandas à ces fins, présentés
respectivement dans le {ref}`chap:intro-python` et le {ref}`chap:pandas`. Bien
qu'il existe de nombreuses alternatives valables, ces deux technologies
constituent aujourd'hui une partie centrale de l'écosystème de l'analyse de
données, aussi bien dans le monde académique que professionnel.

[^big-data]: Un jeu de données est considéré comme de petite taille lorsqu'il
peut être traité avec les ressources disponibles sur un seul ordinateur. Dans
le cas le plus simple &mdash;celui qui est abordé dans ce livre&mdash;
l'ensemble des données tient entièrement dans la mémoire centrale de la
machine. De manière plus générale, on parle encore de données «gérables
localement» si le jeu de données peut être stocké sur disque et chargé
progressivement en mémoire vive, par exemple un enregistrement à la fois.
Lorsque la taille des données dépasse largement la capacité de stockage
disponible (en gros, plus d’un téraoctet avec le matériel actuellement
disponible), on entre dans le domaine des mégadonnées, qui requiert des
approches computationnelles différentes de celles de l’analyse classique.

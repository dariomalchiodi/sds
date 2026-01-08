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

(chap_introduction-python)=
# Introduction à Python

> Beautiful is better than ugly.<br/>
> Explicit is better than implicit.<br/>
> Simple is better than complex.<br/>
> Complex is better than complicated.<br/>
> Flat is better than nested.<br/>
> Sparse is better than dense.<br/>
> Readability counts.<br/>
> Special cases aren't special enough to break the rules.<br/>
> Although practicality beats purity.<br/>
> Errors should never pass silently.<br/>
> Unless explicitly silenced.<br/>
> In the face of ambiguity, refuse the temptation to guess.<br/>
> There should be one-- and preferably only one --obvious way to do it.<br/>
> Although that way may not be obvious at first unless you're Dutch.<br/>
> Now is better than never.<br/>
> Although never is often better than *right* now.<br/>
> If the implementation is hard to explain, it's a bad idea.<br/>
> If the implementation is easy to explain, it may be a good idea.<br/>
> Namespaces are one honking great idea -- let's do more of those!<br/>
>
> --- The Zen of Python, by Tim Peters[^zen]

Ce chapitre décrit brièvement les principaux outils permettant d'analyser des
données de manière exploratoire en utilisant
[Python](https://www.python.org){.external} comme langage de programmation, les
[notebooks](https://fr.wikipedia.org/wiki/Notebook_(programmation)){.external}
pour écrire et exécuter le code, ainsi que les principales bibliothèques du
_Python data science stack_, qui seront introduites au fur et à mesure qu'elles
se révéleront nécessaires.
```{margin}
Les _notebooks_ peuvent être exécutés dans divers environnements de
développement : au moment où ce livre a été rédigé, parmi les plus répandus
figurent [Jupyter](https://jupyter.org/){.external} et [Visual Studio
Code](https://code.visualstudio.com/){.external}, qui présentent aussi
l'avantage d'être gratuits, bien qu'il existe d'autres alternatives.
```

Tous les outils mentionnés appartiennent à la catégorie <a
href="https://fr.wikipedia.org/wiki/Free/Libre_Open_Source_Software"
target="_blank">FLOSS</a> et sont donc distribués sous des licences permettant,
entre autres, leur usage libre.
```{margin}
L'acronyme FLOSS signifie « Free/Libre Open Source Software »
```

Cette présentation s'adresse à des étudiants ayant déjà une certaine
familiarité avec la programmation informatique et, en particulier, à ceux qui
maîtrisent au moins un langage de programmation adoptant une approche
impérative et procédurale. J'introduirai en revanche certaines notions de
base du paradigme de programmation orientée objet, nécessaires pour utiliser
le _data science stack_ de Python et qui ne sont pas toujours à la portée de
ceux qui commencent l'étude de cette discipline.

[^zen]: Le « Zen de Python » est le nom donné officiellement à $19$ lignes
directrices pour écrire du code Python de manière à en exploiter l'élégance et
les structures syntaxiques, plutôt que de traduire de façon littérale la
syntaxe d'autres langages&mdash;ce qu'on appelle, en jargon, « écrire du code
pythonique ». Ces lignes directrices, dans le domaine public, ont été rédigées
en 1999 par Tim Peters, l'un des principaux contributeurs de Python. En plus
d'être publiées dans une [section
dédiée](https://peps.python.org/pep-0020/){.external} des _Python Enhancement
Proposals_, elles s'affichent automatiquement en exécutant la ligne de code
Python `import this`.

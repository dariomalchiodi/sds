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

```{raw} html

<script type="module" src="https://pyscript.net/releases/2025.5.1/core.js"></script>
```

(sec:conventions)=
# Conventions

Comme mentionné dans le paragraphe précédent, je vais souvent insérer du code
dans le texte, non pas tant pour qu’il soit exécuté, mais dans le but 
d'illustrer des concepts (par exemple, pour montrer que les littéraux `true` et
`false` sont les seules valeurs possibles du type de données `bool`). Dans ce
cas, j’utiliserai une police à chasse fixe avec une couleur différente de celle
du texte principal. Quand il sera nécessaire de montrer une ou plusieurs lignes
de code destinées à être exécutées lors de la lecture, ces lignes apparaîtront
dans un encadré qui rappelle une _cellule de code_ typique d’un _notebook_.
Là encore, j’utiliserai une police à chasse fixe, mais la coloration syntaxique
mettra en évidence certains éléments du code (comme les variables, les
littéraux, les mots-clés, etc.), à la manière des éditeurs modernes de type
IDE. Le code sera aussi visuellement séparé du texte principal, comme dans
l’exemple suivant.
```{margin}
Il est courant d’utiliser une police à chasse fixe (où chaque glyphe a la même
largeur) pour afficher le code, les entrées et les sorties, pour diverses
raisons qui en améliorent la lisibilité, comme la facilité d’indenter les
instructions ou la réduction du risque de confondre des caractères similaires
comme 1 et l.
```

```python
age = 24
print(age <= 42)
```

En général, j’afficherai le résultat de l’exécution dans une
_cellule de sortie_ spécifique, placée juste après celle contenant le code,
comme ci-dessous.

```python
print(age <= 42)
```

Enfin, j’utiliserai un style distinctif pour signaler certains encadrés
contenant des notions spécifiques, comme illustré ci-dessous.

```{admonition} _
:class: naming
Cet encadrés contient des remarques sur la terminologie utilisée dans un domaine
particulier, ou des variantes par rapport aux expressions introduites.
```

```{prf:definition}
:label: marquplace-definition
:class: no-number
Cet encadré définit formellement un ou plusieurs concepts.
```
```{margin}
Les définitions, exemples, etc. seront généralement numérotés, et souvent
accompagnés d’un nom spécifique entre parenthèses.
```

```{prf:example}
:label: marquplace-esempio
:class: no-number
Cet encadré contient un exemple.
```

````{prf:theorem}
:label: marquplace-teorema
:class: no-number
Cet encadré présente l’énoncé d’un théorème.
````

```{prf:corollary}
:label: marquplace-corollario
:class: no-number
Cet encadré contient l’énoncé d’un corollaire.
```

```{prf:lemma}
:class: no-number
:label: marquplace-lemma
Cet encadré contient l’énoncé d’un lemme.
```

```{admonition} _
:class: myproof
Cet encadré contient la démonstration d’un théorème, corollaire ou lemme. Dans
certains cas, je choisirai de ne pas inclure la démonstration, notamment
lorsque le résultat théorique est important mais que sa présentation nécessite
des connaissances mathématiques avancées.
```

```{note}
Ce type de encadré met en valeur certains aspects secondaires que je préfère
intégrer dans le texte plutôt que dans des notes de bas de page.
```

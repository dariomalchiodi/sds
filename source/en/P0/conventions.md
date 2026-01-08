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

(sec_conventions)=
# Conventions

As mentioned in the previous paragraph, I will often mix the text with code,
not so much for the purpose of executing it, but more for illustrative purposes
(for example, to indicate the literals `true` and `false` as the only possible
values for the `bool` data type). In such cases, I will use a monospaced font
with a color different from that of the main text. When instead it is necessary
to show one or more lines of code intended to be executed by the reader, I will
display these lines inside a box that resembles the typical _code cell_ in a
_notebook_. Here too, I will use a monospaced font, but the text will be
color-highlighted to emphasize specific elements in the code (such as
variables, literals, keywords, and so on, similar to what is commonly done by
modern IDEs). Moreover, the code will appear separated from the main text, as
in the following example.

```{margin}
It is common practice to use a monospaced font (in which all glyphs used to
represent a character have the same width) for displaying code, input, and
output, for a number of reasons that enhance readability, such as easier
indentation of statements and reduced risk of confusing similar characters
like 1 and l.
```

```python
age = 24
print(age <= 42)
```

As a rule, I will display the output resulting from execution inside a
dedicated _output cell_, placed directly below the corresponding code cell and
shown as follows.


```python
print(age <= 42)
```

Finally, I will use a specific style to highlight certain elements within the
text, as exemplified below.

```{admonition} _
:class: naming
This type of area contains notes related to the nomenclature used in a
particular context, or to the description of alternative terms compared to
those introduced.
```

```{prf:definition}
:label: placeholder-definition
:class: no-number
This area formally defines one or more concepts.
```
```{margin}
Definitions, examples, and so on will typically be numbered, and often
accompanied by a specific name enclosed in parentheses.
```

```{prf:example}
:label: placeholder-example
:class: no-number
This area contains an example.
```

````{prf:theorem}
:label: placeholder-theorem
:class: no-number
This area contains the statement of a theorem.
````

```{prf:corollay}
:label: placeholder-corollary
:class: no-number
This area contains the definition of a corollary.
```

```{prf:lemma}
:class: no-number
:label: segnaposto-lemma
This area contains the definition of a lemma.
```


```{admonition} _
:class: myproof
This area includes the proof of a theorem, corollary, or lemma. For some
theorems, I will omit the corresponding proof. This will happen when it is
important to introduce a relevant theoretical result, although its proof
requires advanced mathematical knowledge.
```

```{note}
This type of area highlights some secondary aspects that I prefer to emphasize
in the main text, rather than describe in footnotes.
```
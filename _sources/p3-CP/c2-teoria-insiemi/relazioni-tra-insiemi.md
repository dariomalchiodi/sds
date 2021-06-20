---
jupytext:
  formats: ipynb,md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.10.3
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

```{code-cell} ipython3
:tags: [remove-cell]

%matplotlib inline
%run init.py
```

# Relazioni tra insiemi

A partire dalla nozione di _sottoinsieme_ è possibile derivare una serie di relazioni tra insiemi di carattere generale; più precisamente:

```{margin}
in alternativa si dice che $T$ è un _sovrainsieme_ di $S$ e si scrive $T \supseteq S$
```
- quando ogni elemento sappartenente a un insieme $S$ risulta appartenente anche a un
  secondo insieme $T$, si dice che $S$ è un _sottoinsieme_ di $T$ (o che $S$ è _incluso_ 
  in $T$) e si indica questo fatto con la notazione $S \subseteq T$
  (vedi {numref}`venn-subset`):

$$ S \subseteq T \leftrightarrow \forall s \in \Omega \ (s \in S \rightarrow s \in T) ;$$

```{code-cell} ipython3
:tags: [hide-cell, remove-output]

fig = subset_venn()

glue("venn-subset-picture", fig, display=False)
```

```{glue:figure} venn-subset-picture
:figwidth: 100%
:name: "venn-subset"

Un diagramma di Venn per descrivere due insiemi $S$ e $T$ tali che $S \subseteq T$.
```

+++

- due insiemi si dicono uguali quando si includono mutuamente:

$$ S = T \leftrightarrow S \subseteq T \wedge T \subseteq S ;$$

- due insiemi si dicono diversi quando non sono uguali;

- tra due insiemi sussiste la relazione di inclusione _in senso stretto_ quando uno dei due è incluso nell'altro e in aggiunta i due insiemi non sono uguali:

$$ S \subset T \leftrightarrow S \subseteq T \wedge T \neq S .$$

Si verifica facilmente come qualunque insieme risulti sempre incluso nell'insieme universo, e come analogamente l'insieme vuoto risulti sempre incluso in qualunque insieme:

$$ \forall S \subseteq \Omega \ \{\} \subseteq S \subseteq \Omega ,$$

e questa relazione continua a valere se si considera la relazione di inclusione in senso stretto, a patto che $S$ sia diverso dall'insieme vuoto (affinché valga la prima parte della relazione) e dall'insieme universo (affinché possa valere la sua seconda parte).

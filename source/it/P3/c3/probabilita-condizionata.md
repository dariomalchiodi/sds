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

(sec:probabilita-condizionata)=
# Probabilità condizionata

Immaginiamo di fissare un esperimento casuale $\mathcal E$ e definire il
corrispondente spazio di proababilità $(\Omega, \mathsf A, \mathbb P)$. Dato
un generico evento $E \in \mathsf A$, se dopo che $\mathcal E$ è stato eseguito
noi sapessimo qual è l'esito $\omega \in \Omega$ che è stato osservato,
sapremmo automaticamente se $E$ si è verificato oppure no. Immaginiamo di non
conoscere con precisione $\omega$, ma di avere accesso a qualche forma
_parziale_ di informazione: più precisamente, immaginiamo di sapere che un
altro evento $F$ risulta verificato. La _probabilità condizionata_ è uno
strumento che ci permette di capire quanto questa informazione riduca
l'incertezza sull'evento originale $E$.

```{margin}
Il requisito che impone $\mathbb P(F) \neq 0$, oltre a garantire che il
rapporto {eq}`eq:prob-cond` non abbia un denominatore nullo e risulti
indefinito, è strettamente legato al significato di probabilità condizionata:
l'unico evento con probabilità nulla è quello impossibile, e dunque non ha
senso ipotizzare che esso si sia verificato. In generale, si dice che la
probabilità $\mathbb P(E \mid F)$ è indefinita quando $\mathbb P(F) = 0$.
```
````{prf:definition} Probabilità condizionata
:label: def:conditional_probability

Siano $E, F \subseteq \Omega$ due eventi in uno spazio di probabilità
$(\Omega, \mathbb A, \mathbb P)$: se $\mathbb P(F) \neq 0$ si definisce
_probabilità condizionata di $E$ dato $F$_ (o, più brevemente, _proababilità di
$E$ dato $F$_) il rapporto

```{math}
:label: eq:prob-cond

\mathbb P(E \mid F) = \frac{\mathbb P(E \cap F)}{\mathbb P(F)}.
```
````


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

(sec_assiomi-kolmogorov)=
# Assiomi di Kolmogorov 

````{prf:definition} Assiomi di Kolmogorov
:label: def-assiomi-kolmogorov
A partire da un fissato spazio misurabile $(\Omega, \mathsf A)$, definiamo
_funzione di probabilità_ ogni funzione
$\mathbb P: \mathsf A \rightarrow \mathbb R$ che soddisfa i seguenti
_assiomi di Kolmogorov_:

1. la probabilità associata a un evento è sempre non negativa:
   ```{math}
   :label: kolmogorov-axiom-1
   \forall E \in \mathsf A \quad \mathbb P(E) \geq 0,
   ```
2. la probabilità associata allo spazio degli esiti è uguale a $1$:
   ```{math}
   :label: kolmogorov-axiom-2
   \mathbb P(\Omega) = 1,
   ```
3. la probabilità associata all'unione di due eventi disgiunti è uguale alla
   somma delle probabilità associate ai due eventi:
   ```{math}
   :label: kolmogorov-axiom-3
   \forall E, F \in \mathsf A \quad E \cap F = \{\} \rightarrow
   \mathbb P(E \cup F) = \mathbb P(E) + \mathbb P(F).
   ```

Nel caso in cui $\mathsf A$ sia una sigma-algebra, quest'ultimo assioma si
estende a ogni successione infinita di eventi:

```{math}
:label: kolmogorov-axiom-3-sigma-algebra
\forall E_1, E_2, \ldots \in \mathsf A \; (\forall i, j E_i \cap E_j = \{\})
\rightarrow \bigcup_{i=1}^{+\infty} E_i \in \mathsf A.
```

````

Gli assiomi di Kolmogorov permettono di definire la funzione di probabilità
per uno spazio misurabile (i) indipendentemente dal _significato_ che viene
dato al concetto stesso di probabilità e (ii) in modo da garantire che agli
eventi vengano assegnate delle probabilità secondo uno schema _coerente_.

Dato uno spazio misurabile $(\Omega, \mathsf A)$ e fissata una funzione di
probabilità $\mathbb P$ che soddisfa la {prf:ref}`def-assiomi-kolmogorov`,
si dice che la terna $(\Omega, \mathsf A, \mathbb P)$ rappresenta uno
_spazio di probabilità_.

````{prf:theorem} Probabilità dell'evento complementare
:label: probabilita-evento-complementare

```{math}
\forall E \subseteq \Omega \quad \mathbb P(\overline E) = 1 - \mathbb P(E).
```
````
````{admonition} _
:class: myproof

Dato un generico $E \subseteq \Omega$, si ha $E \cup \overline E = \Omega$ e
$E \cap \overline E = \{\}$, pertanto

```{math}
1 \underset{(11.2)}{=} \mathbb P(\Omega) = \mathbb P(E \cup \overline E)
   \underset{(11.3)}{=} \mathbb P(E) + \mathbb P(\overline E),
```
da cui si ottiene la tesi.

````


````{prf:corollary} Probabilità dell'evento impossibile
:label: probabilita-evento-impossibile

```{math}
\mathbb P(\{\}) = 0
```
````
````{admonition} _
:class: myproof

La tesi si ottiene dal {prf:ref}`probabilita-evento-complementare`,
quando $E = \Omega$.
````

````{prf:theorem} Probabilità dell'unione di eventi
:label: probabilita-unione-eventi

```{math}
\forall E, F \subseteq \Omega \quad \mathbb P(E \cup F) =
\mathbb P(E) + \mathbb P(F) - \mathbb P(E \cap F).
```
````
````{admonition} _
:class: myproof

Per la distributività dell'intersezione rispetto all'unione si ha

```{math}
(E \cap \overline F) \cup (E \cap F) = E \cap (\overline F \cup F)
= E \cap \Omega = E,
```

inoltre sfruttando le proprietà di associatività, commutatività
e idempotenza si ottiene

```{math}
(E \cap \overline F) \cap (E \cap F) =
(E \cap E) \cap (F \cap \overline F) = E \cap \{\} = \{\}.
```

Per il terzo assioma di Kolmogorov, si ha dunque
$\mathbb P(E) = \mathbb P(E \cap \overline F) + \mathbb P (E \cap F)$, e in
modo analogo si dimostra che
$\mathbb P(F) = \mathbb P(\overline E \cap F) + \mathbb P (E \cap F)$, che
equivale a
$\mathbb P(\overline E \cap F) = \mathbb P(F) - \mathbb P (E \cap F)$.


Si verifica facilmente che $E \cap \overline F$, $E \cap F$ e
$\overline E \cap F$ sono a due a due disgiunti e che la loro unione coincide
con $E \cup F$, pertanto per l'estensione del terzo assioma di Kolmogorov
all'unione di tre insiemi disgiunti si ha

```{math}
\mathbb P(E \cup F) =
\underbrace{\mathbb P(E \cap \overline F) + \mathbb P(E \cap F)}_{\mathbb P(E)}
+
\underbrace{\mathbb P(\overline E \cap F)}_{\mathbb P(F) - \mathbb P(E \cap F)}
```
da cui segue la tesi.
````


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

(sec:modello-esponenziale)=
# Il modello esponenziale

Nel {numref}`sec:modello-geometrico` abbiamo visto che la funzione di
ripartizione di una variabile aleatoria $X$ con distribuzione geometrica di
parametro $p \in (0, 1]$ è definita come

```{math}
F_X(x; p) = 1 - (1 - p)^{\lfloor x \rfloor + 1} \mathrm
            I_{\mathbb N \cup \{0\}}(x) \enspace.
```

Dato $\lambda \in [0, +\infty)$, definiamo $Y = \frac{p}{\lambda} X$. In altre
parole, $Y$ si ottiene scalando $X$ di un fattore opportuno e ciò porta ad
«addensare» i relativi punti di massa di quest'ultima (che vengono divisi per
una quantità positiva e moltiplicati per un valore tra zero e uno). La
funzione di ripartizione di $Y$ si ottiene facilmente, in quanto

```{math}
F_Y(x; p, \lambda) = \mathbb P(Y \leq x) 
                   = \mathbb P\left(X \leq \frac{\lambda}{p} x \right)
                   = F_X\left(\frac{\lambda}{p}x \right)
                   = 1 - (1 - p)^{\left\lfloor \frac{\lambda x}{p}
                                               \right\rfloor + 1} \enspace.
```

```{margin}
In questo caso stiamo sfruttando il fatto che
$x - 1 \leq \lfloor x \rfloor \leq x$ (vedi
{numref}`sec:dal-discreto-al-continuo`) unitamente al fatto che l'elevamento
fatto con base $1 - p$ è un'operazione monotona non crescente.
```
Concentriamoci sulla quantità
$(1 - p)^{\left\lfloor \frac{\lambda x}{p} \right\rfloor + 1}$, notando che
vale

```{math}
:label: eq:geometric-to-exponential
(1 - p)^{\frac{\lambda x}{p}} \geq
(1 - p)^{\left\lfloor \frac{\lambda x}{p} \right\rfloor + 1} \geq
(1 - p)^{\frac{\lambda x}{p} + 1}.
```

Studiamo il limite per $p \to 0$ della quantità a sinistra di questa catena
di disuguaglianze:

```{margin}
Si verifica facilmente che $\lim_{p \to 0}\frac{\ln(1 - p)}{p} = -1$ applicando
il teorema di de l'Hôpital.
```
```{math}
\lim_{p \to 0} (1 - p)^{\frac{\lambda x}{p}}
 = \lim_{p \to 0} \mathrm e^{\ln (1 - p)^{\frac{\lambda x}{p}}}
 = \lim_{p \to 0} \mathrm e^{\lambda x \frac{\ln (1 - p)}{p}}
 = \mathrm e^{-\lambda x} \enspace.
```
D'altra parte, per quanto riguarda la quantità più a destra in
{eq}`eq:geometric-to-exponential` si ha che

```{math}
\lim_{p \to 0}(1 - p)^{\frac{\lambda x}{p} + 1}
= \lim_{p \to 0}(1 - p)^{\frac{\lambda x}{p}}
  -\lim_{p \to 0} p (1 - p)^{\frac{\lambda x}{p}}
  = \mathrm e^{-\lambda x} - 0 \enspace,
```

pertanto applicando il teorema dei due Carabinieri si ottiene

```{math}
\lim_{p \to 0} F_Y(x, p, \lambda) = 1 - \mathrm e^{-\lambda x} \enspace.
```

Possiamo verificare facilmente che

```{math}
F(x; \lambda) \coloneqq
     \left(1 - \mathrm e^{-\lambda x} \right) \; \mathrm I_{\mathbb R^+}(x)
```     

soddisfa i requisiti richiesti per essere una funzione di ripartizione
continua. La distribuzione corrispondente è detta _distribuzione esponenziale_
e la sua densità sarà pertanto definita come

```{math}
f(x; \lambda) = F'(x; \lambda) = \lambda  \mathrm e^{-\lambda x}
                                 \;\mathrm I_{\mathbb R^+}(x).
```
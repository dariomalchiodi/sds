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
:label: eq:cdf-exponential
F(x; \lambda) \coloneqq
     \left(1 - \mathrm e^{-\lambda x} \right) \; \mathrm I_{\mathbb R^+}(x)
```     

soddisfa i requisiti richiesti per essere una funzione di ripartizione
continua. La distribuzione corrispondente è detta _distribuzione esponenziale_
e la sua densità sarà ottenuta derivando {eq}`eq:cdf-exponential`.

````{prf:definition} La famiglia delle distribuzioni esponenziali

Dato $\lambda \in [0, +\infty)$, la  _distribuzione esponenziale_ è definita
dalla densità

```{math}
f(x; \lambda) = F'(x; \lambda) = \lambda  \mathrm e^{-\lambda x}
                                 \;\mathrm I_{\mathbb R^+}(x) \enspace,
```

o in modo equivalente dalla ripartizione

```{math}
F(x; \lambda) = \left(1 - \mathrm e^{-\lambda x} \right)
                \; \mathrm I_{\mathbb R^+}(x) \enspace.
```

L'insieme di tutte le distribuzioni esponenziali al variare dei possibili
valori del relativo parametro $\lambda$ viene detta _famiglia delle
distribuzioni esponenziali_.
````

Il valore atteso e la varianza delle distribuzioni esponenziali si ottengono
facilmente in funzione del loro parametro, applicando le relative definizioni.

`````{prf:lemma}
Data $X \sim \mathrm E(\lambda)$, con $\lambda \in [0, +\infty)$, si ha

```{math}
\mathbb E(X) = \frac{1}{\lambda}, \quad
\mathrm{Var}(X) = \frac{1}{\lambda^2} \enspace.
```

````{prf:proof}

Il calcolo del valore atteso si può effettuare integrando per parti:
definendo $f(x) = x$ e $g(x) = \mathrm e^{-\lambda x}$ si ha

\begin{align*}
\mathbb E(X) &= \int_{-\infty}^{+\infty} x f_X(x; \lambda) \; \mathrm d x
              = \int_0^{+\infty} \lambda x \mathrm e^{-\lambda x}
                \; \mathrm d x \\
             &= -\int_0^{+\infty} f(x) \cdot g'(x) \; \mathrm d x \\
             &= \underbrace{-x \mathrm e^{-\lambda x} \bigg|_0^{+\infty}}_{=0}
                + \int_0^{+\infty} \mathrm e^{-\lambda x} \; \mathrm d x
              = \frac{1}{\lambda} \underbrace{\int_0^{+\infty}
                        \lambda \mathrm e^{-\lambda x} \; \mathrm d x}_{=1}
              = \frac{1}{\lambda} \enspace.
\end{align*}

Procedendo in modo analogo, ma ponendo $f(x)=x^2$, si può calcolare il
momento secondo:

\begin{align*}
\mathbb E(X^2) &= \int_0^{+\infty}\lambda x^2 \mathrm e^{-\lambda x}
                  \;\mathrm d x
                = -\int_0^{+\infty} f(x) g'(x) \;\mathrm d x \\
               &= \underbrace{-x^2 \mathrm e^{-\lambda x}
                              \bigg|_0^{+\infty}}_{=0} +
                  2 \int_0^{+\infty} x \mathrm e^{-\lambda x}
                                \; \mathrm d x \\
               &= \frac{2}{\lambda} \underbrace{\int_0^{+\infty}
                                \lambda x \mathrm e^{-\lambda x}
                                \; \mathrm d x}_{= 1 / \lambda}
                = \frac{2}{\lambda^2} \enspace.
\end{align*}

Pertanto $\mathrm{Var}(X) = \frac{2}{\lambda^2} - \frac{1}{\lambda^2} =
\frac{1}{\lambda^2}$.

````

`````
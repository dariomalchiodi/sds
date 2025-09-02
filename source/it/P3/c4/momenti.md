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

(sec:momenti)=
# Momenti

````{prf:theorem}
:label: teo:mgf-method

Siano date $n$ variabili aleatorie $X_1, \dots, X_n$ tra loro indipendenti e
ciascuna avente la stessa distribuzione di una variabile aleatoria $X$, della
quale $m_X$ indica la funzione generatrice dei momenti. Posto
$Y \triangleq \sum_{i=1}^n X_i$, si ha

```{math}
m_Y(t) = \left( m_X(t) \right)^n \enspace.
```
````
````{admonition} _
:class: myproof

La funzione generatrice dei momenti di $Y$ è tale che

```{math}
m_Y(t) = \mathbb E\left( \mathrm e^{tY} \right)
       = \mathbb E\left( \mathrm e^{t\sum_{i=1}^n X_i} \right)
       = \mathbb E\left( \prod_{i=1}^n \mathrm e^{t X_i} \right)
       = \prod_{i=1}^n \mathbb E\left( \mathrm e^{t X_i} \right)
       = \prod_{i=1}^n m_X(t)
       = \left( m_X(t) \right)^n \enspace,
```

dove il terzultimo passaggio è giustificato dall'indipendenza di
$X_1, \dots, X_n$.
````

````{prf:theorem}
:label: teo:central-moments
Data una variabile aleatoria $X$ tale con valore atteso finito
$\mathbb E(X) = \mu$, posto $Y \triangleq X - \mu$ si ha

$$m_Y^{(n)}(t) = \mathrm  e^{-t \mu}
               \sum_{i=0}^n \binom{n}{i}(-\mu)^i m_X^{n-i}(t) \enspace. $$
````
````{prf:proof}
Per semplificare la notazione, poniamo $f(t) = \mathrm e^{- t \mu} g(t)$, così
che l'enunciato diventa

```{math}
f^{(n)}(t) = \mathrm e^{-t \mu} \sum_{i=0}^n \binom{n}{i}(-\mu)^i g^{n-i}(t)
             \enspace,
```

e dimostriamo per induzione quest'ultima equazione. Il caso base $n = 1$ è
semplice da trattare, in quanto


```{math}
f'(t) = -\mu \mathrm e^{-t \mu} g(t) + \mathrm e^{-t\mu} g'(t)
      = \mathrm e^{-t\mu} (g'(t) - \mu g(t))
      = \sum_{i=0}^1 \binom{1}{i}(-\mu)^i g^{n-i}(t) \enspace.
```

Per quanto riguarda il passo dell'induzione, si ha

```{math}
\begin{align*}
f^{(n+1)}(t) &= \frac{\mathrm d}{\mathrm d t} f^{(n)}(t)
              = \frac{\mathrm d}{\mathrm d t} \mathrm e^{-t \mu}
                       \sum_{i=0}^n \binom{n}{i}(-\mu)^i g^{(n-i)}(t) \\
             &= -\mu \mathrm e^{-t \mu}
                       \sum_{i=0}^n \binom{n}{i}(-\mu)^i g^{(n-i)}(t)
                + \mathrm e^{-t \mu}
                       \sum_{i=0}^n \binom{n}{i}(-\mu)^i g^{(n-i+1)}(t) \\
             &= \mathrm e^{-t \mu} \left( 
                    \sum_{i=0}^n \binom{n}{i}(-\mu)^{i+1} g^{(n-i)}(t) +
                    \sum_{i=0}^n \binom{n}{i}(-\mu)^i g^{(n+1-i)}(t)
                \right) \\
             &= \mathrm e^{-t \mu} \left( 
                    \sum_{j=1}^{n+1} \binom{n}{j-1}(-\mu)^{j} g^{(n-j+1)}(t) +
                    \sum_{j=0}^n \binom{n}{j}(-\mu)^i g^{(n+1-j)}(t)
                \right) \\
             &= \mathrm e^{-t \mu} \left( 
                    \sum_{j=0}^{n+1} \binom{n}{j-1}(-\mu)^{j} g^{(n+1-j)}(t) +
                    \sum_{j=0}^{n+1} \binom{n}{j}(-\mu)^i g^{(n+1-j)}(t)
                \right) \\
             &= \mathrm e^{-t \mu}  
                \sum_{j=0}^{n+1} \left( \binom{n}{j-1} + \binom{n}{j} \right)
                (-\mu)^{j} g^{(n+1-j)}(t) \enspace.
\end{align*}
```

Si verifica facilmente che

```{math}
\binom{n}{j-1} + \binom{n}{j} = \binom{n+1}{j} \enspace,
```

da cui segue la tesi.

````

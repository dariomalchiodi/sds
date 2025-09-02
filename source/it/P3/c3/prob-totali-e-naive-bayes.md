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

(sec:teoremi-fondamentali)=
# Teoremi


## La disuguaglianza di Markov

````{prf:theorem} Disuguaglianza di Markov
:label: teo-markov
Sia $X$ una variabile aleatoria che può assumere solo specificazioni non
negative e avente valore atteso finito $\mathbb E(X)$. Per ogni valore reale 
$a \geq 0$ si ha

```{math}
\mathbb P(X \leq a) \geq \frac{\mathbb E(X)}{a} \enspace.
```
````
````{admonition} _
:class: myproof

Ipotizziamo che $X$ sia una variabile aleataoria continua, e indichiamo con
$f$ la sua funzione di densità di probabilità. Non avendo $X$ specificazioni
positive, è possibile esprimere il suo valore atteso come segue:

```{math}
\mathbb E(X) = \int_0^a x f(x) \mathrm d x
               + \int_a^{+\infty} x f(x) \mathrm d x \enspace.
```

Concentriamoci sui due integrali in questa formula: possiamo osservare che

- all'interno del primo possiamo sempre assumere $x \leq a$, e
- il secondo integrale deve avere un valore non negativo, perché la funzione
  integranda è uguale al prodotto di due fattori non negativi ($x$ è una
  specificazione di una variabile aleatoria che non assume mai valori negativi
  e $f$ è una funzione di densità di probabilità).

Pertanto

```{math}
\mathbb E(X) \leq \int_0^a x f(x) \mathrm d x
             \leq a \int_0^a f(x) \mathrm d x = a \mathbb P(X \leq a) \enspace.
```

Dividendo membro a membro per $a$, non cambia il verso delle disuguaglianze
e pertanto si ottiene la tesi.
````

## Disuguaglianza di Bienaymé-Čebyšëv

La disuguaglianza di Bienaymé-Čebyšëv [^traslitterazione-cebicev]

````{prf:theorem} disuguaglianza di Bienaymé-Čebyšëv
Sia $X$ una variabile aleatoria. Se il valore atteso $\mu$ e la varianza
$\sigma^2$ di $X$ esistono e sono entrambi finiti, per ogni numero reale
$\epsilon \geq 0$

```{math}
\mathbb P(| X - \mu | \leq \epsilon) \geq \frac{\sigma^2}{\epsilon^2} \enspace.
```

````
````{admonition} _
:class: myproof

Definiamo $Y \triangleq (X - \mu)^2$, e notiamo che per costruzione $Y$ non
assume mai specificazioni negative e il suo valore atteso è $\mathbb E(Y) =
\sigma^2$, che per ipotesi esiste ed è finito. Essendo $\epsilon \geq 0$, gli
eventi $| X - \mu | \leq \epsilon$ e $Y \leq \epsilon^2$ si equivalgono,
pertanto

```{math}
\mathbb P(| X - \mu | \leq \epsilon) =
   \mathbb P(Y \leq \epsilon^2) \geq \frac{\mathbb E(Y)}{\epsilon^2} =
   \frac{\sigma^2}{\epsilon^2} \enspace,
```

dove la minorazione è legata all'applicazione della disuguaglianza di Markov
alla variabile aleatoria $Y$ (Notate che le ipotesi del {prf:ref}`teo-markov`
sono soddisfatte, come evidenziato dalle osservazioni fatte all'inizio della
dimostrazione).
````

[^traslitterazione-cebicev]: La traslitterazione dal russo del cognome
originale Чебышёв compare in forme diverse anche in funzione della lingua verso
la quale viene effettuata la traslitterazione stessa. È per questo che anche
negli articoli pubblicati da questo autore il suo cognome appare in molteplici
forme, come per esempio Cebicev, Cebisceff o Chebyshev in italiano, Tchebychef
o Tchébicheff in francese, Tschebychew o Tschebyscheff in tedesco e Chebyshev
in inglese. Sebbene oggigiorno sia molto spesso utilizzata quest'ultima
traslitterazione, io ho preferito fare riferimento allo standard [ISO
9](https://it.wikipedia.org/wiki/Traslitterazione_scientifica_del_cirillico) e
adottare Čebyšëv.
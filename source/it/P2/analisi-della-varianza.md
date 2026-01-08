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

```{code-cell} python
:tags: [remove-cell]

import matplotlib.pyplot as plt
plt.style.use('../_static/sds.mplstyle')
%matplotlib inline
plt.ioff()
```

(sec_analisi-della-varianza)=
# Analisi della varianza

Ipotizziamo di avere a disposizione delle osservazioni di un medesimo
attributo divise in $G$ gruppi, per esempio perché si tratta del reddito di
individui che vivono in diverse città, oppure di un valore ematico di
pazienti sottoposti a diversi trattamenti clinici e così via. Formalmente,
indichiamo rispettivamente con $n_1, \dots, n_G$ le numerosità dei vari
gruppi, con $n = n_1 + \dots + n_G$ il numero totale di osservazioni e,
fissato $g \in \{1, \dots, G\}$ e $i \in \{1, \dots, n_g\}$, denotiamo con
$x^g_i$ il valore dell'$i$-esima osservazione nel gruppo $g$.

Se si è interessati a valutare l'ipotesi che i valori delle medie nei vari
gruppi siano sensibilmente differenti, per esempio perché si vuole dimostrare
che il reddito non sia troppo diverso in un gruppo di città, oppure per
dimostrare l'efficacia di un dato trattamento medico, è possibile applicare
un metodo chiamato _ANOVA_ (_ANalysis Of VAriance_). L'idea alla base di
questo metodo è che se non vi sono sostanziali differenze tra i gruppi
considerati, allora calcolare la varianza all'interno di un gruppo qualsiasi
non dovrebbe portare a un risultato molto dissimile da quello ottenuto
effettuando il calcolo su tutti i dati a disposizione. Più formalmente,
definite:

- la media campionaria
  $\overline x = \frac{1}{n} \sum_{g=1}^G \sum_{i=1}^{n_g} x^g_i$ su tutte
  le osservazioni;

- la media campionaria $\overline x^g = \frac{1}{n_g} \sum_{i=1}^{n_g} x^g_i$
  all'interno del $g$-esimo gruppo, per ogni $g = 1, \dots, n_G$;

- la somma totale degli scarti

```{math}
\mathrm{SS}_{\mathrm T} = \sum_{g=1}^G \sum_{i=1}^{n_g}
                          \left( x^g_i - \overline x \right)^2;
```

- la somma degli scarti _entro i gruppi_ (o, usando la terminologia inglese,
  _within groups_)

```{math}
\mathrm{SS}_{\mathrm W} = \sum_{g=1}^G \sum_{i=1}^{n_g}
                          \left( x^g_i - \overline x^g \right)^2;
```

- la somma degli scarti _tra i gruppi_ (o, usando la terminologia inglese,
  _between groups_), pesata rispetto alla numerosità dei vari gruppi:

```{math}
\mathrm{SS}_{\mathrm B} = \sum_{g=1}^G n_g
                          \left( \overline x^g - \overline x \right)^2;
```

A partire da ognuna di queste somme è facile calcolare le corrispondenti
varianze campionarie:

- la varianza campionaria su tutte le osservazioni:
  $s^2_{\mathrm T} = \frac{1}{n-1} \mathrm{SS}_{\mathrm T}$;

- la varianza campionaria delle medie tra i gruppi:
  $s^2_{\mathrm B} = \frac{1}{G-1} \mathrm{SS}_{\mathrm B}$ (il motivo per
  cui viene fatta la divisione per $G-1$ è analogo alla ragione per cui il
  calcolo della varianza campionaria viene fatta dividendo per $n-1$, e
  richiede un maggiore approfondimento teorico per poter essere
  giustificato);

- la varianza campionaria dei valori entro i gruppi:
  $s^2_{\mathrm W} = \frac{1}{n-G} \mathrm{SS}_{\mathrm W}$.

Si può mostrare (chi è interessato può leggere il paragrafo opzionale che
segue) che
$\mathrm{SS}_{\mathrm T} = \mathrm{SS}_{\mathrm W} + \mathrm{SS}_{\mathrm B}$,
e quindi che

```{math}
\begin{align*}
\frac{\mathrm{SS}_{\mathrm T}}{n-1} &= \frac{\mathrm{SS}_{\mathrm W}}{n-1} +\frac{\mathrm{SS}_{\mathrm B}}{n-1}, \\
&= \frac{n-G}{n-1} \frac{\mathrm{SS}_{\mathrm W}}{n-G} + \frac{G-1}{n-1} \frac{\mathrm{SS}_{\mathrm B}}{G-1}.
\end{align*}
```

Pertanto,

```{math}
\begin{aligned}
\text{varianza totale} = \frac{n-G}{n-1} \text{varianza entro i gruppi} + \\
                         \frac{G-1}{n-1} \text{varianza tra i gruppi}.
\end{aligned}
```

```{margin}
Per validare o confutare questo tipi di ipotesi esistono metodi
quantitativi basati sul calcolo di indici che coinvolgono le quantità che noi
abbiamo confrontato in modo qualitativo. L'uso di questi metodi richiede però
un approfondimento teorico che va al di là della trattazione in questo libro.
```
Possiamo utilizzare questa uguaglianza per validare o confutare l'ipotesi che
le medie nei gruppi siano diverse: se la varianza totale e la varianza entro
i gruppi assumono valori non troppo diversi tra loro (e dunque la varianza
  tra i gruppi risulta trascurabile), allora si confuta l'ipotesi; se al
  contrario la varianza tra i gruppi assume un valore elevato si può
  convalidare l'ipotesi.

Per applicare la tecnica di analisi della varianza selezioniamo per esempio
i due gruppi dei supereroi corrispondenti alle due case editrici più
rappresentate: Marvel e DC, e concentriamoci per ogni gruppo sull'indice di
forza.

```{margin}
Questa cella mostra come effettuare un'operazione di selezione
complessa su di un _dataframe_, basandosi sull'operatore `&` di congiungzione
logica. Analogamente, l'operatore `|` permette di calcolare disgiunzioni
logiche.
```
```{code-cell} python
import pandas as pd

heroes = pd.read_csv('data/heroes.csv', index_col=0)

marvel_strength = heroes[(heroes['creator'] == 'Marvel Comics') &
                         (pd.notnull(heroes['strength']))]['strength']
dc_strength = heroes[(heroes['creator'] == 'DC Comics') & \
                     (pd.notnull(heroes['strength']))]['strength']
```

Iniziamo calcolando $\mathrm{SS}_{\mathrm T}$.

```{code-cell} python
all_strength = pd.concat([marvel_strength, dc_strength])
sum_total = sum((all_strength - all_strength.mean())**2)
sum_total
```

Analogamente calcoliamo $\mathrm{SS}_{\mathrm W}$.

```{code-cell} python
sum_within = sum((marvel_strength - marvel_strength.mean())**2) + \
                    sum((dc_strength - dc_strength.mean())**2)
sum_within
```

Infine, calcoliamo $\mathrm{SS}_{\mathrm B}$.

```{code-cell} python
sum_between = len(marvel_strength) * (marvel_strength.mean() - all_strength.mean())**2 + \
                    len(dc_strength) * (dc_strength.mean() - all_strength.mean())**2
sum_between
```

Verifichiamo innanzitutto che valga, nei limiti dell'approssimazione in
virgola mobile, l'uguaglianza
$\mathrm{SS}_{\mathrm T} = \mathrm{SS}_{\mathrm W} + \mathrm{SS}_{\mathrm B}$.

```{code-cell} python
sum_total - sum_within - sum_between
```

Calcoliamo infine la varianza totale e la varianza entro i gruppi utilizzando
le formule sopra descritte.

```{code-cell} python
n = len(all_strength)

total_var = sum_total / (n-1)
total_var
```

```{code-cell} python
within_var = sum_within / (n-2)
within_var * (n-2) / (n-1)
```

I due valori sono molto vicini, e quindi possiamo avvalorare l'ipotesi che i
valori medi dell'indice di forza siano sostanzialmente uguali.

Riscriviamo il codice in modo da incorporare in una funzione la procedura di
analisi della varianza, in modo da gestire anche più di due gruppi di
osservazioni: la funzione accetterà una lista di tali gruppi come argomento,
e restituirà una coppia i cui elementi saranno rispettivamente la varianza
totale e la varianza entro i gruppi.

```{code-cell} python
import numpy as np

def anova(groups):
    all_elements = pd.concat(groups)

    sum_total = sum((all_elements - all_elements.mean())**2)
    sum_within = sum([sum((g - g.mean())**2) for g in groups])

    sum_between = sum([len(g) * (g.mean()-all_elements.mean())**2
                       for g in groups])
    print(f'this should be almost zero: {np.abs(sum_total - sum_within - sum_between)}')
    
    n = len(all_elements)
    total_var = sum_total / (n-1)
    within_var = sum_within / (n-len(groups))

    return (total_var, within_var*(n-len(groups))/(n-1))
```

Verifichiamo che i valori restituiti per i due gruppi già considerati siano
gli stessi.

```{code-cell} python
anova([dc_strength, marvel_strength])
```

Applicando la procedura all'indice di forza suddiviso tra supereroi e
supereroine si ottengono due valori tutto sommato relativamente simili, così
che non si possa avvalorare l'ipotesi che l'indice di forza sia distribuito
in modo sostanzialmente diverso tra i due generi.

```{code-cell} python
male_strength = heroes[(heroes['creator'] == 'Marvel Comics') & \
                       (pd.notnull(heroes['strength']))]['strength']
female_strength = heroes[(heroes['creator'] == 'DC Comics') & \
                         (pd.notnull(heroes['strength']))]['strength']
anova([male_strength, female_strength])
```

Le cose cambiano se consideriamo la divisione tra generi per i supereroi DC,
valutando la differenza nella distribuzione del peso.

```{code-cell} python
male_weight = heroes[(heroes['creator'] == 'DC Comics') & \
                   (pd.notnull(heroes['weight']))]['weight']
female_weight = heroes[(heroes['creator'] == 'DC Comics') & \
                     (pd.notnull(heroes['weight']))]['weight']
anova([male_weight, female_weight])
```


## Dimostrazione <sup>*</sup>

Innanzitutto notiamo che per ogni $g = 1, \dots, G$,

```{math}
\sum_{i=1}^{n_g} x^g_i = n_g \overline x^g,
```

e quindi

```{math}
\begin{align*}
\mathrm{SS}_{\mathrm T}  &= \sum_{g=1}^G \sum_{i=1}^{n_g}
                            \left( \left(x^g_i\right)^2
                            - 2 \overline x x^g_i +
                            \left( \overline x \right)^2 \right) \\
                         &= \sum_{g=1}^G \sum_{i=1}^{n_g}
                            \left( \left(x^g_i\right)^2
                            - 2 \overline x x^g_i +
                            \left( \overline x \right)^2 +
                            \left( \overline x^g \right)^2 -
                            \left( \overline x^g \right)^2 +
                            2 x^g_i \overline x^g
                            - 2 x^g_i \overline x^g \right) = \\
                         &= \sum_{g=1}^G \sum_{i=1}^{n_g}
                            \left( x^g_i - \overline x^g \right)^2
                            + \sum_{g=1}^G \sum_{i=1}^{n_g}
                            \left( \left( \overline x \right)^2
                            - \left( \overline x^g \right)^2
                            -2 \overline x x^g_i
                            + 2 x^g_i \overline x^g  \right) = \\
                         &= \mathrm{SS}_{\mathrm W} + \sum_{g=1}^G
                            \left( n_g \left( \overline x \right)^2
                            - n_g \left( \overline x^g \right)^2
                            - 2 \overline x \sum_{i=1}^{n_g} x^g_i
                            + 2 \overline x^g \sum_{i=1}^{n_g} x^g_i \right) = \\
                         &= \mathrm{SS}_{\mathrm W} + \sum_{g=1}^G n_g
                            \left( \left( \overline x \right)^2
                            - \left( \overline x^g \right)^2
                            - 2 \overline x \overline x^g
                            + 2 \left( \overline x^g \right)^2 \right) = \\
                         &= \mathrm{SS}_{\mathrm W} + \sum_{g=1}^G n_g
                            \left( \overline x^g - \overline x \right)^2
                            = \mathrm{SS}_{\mathrm W} + \mathrm{SS}_{\mathrm B}.
\end{align*}
```


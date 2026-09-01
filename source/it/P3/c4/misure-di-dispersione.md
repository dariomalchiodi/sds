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

(sec-misure-di-dispersione)=
# Misure di dispersione

Come abbiamo visto nel paragrafo precedente, la centralità è solo uno degli
aspetti che descrivono la distribuzione di una variabile aleatoria. La seconda
caratteristica che si studia prende il nome di _dispersione_, o _variabilità_.
Se la centralità ci permette di capire _dove_ si colloca una distribuzione
lungo l'insieme dei valori possibili, la dispersione permette invece di
valutarne l'_estensione_, cioè quanto i valori che la variabile aleatoria può
assumere risultano più o meno distanti tra loro. Come per la centralità,
esistono vari indici ai quali si può fare riferimento, e io qui mi limiterò a
introdurre solo quelli principali, considerando separatamente le due modalità
con la quale si può calcolare la dispersione: rispetto a un valore centrale di
riferimento, oppure nei termini della distanza tra i valori della
distribuzione.

## Dispersione rispetto a un valore centrale

Nel {ref}`sec-misure-di-centralita` abbiamo visto che il valore atteso individua il
_baricentro_ di una variabile aleatoria, specificando che la sua distribuzione
è descritta solo parzialmente da questo indice. In altre parole, possono
esistere variabili aleatorie diverse che hanno uno stesso valore atteso, e un
modo per differenziarle consiste proprio nel valutare quanto i loro valori
tendano a discostarsi rispetto a questo valore atteso, come mostrato
nell'esempio che segue.

````{prf:example}
:label: ex-var-stessa-media

Consideriamo due variabili aleatorie:

- $X$, con supporto $S_X = \{3, 5, 6\}$ e funzione di massa di probabilità
  definita da $p_X(3) = 0.1$, $p_X(5) = 0.7$ e $p_X(6) = 0.2$;
- $Y$, caratterizzata da $S_Y = \{1, 5, 7\}$ e $p_Y(1) = 0.1$, $p_Y(5) = 0.7$ e
  $p_Y(7) = 0.2$.

Si verifica facilmente che

```{math}
\begin{align*}
\mathbb E(X) &= 3 \cdot 0.1 + 5 \cdot 0.7 + 6 \cdot 0.2 = 5 \enspace, \\
\mathbb E(Y) &= 1 \cdot 0.1 + 5 \cdot 0.7 + 7 \cdot 0.2 = 5 \enspace.
\end{align*}
```

I due valori attesi sono uguali, ma le due distribuzioni sono chiaramente
distinte. In particolare, quella di $X$ è più _concentrata_ attorno al valore
atteso: i suoi valori diversi da $5$ si trovano infatti a distanza $2$ e $1$
dal valore atteso comune. La distribuzione di $Y$ è invece più sparsa, poiché
gli analoghi scarti diventano rispettivamente pari a $4$ e $2$. La
{numref}`fig_ex-dispersione` mostra una famiglia di distribuzioni che collega
progressivamente questi due casi: spostando il selettore verso destra, le masse
di probabilità più lontane dal centro si allontanano ulteriormente, mentre il
valore atteso rimane fissato in $5$. In questo modo si visualizza come una
stessa centralità possa accompagnarsi a diversi gradi di dispersione.
````

````{customfigure}
:name: fig_ex-dispersione
:class: left-align

```{interactive-code} python
:tags: [toggle-code]

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch
from pyscript import display
from pyscript.web import page, when

fig_dispersion, ax_dispersion = plt.subplots()
probabilities = np.array([0.1, 0.7, 0.2])
initial_values = np.array([4.0, 5.0, 5.5])

stem_lines = ax_dispersion.vlines(initial_values, 0, probabilities)
point_markers, = ax_dispersion.plot(initial_values, probabilities, 'o',
                                    color='C0')

ax_dispersion.set_xlabel(r'$x$')
ax_dispersion.set_ylabel(r'$p_X$')
ax_dispersion.set_xlim(0, 7.5)
ax_dispersion.set_ylim(0, 0.8)
ax_dispersion.axvline(5, color='#cc6600', linestyle='--', linewidth=.5)

def render_dispersion_plot():
  dist = float(page['#dist'][0].value)

  values = np.array([5 - dist, 5, 5 + dist/2])
  segments = [((value, 0), (value, probability))
              for value, probability in zip(values, probabilities)]

  stem_lines.set_segments(segments)
  point_markers.set_data(values, probabilities)

  if dist == 2:
    ax_dispersion.set_ylabel(r'$p_X$')
  elif dist == 4:
    ax_dispersion.set_ylabel(r'$p_Y$')
  else:
    ax_dispersion.set_ylabel(r'$p_Z$')

  display(fig_dispersion, target='graph-%this%', append=False)


@when('input', '#dist')
def update_dispersion_plot(event):
  render_dispersion_plot()


render_dispersion_plot()
```

```{raw} html
<div class="plot-container">
   <div class="model-slider-container" style="white-space: nowrap;">
      <!-- <label for="dist">Distanza: </label> -->
      <input type="range" id="dist" min="2" max="4" value="2" step="0.05" />
   </div>
</div>
```

Funzioni di massa di probabilità di una famiglia di variabili aleatorie
discrete, tutte con valore atteso uguale a $5$, ma con diversa dispersione
attorno a questo valore. Con il selettore completamente a sinistra si ottiene
la distribuzione della variabile $X$ dell'{prf:ref}`ex-var-stessa-media`; con
il selettore completamente a destra si ottiene invece quella di $Y$.
Nelle posizioni intermedie si visualizzano distribuzioni con la stessa
centralità, ma via via più disperse.
````


L'esempio precedente introduce il concetto di dispersione di una distribuzione
_attorno a un valore centrale_, che in questo caso è proprio il valore atteso.
Anche quando quest'ultimo risulta fissato, esistono in generale infinite
distribuzioni aventi ognuna una dispersione differente: si può concentrare la
probabilità vicino al valore atteso, oppure distribuirla più lontano,
mantenendo inalterato il baricentro complessivo. Una prima idea per
quantificare questo aspetto per una variabile aleatoria $X$ potrebbe essere
quella di misurare il valore atteso dello _scarto dalla media_, cioè
considerare la variabile $X - \mathbb E(X)$. Il problema è che, come mostrato
alla fine del capitolo precedente, ogni variabile aleatoria centrata ha valore
atteso nullo. In altre parole, 

```{math}
\mathbb E(X - \mathbb E(X)) = 0
```

```{margin}
In teoria, si potrebbe utilizzare anche la variabile
$\lvert X - \mathbb E(X) \rvert$, che considera gli scarti in valore assoluto
al posto di quelli quadratici, ma ciò introdurrebbe delle complicazioni nei
calcoli successivi.
```
vale sempre, indipendentemente dal fatto che la distribuzione sia molto
concentrata o molto dispersa. Gli scarti positivi e quelli negativi si
compensano infatti esattamente. Per ottenere un vero indice di dispersione,
occorre quindi trasformare gli scarti in modo da evitare queste
compensazioni, e tipicamente questo viene fatto elevandoli al quadrato. Ciò
porta alla definizione della _varianza_ e della _deviazione standard_,
indici a cui si fa comunemente riferimento per valutare la dispersione attorno
al valore atteso, introdotti di seguito.

````{prf:definition} Varianza e deviazione standard
:label: def-varianza

Sia $X$ una variabile aleatoria che ammette valore atteso, e sia
$\mu = \mathbb E(X)$. Se anche $(X - \mu)^2$ ammette valore atteso, si
definiscono la _varianza_ di $X$ come

```{math}
\operatorname{Var}(X) \triangleq \mathbb E \left( (X - \mu)^2 \right) \enspace
```

e la _deviazione standard_ di $X$ come la radice quadrata della varianza:

```{math}
\operatorname{SD}(X) \triangleq \sqrt{\operatorname{Var}(X)} \enspace.
```

mentre negli altri casi si dice che $X$ non ammette varianza, né deviazione
standard.
````

```{figure} https://upload.wikimedia.org/wikipedia/commons/a/aa/Youngronaldfisher2.JPG
---
figclass: margin
name: fig_pearson
width: 200px
align: left
---
Ritratto di Ronald Aylmer Fisher (Fotografia di autore sconosciuto, 1913. Immagine di
pubblico dominio. Fonte: [Wikimedia Commons](https://upload.wikimedia.org/wikipedia/commons/a/aa/Youngronaldfisher2.JPG)).
```
```{admonition} _
:class: naming

Mentre per il valore atteso si utilizza tipicamente la notazione
$\mathbb E(X)$, che è particolarmente compatta, l'uso di
$\operatorname{Var}(X)$ e $\operatorname{SD}(X)$ per varianza e deviazione
standard risulta un po' più pesante, ma nella pratica è universalmente
accettato. La sigla $\operatorname{SD}$ è talvolta sostituita da
$\operatorname{std}$, soprattutto in ambito informatico. Si incontrano
frequentemente anche le notazioni $\sigma_X^2$ e $\sigma_X$ per varianza e
deviazione standard, omettendo il pedice quando la variabile aleatoria
considerata è chiara dal contesto. Questo modo di procedere ha gli stessi
vantaggi e svantaggi dell'uso di $\mu_X$ per denotare il valore atteso di $X$.
È interessante sottolineare che il termine _deviazione standard_ è stato
introdotto nel 1894 da Karl Pearson, unitamente al al simbolo $\sigma$,
presumibilmente basandosi sull'associazione con l'iniziale S. Solo più di venti
anni dopo, Ronald Aylmer Fisher introdusse il termine _varianza_, usando
$\sigma^2$ come notazione per denotarla. L'apparizione di $\operatorname{Var}$,
invece, risulta più difficile da tracciare con precisione: sicuramente compare
in {cite:p}`feller`, la cui influenza ha sicuramente contribuito a diffonderne
l'utilizzo.
```

La varianza è dunque il valore atteso dello _scarto quadratico_ dalla media,
ed esprime il baricentro di questo tipo di scarti, calcolato rispetto alla
distribuzione della variabile aleatoria. Il suo valore ci dice quindi quale
sia, in media, lo scarto quadratico dei valori di $X$ rispetto a
$\mathbb E(X)$. Nel caso discreto, si avrà dunque

```{math}
\operatorname{Var}(X) = \sum_{x \in S_X} (x - \mu)^2 \, p_X(x) \enspace.
```

````{prf:example} Confrontare due dispersioni
:label: ex-var-confronto

Riprendiamo le variabili dell'{prf:ref}`ex-var-stessa-media`. Per $X$ si ha

```{math}
\begin{align*}
\operatorname{Var}(X)
        &= (3-5)^2 \cdot 0.1 + (5-5)^2 \cdot 0.7 + (6-5)^2 \cdot 0.2 \\
        &= 4 \cdot 0.1 + 0 \cdot 0.7 + 1 \cdot 0.2 = 0.6 \enspace.
\end{align*}
```

Per $Y$, invece,

```{math}
\begin{align*}
\operatorname{Var}(Y)
        &= (1-5)^2 \cdot 0.1 + (5-5)^2 \cdot 0.7 + (7-5)^2 \cdot 0.2 \\
        &= 16 \cdot 0.1 + 0 \cdot 0.7 + 4 \cdot 0.2 = 2.4 \enspace,
\end{align*}
```

e questo cattura in modo quantitativo la differenza tra la dispersione di $X$
e $Y$: la prima variabile aleatoria è più concentrata della seconda attorno al
proprio valore atteso. La {numref}`fig_ex-varianza` mostra lo stesso grafico
contenuto nella {numref}`fig_ex-dispersione`, evidenziando per ogni
distribuzione quali siano i valori degli scarti e calcolando esplicitamente
la varianza.
````

````{customfigure}
:name: fig_ex-varianza
:class: left-align

```{interactive-code} python
:tags: [toggle-code]

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch
from pyscript import display
from pyscript.web import page, when

fig_var, ax_var = plt.subplots()
probabilities_var = np.array([0.1, 0.7, 0.2])
initial_values_var = np.array([4.0, 5.0, 5.5])

stem_lines_var = ax_var.vlines(initial_values_var, 0, probabilities_var)
point_markers_var, = ax_var.plot(initial_values_var, probabilities_var, 'o',
                                 color='C0')
left_arrow_var = FancyArrowPatch((initial_values_var[0], 0.5),
                                 (initial_values_var[1], 0.5),
                                 arrowstyle='<->', mutation_scale=12,
                                 linewidth=1.0, color='#9aa3ad')
right_arrow_var = FancyArrowPatch((initial_values_var[1], 0.5),
                                  (initial_values_var[2], 0.5),
                                  arrowstyle='<->', mutation_scale=12,
                                  linewidth=1.0, color='#9aa3ad')
ax_var.add_patch(left_arrow_var)
ax_var.add_patch(right_arrow_var)
left_distance_label = ax_var.text(np.mean(initial_values_var[:2]), 0.52, '',
                                  ha='center', va='bottom', color='#7f8790')
right_distance_label = ax_var.text(np.mean(initial_values_var[1:]), 0.52, '',
                                   ha='center', va='bottom', color='#7f8790')

ax_var.set_xlabel(r'$x$')
ax_var.set_ylabel(r'$p_X$')
ax_var.set_xlim(0, 7.5)
ax_var.set_ylim(0, 0.8)
ax_var.axvline(5, color='#cc6600', linestyle='--', linewidth=.5)

def render_var_plot():
  dist = float(page['#dist-var'][0].value)

  values = np.array([5 - dist, 5, 5 + dist/2])
  segments = [((value, 0), (value, probability))
              for value, probability in zip(values, probabilities_var)]

  stem_lines_var.set_segments(segments)
  point_markers_var.set_data(values, probabilities_var)
  left_arrow_var.set_positions((values[0], 0.5), (values[1], 0.5))
  right_arrow_var.set_positions((values[1], 0.5), (values[2], 0.5))
  left_distance = values[0] - values[1]
  right_distance = values[2] - values[1]
  left_distance_label.set_position(((values[0] + values[1]) / 2, 0.52))
  right_distance_label.set_position(((values[1] + values[2]) / 2, 0.52))
  left_distance_label.set_text(f'${left_distance:.2f}$')
  right_distance_label.set_text(f'${right_distance:.2f}$')
  var = left_distance**2 * 0.1 + right_distance**2 * 0.2

  if dist == 2:
    rv = 'X'
  elif dist == 4:
    rv = 'Y'
  else:
    rv = 'Z'

  ax_var.set_title(rf'$\operatorname{{Var}}({rv}) = '
                   rf'0.1 ({left_distance:.2f})^2 + '
                   rf'0.2 \cdot {right_distance:.2f}^2 = {var:.2f}$')

  ax_var.set_ylabel(rf'$p_{rv}$')

  display(fig_var, target='graph-%this%', append=False)


@when('input', '#dist-var')
def update_dispersion_plot(event):
  render_var_plot()


render_var_plot()
```

```{raw} html
<div class="plot-container">
   <div class="model-slider-container" style="white-space: nowrap;">
      <!-- <label for="dist">Distanza: </label> -->
      <input type="range" id="dist-var" min="2" max="4" value="2" step="0.05" />
   </div>
</div>
```

Stesso grafico della {numref}`fig_ex-dispersione`, con indicazione degli scarti
tra i punti di massa e il valore atteso. Nella parte alta del grafico viene
evidenziato il calcolo della varianza.
````

Varianza e deviazione standard sono legate da una trasformazione monotona,
quindi in generale racchiudono lo stesso tipo di informazione: più il loro
valore è vicino a zero, più la distribuzione tende a essere concentrata
attorno al valore atteso. La differenza tra i due indici è legata al fatto
che $\operatorname{Var}(X)$ è espressa in un'unità di misura che corrisponde
al quadrato dell'unità di misura di $X$, che molto spesso risulta difficile da
interpretare: per esempio, se $X$ indicasse i millilitri di precipitazione in
una data località in un mese, $\operatorname{Var}(X)$ sarebbe misurato in
$\mathrm{mL}^{2}$, un'unità dal significato poco intuitivo. La deviazione
standard, invece, è sempre espressa nella stessa unità di misura di $X$ e
risulta quindi più facilmente comprensibile.

````{prf:example}
:label: ex-deviazione-standard

Nell'{prf:ref}`ex-var-confronto` abbiamo trovato
$\operatorname{Var}(X) = 0.6$ e $\operatorname{Var}(Y) = 2.4$. Le
corrispondenti deviazioni standard sono quindi
$\operatorname{SD}(X) = \sqrt{0.6} \approx 0.77$ e
$\operatorname{SD}(Y) = \sqrt{2.4} \approx 1.55$. La seconda variabile ha
varianza maggiore, e giocoforza anche una maggiore deviazione standard, ma
quest'ultima ha il vantaggio di essere espressa nella stessa unità di misura
della variabile aleatoria: pur contenendo la stessa informazione della
varianza, risulta generalmente più immediata da interpretare.
````

La {prf:ref}`def-varianza` è concettualmente molto trasparente, ma non sempre è
la più comoda per i calcoli. Espandendo il quadrato, si ottiene una formula
equivalente, che risulta spesso più maneggevole.

````{prf:theorem}
:label: teo-var-alternative

Sia $X$ una variabile aleatoria che ammette valore atteso[^ex2-ex] e tale che
$X^2$ ammetta un valore atteso. Allora

```{math}
:label: eq_var-alternative

\operatorname{Var}(X) = \mathbb E \left( X^2 \right) - \mathbb E(X)^2 \enspace.
```
````
````{sds-proof}
Posto $\mu = \mathbb E(X)$, dalla definizione di varianza si ottiene

```{math}
\operatorname{Var}(X) = \mathbb E \left( (X - \mu)^2 \right)
                 = \mathbb E(X^2 - 2\mu X + \mu^2) \enspace.
```

Applicando le proprietà del valore atteso dimostrate a partire dal
{prf:ref}`teo-valore-atteso-trasf-affini`, si ricava

```{math}
\operatorname{Var}(X) = \mathbb E(X^2) - 2\mu\, \mathbb E(X) + \mu^2
                 = \mathbb E(X^2) - 2\mu^2 + \mu^2
                 = \mathbb E(X^2) - \mathbb E(X)^2 \enspace.
```

````

````{prf:example}
:label: ex-var-formula-alternativa

Riprendendo l'{prf:ref}`ex-var-confronto`, si ha

```{math}
\begin{align*}
\mathbb E(X^2) &= 9 \cdot 0.1 + 25 \cdot 0.7 + 36 \cdot 0.2 = 25.6
                  \enspace, \\
\mathbb E(Y^2) &= 1 \cdot 0.1 + 25 \cdot 0.7 + 49 \cdot 0.2 = 27.4
                  \enspace.
\end{align*}
```

Siccome $\mathbb E(X) = \mathbb E(Y) = 5$, e dunque
$\mathbb E(X)^2 = \mathbb E(Y)^2 = 25$, si ricava
$\operatorname{Var}(X) = 25.6 - 25 = 0.6$ e
$\operatorname{Var}(Y) = 27.4 - 25 = 2.4$, in linea con quanto ricavato
nell'{prf:ref}`ex-var-confronto`.
````

````{prf:example}
:label: ex-var-indicatrice

Sia $I_A$ la variabile indicatrice di un evento $A$, e sia
$p = \mathbb P(A)$.
Poiché $I_A$ può assumere solo i valori $0$ e $1$, si ha $I_A^2 = I_A$.
Pertanto, usando {eq}`eq_var-alternative`,

```{math}
\operatorname{Var}(I_A) = \mathbb E(I_A^2) - \mathbb E(I_A)^2
                   = \mathbb E(I_A) - \mathbb E(I_A)^2
                   = p - p^2 = p(1-p) \enspace.
```

La varianza è nulla solo quando l'evento è certo oppure impossibile. È invece
più grande quando l'esito è più incerto, e raggiunge il proprio massimo quando
$p = 0.5$.
````

````{prf:example}
:label: ex-var-dado

Sia $X$ la variabile aleatoria che descrive il risultato del lancio di un dado
bilanciato a sei facce. Nell'{prf:ref}`ex-ea-dado` abbiamo calcolato
$\mathbb E(X) = \frac{7}{2}$, pertanto si avrà

```{math}
\operatorname{Var}(X) = \sum_{i=1}^6 \left(i - \frac{7}{2}\right)^2 \frac{1}{6}
                        \enspace,
```

che, anche riconoscendo la simmetria dei valori  elevati al quadrato, risulta
relativamente poco pratica da calcolare. D'altro canto, applicando
{eq}`eq_sum-pow-2` si ottiene

```{math}
\mathbb E(X^2) = \sum_{i=1}^6 i^2 \frac{1}{6}
               = \frac{1}{6} \sum_{i=1}^6 i^2
               = \frac{1}{6} \frac{6 \cdot 7 \cdot 13}{6}
               = \frac{91}{6} \enspace,
```

e {eq}`eq_var-alternative` permette di ricavare

```{math}
\operatorname{Var}(X) = \mathbb E(X^2) - \mathbb E(X)^2
                      = \frac{91}{6} - \left(\frac{7}{2}\right)^2
                      = \frac{35}{12} \enspace.
```

````

Nel paragrafo precedente abbiamo visto che se si trasforma una
variabile aleatoria mediante una funzione affine $x \mapsto ax+b$, il valore
atteso della variabile trasformata è legato a quello della variabile originale
dalla stessa trasformazione. È naturale chiedersi che cosa accada invece alla
varianza. La risposta è semplice: una traslazione non cambia la dispersione
catturata da questo indice, mentre una riscalatura la moltiplica per il
quadrato del fattore.

````{prf:theorem} Varianza di trasformazioni affini
:label: teo-var-trasf-affini

Sia $X$ una variabile aleatoria che ammette varianza e siano $a, b \in \mathbb
R$. Allora

```{math}
\operatorname{Var}(aX + b) = a^2 \, \operatorname{Var}(X) \enspace.
```
````
````{sds-proof}
Per il {prf:ref}`teo-valore-atteso-trasf-affini`, si ha
$\mathbb E(aX+b) = a\,\mathbb E(X) + b$. Pertanto

```{math}
\begin{align*}
\operatorname{Var}(a X + b)
   &= \mathbb E\left(\left(a X + b - \mathbb E(a X + b)\right)^2\right) \\
   &= \mathbb E\left(\left(a X + b - a\mathbb E(X)- b \right)^2\right) \\
   &= \mathbb E\left(\left(a(X - \mathbb E(X))\right)^2\right) \\
   &= a^2 \, \mathbb E\left((X - \mathbb E(X))^2\right) \\
   &= a^2 \, \operatorname{Var}(X) \enspace,
\end{align*}
```

che conclude la dimostrazione.
````

Tre conseguenze particolarmente utili sono le seguenti:

- per ogni $b \in \mathbb R$, $\operatorname{Var}(X+b) =
  \operatorname{Var}(X)$, a riprova del fatto che la traslazione è
  un'operazione che non modifica la dispersione dei valori coinvolti;
- per ogni $a \in \mathbb R$, $\operatorname{Var}(aX) = a^2
  \operatorname{Var}(X)$, dunque riscalare la descrizione dei valori di $X$
  (per esempio modificando l'unità di misura) modifica quadraticamente la loro
  varianza;
- per ogni $b \in \mathbb R$,
  $\operatorname{Var}(b) = \operatorname{Var}(0 \cdot X + b) = 0$, e dunque
  le variabili aleatorie degeneri hanno varianza e deviazione standard nulla,
  come è naturale attendersi, perché l'unico valore osservabile coincide con
  il valore atteso.

````{prf:example} Cambiare origine e cambiare scala
:label: ex-var-trasf-affini

Sia $X$ la distanza, in metri, coperta da un balzo d'ombra di
{extlink}`Silhouette <https://marvel.fandom.com/wiki/Silhouette_Chord_(Earth-616)>`,
e supponiamo che $\operatorname{Var}(X) = 9 \, \mathrm{m}^2$. Se un nuovo
sensore misura la stessa distanza a partire da una piattaforma spostata di due
metri, la variabile osservata diventa $Y = X + 2$. In questo caso

```{math}
\operatorname{Var}(Y) = \operatorname{Var}(X+2) = \operatorname{Var}(X)
                      = 9 \, \mathrm{m}^2 \enspace.
```

Se invece vogliamo esprimere la stessa distanza in centimetri, dobbiamo porre
$Z = 100 X$, e allora

```{math}
\operatorname{Var}(Z) = \operatorname{Var}(100X) 
                      = 100^2 \, \operatorname{Var}(X)
                      = 10\,000 \cdot 9 = 90\,000 \mathrm{cm}^2 \enspace.
```

La dispersione fisica non è cambiata: è cambiata solo l'unità di misura, e per
questo la varianza viene moltiplicata per il quadrato del fattore di
conversione: nove metri quadrati corrispondono infatti a novantamila centimetri
quadrati.
````

````{customfigure}
:name: fig_ex-var-trasf-affini
:class: left-align

```{interactive-code} python
:tags: [toggle-code]

import matplotlib.pyplot as plt
import numpy as np
from pyscript import display
from pyscript.web import page, when


fig_affine, ax_affine = plt.subplots()
base_values_affine = np.array([3.0, 5.0, 6.0])
probabilities_affine = np.array([0.1, 0.7, 0.2])

stem_lines_affine = ax_affine.vlines(base_values_affine, 0, probabilities_affine)
point_markers_affine, = ax_affine.plot(base_values_affine, probabilities_affine,
                                       'o', color='C0')

ax_affine.set_xlabel(r'$x$')
ax_affine.set_ylabel(r'$p_{aX+b}$')
ax_affine.set_ylim(0, 1.05)
ax_affine.set_xlim(-20.5, 20.5)


def aggregate_pmf(values, probabilities):
  rounded_values = np.round(values, 10)
  order = np.argsort(rounded_values)
  sorted_values = rounded_values[order]
  sorted_probabilities = probabilities[order]

  aggregated_values = []
  aggregated_probabilities = []

  for value, probability in zip(sorted_values, sorted_probabilities):
    if aggregated_values and abs(value - aggregated_values[-1]) < 1e-9:
      aggregated_probabilities[-1] += probability
    else:
      aggregated_values.append(value)
      aggregated_probabilities.append(probability)

  return np.array(aggregated_values), np.array(aggregated_probabilities)


def render_affine_plot():
  a = float(page['#affine-a'][0].value)
  b = float(page['#affine-b'][0].value)

  transformed_values = a * base_values_affine + b
  plot_values, plot_probabilities = aggregate_pmf(transformed_values,
                                                  probabilities_affine)
  segments = [((value, 0), (value, probability))
              for value, probability in zip(plot_values, plot_probabilities)]

  stem_lines_affine.set_segments(segments)
  point_markers_affine.set_data(plot_values, plot_probabilities)

  page['#affine-a-value'][0].innerHTML = f'{a:.2f}'
  page['#affine-b-value'][0].innerHTML = f'{b:.2f}'

  display(fig_affine, target='graph-%this%', append=False)


@when('input', '#affine-a, #affine-b')
def update_affine_plot(event):
  render_affine_plot()


render_affine_plot()
```

```{raw} html
<div class="plot-container">
   <div class="model-slider-container" style="display: flex; flex-wrap: wrap; gap: 0.75rem 1rem; align-items: center;">
      <label for="affine-a">\(a\): </label>
      <input type="range" id="affine-a" min="-2.00" max="2.00" value="1.00" step="0.05" />
      <span id="affine-a-value">1.00</span>
      <label for="affine-b">\(b\): </label>
      <input type="range" id="affine-b" min="-4.00" max="4.00" value="0.00" step="0.05" />
      <span id="affine-b-value">0.00</span>
   </div>
</div>
```

Distribuzione iniziale delle Figure {numref}`{number} <fig_ex-dispersione>` e {numref}`{number} <fig_ex-varianza>`, trasformata nella distribuzione di
$a X + b$ al variare di $a$ e $b$. Quando $a=1$ e $b=0$, si recupera
esattamente la funzione di massa di probabilità di $X$.
````

````{prf:corollary}
:label: teo-sd-trasf-affini

Sia $X$ una variabile aleatoria che ammette deviazione standard e siano
$a, b \in \mathbb R$. Allora

```{math}
\operatorname{SD}(aX + b) = \lvert a \rvert \, \operatorname{SD}(X) \enspace.
```
````
````{sds-proof}
Applicando il {prf:ref}`teo-var-trasf-affini` si ottiene direttamente

```{math}
\begin{align*}
\operatorname{SD}(a X + b) &= \sqrt{\operatorname{Var}(a x + b)} \\
   &= \sqrt{a^2 \, \operatorname{Var}(X)} \\
   &= \lvert a \rvert \, \operatorname{SD}(X) \enspace.
\end{align*}
```
````

Anche in questo caso, come conseguenza si otiene che la deviazione standard
non viene influenzata da una traslazione; ora, però, l'effetto di un'eventuale
riscalatura è quello di moltiplicare la deviazione standard per il 
corrispondente fattore di conversione: per ogni $a \in \mathbb R$,
$\operatorname{SD}(a X) = \lvert a \rvert \operatorname{SD}(X)$.

````{prf:example}
:label: ex-sd-trasf-affini

Riprendendo l'{prf:ref}`ex-var-trasf-affini`, avremo 
$\operatorname{SD}(Y) = \operatorname{SD}(X) = 3 \, \mathrm{m}$ e
$\operatorname{SD}(Z) = 100 \operatorname{SD}(X) = 300 \, \mathrm{cm}$.
````

Varianza e deviazione standard sono spesso usate in parallelo: la prima perché
è algebricamente più comoda da trattare e si combina molto bene con le
trasformazioni e con le somme di variabili aleatorie; la seconda perché è più
immediata da interpretare e da comunicare.

Nell'{prf:ref}`ex-ea-centratura` abbiamo visto che è possibile centrare una
variabile aleatoria, sottraendole il suo valore atteso. Applicando
successivamente un'opportuna scalatura, si ottiene una trasformazione di
particolare importanza per lo studio delle distribuzioni.

````{prf:definition} Standardizzazione di una variabile aleatoria
:label: def-standardizzazione-va

```{margin}
Si usa il termine _standardizzazione_ anche per indicare più in generale la
trasformazione che sottrae il valore atteso e divide per la deviazione
standard.
```
Sia $X$ una variabile aleatoria che ammette valore atteso $\mu$ e varianza
$\sigma^2$. La variabile aleatoria

```{math}
X' = \frac{X-\mu}{\sigma}
```

viene detta _standardizzazione_ di $X$.
````

````{prf:corollary}
:label: cor-standardizzazione-va

Sia $X$ una variabile aleatoria che ammette varianza. La sua standardizzazione
$X'$ è tale che

```{math}
\begin{aligned}
\mathbb E(X')          &= 0 \enspace,
\operatorname{Var}(X') &= 1 \enspace.
\end{aligned}
```
````
````{sds-proof}
Sia $\sigma^2$ la varianza di $X$, e sia $\mu$ il suo valore atteso, che
deve necessariamente esistere perché esiste la varianza. Applicando il
{prf:ref}`teo-valore-atteso-trasf-affini` si ottiene immediatamente

```{math}
\mathbb E(X') = \frac{1}{\sigma} \, \mathbb E(X - \mu) = 0 \enspace.
```
Analogamente, il {prf:ref}`teo-var-trasf-affini` assicura che

```{math}
\operatorname{Var}(X') = \frac{1}{\sigma^2}\operatorname{Var}(X - \mu)
= \frac{\operatorname{Var}(X)}{\sigma^2} = 1 \enspace.
```
````

In generale, si può studiare la dispersione di $X$ attorno a un qualsiasi
valore $c \in \mathbb R$. Se si continuano a utilizzare gli scarti quadratici,
ciò equivale a considerare il valore atteso $\mathbb E\left((X-c)^2\right)$. La
varianza, che corrisponde al caso particolare in cui $c = \mathbb E(X)$,
soddisfa una particolare proprietà. Infatti, posto $\mu = \mathbb E(X)$, si ha
ovviamente $X - c = (X - \mu) + (\mu - c)$. Pertanto

```{math}
\begin{align*}
\mathbb E\left((X-c)^2\right)
   &= \mathbb E\left(\left((X-\mu) + (\mu-c)\right)^2\right) \\
   &= \mathbb E\left((X-\mu)^2\right) + 2(\mu-c)\mathbb E(X-\mu) + (\mu-c)^2 \\
   &= \operatorname{Var}(X) + (\mu-c)^2 \enspace,
\end{align*}
```

poiché $\mathbb E(X-\mu) = \mathbb E(X)-\mu = 0$. Siccome il termine
$(\mu - c)^2$ è sempre non negativo,
$\mathbb E\left((X-c)^2\right) \geq \operatorname{Var}(X)$, e la quantità
$\mathbb E\left((X-c)^2\right)$ è minima esattamente quando $c = \mathbb E(X)$.
Questo risultato chiarisce un punto importante: il valore atteso non è soltanto
un valore centrale naturale, ma è anche il riferimento che rende minima la
dispersione misurata tramite gli scarti quadratici,come esemplificato nella
{numref}`fig_ex-scarto-quadratico-c`.

````{customfigure}
:name: fig_ex-scarto-quadratico-c
:class: left-align

```{interactive-code} python
:tags: [toggle-code]

import matplotlib.pyplot as plt
import numpy as np
from pyscript import display
from pyscript.web import page, when


fig_c, ax_c = plt.subplots()
values_c = np.array([3.0, 5.0, 6.0])
probabilities_c = np.array([0.1, 0.7, 0.2])
initial_c = 5.0

stem_lines_c = ax_c.vlines(values_c, 0, probabilities_c)
point_markers_c, = ax_c.plot(values_c, probabilities_c, 'o', color='C0')
center_line_c = ax_c.axvline(initial_c, color='#cc6600', linestyle='--', linewidth=1.2)
arrow_levels_c = np.array([0.28, 0.5, 0.82])
distance_arrows_c = [
  FancyArrowPatch((value, level), (initial_c, level), arrowstyle='<->',
          mutation_scale=11, linewidth=1.0, color='#9aa3ad')
  for value, level in zip(values_c, arrow_levels_c)
]
for arrow in distance_arrows_c:
  ax_c.add_patch(arrow)
arrow_labels_c = [
  ax_c.text((value + initial_c) / 2, level + 0.02, '', ha='center',
        va='bottom', color='#7f8790')
  for value, level in zip(values_c, arrow_levels_c)
]
distance_labels_c = [
    ax_c.text(value, probability + 0.04, '', ha='center', va='bottom', color='#7f8790')
    for value, probability in zip(values_c, probabilities_c)
]

ax_c.set_xlabel(r'$x$')
ax_c.set_ylabel(r'$p_X$')
ax_c.set_xlim(1.5, 7.0)
ax_c.set_ylim(0, 1.0)


def render_c_plot():
  c = float(page['#center-c'][0].value)
  distances = values_c - c
  squared_distances = (values_c - c) ** 2
  expected_dispersion = np.dot(probabilities_c, squared_distances)

  center_line_c.set_xdata([c, c])

  for arrow, label, value, level, distance in zip(
      distance_arrows_c, arrow_labels_c, values_c, arrow_levels_c, distances):
    if abs(distance) < 1e-9:
      arrow.set_positions((c - 0.03, level), (c + 0.03, level))
      label.set_position((c, level + 0.02))
    else:
      arrow.set_positions((value, level), (c, level))
      label.set_position(((value + c) / 2, level + 0.02))
    label.set_text(f'${distance:.2f}$')



  page['#center-c-value'][0].innerHTML = f'{c:.2f}'

  ax_c.set_title(
      rf'$\mathbb{{E}}\left((X-{c:.2f})^2\right) = {expected_dispersion:.2f}$')

  display(fig_c, target='graph-%this%', append=False)


@when('input', '#center-c')
def update_c_plot(event):
  render_c_plot()


render_c_plot()
```

```{raw} html
<div class="plot-container">
   <div class="model-slider-container" style="display: flex; flex-wrap: wrap; gap: 0.75rem 1rem; align-items: center;">
      <label for="center-c">Valore centrale \(c\): </label>
      <input type="range" id="center-c" min="2.00" max="6.50" value="5.00" step="0.05" />
      <span id="center-c-value">5.00</span>
   </div>
</div>
```

Distribuzione iniziale delle Figure {numref}`{number} <fig_ex-dispersione>` e
{numref}`{number} <fig_ex-varianza>`, con un segmento verticale mobile che
identifica il valore centrale $c$. Spostando il selettore si aggiornano i
valori dei singoli scarti e quello di $\mathbb E((X-c)^2)$, mostrando come la
dispersione quadratica attorno a $c$ venga minimizzata quando
$c = \mathbb E(X)$.
````

Naturalmente, lo scarto quadratico non è l'unico modo per misurare la
dispersione attorno a un valore assegnato $c$. Si possono considerare, per
esempio:

- lo _scarto assoluto medio_ attorno a $c$, dato da
  $\mathbb E(\lvert X-c\rvert)$, che penalizza meno fortemente gli scarti molto
  grandi e conduce a proprietà di ottimalità diverse, legate alla mediana più
  che alla media[^mae-mediana];
- gli _scarti di ordine_ $p$, della forma $\mathbb E(\lvert X-c \rvert^p)$ per
  $p > 0$, che generalizzano sia il caso assoluto ($p=1$) sia quello
  quadratico ($p=2$).

La scelta dell'indice dipende dunque dal tipo di applicazione e da quali scarti
si desidera pesare maggiormente. La varianza resta però particolarmente
importante perché combina una chiara interpretazione geometrica con particolari
proprietà algebriche che vedremo nel seguito.

(sec:quantili)=
## Quantili

Un secondo modo di descrivere la dispersione di una variabile aleatoria non
consiste nel misurarne gli scarti rispetto a un singolo valore centrale, ma
nel guardare come la massa di probabilità si distribuisce lungo la retta
reale. In quest'ottica entrano in gioco i _quantili_, che sono delle soglie
capaci di suddividere la massa di probabilità in due parti ben definite.

````{prf:definition} Quantili di una variabile aleatoria discreta
:label: def-quantili-va-discreta

Sia $X$ una variabile aleatoria discreta e sia $q \in (0,1)$. Si dice
_quantile di livello_ $q$ di $X$ il valore

```{math}
x_q \triangleq \min_x \mathbb P(X \leq x) \geq q \enspace.
```

````

In altre parole, una volta fissato il livello, il quantile $x_q$ permette di
suddividere la massa di probabilità in due parti:

- la prima è associata all'insieme $(-\infty, x_q]$, sul quale $X$ assume
  probabilità almeno $q$;
- la seconda corrisponde a $(x_q, +\infty)$, in cui $X$ assume probabilità
  al più $1 - q$.

In particolare, la mediana (vedi {prf:ref}`def-mediana-va-discreta`) può essere
vista come un quantile di livello $0.5$, o, alternativamente, i quantili si
possono pensare come a una generalizzazione del concetto di mediana.

Se $F_X$ denota la funzione di ripartizione di $X$, allora $x_q$ è anche il più
piccolo valore per cui $F_X(x_q) \geq q$. Siccome siamo nel caso discreto,
$F_X$ è costante a tratti, e dunque cresce per salti. Di conseguenza, un
quantile è il primo punto in cui la probabilità cumulata raggiunge oppure
supera il livello richiesto. Tuttavia, una volta raggiunto $x_q$, la
disuguaglianza $F_X(x) \geq q$ continua in generale a valere anche per tutti i
valori successivi $x \geq x_q$. È per questo che la
{prf:ref}`def-quantili-va-discreta` richiede di considerare il più piccolo tra
essi, così da definire il quantile in modo univoco.

````{prf:example}
:label: ex-quantili-perfetto

Consideriamo la distribuzione illustrata in {numref}`fig_ex-quantili-salti-05`,
che fa riferimento a una variabile aleatoria $X$ con supporto e funzione di
massa di probabilità definiti nella tabella che segue.

| $x$ |  $p_X(x)$ |
| :-: | :-------: |
| $1$ | $0.2$     |
| $2$ | $0.3$     |
| $4$ | $0.3$     |
| $6$ | $0.2$     |

La {numref}`fig_ex-quantili-salti-05` mostra il grafico della funzione di massa
di probabilità di $X$, evidenziando come il quantile di livello $0.5$ sia
$x_{0.5} = 2$. Infatti, $F_X(2) = 0.2 + 0.3 = 0.5$, mentre per ogni $x < 2$ si
ha $F_X(x) < 0.5$. Interagendo con il grafico, è possibile selezionare un
qualsiasi punto sull'asse delle ascisse, visualizzando il corrispondente valore
di $F_X$ e marcando rispettivamente con ✓ e ✕ i casi nei quali il punto
selezionato soddisfi oppure no la condizione alla base della
{prf:ref}`def-quantili-va-discreta`. Agendo sul selettore nella figura, si
vede che tutti e soli i punti $x > 2$ soddisfano questa condizione, dunque
il quantile deve essere il più piccolo tra essi, che è appunto $2$.
````

````{customfigure}
:name: fig_ex-quantili-salti-05
:class: left-align

```{interactive-code} python
:tags: [toggle-code]

import matplotlib.pyplot as plt
import numpy as np
from pyscript import display
from pyscript.web import page, when


support_jump_05 = np.array([1.0, 2.0, 4.0, 6.0])
support_jump_05_label = [f'{l:.0f}' for l in support_jump_05]
support_jump_05_label[1] = r'$x_{0.5} = 2$'
probabilities_jump_05 = np.array([0.2, 0.3, 0.3, 0.2])
cdf_jump_05 = np.cumsum(probabilities_jump_05)
right_endpoints_jump_05 = np.append(support_jump_05[1:], support_jump_05[-1] + 1)
ytick_labels_jump_05 = [f'{value:.1f}' for value in cdf_jump_05]
fixed_level_jump_05 = 0.5
quantile_index_jump_05 = int(np.searchsorted(cdf_jump_05, fixed_level_jump_05, side='left'))
quantile_jump_05 = support_jump_05[quantile_index_jump_05]
previous_cdf_jump_05 = 0.0 if quantile_index_jump_05 == 0 else cdf_jump_05[quantile_index_jump_05 - 1]

fig_jump_05, ax_jump_05 = plt.subplots()
ax_jump_05.hlines(
  np.concatenate(([0.0], cdf_jump_05)),
  np.concatenate(([0.5], support_jump_05)),
  np.concatenate(([1.0], right_endpoints_jump_05)),
  color='#006699', linewidth=1)
highlight_plateau_jump_05 = ax_jump_05.hlines(
  cdf_jump_05[quantile_index_jump_05], quantile_jump_05, right_endpoints_jump_05[quantile_index_jump_05],
  color='#cc6600', linewidth=1)
ax_jump_05.plot(support_jump_05, cdf_jump_05, linestyle='None', marker='o',
                color='#006699', zorder=3)
ax_jump_05.plot(np.concatenate(([support_jump_05[0]], right_endpoints_jump_05[:-1])),
                np.concatenate(([0.0], cdf_jump_05[:-1])),
                linestyle='None', marker='o', markerfacecolor='white',
                markeredgecolor='#006699', markeredgewidth=0.8, zorder=3)
lower_quantile_marker_jump_05, = ax_jump_05.plot(
  [quantile_jump_05], [previous_cdf_jump_05], linestyle='None', marker='o',
  markerfacecolor='white', markeredgecolor='#cc6600',
  markeredgewidth=0.8, zorder=4)
upper_quantile_marker_jump_05, = ax_jump_05.plot(
  [quantile_jump_05], [cdf_jump_05[quantile_index_jump_05]], linestyle='None', marker='o',
  color='#cc6600', zorder=5)
level_line_jump_05, = ax_jump_05.plot(
  [0.5, 7.1], [fixed_level_jump_05, fixed_level_jump_05], color='#cc6600',
  linestyle='--', linewidth=.8)
quantile_line_jump_05, = ax_jump_05.plot(
  [quantile_jump_05, quantile_jump_05], [-0.02, 1.05], color='#cc6600',
  linestyle='--', linewidth=.8)
probe_line_jump_05, = ax_jump_05.plot(
  [quantile_jump_05, quantile_jump_05], [0.0, cdf_jump_05[quantile_index_jump_05]], color='#2a7f62',
  linestyle='--', linewidth=.9)
probe_marker_jump_05, = ax_jump_05.plot(
  [quantile_jump_05], [cdf_jump_05[quantile_index_jump_05]], linestyle='None', marker='o',
  color='#2a7f62', zorder=5)

ax_jump_05.set_xticks(support_jump_05)
ax_jump_05.set_xticklabels(support_jump_05_label)
ax_jump_05.set_yticks(np.concatenate(([0.0], cdf_jump_05)))
ax_jump_05.set_yticklabels(['0.0'] + ytick_labels_jump_05)
ax_jump_05.set_xlim(0.5, 7.1)
ax_jump_05.set_ylim(-0.02, 1.05)
ax_jump_05.set_xlabel(r'$x$')
ax_jump_05.set_ylabel(r'$F_X(x)$')
ax_jump_05.grid(axis='y', alpha=0.15)


def cdf_at_point_jump_05(x_value):
  index = np.searchsorted(support_jump_05, x_value, side='right') - 1
  if index < 0:
    return 0.0
  return cdf_jump_05[index]


def render_jump_quantile_plot_05():
  x_value = float(page['#quantile-probe-x-05'][0].value)
  cdf_value = cdf_at_point_jump_05(x_value)
  
  cdf_status = '✓' if cdf_value >= fixed_level_jump_05 else '✕'

  highlight_plateau_jump_05.set_segments(
    [[(quantile_jump_05, fixed_level_jump_05),
      (right_endpoints_jump_05[quantile_index_jump_05], fixed_level_jump_05)]])
  probe_line_jump_05.set_data([x_value, x_value], [0.0, cdf_value])
  probe_marker_jump_05.set_data([x_value], [cdf_value])
  lower_quantile_marker_jump_05.set_data([quantile_jump_05], [previous_cdf_jump_05])
  upper_quantile_marker_jump_05.set_data([quantile_jump_05], [fixed_level_jump_05])
  level_line_jump_05.set_data([0.5, 7.1], [fixed_level_jump_05, fixed_level_jump_05])
  quantile_line_jump_05.set_data([quantile_jump_05, quantile_jump_05], [-0.02, 1.05])

  page['#quantile-probe-x-value-05'][0].innerHTML = f'{x_value:.2f}'
  page['#quantile-probe-cdf-value-05'][0].innerHTML = f'{cdf_value:.2f}'
  page['#quantile-probe-cdf-status-05'][0].innerHTML = cdf_status

  display(fig_jump_05, target='graph-%this%', append=False)


@when('input', '#quantile-probe-x-05')
def update_jump_quantile_plot_05(event):
  render_jump_quantile_plot_05()


render_jump_quantile_plot_05()
```

```{raw} html
<div class="plot-container">
  <div class="model-slider-container" style="display: flex; flex-wrap: wrap; gap: 0.75rem 1rem; align-items: center;">
      <label for="quantile-probe-x-05">\(x\): </label>
      <input type="range" id="quantile-probe-x-05" min="0.50" max="6.80" value="2.00" step="0.05" />
      <span id="quantile-probe-x-value-05">2.00</span>
      <span>\(\mathbb P(X \leq x) = \)<span id="quantile-probe-cdf-value-05" style="margin-left: 0.3em;">0.50</span><span id="quantile-probe-cdf-status-05" style="margin-left: 0.35em;">✓</span></span>
   </div>
</div>
```

Funzione di ripartizione della variabile aleatoria descritta
nell'{prf:ref}`ex-quantili-perfetto`, evidenziando il quantile $x_{0.5}$. Il
selettore permette di considerare un qualunque punto $x$ sull'asse delle
ascisse, mostrando il valore di $\mathbb P(X \leq x)$ ed evidenziando quando
questo soddisfa la condizione alla base della
{prf:ref}`def-quantili-va-discreta`.
````

Nell'esempio precedente, il valore della funzione di ripartizione calcolato sul
quantile selezionato è esattamente uguale al livello: ciò è dovuto al fatto
che, passando dal punto di massa $x = 1$ a quello appena successivo, $F_X$
aumenta da $0.2$ a $0.5$, che è esattamente il livello richiesto. Siccome in
una variabile discreta la ripartizione aumenta «per salti», questo
comportamento non è assolutamente garantito, come evidenziato nel seguente
esempio.

````{prf:example}
:label: ex-quantili-imperfetto

La {numref}`fig_ex-quantili-salti-06` mostra la stessa distribuzione
dell'{prf:ref}`ex-quantili-perfetto`, concentrandosi sul quantile $x_{0.6}$.
In questo caso, passando da $x = 2$ a $x = 4$, $F_X$ aumenta da $0.5$ a $0.8$.
Pertanto, $x_{0.6} = 4$, ma $F_X(x_{0.6}) \neq 0.6$.
````

````{customfigure}
:name: fig_ex-quantili-salti-06
:class: left-align

```{interactive-code} python
:tags: [toggle-code]

import matplotlib.pyplot as plt
import numpy as np
from pyscript import display
from pyscript.web import page, when


support_jump_06 = np.array([1.0, 2.0, 4.0, 6.0])
support_jump_06_label = [f'{l:.0f}' for l in support_jump_06]
support_jump_06_label[2] = r'$x_{0.6} = 4$'
probabilities_jump_06 = np.array([0.2, 0.3, 0.3, 0.2])
cdf_jump_06 = np.cumsum(probabilities_jump_06)
right_endpoints_jump_06 = np.append(support_jump_06[1:], support_jump_06[-1] + 1)
ytick_labels_jump_06 = [f'{value:.1f}' for value in cdf_jump_06]
fixed_level_jump_06 = 0.6
quantile_index_jump_06 = int(np.searchsorted(cdf_jump_06, fixed_level_jump_06, side='left'))
quantile_jump_06 = support_jump_06[quantile_index_jump_06]
previous_cdf_jump_06 = 0.0 if quantile_index_jump_06 == 0 else cdf_jump_06[quantile_index_jump_06 - 1]

fig_jump_06, ax_jump_06 = plt.subplots()
ax_jump_06.hlines(
  np.concatenate(([0.0], cdf_jump_06)),
  np.concatenate(([0.5], support_jump_06)),
  np.concatenate(([1.0], right_endpoints_jump_06)),
  color='#006699', linewidth=1)
highlight_plateau_jump_06 = ax_jump_06.hlines(
  cdf_jump_06[quantile_index_jump_06], quantile_jump_06, right_endpoints_jump_06[quantile_index_jump_06],
  color='#cc6600', linewidth=1)
ax_jump_06.plot(support_jump_06, cdf_jump_06, linestyle='None', marker='o',
                color='#006699', zorder=3)
ax_jump_06.plot(np.concatenate(([support_jump_06[0]], right_endpoints_jump_06[:-1])),
                np.concatenate(([0.0], cdf_jump_06[:-1])),
                linestyle='None', marker='o', markerfacecolor='white',
                markeredgecolor='#006699', markeredgewidth=0.8, zorder=3)
lower_quantile_marker_jump_06, = ax_jump_06.plot(
  [quantile_jump_06], [previous_cdf_jump_06], linestyle='None', marker='o',
  markerfacecolor='white', markeredgecolor='#cc6600',
  markeredgewidth=0.8, zorder=4)
upper_quantile_marker_jump_06, = ax_jump_06.plot(
  [quantile_jump_06], [cdf_jump_06[quantile_index_jump_06]], linestyle='None', marker='o',
  color='#cc6600', zorder=5)
level_line_jump_06, = ax_jump_06.plot(
  [0.5, 7.1], [fixed_level_jump_06, fixed_level_jump_06], color='#cc6600',
  linestyle='--', linewidth=.8)
quantile_line_jump_06, = ax_jump_06.plot(
  [quantile_jump_06, quantile_jump_06], [-0.02, 1.05], color='#cc6600',
  linestyle='--', linewidth=.8)
probe_line_jump_06, = ax_jump_06.plot(
  [quantile_jump_06, quantile_jump_06], [0.0, cdf_jump_06[quantile_index_jump_06]], color='#2a7f62',
  linestyle='--', linewidth=.9)
probe_marker_jump_06, = ax_jump_06.plot(
  [quantile_jump_06], [cdf_jump_06[quantile_index_jump_06]], linestyle='None', marker='o',
  color='#2a7f62', zorder=5)

ax_jump_06.set_xticks(support_jump_06)
ax_jump_06.set_yticks(np.concatenate(([0.0], cdf_jump_06)))
ax_jump_06.set_yticklabels(['0.0'] + ytick_labels_jump_06)
ax_jump_06.set_xlim(0.5, 7.1)
ax_jump_06.set_ylim(-0.02, 1.05)
ax_jump_06.set_xlabel(r'$x$')
ax_jump_06.set_ylabel(r'$F_X(x)$')
ax_jump_06.grid(axis='y', alpha=0.15)


def cdf_at_point_jump_06(x_value):
  index = np.searchsorted(support_jump_06, x_value, side='right') - 1
  if index < 0:
    return 0.0
  return cdf_jump_06[index]


def render_jump_quantile_plot_06():
  x_value = float(page['#quantile-probe-x-06'][0].value)
  cdf_value = cdf_at_point_jump_06(x_value)

  cdf_status = '✓' if cdf_value >= fixed_level_jump_06 else '✕'

  highlight_plateau_jump_06.set_segments(
    [[(quantile_jump_06, cdf_jump_06[quantile_index_jump_06]),
      (right_endpoints_jump_06[quantile_index_jump_06], cdf_jump_06[quantile_index_jump_06])]])
  probe_line_jump_06.set_data([x_value, x_value], [0.0, cdf_value])
  probe_marker_jump_06.set_data([x_value], [cdf_value])
  lower_quantile_marker_jump_06.set_data([quantile_jump_06], [previous_cdf_jump_06])
  upper_quantile_marker_jump_06.set_data([quantile_jump_06], [cdf_jump_06[quantile_index_jump_06]])
  level_line_jump_06.set_data([0.5, 7.1], [fixed_level_jump_06, fixed_level_jump_06])
  quantile_line_jump_06.set_data([quantile_jump_06, quantile_jump_06], [-0.02, 1.05])

  page['#quantile-probe-x-value-06'][0].innerHTML = f'{x_value:.2f}'
  page['#quantile-probe-cdf-value-06'][0].innerHTML = f'{cdf_value:.2f}'
  page['#quantile-probe-cdf-status-06'][0].innerHTML = cdf_status

  display(fig_jump_06, target='graph-%this%', append=False)


@when('input', '#quantile-probe-x-06')
def update_jump_quantile_plot_06(event):
  render_jump_quantile_plot_06()


render_jump_quantile_plot_06()
```

```{raw} html
<div class="plot-container">
   <div class="model-slider-container" style="display: flex; flex-wrap: wrap; gap: 0.75rem 1rem; align-items: center;">
      <label for="quantile-probe-x-06">\(x\): </label>
      <input type="range" id="quantile-probe-x-06" min="0.50" max="6.80" value="4.00" step="0.05" />
      <span id="quantile-probe-x-value-06">4.00</span>
      <span>\(\mathbb P(X \leq x) = \)<span id="quantile-probe-cdf-value-06">0.80</span><span id="quantile-probe-cdf-status-06" style="margin-left: 0.35em;">✓</span></span>
   </div>
</div>
```

Funzione di ripartizione della variabile aleatoria descritta
nell'{prf:ref}`ex-quantili-imperfetto`, evidenziando il quantile $x_{0.6}$.
Stessa notazione della {numref}`fig_ex-quantili-salti-05`.
````

````{prf:example}
:label: ex-quantili-dado

Consideriamo la variabile aleatoria $X$ che descrive il risultato del lancio di
un dado bilanciato a sei facce. Per ogni $k \in \{1,\dots,6\}$ si ha
$\mathbb P(X = x) = \tfrac{1}{6}$, e quindi
$F_X(x) = \tfrac{\lfloor x \rfloor}{6}$ ogni volta che $1 \leq x \leq 6$. Ora,
affinché un valore $x$ sia candidato a essere il quantile di $X$ di un generico
livello $q$, deve valere $F_X(x) \geq q$, ovvero $\lfloor x \rfloor \geq 6 q$.
Pertanto,

```{math}
:label: eq-quantile-dado

x_q = \min_x \{ \lfloor x \rfloor \geq 6 q \} = \lceil 6q \rceil \enspace.
```

Per esempio, il quantile di livello $0.25$ è
$x_{0.25} = \lceil \tfrac{6}{4} \rceil = 2$, e la mediana è
$m = \lceil \tfrac{6}{2} \rceil = 3$. La {numref}`fig_ex-quantili-dado`
visualizza il grafico di $F_X$ e permette di evidenziare i quantili di $X$ in
modo interattivo: selezionando il livello $q$, la figura viene rigenerata
evidenziando $x_q$.

````

````{customfigure}
:name: fig_ex-quantili-dado
:class: left-align

```{interactive-code} python
:tags: [toggle-code]

from fractions import Fraction
import matplotlib.pyplot as plt
import numpy as np
from pyscript import display
from pyscript.web import page, when


v = np.arange(1, 7)
p = np.full(6, 1 / 6)
cdf_values = np.cumsum(p)
right_endpoints = np.append(v[1:], v[-1] + 1)
ticks = cdf_values
tick_labels = [str(Fraction(tick).limit_denominator(36)) for tick in ticks]

fig_quantile, ax_quantile = plt.subplots()
base_plateaus = ax_quantile.hlines(np.concatenate(([0], cdf_values)),
                                   np.concatenate(([0.5], v)),
                                   np.concatenate(([1.0], right_endpoints)),
                                   color='#006699', linewidth=2.2)
highlight_plateau = ax_quantile.hlines(cdf_values[0], v[0], v[1],
                                       color='#cc6600', linewidth=3.2)
closed_markers, = ax_quantile.plot(v, cdf_values, linestyle='None', marker='o',
                                   color='#006699', zorder=3)
open_markers, = ax_quantile.plot(np.concatenate(([v[0]], right_endpoints[:-1])),
                                 np.concatenate(([0.0], cdf_values[:-1])),
                                 linestyle='None', marker='o',
                                 markerfacecolor='white',
                                 markeredgecolor='#006699',
                                 markeredgewidth=0.8, zorder=3)
lower_quantile_marker, = ax_quantile.plot([v[0]], [0.0], linestyle='None',
                                          marker='o', markerfacecolor='white',
                                          markeredgecolor='#cc6600',
                                          markeredgewidth=0.8,                zorder=4)
upper_quantile_marker, = ax_quantile.plot([v[0]], [cdf_values[0]],
                                          linestyle='None', marker='o',
                                          color='#cc6600',
                                          zorder=5)
level_line, = ax_quantile.plot([0.5, 7.1], [cdf_values[0], cdf_values[0]],
                               color='#cc6600', linestyle='--', linewidth=.8)
quantile_line, = ax_quantile.plot([v[0], v[0]], [-0.02, 1.05],
                                  color='#cc6600', linestyle='--',
                                  linewidth=.8)

ax_quantile.set_xticks(v)
ax_quantile.set_yticks(np.concatenate(([0], ticks)))
ax_quantile.set_yticklabels(['0'] + tick_labels)
ax_quantile.set_xlim(0.5, 7.1)
ax_quantile.set_ylim(-0.02, 1.05)
ax_quantile.set_xlabel(r'$x$')
ax_quantile.set_ylabel(r'$F_X$')
ax_quantile.grid(axis='y', alpha=0.15)


def render_quantile_plot():
  level = float(page['#quantile-level'][0].value)
  quantile_index = int(np.searchsorted(cdf_values, level, side='left'))
  quantile = int(v[quantile_index])
  cdf_at_quantile = cdf_values[quantile_index]
  previous_cdf = 0.0 if quantile_index == 0 else cdf_values[quantile_index - 1]

  highlight_plateau.set_segments([[(quantile, cdf_at_quantile),
                                   (quantile + 1, cdf_at_quantile)]])
  lower_quantile_marker.set_data([quantile], [previous_cdf])
  upper_quantile_marker.set_data([quantile], [cdf_at_quantile])
  level_line.set_data([0.5, 7.1], [level, level])
  quantile_line.set_data([quantile, quantile], [-0.02, 1.05])

  page['#quantile-level-value'][0].innerHTML = f'{level:.2f}'
  page['#quantile-x-value'][0].innerHTML = f'{quantile}'

  display(fig_quantile, target='graph-%this%', append=False)


@when('input', '#quantile-level')
def update_quantile_plot(event):
  render_quantile_plot()


render_quantile_plot()
```

```{raw} html
<div class="plot-container">
   <div class="model-slider-container" style="white-space: nowrap;">
      <label for="quantile-level">Livello \(q\): </label>
      <input type="range" id="quantile-level" min="0.05" max="1.00" value="0.50" step="0.05" style="width: 110px;" />
      <span id="quantile-level-value">0.50</span>
   </div>
   <div class="model-slider-container">
      <span>Quantile \(x_q = \)<span id="quantile-x-value"
                                style="margin-left: 0.3em;">3</span></span>
   </div>
</div>
```

Quantili della distribuzione di una variabile aleatoria che descrive il
valore ottenuto lanciando un dado bilanciato a sei facce.
````

Chiaramente, i quantili di una distribuzione hanno in comune non solo il nome,
ma anche un significato analogo a quello dell'omonimo concetto incontrato
nell'ambito della statistica descrittiva. L'idea di fondo è la stessa:
individuare soglie che separino la massa totale in porzioni assegnate. Nel
caso della statistica descrittiva, la «massa» è costituita dalle osservazioni
nel campione, ognuna avente lo stesso peso. Qui, invece, si fa riferimento
direttamente alla massa di probabilità della variabile aleatoria. Anche in
questo caso, quindi, è possibile considerare delle granularità differenti
per descrivere la distribuzione:se la si suddivide in quattro parti di uguale
probabilità si ottengono i _quartili_; se la si ripartisce in dieci o in cento
parti si parla rispettivamente di _decili_ e di _percentili_. Nel caso
discreto, questa suddivisione va intesa nel senso già chiarito sopra: il
quantile (o quartile, e via discorrendo) cercato è sempre il più piccolo valore
per cui la probabilità cumulata raggiunge o supera il livello fissato.

## Altre misure di dispersione

Varianza e deviazione standard misurano la dispersione traducendola in termini
di distanza rispetto a un valore centrale, tipicamente il valore atteso.
Esistono però anche altri indici che adottano un punto di vista diverso:
anziché misurare direttamente gli scarti da un centro, descrivono quanto la
distribuzione sia ampia o quanto risultino distanti tra loro sue porzioni
significative.

````{prf:definition} Range
:label: def-range

Sia $X$ una variabile aleatoria discreta con supporto $S_X$. Il _range_ (o
_intervallo di variazione_) di $X$ è definito come

```{math}
\sup S_X - \inf S_X \enspace
```

quando entrambi gli estremi sono finiti, ed è indefinito altrimenti.
````

````{prf:example}
Le variabili aleatorie descritte negli Esempi
{prf:numref}`ex-quantili-perfetto`, {prf:numref}`ex-quantili-imperfetto` e
{prf:numref}`ex-quantili-dado` hanno tutte _range_ uguale a cinque, perchè il
loro supporto ammette minimo e massimo, rispettivamente uguali a sei e a uno.

Invece, la variabile aleatoria dell'{prf:ref}`ex-va-geometrica-inf` ha
$\mathbb N$ come supporto, il cui estremo superiore è infinito. Pertanto,
il range di questa variabile non è definito.
````

Se una variabile aleatoria ha supporto finito, allora è sempre possibile
calcolare il suo _range_; d'altro canto, non è necessariamente vero che il
range non sia definito quando il supporto è infinito, come mostrato 
nell'esempio che segue.

````{prf:example}
Consideriamo una variabile aleatoria discreta $X$ con supporto
$S_X = \left\{ \tfrac{1}{n} : n \in \mathbb{N} \right\}$. Questo insieme ha $1$
come elemento massimo, non ammette un valore minimo, ma ha estremo inferiore
pari a zero. Pertanto, $\inf S_X = 0$, $\sup S_X = 1$ e il range di $X$ è
uguale a $1$.
````

Il _range_ tiene conto soltanto dei due valori estremi che la variabile può
assumere. Per questo motivo è molto immediato da interpretare, ma risulta anche
piuttosto sensibile a eventuali valori estremi rari, e soprattutto trascura il
modo in cui la probabilità è distribuita all'interno del supporto stesso.
Un'alternativa più robusta si ottiene sfruttando i quantili.

```{margin}
Nella letteratura in lingua italiana si usa spesso il termine
_range interquartile_, o anche l'acronimo inglese _IQR_, ma anche intervallo interquartile o scarto interquartile.
```
````{prf:definition} Distanza interquartile
:label: def-iqr

La _distanza interquartile_ di una variabile aleatoria $X$ è definita come
$x_{0.75} - x_{0.25}$, dove $x_{0.25}$ e $x_{0.75}$ indicano rispettivamente
il primo e il terzo quartile della distribuzione di $X$.

````

La distanza interquartile misura l'ampiezza dell'intervallo che contiene almeno
la metà centrale della massa di probabilità e costituisce dunque una misura di
dispersione alternativa alla varianza e alla deviazione standard. Rispetto a
queste ultime, è meno influenzata dalle _code della distribuzione_ (cioè dalle
sue parti più esterne) e descrive più specificamente la dispersione della sua
parte centrale; d'altra parte, fornisce una descrizione meno completa della
distribuzione, poiché dipende soltanto dal primo e dal terzo quartile e non
tiene conto direttamente di come la massa di probabilità sia distribuita al
loro interno, o al di fuori di essi. Lo stesso principio può essere applicato
con granularità diverse, considerando la distanza tra coppie di quantili
simmetrici rispetto alla mediana. Per esempio, oltre alla distanza
interquartile si può considerare la distanza tra il primo e il nono decile, o
più in generale tra due percentili opportunamente scelti, ottenendo misure
dell'ampiezza di porzioni centrali più o meno estese della distribuzione. In
questo senso, il range e la distanza interquartile sono due casi
particolarmente importanti di una famiglia più ampia di misure di dispersione
che non fanno riferimento allo scostamento da un singolo valore centrale.

Proprio come per la statistica descrittiva, i quartili possono essere usati per
visualizzare graficamente una distribuzione, tracciandone un _box plot_.
Sebbene questo tipo di grafico sia utilizzato poco frequentemente, permette
di dare una descrizione di alcuni aspetti fondamentali di una variabile
aleatoria $X$: la centralità, espressa dalla mediana, e la dispersione,
indicata dalla distanza interquartile e dal _range_. Quando $S_X$ è finito, il
_box plot_ si costruisce in modo molto simile a quanto abbiamo già visto: la
scatola è delimitata dal primo e dal terzo quartile, i baffi dagli estremi
della distribuzione e la mediana è posizionata nella scatola. C'è però una
differenza fondamentale: in genere non si utilizza l'euristica di Tukey per
individuare valori fuori scala.

````{prf:example}
:label: ex-boxplot-dado

Consideriamo la variabile aleatoria $X$ che indica l'esito del lancio di un
dato bilanciato a sei facce, già discussa nell'{prf:ref}`ex-quantili-dado`.
In questo caso, il minimo è $1$ e il massimo è $6$. Inoltre, per
{eq}`eq-quantile-dado`,

```{math}
\begin{aligned}
x_{0.25} &= 2 \enspace, \\
x_{0.5}  &= 3 \enspace, \\
x_{0.75} &= 5 \enspace.
\end{aligned}
```

Il corrispondente diagramma a scatola ha dunque i baffi che si estendono fino a
$1$ a sinistra e fino a $6$ a destra, la scatola compresa tra $2$ e $5$, e il
segmento della mediana posizionato in $3$, come mostrato in
{numref}`fig-boxplot-dado`. La distanza interquartile
vale $x_{0.75} - x_{0.25} = 3$, mentre il range è uguale a $6-1 = 5$.
````

````{customfigure}
:name: fig-boxplot-dado
:class: left-align

```{margin}
Per disegnare un _box plot_ che descrive una distribuzione, `matplotlib` mette
a disposizione il metodo `bxp`, che a partire dai valori dei quartili, del
minimo e del massimo, genera direttamente il diagramma. Non va confuso con
`boxplot`, il cui risultato dipende dai quantili empirici calcolati su una
sequenza di dati, e che solo successivamente usa `bxp`.
```
```{code-cell} python
:tags: [hide-input]

import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(4, 1))

minimum = 1
first_quartile = 2
median = 3
third_quartile = 5
maximum = 6

stats = [{
    "label": "",
    "q1": first_quartile,
    "med": median,
    "q3": third_quartile,
    "whislo": minimum,
    "whishi": maximum,
    "fliers": [],
}]

ax.bxp(stats, orientation='horizontal', widths=0.5)

for x_value, y_value, text in [(minimum, 0.5, minimum),
                               (first_quartile, 1.35, first_quartile),
                               (median, 0.5, median),
                               (third_quartile, 1.35, third_quartile),
                               (maximum, 0.5, maximum)]:
  ax.text(x_value, y_value, text, ha='center')

ax.set_xlim(0, 10)
ax.axis('off')
plt.show()
```

_Box plot_ della distribuzione descritta nell'{prf:ref}`ex-boxplot-dado`.
````

````{prf:example}
:label: ex-boxplot-distribuzione-concentrata

Riconsideriamo la variabile aleatoria $Y$ introdotta
nell'{prf:ref}`ex-var-stessa-media`, con $S_Y = \{1, 5, 7 \}$. La sua
funzione di ripartizione è tale che $F_Y(1) = 0.1$, $F_Y(5) = 0.8$ e
$F_Y(7) = 1$, pertanto $5$ è al contempo primo quartile, mediana e terzo
quartile. Come evidenziato in {numref}`fig-boxplot-distribuzione-concentrata`,
la scatola del _box plot_ della distribuzione di $Y$ si riduce quindi a un
segmento in corrispondenza di $y = 5$. Ciò rende visibile in modo molto netto
il fatto che la massa di probabilità centrale è tutta raccolta attorno a un
singolo valore, pur in presenza di una dispersione complessiva non
trascurabile, come mostrano i due baffi che si estendono da $1$ a $7$.
````

````{customfigure}
:name: fig-boxplot-distribuzione-concentrata
:class: left-align

```{code-cell} python
:tags: [hide-input]

import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(4, 1))

minimum = 1
first_quartile = 5
median = 5
third_quartile = 5
maximum = 7

stats = [{
    "label": "",
    "q1": first_quartile,
    "med": median,
    "q3": third_quartile,
    "whislo": minimum,
    "whishi": maximum,
    "fliers": [],
}]

ax.bxp(stats, orientation='horizontal', widths=0.5)

for x_value, y_value, text in [(minimum, 0.5, minimum),
                               (first_quartile, 1.35, first_quartile),
                               (median, 0.5, median),
                               (third_quartile, 1.35, third_quartile),
                               (maximum, 0.5, maximum)]:
  ax.text(x_value, y_value, text, ha='center')

ax.set_xlim(0, 10)
ax.axis('off')
plt.show()
```

_Box plot_ della variabile aleatoria $Y$ dell'{prf:ref}`ex-var-stessa-media`.
````

`````{prf:example}
:label: ex-boxplot-infinito

La variabile aleatoria $X$ descritta nell'{prf:ref}`ex-va-infinita`,
caratterizzata dalla funzione di massa di probabilità

```{math}
p_X(i) = \frac{1}{5} \left(\frac{4}{5}\right)^i
\mathbb 1_{\mathbb N \cup \{ 0 \}}(i) \enspace,
```

ammette una forma relativamente semplice per la funzione di ripartizione.
Dato $x \geq 0$, infatti, per {eq}`eq-sum-geometrica` si ha

```{math}
F_X(x) = \sum_{i=0}^{\lfloor x\rfloor} \frac{1}{5}\left(\frac{4}{5}\right)^i =
1-\left(\frac{4}{5}\right)^{\lfloor x\rfloor+1} \enspace.
```

Pertanto, fissato $q\in(0,1)$, il quantile corrispondente è definito da

````{margin}
```{code-cell} python
:tags: [hide-input]

import matplotlib.pyplot as plt
import numpy as np

q = 0.5
x_q = np.log(1-q)/np.log(4/5) - 1

n = np.floor(x_q)

fig,ax = plt.subplots(figsize=(5, 1))

ax.plot([n-1.5, n+1.5], [0, 0], 'k')

ax.set_xticks([])
ax.set_yticks([])

s  = -1
spacing = {1: -.55, -1: .2}
for x, l in zip([n-1, x_q, n+1],
                [r'$n-1$', r'$\frac{\ln(1-q)}{\ln(4/5)} - 1$', r'$n+1$']):
    ax.plot([x] * 2, [-.1, .1], 'k')
    ax.text(x, spacing[s], l, ha='center', fontsize=18)
    s *= -1

ax.set_ylim(-.5, .5)
ax.axis('off')
plt.show()
```
Qualunque valore più piccolo dell'intero appena superiore a
$\alpha = \ln(1-q)/\ln(4/5) - 1$ viene troncato a un numero intero che
per definiizone non eccede $\alpha$ stesso.
````

```{math}
\begin{aligned}
x_q &= \inf_x \{F_X(x) \geq q \}
    = \inf_x \left\{ \left(\frac{4}{5}\right)^{\lfloor x \rfloor+1}
             \leq 1 - q \right\} \\
    &= \inf_x \left\{ (\lfloor x \rfloor + 1) \ln\frac{4}{5}
             \leq \ln(1-q) \right\} \\
    &= \inf_x \left\{ \lfloor x \rfloor
             \geq \frac{\ln(1-q)}{\ln(4/5)} - 1 \right\} \\
    &= \left\lceil \frac{\ln(1-q)}{\ln(4/5)} - 1 \right\rceil
     = \left\lceil \frac{\ln(1-q)}{\ln(4/5)} \right\rceil - 1 \enspace,
\end{aligned}
```

e i primi tre quartili hanno la forma seguente:

```{margin}
Si verifica facilmente che $\ln(3/4)/\ln(4/5) \approx 1.289$,
$\ln(1/2)/\ln(4/5) \approx 3.106$ e $\ln(1/4)/\ln(4/5) \approx 6.213$.
```
```{math}
\begin{aligned}
x_{0.25} &= \left\lceil
                 \frac{\ln(3/4)}{\ln(4/5)} \right\rceil - 1 = 1 \enspace, \\
x_{0.5}  &= \left\lceil
                  \frac{\ln(1/2)}{\ln(4/5)} \right\rceil - 1 = 3 \enspace, \\
x_{0.75} &= \left\lceil
                 \frac{\ln(1/4)}{\ln(4/5)} \right\rceil - 1 = 6 \enspace.
\end{aligned}
```

Riassumendo, $X$ ha mediana $m_X = 3$ e distanza interquartile pari a cinque.
Il suo valore minimo è zero, mentre non esiste un valore massimo, poiché il
supporto è illimitato superiormente, e questo rende indefinito il _range_.
È comunque possibile disegnare una forma generalizzata di _box plot_, mostrata
nella {numref}`fig-boxplot-infinito`, in cui il baffo destro viene parzialmente
tratteggiato, a significare che si estende indefinitamente verso
$+\infty$. Questa rappresentazione, oltre a visualizzare l'informazione
relativa alla centralità e alla dispersione veicolata dalla mediana e dalla
distanza interquartile, evidenzia un aspetto importante della distribuzione: la
massa di probabilità che si trova prima della mediana è collocata in $[0, 3)$,
mentre quella rimanente è contenuta in $[3, +\infty)$. Queste due masse sono
approssimativamente uguali (ammontano rispettivamente al $49\%$ e al $51\%$),
dunque la massa di probabilità si dispone in modo diverso a sinistra e a
destra rispetto al suo valore centrale, rendendo la distribuzione di $X$
asimmetrica. Questo aspetto verrà approfondito nel prossimo paragrafo.
`````

````{customfigure}
:name: fig-boxplot-infinito
:class: left-align

```{margin}
Il metodo `bxp` richiede dei valori finiti per gli estremi dei baffi, qiundi
non può essere utilizzato direttamente per produrre una variante generalizzata 
del diagramma. Con un piccolo _hack_ è però possibile realizzare un _box plot_
senza un baffo, aggiungendo poi un segmento pieno e uno tratteggiato, come
nel codice usato per questa figura.
```
```{code-cell} python
:tags: [hide-input]

import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(4, 1))

minimum = 0
first_quartile = 1
median = 3
third_quartile = 6
right_whisker_solid_end = 7
right_whisker_dashed_end = 8.5

stats = [{
    "label": "",
    "q1": first_quartile,
    "med": median,
    "q3": third_quartile,
    "whislo": minimum,
    "whishi": right_whisker_solid_end,
    "fliers": [],
}]

box = ax.bxp(stats, orientation='horizontal', widths=0.5)

box['caps'][1].set_visible(False)
right_whisker = box['whiskers'][1]
ax.plot([right_whisker_solid_end, right_whisker_dashed_end], [1, 1],
        color=right_whisker.get_color(),
        linewidth=right_whisker.get_linewidth(),
        linestyle='--')

for x_value, y_value, text in [(minimum, 0.5, minimum),
                               (first_quartile, 1.35, first_quartile),
                               (median, 0.5, median),
                               (third_quartile, 1.35, third_quartile)]:
  ax.text(x_value, y_value, text, ha='center')

ax.set_xlim(-1, 9)
ax.axis('off')
plt.show()
```

Box plot generalizzato della distribuzione descritta nell'{prf:ref}`ex-boxplot-infinito`.
````


Accanto a questi indici, esistono naturalmente anche altre misure di
dispersione che non discuteremo in dettaglio qui. Come gia accennato,  alcune
si basano su quantili diversi dai quartili; altre confrontano direttamente le
distanze tra coppie di valori possibili della distribuzione. L'idea comune,
però, rimane sempre la stessa: valutare quanto i valori di una variabile
aleatoria risultino sparsi, senza necessariamente riferirsi agli scarti
rispetto a un valore centrale.

[^ex2-ex]: In realtà, basterebbe richiedere che $X^2$ ammetta valore
atteso, perché questo implica che anche $X$ lo ammette. Infatti, partendo dal
fatto che $1 + x^2 - 2 \lvert x \rvert$ è sempre una quantità non negativa
(infatti è uguale all'espansione di $(1+x)^2$ e di $(1-x)^2$, rispettivamente
quando $x$ è minore oppure maggiore o uguale a zero), si ottiene
$\lvert x \rvert \leq (1 + x^2)/2$, da cui segue
$\mathbb E(\lvert X \rvert) \leq (1 + \mathbb E(X^2))/2$ (vedi
{ref}`ex-monotonicita-e`). Pertanto, se $X^2$ ammette valore atteso allora
anche la sommatoria alla base di $\mathbb E(X)$ deve convergere assolutamente.
In una {ref}`nota <nota-esistenza-momenti>` del {ref}`sec_momenti` è illustrata
un'estensione di questo risultato.

[^mae-mediana]: In modo del tutto analogo a quanto accade per gli scarti
quadratici, anche la quantità $\mathbb E(\lvert X-c \rvert)$ può essere vista
come una misura di dispersione attorno a un valore centrale $c$. In questo
caso, però, il valore di $c$ che la minimizza è la mediana della distribuzione
di $X$. Si ottiene così un parallelo interessante: la varianza nasce dal fatto
che il valore atteso minimizza lo scarto quadratico medio, mentre lo scarto
assoluto medio è naturalmente legato alla mediana, che minimizza la dispersione
misurata in termini di valori assoluti.


## Vero o falso?

Analizzate ciascuna delle seguenti affermazioni, che riguardano una variabile
aleatoria discreta $X$ che ammette varianza, e dite se è vera o falsa,
motivando il vostro ragionamento. Cliccate su di essa per visualizzare la
risposta corretta.

````{tf-item}
Se $X$ assume valori negativi, allora anche $\operatorname{Var}(X)$ è negativa.
+++
**Falsa**. La {prf:ref}`def-varianza` definisce la varianza come il valore
atteso dello scarto quadratico $(X - \mu)^2$, che è una quantità non negativa:
la varianza non può quindi essere negativa, quale che sia il segno dei valori
di $X$. È proprio per evitare la compensazione tra scarti positivi e negativi,
che rende $\mathbb E(X - \mu)$ sempre nullo, che gli scarti vengono elevati al
quadrato.
````

````{tf-item}
La deviazione standard è espressa nella stessa unità di misura dei valori di
$X$, mentre la varianza no.
+++
**Vera**. Elevando al quadrato gli scarti si eleva al quadrato anche la loro
unità di misura: se $X$ indica dei millilitri, $\operatorname{Var}(X)$ è
misurata in $\mathrm{mL}^2$. La deviazione standard, essendo la radice quadrata
della varianza, risulta espressa nell'unità di misura di $X$, e per questo
risulta generalmente più immediata da interpretare, come osservato
nell'{prf:ref}`ex-deviazione-standard`.
````

````{tf-item}
Se $X$ ammette varianza, allora $\mathbb E(X^2) \geq \mathbb E(X)^2$.
+++
**Vera**. Per il {prf:ref}`teo-var-alternative` la differenza tra i due membri
è esattamente $\operatorname{Var}(X)$, che non è mai negativa. Le due quantità
coincidono quindi soltanto quando la varianza è nulla.
````

````{tf-item}
Sommare una costante $b$ a una variabile aleatoria $X$ non cambia la varianza,
ma ne cambia la deviazione standard.
+++
**Falsa**. Ponendo $a = 1$ nel {prf:ref}`teo-var-trasf-affini` si ottiene
$\operatorname{Var}(X + b) = \operatorname{Var}(X)$, dunque effettivamente la
varianza rimane la stessa. Però la deviazione standard è la radice quadrata
della varianza: se non cambia la prima, non cambia nemmeno la seconda.
````

````{tf-item}
Per ogni $a \in \mathbb R$ vale
$\operatorname{SD}(a X) = a \operatorname{SD}(X)$.
+++
**Falsa**. Il {prf:ref}`teo-sd-trasf-affini` stabilisce che il fattore deve
essere il valore assoluto di $a$:
$\operatorname{SD}(aX + b) = \lvert a \rvert
\operatorname{SD}(X)$. Per $a = -3$, per esempio, si ottiene
$\operatorname{SD}(-3X) = 3 \operatorname{SD}(X)$, mentre l'affermazione
darebbe una deviazione standard negativa, che non può esistere per definizione,
essendo la radice quadrata della varianza.
````

````{tf-item}
La varianza di una variabile indicatrice $I_A$ è tanto più grande quanto più
l'evento $A$ è probabile.
+++
**Falsa**. Nell'{prf:ref}`ex-var-indicatrice` si ricava
$\operatorname{Var}(I_A) = p(1-p)$, con $p = \mathbb P(A)$: la varianza aumenta
man mano che ci si avvicina a un evento di probabilità $p = 0.5$, al contrario,
quando l'evento tende a diventare molto probabile (o molto improbabile), la
varianza diminuisce e si avvicina a zero.
````

````{tf-item}
Tra tutti i valori $c \in \mathbb R$, quello che rende minima la quantità
$\mathbb E\left((X-c)^2\right)$ è la mediana di $X$.
+++
**Falsa**. Posto $\mu = \mathbb E(X)$, si ottiene l'identità
$\mathbb E\left((X-c)^2\right) = \operatorname{Var}(X) + (\mu-c)^2$, in cui il
termine $(\mu-c)^2$ è non negativo e si annulla soltanto per $c = \mu$: il
minimo si raggiunge dunque nel valore atteso ed è pari alla varianza. È invece
lo scarto assoluto medio $\mathbb E(\lvert X-c \rvert)$ a essere minimizzato
dalla mediana.
````

````{tf-item}
Nel caso discreto, il quantile di livello $q$ soddisfa sempre $F_X(x_q) = q$.
+++
**Falsa**. La funzione di ripartizione di una variabile aleatoria discreta
cresce «per salti», quindi il livello richiesto può venire superato e
non raggiunto esattamente: la {prf:ref}`def-quantili-va-discreta` chiede
infatti $\mathbb P(X \leq x) \geq q$. L'{prf:ref}`ex-quantili-imperfetto`
mostra proprio un caso di questo tipo, in cui $x_{0.6} = 4$ ma
$F_X(x_{0.6}) = 0.8$.
````

````{tf-item}
La mediana di $X$ coincide con il suo quantile di livello $0.5$.
+++
**Vera**. La {prf:ref}`def-quantili-va-discreta` individua il più piccolo
valore in cui la probabilità cumulata raggiunge il livello fissato; per
$q = 0.5$ si ritrova la {prf:ref}`def-mediana-va-discreta`. I quantili si
possono quindi leggere come una generalizzazione della mediana.
````

````{tf-item}
Se il supporto di $X$ è infinito, il range di $X$ non è definito.
+++
**Falsa**. La {prf:ref}`def-range` richiede che $\inf S_X$ e $\sup S_X$ siano
entrambi finiti, e questo può accadere anche con un supporto infinito: per
$S_X = \left\{ \tfrac{1}{n} : n \in \mathbb{N} \right\}$ si ha $\inf S_X = 0$ e
$\sup S_X = 1$, quindi il range è uguale a $1$. Il range non è invece definito,
per esempio, per la variabile aleatoria dell'{prf:ref}`ex-va-geometrica-inf`,
il cui supporto è $\mathbb N$.
````

````{tf-item}
La distanza interquartile è meno influenzata dalle code della distribuzione
rispetto alla deviazione standard.
+++
**Vera**. La {prf:ref}`def-iqr` dipende soltanto dal primo e dal terzo
quartile, quindi misura l'ampiezza della metà centrale della massa di
probabilità e ignora come questa sia distribuita agli estremi. Per lo stesso
motivo, però, descrive la distribuzione in modo meno completo della deviazione
standard.
````

````{tf-item}
Quando si traccia il _box plot_ di una variabile aleatoria, si evidenziano
sempre i valori fuori scala.
+++
**Falsa**. In linea di principio, proprio come nella statistica descrittiva, è
possibile sia evidenziare gli _outlier_ applicando la regola euristica di
Tukey, oppure scegliere di non farlo, estendendo i baffi fino agli estremi
della distribuzione. Normalmente, si utilizza questa seconda modalità.
````

## Esercizi

````{exercise} •
:label: ex-disp-flatman

Quando {extlink}`Flatman
<https://marvel.fandom.com/wiki/Val_Ventura_(Earth-616)>` si appiattisce per
infilarsi sotto una porta, il suo spessore $T$, misurato in millimetri, è una
variabile aleatoria con supporto $S_T = \{1, 2, 3\}$ e funzione di massa di
probabilità

```{math}
p_T(1) = 0.2, \qquad p_T(2) = 0.5, \qquad p_T(3) = 0.3 \enspace.
```

1. Calcolate la varianza di $T$ applicando la {prf:ref}`def-varianza`.
2. Ricalcolate la varianza usando {eq}`eq_var-alternative` e verificate di
   ottenere lo stesso risultato del punto precedente.
3. Calcolate la deviazione standard di $T$ e indicate in quale unità di misura
   è espressa questa quantità.
````
````{solution} ex-disp-flatman
:class: dropdown

1. Siccome $\mathbb E(T) = 1 \cdot 0.2 + 2 \cdot 0.5 + 3 \cdot 0.3 = 2.1$, si
   ha
   ```{math}
   \operatorname{Var}(T) = (1-2.1)^2 \cdot 0.2 + (2-2.1)^2 \cdot 0.5
                         + (3-2.1)^2 \cdot 0.3 = 0.49 \enspace.
   ```

2. Si ha $\mathbb E(T^2) = 1 \cdot 0.2 + 4 \cdot 0.5 + 9 \cdot 0.3 = 4.9$, da
   cui $\operatorname{Var}(T) = 4.9 - 2.1^2 = 0.49$, in accordo con il punto
   precedente.

3. La deviazione standard è $\operatorname{SD}(T) = \sqrt{0.49} = 0.7$, ed è
   espressa in millimetri, come $T$.
````

````{exercise} ••
:label: ex-disp-standardizzazione

Sia $X$ una variabile aleatoria che ammette valore atteso $\mu$ e varianza
$\sigma^2 > 0$, e sia $Y = a X + b$, con $a, b \in \mathbb R$.

1. Esprimete $\mathbb E(Y)$ e $\operatorname{Var}(Y)$ in funzione di $\mu$,
   $\sigma^2$, $a$ e $b$.
2. Determinate $a$ e $b$ in modo che $\mathbb E(Y) = 0$ e
   $\operatorname{Var}(Y) = 1$.
````
````{solution} ex-disp-standardizzazione
:class: dropdown

1. Per iTeoremi {prf:numref}`teo-valore-atteso-trasf-affini` e
   {prf:ref}`teo-var-trasf-affini`si ha $\mathbb E(Y) = a \mu + b$ e
   $\operatorname{Var}(Y) = a^2 \sigma^2$, rispettivamente.

2. Da $a^2 \sigma^2 = 1$ segue $a = \pm 1/\sigma$, e imponendo
   $a\mu + b = 0$ si ricava $b = -a \mu = \mp \mu / \sigma$.
   ```{math}
   Y = \pm\frac{X}{\sigma} \mp\frac{\mu}{\sigma}
     = \pm \frac{X - \mu}{\sigma} \enspace.
   ```
````

````{exercise} •
:label: ex-disp-bouncing-boy

Rimbalzando lungo un corridoio,
{extlink}`Bouncing Boy <https://dc.fandom.com/wiki/Charles_Foster_Taine>`
percorre un numero di metri $B$ con supporto $S_B = \{1, 2, 4, 8\}$, dove i
quattro valori sono equiprobabili.

1. Scrivete la funzione di ripartizione $F_B$ nei punti del supporto.
2. Determinate i tre quartili $x_{0.25}$, $x_{0.5}$ e $x_{0.75}$.
3. Calcolate la distanza interquartile e il _range_ di $B$, e dite quale dei
   due indici è più sensibile a un eventuale aumento del valore $8$.
````
````{solution} ex-disp-bouncing-boy
:class: dropdown

1. Essendo i valori equiprobabili, ciascuno ha massa $0.25$ e quindi
   $F_B(1) = 0.25$, $F_B(2) = 0.5$, $F_B(4) = 0.75$ e $F_B(8) = 1$.

2. Applicando la {prf:ref}`def-quantili-va-discreta`, il quantile di livello
   $q$ è il più piccolo valore del supporto in cui $F_B$ raggiunge o supera
   $q$:
   $x_{0.25} = 1$, $x_{0.5} = 2$ e $x_{0.75} = 4$. In questo caso i tre livelli
   vengono raggiunti esattamente, perché coincidono con i valori assunti da
   $F_B$.

3. La distanza interquartile è $x_{0.75} - x_{0.25} = 4 - 1 = 3$, mentre il
   _range_ è $8 - 1 = 7$. Il _range_ è il più sensibile al valore $8$: dipende
   direttamente dal massimo del supporto, quindi aumenterebbe al crescere di
   quest'ultimo; la distanza interquartile, invece, non cambierebbe.
````

````{exercise} ••
:label: ex-verifica-formula-alt

Riprendendo l'{prf:ref}`ex-var-indicatrice`, calcolate la varianza della
variabile indicatrice di un evento $A$ applicando direttamente la
{prf:ref}`def-varianza`.
````
````{solution} ex-verifica-formula-alt
:class: dropdown

Indicando con $A$ l'evento di riferimento e con $p$ la sua probabilità, si ha
$\mathbb E(I_A) = p$ e
```{math}
\operatorname{Var}(I_A) =
(0 - p)^2 \mathbb P(I_A=0) + (1 - p)^2 \mathbb P(I_A=1) =
p^2 (1 - p) + p (1 - p)^2 = p(1-p)\enspace.
```
````

````{exercise} ••
:label: ex-prg-varianza

Scrivete una funzione `var` che accetta come argomenti:

- una lista di valori,
- una lista di masse di probabilità che ha la stessa lunghezza dell'argomento
  precedente e i cui elementi sommano a $1$,

e che restituisce la varianza della corrispondente variabile aleatoria.
Verificate il funzionamento di questa funzione su:

- una variabile aleatoria degenere che è sempre uguale a $1$,
- una variabile aleatoria che assume solamente le specificazioni $0$ e
  $1$ con uguale probabilità,
- una variabile aleatoria che assume solamente le specificazioni $0$ e
  $1$, rispettivamente con probabilità $\tfrac{3}{5}$ e $\tfrac{2}{5}$,
- la variabile aleatoria che indica il risultato del lancio di un dado
  bilanciato a sei facce.
````
````{solution} ex-prg-varianza
:class: dropdown

La cella seguente riporta la definizione della funzione `expected_value`
fornita nella soluzione dell'{ref}`ex-prg-ex` e la utilizza per calcolare
la varianza, applicando direttamente la {prf:ref}`def-varianza`. Vengono poi
eseguiti i test indicati.

```{code-cell} python

def expected_value(x, p):
    assert len(x) == len(p), "x and p must have the same length"
    assert abs(sum(p) - 1) < 1e-6, "Probabilities must sum to 1"
    return sum(x_i * p_i for x_i, p_i in zip(x, p))

def variance(x, p):
    mu = expected_value(x, p)
    return sum(p_i * (x_i - mu) ** 2 for x_i, p_i in zip(x, p))

assert variance([1], [1]) == 0
assert variance([0, 1], [0.5, 0.5]) == 0.25
assert variance([0, 1], [3/5, 2/5]) == 0.24
assert variance(np.arange(1, 7), [1/6] * 6) == 35/12
```
````

````{exercise} ••
:label: ex-var-nulla

Dimostrate che $\operatorname{Var}(X) = 0$ se e solo se $X$ è una variabile
aleatoria degenere.
````
````{solution} ex-var-nulla
:class: dropdown

Il fatto che una variabile aleatoria degenere abbia varianza nulla è una
conseguenza diretta del {prf:ref}`teo-var-trasf-affini`. D'altro canto, se
$\operatorname{Var}(X) = 0$, allora
```{math}
\sum_{x \in S_X} (x - \mathbb E(X))^2 p_X(x) = 0 \enspace,
```

e notando che ogni singolo addendo nella somma non è mai negativo, ciò
implica che per ogni $x \in S_X$ deve valere $(x - \mathbb E(X))^2 p_X(x) = 0$.
Inoltre, $p_X$ è positiva sui valori del supporto di $X$, dunque
$x - \mathbb E(X) = 0$. Concludendo, $x = \mathbb E(X)$ per ogni valore del
supporto, che deve quindi essere un insieme singoletto.
````

````{exercise} ••
:label: ex-var-aff-alt

Dimostrate l'enunciato del {prf:ref}`teo-var-trasf-affini` applicando
{eq}`eq_var-alternative`.
````
````{solution} ex-var-aff-alt
:class: dropdown

Usando la formula alternativa per il calcolo della varianza e tenendo conto
delle proprietà del valore atteso, si ha

```{math}
\begin{aligned}
\operatorname{Var}(a X + b) &= \mathbb E((a X + b)^2) - \mathbb E(a X + b)^2 \\
&= \mathbb E(a^2 X^2 + 2 a b X + b^2) - (a \mathbb E(X) + b)^2 \\
&= a^2 \mathbb E(X)^2 + 2 a b \mathbb E(X) + b^2 - a^2 \mathbb E(X)^2
- 2 a b \mathbb E(X) - b^2 \\
&= a^2 (\mathbb E(X^2) - \mathbb E(X)^2) \enspace.
\end{aligned}
```
````

````{exercise} ••
:label: ex-disp-scarto-da-c

Con riferimento alla variabile $T$ dell'{ref}`ex-disp-flatman`, per la quale
$\mu = \mathbb E(T) = 2.1$ e $\operatorname{Var}(T) = 0.49$:

1. Calcolate $\mathbb E\left((T-c)^2\right)$ per $c = 2$ e per $c = 3$.
2. Verificate i due risultati usando l'identità
   $\mathbb E\left((T-c)^2\right) = \operatorname{Var}(T) + (\mu - c)^2$.
3. Scrivete del codice che visualizzi il grafico di
   $\mathbb E\left((T-c)^2\right)$ al variare di $c$, evidenziandone il minimo
   e commentando i risultati ottenuti.
````
````{solution} ex-disp-scarto-da-c
:class: dropdown

1. Per $c = 2$ si ha
   $\mathbb E\left((T-2)^2\right) = 1\cdot 0.2 + 0\cdot 0.5 + 1\cdot 0.3= 0.5$,
   mentre quando $c = 3$ il valore atteso è
   $\mathbb E\left((T-3)^2\right) = 4\cdot 0.2 + 1\cdot 0.5 + 0\cdot 0.3 =1.3$.

2. Sostituendo nei membri a sinistra dell'identità i valori di $c$,
   $\operatorname{Var}(T)$ e $\mu$ si ottiene
   $0.49 + (2.1-2)^2 = 0.49 + 0.01 = 0.5$ nel primo caso e
   $0.49 + (2.1-3)^2 = 0.49 + 0.81 = 1.3$ nel secondo, che coincidono con i
   valori calcolati direttamente.

3. Sappiamo che il minimo di $\mathbb E\left((T-c)^2\right)$ si trova in
   corrispondenza di $c = \mu = 2.1$, quindi possiamo disegnare il grafico
   richiesto e sovrapporlo a un segmento in corrispondenza del minimo.
   
```{code-cell} python

import matplotlib.pyplot as plt
import numpy as np

c_values = np.linspace(-1, 4, 400)
exp_deviation = sum(((1 - c_values) ** 2) * p for p in (0.2, 0.5, 0.3))

fig, ax = plt.subplots()
ax.plot(c_values, exp_deviation)
ax.vlines(2.1, 0, 10, color='#cc6600', linewidth=0.8, linestyle=(0, (7, 4)))
ax.set_xlabel(r'$c$')
ax.set_xlim(-1, 4)
ax.set_ylim(0, exp_deviation.max() + 0.2)
ax.grid(axis='y', alpha=0.15)
plt.show()
```
   
````

````{exercise} ••••
:label: ex-quantile-fuori-supporto

Il quantile di una variabile aleatoria coincide sempre con un valore del suo
supporto? In caso affermativo, dimostratelo, altrimenti fornite un
controesempio (suggerimento: rivedete l'{prf:ref}`ex-ea-mediana-nosupp`).
````
````{solution} ex-quantile-fuori-supporto
:class: dropdown

L'{prf:ref}`ex-ea-mediana-nosupp` mostra che la mediana, che il quantile di
livello $0.5$ può non essere un elemento del supporto della variabile
aleatoria.
````

````{exercise} •••
:label: ex-disp-darkhawk

L'altezza raggiunta da {extlink}`Darkhawk
<https://marvel.fandom.com/wiki/Christopher_Powell_(Earth-616)>` in un balzo è
una variabile aleatoria $X$, misurata in metri, con $\mathbb E(X) = 40$ e
$\operatorname{Var}(X) = 6.25$.

1. Calcolate $\operatorname{SD}(X)$ e $\mathbb E(X^2)$.
2. Un secondo sensore misura la stessa altezza in centimetri: posto
   $Z = 100 X$, calcolate $\operatorname{Var}(Z)$ e $\operatorname{SD}(Z)$,
   specificando le unità di misura corrispondenti.
3. Un terzo sensore è collocato su una piattaforma alta tre metri, e misura
   quindi $W = X - 3$. Calcolate $\operatorname{Var}(W)$ e commentate il
   risultato.
4. Un quarto sensore misura la distanza $V = 50 - X$ tra Darkhawk e il soffitto
   di un hangar alto cinquanta metri. Calcolate $\operatorname{SD}(V)$.
````
````{solution} ex-disp-darkhawk
:class: dropdown

1. $\operatorname{SD}(X) = \sqrt{6.25} = 2.5 \, \mathrm{m}$. Riscrivendo
   {eq}`eq_var-alternative` come
   $\mathbb E(X^2) = \operatorname{Var}(X) + \mathbb E(X)^2$ si ottiene
   $\mathbb E(X^2) = 6.25 + 1600 = 1606.25 \, \mathrm{m}^2$.

2. Per il {prf:ref}`teo-var-trasf-affini`,
   $\operatorname{Var}(Z) = 100^2 \cdot 6.25 = 62\,500 \, \mathrm{cm}^2$, e per
   il {prf:ref}`teo-sd-trasf-affini`,
   $\operatorname{SD}(Z) = 100 \cdot 2.5 = 250 \, \mathrm{cm}$. La dispersione
   fisica è la stessa: è cambiata solo l'unità di misura.

3. La variabile $W$ è costruita applicando una traslazione, ponendo quindi
   $a = 1$ nel {prf:ref}`teo-var-trasf-affini`:
   $\operatorname{Var}(W) = \operatorname{Var}(X) = 6.25 \, \mathrm{m}^2$.
   Spostare l'origine delle misure cambia il valore atteso, che diventa
   $37$ metri, ma non modifica quanto le altezze siano disperse.

4. Anche in questo caso viene applicata a $X$ una trasformazione affine, con
   $a = -1$ e $b = 50$, quindi
   $\operatorname{SD}(V) = \lvert -1 \rvert \operatorname{SD}(X)
   = 2.5 \, \mathrm{m}$: misurare la distanza dal soffitto anziché da terra
   ribalta l'ordine dei valori, ma non altera la dispersione.
````

````{exercise} ••
:label: ex-disp-due-punti

Sia $X$ una variabile aleatoria con supporto $S_X = \{\alpha, \beta\}$, dove
$\alpha < \beta$, e sia $p = \mathbb P(X = \beta)$, con $p \in (0,1)$.

1. Verificate che $X = \alpha + (\beta - \alpha) I$, dove $I$ è la variabile
   indicatrice dell'evento $\{X = \beta\}$.
2. Sfruttando il punto precedente e l'{prf:ref}`ex-var-indicatrice`, mostrate
   che $\operatorname{Var}(X) = (\beta-\alpha)^2 p (1-p)$.
3. Determinate il valore di $p$ che rende massima la varianza e calcolate il
   valore massimo, esprimendolo in funzione del _range_ di $X$.
````
````{solution} ex-disp-due-punti
:class: dropdown

1. La variabile $I$ vale $1$ con probabilità $p$ e $0$ con probabilità $1 - p$.
   Questi due casi corrispondono rispettivamente al verificarsi degli eventi
   $X = \beta$ e $X = \alpha$. In particolare:
   - con probabilità $p$ si ha $X = \beta = \alpha + (\beta - \alpha) \cdot 1$;
   - con probabilità $1 - p$ si ha
     $X = \alpha = \alpha + (\beta - \alpha) \cdot 0$.
   Quindi $X$ e $\alpha + (\beta - \alpha) I$ assumono gli stessi valori con
   le medesime probabilità.

2. La trasformazione applicata a $I$ è affine, con $a = \beta - \alpha$ e
   $b = \alpha$. Per il {prf:ref}`teo-var-trasf-affini` e per
   l'{prf:ref}`ex-var-indicatrice`, si ha
   ```{math}
   \operatorname{Var}(X) = (\beta-\alpha)^2 \operatorname{Var}(I)
                         = (\beta-\alpha)^2 p (1-p) \enspace.
   ```

3. Il fattore $(\beta-\alpha)^2$ che compare in $\operatorname{Var}(X)$ non
   dipende da $p$, mentre il massimo di $p(1-p)$ è $p = \tfrac{1}{4}$, e si
   verifica in corrispondenza di  $p = \tfrac{1}{2}$. Siccome il _range_ di $X$
   è $R = \beta - \alpha$, la varianza massima è $R^2/4$, e si ottiene quando i
   due valori sono equiprobabili, cioè quando l'esito dell'osservazione di $X$
   è più incerto.
````

````{exercise} •••
:label: ex-disp-matter-eater-lad

Il numero di oggetti che {extlink}`Matter-Eater Lad
<https://dc.fandom.com/wiki/Tenzil_Kem>` divora in un pasto è una variabile
aleatoria $M$ con supporto $\mathbb N$ e funzione di massa di probabilità
$p_M(k) = 2^{-k} \mathbb 1_\mathbb N(k)$.

1. Verificate che $p_M$ è una funzione di massa di probabilità e che
   $F_M(x) = 1 - 2^{-\lfloor x \rfloor}$.
2. Determinate i tre quartili di $M$ e la sua distanza interquartile.
3. Il _range_ di $M$ è definito? Motivate la risposta.
4. Descrivete il _box plot_ di $M$, specificando dove cadono la scatola, la
   mediana e i baffi.
````
````{solution} ex-disp-matter-eater-lad
:class: dropdown

1. Le masse sono positive e, per {eq}`eq-serie-geometrica-da-uno`,
   $\sum_{k=1}^{+\infty} 2^{-k} = 1$, dunque $p_M$ è una funzione di massa
   di probabilità. Applicando {eq}`eq-sum-geometrica` si ottiene inoltre
   ```{math}
   F_M(x) = \mathbb P(M \leq x) = \sum_{i=1}^{\lfloor x \rfloor} 2^{-i}
   = \sum_{i=0}^{\lfloor x \rfloor} 2^{-i} - 1
   = 2 (1 - 2^{-\lfloor x \rfloor - 1}) - 1
   = 1 - 2^{-\lfloor x \rfloor} \enspace.
   ```

2. Si ha $F_M(1) = 0.5$ e $F_M(2) = 0.75$. Il più piccolo valore in cui la
   ripartizione raggiunge $0.25$ è quindi $x_{0.25} = 1$, che è anche il più
   piccolo valore in cui raggiunge $0.5$: pertanto $x_{0.5} = 1$. Infine
   $x_{0.75} = 2$, e la distanza interquartile è $2 - 1 = 1$.

3. No: il supporto è $\mathbb N$, quindi $\sup S_M = +\infty$ e la
   {prf:ref}`def-range` non è applicabile.

4. La scatola va da $x_{0.25} = 1$ a $x_{0.75} = 2$ e la mediana cade sul suo
   estremo sinistro, perché $x_{0.5} = x_{0.25} = 1$. Il baffo sinistro
   collassa sul bordo della scatola a un punto, dato che il minimo del supporto
   coincide con il primo quartile, mentre quello destro non ha un estremo
   finito e va quindi tracciato come nell'{prf:ref}`ex-boxplot-infinito`, con
   un tratteggio che indica il proseguimento verso $+\infty$. La cella seguente
   permette di disegnare il _box plot_.

```{code-cell} python

import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(4, 1))

minimum = 1
first_quartile = 1
median = 1
third_quartile = 2
right_whisker_solid_end = 3
right_whisker_dashed_end = 4.2

stats = [{
    "label": "",
    "q1": first_quartile,
    "med": median,
    "q3": third_quartile,
    "whislo": minimum,
    "whishi": right_whisker_solid_end,
    "fliers": [],
}]

box = ax.bxp(stats, orientation='horizontal', widths=0.5)

box['caps'][1].set_visible(False)
right_whisker = box['whiskers'][1]
ax.plot([right_whisker_solid_end, right_whisker_dashed_end], [1, 1],
        color=right_whisker.get_color(),
        linewidth=right_whisker.get_linewidth(),
        linestyle='--')

for x_value, y_value, text in [(median, 0.5, median),
                               (third_quartile, 1.35, third_quartile)]:
  ax.text(x_value, y_value, text, ha='center')

ax.set_xlim(0.5, 4.5)
ax.axis('off')
plt.show()
```
````

````{exercise} ••••
:label: ex-disp-limite-range

Sia $X$ una variabile aleatoria discreta il cui supporto $S_X$ ammette minimo
$\alpha$ e massimo $\beta$, e sia $R = \beta - \alpha$ il suo _range_.

1. Posto $c = (\alpha+\beta)/2$, mostrate che
   $\mathbb E\left((X-c)^2\right) \leq R^2/4$.
2. Deducete che $\operatorname{Var}(X) \leq R^2/4$: la varianza di una
   variabile aleatoria non può quindi essere grande se il suo _range_ è
   piccolo.
3. Verificate che disuguaglianza del punto precedente vale per la variabile
   aleatoria dell'{prf:ref}`ex-var-dado`.
4. Dimostrate che quando la massa di probabilità è equamente ripartita sui
   due estremi del supporto, $\operatorname{Var}(X) = R^2/4$.
````
````{solution} ex-disp-limite-range
:class: dropdown

1. Il valore $c$ è il punto medio dell'intervallo $[\alpha, \beta]$, che
   contiene tutto il supporto: per ogni $x \in S_X$ si ha dunque
   $\lvert x - c \rvert \leq R/2$ e quindi $(x-c)^2 \leq R^2/4$. Il valore
   atteso di una quantità che non supera mai $R^2/4$ non può superare $R^2/4$,
   da cui $\mathbb E\left((X-c)^2\right) \leq R^2/4$.

2. Come visto in questo paragrafo,
   $\mathbb E\left((X-c)^2\right) = \operatorname{Var}(X) + (\mu-c)^2$ con
   $\mu = \mathbb E(X)$, e il termine $(\mu-c)^2$ è non negativo. Pertanto
   ```{math}
   \operatorname{Var}(X) \leq \mathbb E\left((X-c)^2\right) \leq
   \frac{R^2}{4} \enspace.
   ```

3. La variabile aleatoria considerata descrive l'esito del lancio di un dado
   a sei facce e bilanciato, per cui si ha $\alpha = 1$, $\beta = 6$ ed
   $R = 5$. Il membro destro della disuguaglianza vale perciò $25/4 = 6.25$,
   mentre la varianza calcolata nell'{prf:ref}`ex-var-dado` è
   $35/12 \approx 2.92$, che rispetta la disuguaglianza.
   
4. Se $\mathbb P(X = \alpha) = \mathbb P(X = \beta) = \tfrac{1}{2}$, allora
   $\mathbb E(X) = \tfrac{\alpha + \beta}{2}$,
   $\mathbb E(X^2) = \tfrac{\alpha^2 + \beta^2}{2}$ e
   ```{math}
   \operatorname{Var}(X) =
   \frac{\alpha^2 + \beta^2}{2} -\frac{\alpha^2 + 2\alpha\beta + \beta^2}{2}
   = \frac{\alpha^2 - 2\alpha\beta + \beta^2}{4} = \frac{(\beta - \alpha)^2}{4}
   \enspace.
   ```
````

## Concetti fondamentali

Pensate ai concetti fondamentali illustrati in questo paragrafo ed elencateli.
Nella lista qui sotto sono già presenti gli stessi concetti, ma nascosti.
Cliccate sul pulsante per mostrarli sotto forma di parole chiave, quindi
confrontateli con la vostra lista. Provate infine a descrivere ciascun concetto
con parole vostre.

````{sds-wordcloud}
Dispersione
Scarto quadratico
Varianza
Deviazione standard
Varianza di trasformazioni affini
Deviazione standard di trasformazioni affini
Quantili
Distanza interquartile
Range
Box plot
````

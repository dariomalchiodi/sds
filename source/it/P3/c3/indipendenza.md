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

(sec_indipendenza)=
# Indipendenza

Nel capitolo precedente abbiamo visto come la probabilità condizionata
$\mathbb P(E \mid F)$ quantifichi quanto sapere che si sia verificato un
evento $F$ modifica la probabiltà di un altro evento $E$. In molte situazioni
concrete, però, questa influenza è assente: sapere che $F$ si è verificato non
cambia la probabilità di $E$, come nell'esempio che segue.

````{prf:example}
Nel lancio di due dadi bilanciati distinguibili &mdash; uno rosso e uno blu,
per facilitare il discorso &mdash; indichiamo con $E$ l'evento «il dado blu
mostra un risultato minore di $4$» e con $F$ l'evento «il dado rosso mostra un
risultato minore di $4$». Quando si verifica $E$, il dado blu può assumere i
valori $1$, $2$ e $3$, e come si vede nella
{numref}`fig-indipendenza-dadi-venn` l'evento (evidenziato in giallo) contiene
$3 \times 6 = 18$ esiti dei $36$ equiprobabili, dunque
$\mathbb P(E) = \frac{18}{36} = \frac{1}{2}$. Ipotizzare che si sia
verificato $F$ (colorato in azzurro nella figura) equivale a restringere l'attenzione ai $18$ esiti nei quali il dado rosso vale $1$, $2$ oppure $3$.
In metà di questi, evidenziati in blu scuro, anche il risultato del dado blu è
minore di $4$, quindi
$\mathbb P(E \mid F) = \frac{9}{18} = \frac{1}{2} = \mathbb P(E)$. In altre
parole, in metà dei casi considerabili il risultato del dado blu è minore o
uguale a $3$, sia nel caso di incertezza completa (la probabilità non
condizionata), sia quando si è verificato $F$.
````

```{code-cell} python
:tags: [hide-input]

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

rosso, blu = np.meshgrid(range(1, 7), range(1, 7))
rosso, blu = rosso.ravel(), blu.ravel()

IN_E = blu < 4
IN_F = rosso < 4
IN_INTERSEZIONE = IN_E & IN_F
SOLO_E = IN_E & ~IN_F
SOLO_F = IN_F & ~IN_E
FUORI = ~(IN_E | IN_F)

with mpl.rc_context({'figure.figsize': (3, 3),
                'figure.dpi': 150,
                'figure.titlesize': 8,
                'xtick.labelsize': 7,
                'ytick.labelsize': 7,
                'axes.labelsize': 7,}):

   fig, ax = plt.subplots()

   BG_COLOR = '#eaf3f5'
   E_COLOR = '#006699'
   F_COLOR = '#c17f24'
   DOT_COLOR = '#010177'
   EDGE_COLOR = '#010177'

   ax.set_facecolor(BG_COLOR)

   ax.axhspan(0.5, 3.5, facecolor=E_COLOR, alpha=0.28, zorder=0)
   ax.axvspan(0.5, 3.5, facecolor=F_COLOR, alpha=0.30, zorder=0)

   ax.axhline(3.5, color=EDGE_COLOR, linestyle='--', linewidth=1.0, zorder=1)
   ax.axvline(3.5, color=EDGE_COLOR, linestyle='--', linewidth=1.0, zorder=1)

   ax.scatter(rosso[FUORI], blu[FUORI], s=20, c='white',
      edgecolors=EDGE_COLOR, linewidths=0.5, zorder=3)
   ax.scatter(rosso[SOLO_E], blu[SOLO_E], s=20, c=E_COLOR,
      edgecolors=EDGE_COLOR, linewidths=0.5, zorder=4)
   ax.scatter(rosso[SOLO_F], blu[SOLO_F], s=20, c=F_COLOR,
      edgecolors=EDGE_COLOR, linewidths=0.5, zorder=4)
   ax.scatter(rosso[IN_INTERSEZIONE], blu[IN_INTERSEZIONE],
      s=20, c=DOT_COLOR, edgecolors=EDGE_COLOR, linewidths=0.5, zorder=5)

   ax.text(1.5, 5.5, r"$F \setminus E$", ha='center', va='center', fontsize=7)
   ax.text(5.5, 1.5, r"$E \setminus F$", ha='center', va='center', fontsize=7)
   ax.text(1.5, 1.5, r"$E \cap F$", ha='center', va='center', fontsize=7)

   ax.set_xlabel('Risultato del dado rosso')
   ax.set_ylabel('Risultato del dado blu')
   ax.set_xticks(range(1, 7))
   ax.set_yticks(range(1, 7))
   ax.set_xlim(0.5, 6.5)
   ax.set_ylim(0.5, 6.5)
   ax.grid(True, color=EDGE_COLOR, alpha=0.12)
   ax.set_aspect('equal')
   plt.show()
```
````{customfigure}
:name: fig-indipendenza-dadi-venn

Diagramma di Venn degli eventi $E =$ «il dado blu mostra un risultato minore di
$4$» e $F =$ «il dado rosso mostra un risultato minore di $4$» nel lancio di
due dadi distinguibili. I $36$ punti della griglia rappresentano gli elementi
dello spazio degli esiti $[1 .. 6]^2$.
````

La definizione seguente introduce la nozione di _indipendenza_ tra eventi,
che formalizza le situazioni, come quella appena vista, in cui il
condizionamento rispetto a un evento non cambia la probabilità risultante.

````{prf:definition} Indipendenza tra due eventi
:label: def-indipendenza

Due eventi $E, F \in \mathsf A$ in uno spazio di probabilità
$(\Omega, \mathsf A, \mathbb P)$ si dicono _indipendenti_ se

```{math}
:label: eq-indipendenza

\mathbb P(E \cap F) = \mathbb P(E)\,\mathbb P(F) \enspace.
```
````

Chi legge attentamente si chiederà come mai la definizione precedente
consideri la probabilità dell'intersezione, piuttosto che ragionare
direttamente in termini di probabilità condizionate. Sebbene questa scelta
possa sembrare poco intuitiva, il lemma seguente mostra che la
```{prf:ref}`def-indipendenza` equivale alla formulazione più intuitiva dalla
quale sono partito.

````{prf:lemma}
:label: lemma-indipendenza-condizioni-equivalenti

Siano $E, F \in \mathsf A$. Le seguenti condizioni sono equivalenti:

1. $\mathbb P(E \cap F) = \mathbb P(E)\mathbb P(F)$,
2. $\mathbb P(E \mid F) = \mathbb P(E)$ quando $\mathbb P(F) > 0$,
3. $\mathbb P(F \mid E) = \mathbb P(F)$ quando $\mathbb P(E) > 0$.
````

````{admonition} _
:class: myproof

Supponiamo vera la prima condizione e mostriamo che questa implica la
seconda. Se $\mathbb P(F) > 0$, è possibile ragionare in termini della
probabilità condizionata $\mathbb P(E \mid F)$, e

```{math}
\mathbb P(E \mid F) = \frac{\mathbb P(E \cap F)}{\mathbb P(F)}
= \frac{\mathbb P(E) \mathbb P(F)}{\mathbb P(F)} = \mathbb P(E) \enspace.
```

D'altra parte, se $\mathbb P(F) > 0$ e $\mathbb P(E \mid F) = \mathbb P(E)$,
allora

```{math}
\frac{\mathbb P(E \cap F)}{\mathbb P(F)} = \mathbb P(E) \enspace,
```

che equivale a $\mathbb P(E \cap F) = \mathbb P(E)\mathbb P(F)$. Petanto,
la prima e la seconda condizione si coimplicano.

Analogamente, quando $\mathbb P(E) > 0$, $\mathbb P(F \mid A)$ è ben definita e

```{math}
\mathbb P(F \mid E) = \frac{\mathbb P(F \cap E)}{\mathbb P(E)}
= \frac{\mathbb P(E \cap F)}{\mathbb P(E)}
= \frac{\mathbb P(E) \mathbb P(F)}{\mathbb P(E)} = \mathbb P(F) \enspace,
```

dunque la prima condizione implica la terza, e l'implicazione inversa si
dimostra in modo analogo a quanto visto sopra.


Riassumendo, $\text{3.} \leftrightarrow \text{1.} \leftrightarrow \text{2.}$,
il che significa che le tre condizioni sono logicamente equivalenti.
````

Il motivo per cui, di solito, si preferisce definire l'indipendenza
introducendo la fattorizzazione
$\mathbb P(E \cap F) = \mathbb P(E) \mathbb P(F)$ è legata a diverse ragioni:

- intuitivamente ci aspettiamo che ogni evento $E$ sia indipendente da
  $\varnothing$, ma $\mathbb P(E \mid \varnothing)$ è indefinita, mentre
  l'intersezione $E \cap \varnothing$ ha probabilità nulla, così come
  $\varnothing$, dunque
  $\mathbb P(E \cap \varnothing) = \mathbb P(E) \mathbb P(\varnothing)$ vale
  anche in questo caso;
- la relazione che coinvolge la probabilità condizionata sembra
  attribuire maggiore importanza all'evento rispetto al quale si condiziona,
  mentre &mdash; al contrario &mdash; nessuno dei due eventi svolge un ruolo
  privilegiato in {eq}`eq-indipendenza`, e ciò mette in evidenza un ovvio
  carattere simmetrico nell'indipendenza ($E$ è indipendente da $F$ se e solo
  se $F$ è indipendente da $E$);
- infine, la {prf:ref}`def-indipendenza` si estende in modo naturale al
  caso di più eventi ed è coerente con l'applicazione del concetto di
  indipendenza al contesto delle variabili aleatorie, come vedremo nel
  {ref}`sec_indipendenza-va`.

````{prf:example} Pari e dispari con due dadi
:label: ex-indip-pari-dadi

Nell'esempio precedente, abbiamo
$\mathbb P(E \cap F) = \frac{9}{36} = \frac{1}{4}$ e
$\mathbb P(E) = \mathbb P(F) = \frac{1}{2}$, quindi {eq}`eq-indipendenza` è
soddisfatta e, come ci aspettavamo, $E$ ed $F$ sono indipendenti.
````

L'esempio seguente mostra l'indipendenza in un contesto combinatorio,
dove la struttura dell'insieme è costruita in modo da garantire la
condizione {eq}`eq-indipendenza`.

````{prf:example} Album di figurine dei supereroi
:label: ex-indip-album

Un album contiene $48$ figurine di supereroi: $12$ per ciascuna delle
quattro squadre (Avengers, X-Men, Guardiani della Galassia,
Thunderbolts). Tra le $48$ figurine, esattamente $12$ raffigurano
eroi dotati di volo cosmico, distribuite uniformemente: $3$ per
squadra. Si estrae una figurina a caso, e si definiscono

- $A =$ «la figurina appartiene agli Avengers»,
- $V =$ «l'eroe raffigurato ha il potere del volo cosmico».

Si ha $\mathbb P(A) = \frac{1}{4}$ e $\mathbb P(V) = \frac{1}{4}$.
L'evento $A \cap V$ contiene le $3$ figurine degli Avengers con volo
cosmico, quindi $\mathbb P(A \cap V) = \frac{3}{48} = \frac{1}{16}$.
Verificando la condizione {eq}`eq-indipendenza`,

```{math}
\mathbb P(A)\,\mathbb P(V)
= \frac{1}{4} \cdot \frac{1}{4} = \frac{1}{16}
= \mathbb P(A \cap V) \enspace.
```

$A$ e $V$ sono indipendenti: la squadra di appartenenza non fornisce
alcuna informazione sul possesso del volo cosmico, perché tale potere
è distribuito in parti uguali tra le quattro squadre.
````

L'indipendenza viene meno non appena la distribuzione delle
caratteristiche perde l'uniformità. Nell'esercizio di Captain Marvel
del capitolo precedente, per esempio, abbiamo calcolato

```{math}
\mathbb P(E) = \frac{\alpha + 1}{2}
\qquad \text{e} \qquad
\mathbb P(E \mid H) = \alpha \enspace,
```

dove $H =$ «il segnale proviene da Hala» e $E =$ «la scansione su
Hala è negativa». Perché $H$ e $E$ siano indipendenti occorre
$\mathbb P(E \mid H) = \mathbb P(E)$, cioè $\alpha =
(\alpha + 1)/2$, da cui $\alpha = 1$. Ma $\alpha = 1$ è il caso
degenere in cui la scansione non trova mai nulla a prescindere
dall'origine del segnale: per ogni $\alpha \in [0, 1)$, gli eventi
$H$ e $E$ sono _dipendenti_, e l'esito della ricerca aggiorna &mdash;
in misura proporzionale a $1 - \alpha$ &mdash; le probabilità sui
tre pianeti.

```{admonition} Indipendenza e incompatibilità
:class: warning

Indipendenza e incompatibilità sono concetti _opposti_. Se
$\mathbb P(E) > 0$, $\mathbb P(F) > 0$ e $E \cap F = \emptyset$,
allora $\mathbb P(E \cap F) = 0 \neq \mathbb P(E)\mathbb P(F)$:
due eventi incompatibili non banali sono sempre _dipendenti_.
Sapere che uno si è verificato esclude con certezza l'altro,
modificando drasticamente la probabilità di $E$ dato $F$.
```


## Proprietà dell'indipendenza

### Complementazione

````{prf:theorem} Indipendenza e complemento
:label: thm-indip-complemento

Se $E$ e $F$ sono indipendenti, allora $E$ e $\overline F$ sono
indipendenti.
````

_Dimostrazione._ Poiché $E = (E \cap F) \cup (E \cap \overline F)$
è un'unione disgiunta, il teorema dell'evento complementare fornisce

```{math}
\mathbb P(E \cap \overline F)
= \mathbb P(E) - \mathbb P(E \cap F)
= \mathbb P(E) - \mathbb P(E)\mathbb P(F)
= \mathbb P(E)\bigl(1 - \mathbb P(F)\bigr)
= \mathbb P(E)\mathbb P(\overline F) \enspace.
```

Per simmetria della condizione {eq}`eq-indipendenza`, valgono
analogamente l'indipendenza di $\overline E$ e $F$, e quella di
$\overline E$ e $\overline F$. $\square$

### Indipendenza a coppie e indipendenza mutua

L'indipendenza tra due eventi si generalizza a famiglie di tre o
più eventi in modo non immediato. L'esempio seguente, tratto dalle
note di lezione, mostra che l'indipendenza a coppie _non_ implica
l'indipendenza mutua: è possibile che ogni coppia di eventi sia
indipendente, eppure che i tre eventi siano tra loro «legati» in
modo sottile.

````{prf:example} Indipendenza a coppie non è indipendenza mutua
:label: ex-indip-coppie-dadi

Nel lancio di due dadi bilanciati distinguibili, definiamo

- $E =$ «la somma dei due risultati è $7$»,
- $F =$ «il primo dado mostra $4$»,
- $G =$ «il secondo dado mostra $3$».

Ciascuno dei tre eventi ha probabilità $\frac{1}{6}$: $E$ ammette
sei esiti favorevoli su $36$, mentre $F$ e $G$ ne ammettono sei
ciascuno. Per l'intersezione a coppie si ottiene

```{math}
\mathbb P(E \cap F) = \mathbb P\bigl(\{(4,3)\}\bigr)
= \frac{1}{36} = \frac{1}{6} \cdot \frac{1}{6}
= \mathbb P(E)\mathbb P(F) \enspace,
```

e analogamente $\mathbb P(E \cap G) = \mathbb P(E)\mathbb P(G)$
e $\mathbb P(F \cap G) = \mathbb P(F)\mathbb P(G)$: ogni coppia
di eventi è indipendente. Tuttavia, l'intersezione $F \cap G$ è
l'evento certo «il primo dado è $4$ e il secondo è $3$», il che
implica $E$ con certezza:

```{math}
\mathbb P(E \mid F \cap G) = 1 \neq \frac{1}{6} = \mathbb P(E)
\enspace.
```

Gli eventi $E$, $F$, $G$ sono indipendenti a coppie, ma non
_mutualmente_ indipendenti: la conoscenza congiunta di $F$ e $G$
fornisce un'informazione su $E$ che né $F$ né $G$ da soli
riuscivano a trasmettere.
````

La definizione corretta di indipendenza per famiglie di più eventi
richiede che la condizione {eq}`eq-indipendenza` valga per _ogni_
sottoinsieme di eventi, non solo per le coppie.

````{prf:definition} Indipendenza mutua
:label: def-indipendenza-mutua

Gli eventi $E_1, \ldots, E_m \in \mathsf A$ si dicono _mutualmente
indipendenti_ se per ogni sottoinsieme di indici
$1 \leq \alpha_1 < \alpha_2 < \cdots < \alpha_r \leq m$ vale

```{math}
:label: eq-indipendenza-mutua

\mathbb P\!\left(\bigcap_{i=1}^{r} E_{\alpha_i}\right)
= \prod_{i=1}^{r} \mathbb P(E_{\alpha_i}) \enspace.
```
````

```{margin}
Per $m = 3$, la {prf:ref}`def-indipendenza-mutua` richiede
quattro condizioni: le tre per le coppie $(E_1, E_2)$,
$(E_1, E_3)$, $(E_2, E_3)$ e quella per la tripla
$E_1 \cap E_2 \cap E_3$.
```

In pratica, l'indipendenza mutua è spesso _assunta_ come ipotesi
modellistica &mdash; tipicamente quando si descrivono esperimenti
fisicamente separati o azioni di agenti distinti &mdash; piuttosto
che _verificata_ a partire dalla definizione.

Una conseguenza importante della {prf:ref}`def-indipendenza-mutua` è
che ogni evento è indipendente da qualunque evento costruito a
partire dagli altri: se $E_1$, $E_2$, $E_3$ sono mutualmente
indipendenti, allora $E_1$ è indipendente da $E_2 \cup E_3$
(e da $E_2 \cap E_3$, e così via). La dimostrazione, analoga a
quella del {prf:ref}`thm-indip-complemento`, si lascia come
esercizio.


## Sistemi in serie e in parallelo

Un'applicazione classica dell'indipendenza mutua riguarda
l'_affidabilità_ di sistemi composti da più componenti. Si hanno
$m$ componenti indipendenti; la probabilità che l'$i$-esimo
funzioni correttamente è $p_i$.

**Sistema in serie.** Il sistema funziona se e solo se _tutti_ i
componenti funzionano. Poiché gli eventi sono indipendenti,

```{math}
\mathbb P(\text{sistema funziona}) = \prod_{i=1}^{m} p_i \enspace.
```

**Sistema in parallelo.** Il sistema funziona se e solo se
_almeno uno_ dei componenti funziona. Per complementazione e
indipendenza,

```{math}
\mathbb P(\text{sistema funziona})
= 1 - \prod_{i=1}^{m} (1 - p_i) \enspace.
```

````{prf:example} La squadra dei Thunderbolts
:label: ex-indip-thunderbolts

I Thunderbolts, guidati da {extlink}`Songbird
<https://marvel.fandom.com/wiki/Melissa_Gold_(Earth-616)>`, devono
infiltrarsi in una base nemica. La missione ha successo solo se
tutte e tre le componenti seguenti vanno a buon fine:

| Componente   | Responsabile | Probabilità di successo |
|:------------:|:------------:|:-----------------------:|
| Ricognizione | Songbird     | $0{,}90$                |
| Hacking      | Moonstone    | $0{,}85$                |
| Estrazione   | Mach-X       | $0{,}95$                |

Assumendo l'indipendenza (sistema in serie), la probabilità di
completare la missione è

```{math}
\mathbb P(\text{missione riuscita})
= 0{,}90 \times 0{,}85 \times 0{,}95 \approx 0{,}727 \enspace.
```

Se invece bastasse che _almeno uno_ dei tre riuscisse nella propria
parte (sistema in parallelo), la probabilità diventerebbe

```{math}
\mathbb P(\text{almeno uno riesce})
= 1 - (1 - 0{,}90)(1 - 0{,}85)(1 - 0{,}95)
= 1 - 0{,}00075
\approx 0{,}999 \enspace.
```

La ridondanza trasforma un sistema con probabilità di successo del
$72{,}7\%$ in uno quasi infallibile. Il prezzo è che basta il
fallimento di un solo componente a compromettere la prima versione
della missione.
````

(sec_naive-bayes)=
## Classificatori naive Bayes

Una semplice applicazione del teorema di Bayes permette di costruire un
particolare classificatore che prende il nome di _classificatore naive Bayes_.
Consideriamo il caso più semplice possibile in cui abbiamo osservato in una
serie di individui la presenza o l'assenza di una determinata proprietà,
ottenendo per ognuno di essi un'osservazione $x_i \in \{ 0, 1 \}$. Ipotizziamo
inoltre di avere associato a ogni individuo un'etichetta $y_i \in \{ 0, 1 \}$
che denota l'appartenenza o meno a una data classe. Prendendo ad esempio il
dataset dei supereroi, supponiamo che la proprietà osservata faccia riferimento
all'avere oppure no gli occhi neri (indicando con $x_i = 1$ il fatto di avere
gli occhi neri e con $x_i = 0$ il fatto di averli di un altro colore), e la
classe considerata indichi se l'editore corrispondente sia o meno la Marvel
Comics (anche in questo caso, denotando con $y_i = 1$ il fatto di essere un
supereroe Marvel e con $y_i = 0$ il fatto di non esserlo).

Indichiamo inoltre con $N$ l'evento «un supereroe preso a caso ha gli occhi
neri» e con $M$ l'evento «un supereroe preso a caso è un supereroe Marvel»:
grazie al teorema di Bayes sappiamo che vale

```{math}
\mathbb P(M \mid N) = \frac{\mathbb P(N \mid M) \mathbb P(M)}{\mathbb P(N)}
\enspace.
```

Ora, se a partire dal dataset fosse possibile ottenere una stima delle
probabilità che compaiono al secondo membro di questa equazione, sarebbe quindi
immediato ottenere una stima di $\mathbb P(M \mid N)$ da utilizzare per dire
qualcosa sul fatto che un generico supereroe con gli occhi neri sia oppure no
un supereroe Marvel. In particolare, se il valore ottenuto fosse
sufficientemente alto potremmo spingerci oltre e dire che d'ora in avanti
potremo _classificare_ tutti i supereroi con gli occhi neri di cui non
conosciamo l'editore come supereroi Marvel. Allo stesso modo, se il valore
ottenuto fosse particolarmente basso potremmo comportarci in modo analogo,
concludendo però che gli occhi neri indicano un editore diverso dalla Marvel.

Il fatto di poter azzardare l'editore potrebbe sembrare poco utile, visto che
in fondo si tratta di una colonna del nostro dataset e quindi noi già sappiamo
quali siano i valori per questo attributo. In realtà sappiamo che ci potrebbero
essere dei valori mancanti, oppure potremmo in futuro avere a disposizione
nuovi dati per i quali questa informazione non è disponibile.

```{admonition} Nota
:class: naming
Va notato che la scelta di usare il colore degli occhi come proprietà osservata
e la casa editrice come classe è assolutamente arbitraria. In modo analogo
avremmo potuto ragionare in termini di come il fatto di essere un supereroe
Marvel possa essere utilizzato per azzardare il colore degli occhi, scambiando
gli eventi $M$ e $N$ nelle formule.
```

Un modo semplice per stimare le probabilità indicate è quello di osservare con
che frequenza gli eventi associati si verificano nel dataset a nostra
disposizione. In particolare,

- la probabilità $\mathbb P(N \mid M)$ può essere approssimata calcolando la
  frequenza relativa con cui un supereroe Marvel del dataset ha gli occhi neri;
- la probabilità $\mathbb P(M)$ può essere approssimata calcolando la frequenza
  relativa con cui un supereroe del dataset è edito dalla Marvel;
- la probabilità $\mathbb P(N)$ può essere approssimata calcolando la frequenza
  relativa con cui un supereroe del dataset ha gli occhi neri.

Attrezziamoci quindi per poter calcolare queste frequenze, caricando il dataset
e importando le librerie che utilizzeremo.

```{code-cell} python
import pandas as pd
import numpy as np

heroes = pd.read_csv('data/heroes.csv', index_col=0)
```

Possiamo ora approssimare la probabilità dell'evento $M$ come la frequenza
relativa del medesimo evento sul dataset, e quindi calcolando il rapporto tra
il numero di supereroi Marvel e il totale dei supereroi.

```{code-cell} python
marvel_heroes = heroes[heroes['creator']=='Marvel Comics']
p_marvel = len(marvel_heroes) / len(heroes)
p_marvel
```

Allo stesso modo, la probabilità $\mathbb P(N)$ si approssima facilmente
calcolando la frazione di supereroi del dataset che hanno gli occhi neri.

```{code-cell} python
black_eyes_heroes = heroes[heroes['eye_color']=='Black']
p_blackeyes = len(black_eyes_heroes) / len(heroes)
p_blackeyes
```

Infine, una stima della probabilità $\mathbb P(N \mid M)$ si ottiene dividendo il
numero di supereroi Marvel che hanno gli occhi neri per il numero totale di
supereroi Marvel.

```{code-cell} python
blackeyes_and_marvel_heroes = heroes[(heroes['creator']=='Marvel Comics') & \
                                     (heroes['eye_color']=='Black')]

p_blackeyes_given_marvel = len(blackeyes_and_marvel_heroes) / len(marvel_heroes)
p_blackeyes_given_marvel
```

Applicando il teorema di Bayes si ottiene quindi che la probabilità di trovarsi
di fronte a un supereroe Marvel, dato che questo ha gli occhi neri, può essere
approssimata come segue.

```{code-cell} python
p_blackeyes_given_marvel * p_marvel / p_blackeyes
```

Dunque sembrerebbe che gli occhi neri siano leggermente più probabili nei
supereroi **non** Marvel. Ovviamente avremmo ottenuto un risultato coerente se
avessimo applicato lo stesso procedimento per stimare la probabilità
$\mathrm(\overline M \mid N)$.

```{code-cell} python
nonmarvel_heroes = heroes[heroes['creator']!='Marvel Comics']
blackeyes_and_nonmarvel_heroes = heroes[(heroes['creator']!='Marvel Comics') & \
                                        (heroes['eye_color']=='Black')]

p_notmarvel = len(nonmarvel_heroes) / len(heroes)
p_blackeyes_given_notmarvel = len(blackeyes_and_nonmarvel_heroes) / len(nonmarvel_heroes)

p_blackeyes_given_notmarvel * p_notmarvel / p_blackeyes
```

Visto che le due probabilità ottenute sono molto vicine a $\frac{1}{2}$, ha
senso valutare se l'uso di diverse proprietà da osservare _congiuntamente_ ci
possa portare a una procedura più precisa. Per esempio potremmo tener conto sia
del colore degli occhi, sia di quello dei capelli, senza fissare un colore
specifico. Consideriamo pertanto tutti i possibili valori
$\{ o_1, o_2, \dots, o_n \}$ per i colori degli occhi e scriviamo $O = o_i$ per
indicare l'evento «un supereroe a caso ha gli occhi del colore $o_i$».
Procediamo in modo analogo per l'evento $C = c_j$ che equivale a «un supereroe
a caso ha i capelli del colore $c_j$», dove i valori possibili ora
corrispondono all'insieme $\{ c_1, c_2, \dots, c_m \}$. Il teorema di Bayes
permette in questo caso di scrivere

```{math}
\mathbb P(M \mid O = o_i \cap C = c_j) =
    \frac{\mathbb P(O = o_i \cap C = c_j \mid M)
    \mathbb P(M)}{\mathbb P(O = o_i \cap C = c_j)} \enspace.
```

Pertanto si può pensare di estendere il ragionamento visto precedentemente:
dato un supereroe di cui si conoscono i colori $o_i$ e $c_j$ di occhi e
capelli, si approssimano le probabilità al secondo membro dell'equazione e in
funzione del valore ottenuto si classifica il supereroe come «Marvel» oppure
come «non Marvel». I classificatori _naive Bayes_ semplificano il lavoro
approssimando $\mathbb P(O = o_i \cap C = c_j \mid M)$ con la quantità $\mathbb
P(O = o_i \mid M) \mathbb P(C = c_j \mid M)$. Procedendo in questo modo, nel
numeratore della frazione si calcoleranno al più $m + n$ diverse probabilità al
posto di $m n$ (più avanti vedremo come evitare l'analogo problema quando si
calcola il denominatore). L'aggettivo _naive_ nel nome del classificatore
sottolinea la semplicità dell'ipotesi adottata (_naive_ significa infatti
«ingenuo» in inglese).

Concentriamoci per esempio su un supereroe con occhi e capelli neri: la
probabilità che esso sia un supereroe Marvel sarà quindi calcolata da un
classificatore naive Bayes come

```{math}
\mathbb P(M \mid O = \text{neri} \cap C = \text{neri}) \approx
\frac{\mathbb P(O = \text{neri} \mid M) \mathbb P(C = \text{neri} \mid M)
\mathbb P(M)}{\mathbb P((O = \text{neri} \cap C = \text{neri})} \enspace.
```

Alcune delle probabilità coinvolte sono già state calcolate. Nella cella
seguente quelle mancanti sono derivate in modo analogo, ottenendo come
risultato una bassa probabilità di avere a che fare con un supereroe Marvel se
i suoi occhi e i suoi capelli sono neri.

```{code-cell} python
black_eyes_and_hair_heroes = heroes[(heroes['eye_color']=='Black') & \
                                    (heroes['hair_color']=='Black')]

p_blackeyes_and_black_hair = len(black_eyes_and_hair_heroes) / len(heroes)

blackhair_and_marvel_heroes = heroes[(heroes['creator']=='Marvel Comics') & \
                                     (heroes['hair_color']=='Black')]
p_blackhair_given_marvel = len(blackhair_and_marvel_heroes) / len(marvel_heroes)

p_blackeyes_given_marvel * p_blackhair_given_marvel * p_marvel \
     / p_blackeyes_and_black_hair
```

Consideriamo infine il caso più generale in cui vi sono più di due classi su
cui suddividere gli individui. Nell'esempio che stiamo considerando stiamo
quindi dicendo che vi sono valori diversi $\{ e_1, \dots, e_o \}$ per
l'editore, e quindi saremo interessati a eventi della forma $E = e_k$.
Idealmente, una volta osservato un supereroe di cui $o_j$ e $c_j$ indicano
rispettivamente il colore di occhi e capelli sarà necessario calcolare
$\mathbb P(E = e_k \mid O = o_i \cap C = c_j)$ per tutti i possibili $e_k$: il più
alto ottenuto individuerà l'editore da associare al supereroe. È però possibile
semplificare ulteriormente il procedimento, notando che esso consiste nel
determinare, al variare di $k$, il più alto tra i valori

```{math}
\mathbb P(E = e_k \mid O = o_i \cap C = c_j) \approx
\frac{\mathbb P(O = o_i \mid E = e_k) \mathbb P(C = c_j \mid E = e_k)
\mathbb P(E = e_k)}{\mathbb P(O = o_i \cap C = c_j)} \enspace.
```

Ora, il denominatore è indipendente da $k$ e quindi la classificazione si può
effettuare trovando il valore $k$ che massimizza la quantità

```{math}
\mathbb P(O = o_i \mid E = e_k) \mathbb P(C = c_j \mid E = e_k)
\mathbb P(E = e_k) \enspace.
```

Riformuliamo il ragionamento effettuato in modo da renderlo il più generale
possibile: immaginiamo che per un dato individuo si osservino congiuntamente i
valori $x_1, \dots, x_n$ per $n$ proprietà $X_1, \dots, X_n$, e denotiamo con
$X_1 = x_1, \dots, X_n=x_n$ gli eventi corrispondenti. Supponiamo inoltre che
vi siano $m$ possibili classi che corrispondono agli eventi
$Y = y_1, \dots, Y = y_m$. Per ognuna di queste classi vorremo calcolare

```{math}
\mathbb P(Y=y_k \mid X_1=x_1, \dots, X_n=x_n) =
      \frac{\mathbb P(X_1=x_1, \dots, X_n=x_n \mid Y=y_k) \mathbb P(Y=y_k)}
           {\mathbb P(X_1=x_1, \dots, X_n=x_n)}
```

e assegnare l'individuo alla classe per cui tale probabilità è massima.
L'approssimazione alla base del classificatore naive Bayes ci permette di
scrivere

```{math}
\mathbb P(Y=y_k \mid X_1=x_1, \dots, X_n=x_n) \approx \frac{\mathbb P(Y=y_k)
  \displaystyle\prod_{i=1}^n\mathbb P(X_i=x_i \mid Y=y_k)}
                {\mathbb P(X_1=x_1, \dots, X_n=x_n)} \enspace,
```

e tenuto conto che anche in questo caso il denominatore non dipende da $k$,
potremo associare l'individuo alla classe $y_{k^*}$, dove

```{math}
k^* = \arg\max_k \mathbb P(Y = y_k) \prod_{i=1}^n
      \mathbb P(X_i = x_i \mid Y = y_k) \enspace.
```

In realtà non è necessario effettuare «a mano» i calcoli legati a un
classificatore naive Bayes. Come già visto per gli alberi di decisione, la
libreria sklearn mette a disposizione delle classi che permettono di ottenere
direttamente un classificatore a partire dai dati iniziali. Per esemplificarne
il funzionamento, estraiamo dal nostro dataset alcune colonne ed eliminiamo
tutte le righe in cui occorre almeno un valore mancante.

```{code-cell} python
features = ['height', 'weight', 'first_appearance',
            'hair_color', 'eye_color', 'strength', 'intelligence']
heroes_cleaned = heroes.dropna()
X = heroes_cleaned[features].copy()
```

Per gli stessi motivi visti quando abbiamo lavorato con gli alberi di
decisione, è necessario utilizzare solamente dati numerici. Possiamo convertire
gli attributi categorici che corrispondono a genere e colore di occhi e capelli
riutilizzando le classi `LabelEncoder`. Procediamo poi a convertire i valori
degli attributi rimanenti nel modo che segue: dividiamo innanzitutto
l'intervallo di variazione dei corrispondenti valori in quattro intervalli,
utilizzando i quattro quartili come estremi; associamo successivamente un
diverso valore numerico a ogni intervallo ottenuto e trasformiamo ogni
osservazione nel numero che corrisponde all'intervallo individuato. Questa
operazione viene effettuata automaticamente dalla funzione `pd.qcut`, a cui
passiamo le osservazioni, il numero di intervalli da considerare e i valori
numerici da associare a questi ultimi.

```{code-cell} python
from sklearn.preprocessing import LabelEncoder

hair_encoder = LabelEncoder()
hair_encoder.fit(X['hair_color'])
X['hair_color'] = hair_encoder.transform(X['hair_color'])

eye_encoder = LabelEncoder()
eye_encoder.fit(X['eye_color'])
X['eye_color'] = eye_encoder.transform(X['eye_color'])

intelligence_encoder = LabelEncoder()
intelligence_encoder.fit(X['intelligence'])
X['intelligence'] = intelligence_encoder.transform(X['intelligence'])
```

L'ultimo ingrediente mancante è l'insieme dei valori per le classi. Per
semplificarci la vita, ritorniamo alla classificazione binaria inizialmente
considerata: anche in questo caso è necessario lavorare con valori numerici,
quindi costruiamo una serie i cui valori sono `1` in corrispondenza dei
supereroi Marvel e `0` per tutti gli altri casi.

```{code-cell} python
Y = (heroes_cleaned['creator']=='Marvel Comics')
```

In realtà sklearn implementa diverse varianti del classificatore naive Bayes,
ognuna delle quali stima in modo diverso le probabilità
$\mathbb P(X_i = x_i \mid Y = y_k)$. Consideriamo per esempio la classe
`GaussianNB`, che ipotizza che tali probabilità si possano calcolare
utilizzando una distribuzione gaussiana (uno dei modelli teorici che vedremo
tra qualche lezione). La costruzione del classificatore viene fatta usando lo
stesso procedimento visto per gli alberi di decisione: si crea un oggetto della
classe `GaussianNB`, e poi si invoca su di esso il metodo `fit` specificando
come argomenti le osservazioni e le corrispondenti etichette. Dopo sarà
sufficiente invocare il metodo `predict` passando una lista di oggetti da
classificare. Ricordando che per avere una valutazione imparziale di un
classificatore è necessario utilizzare dati non utilizzati per costruire il
classificatore stesso, per semplicità limitiamoci a verificare che cosa succeda
con le osservazioni in `X`.

```{code-cell} python
from sklearn.naive_bayes import GaussianNB

model = GaussianNB()
model.fit(X, Y)

model.predict(X)
```

Il risultato non pare molto confortante, in quanto quasi tutti i casi vengono
associati alla Marvel. Per analizzare meglio i risultati, vediamo separatamente
come vengono classificati i supereroi delle due classi.

```{code-cell} python
model.predict(X[Y==0])
```

```{code-cell} python
model.predict(X[Y==1])
```

A partire dai vettori ottenuti è facile calcolare separatamente il numero di
veri positivi, falsi positivi, falsi negativi e veri negativi. È anche
possibile costruire un dataframe che contenga la corrispondente matrice di
confusione.

```{code-cell} python
tp = sum(model.predict(X[Y==1]))
fn = len(model.predict(X[Y==1])) - tp
fp = sum(model.predict(X[Y==0]))
tn = len(model.predict(X[Y==0])) - fp
pd.DataFrame([[tp, fn],
              [fp, tn]],
              index=['Etichetta positiva', 'Etichetta negativa'],
              columns=['Classif. positiva', 'Classif. negativa'])
```

La matrice evidenzia una buona classificazione dei supereroi Marvel e una
performance molto bassa per quel che riguarda i rimanenti supereroi. Volendo
riassumere in un unico indice la bontà del risultato ottenuto è possibile
calcolare la percentuale di dati corretti.

```{code-cell} python
(tp + tn) / len(X)
```

Tale percentuale di per sé ci dice che poco meno dell'80% dei casi è stata
classificata correttamente. Ciò è dovuto al fatto che nel dataset considerato
vi sono in proporzione molti più supereroi Marvel rispetto a quelli delle altre
case editrici.


## Esercizi

````{exercise} •
:label: ex-indip-album-altra-squadra

Nell'{prf:ref}`ex-indip-album`, si consideri l'evento
$G =$ «la figurina appartiene ai Guardiani della Galassia».

1. Calcolate $\mathbb P(G)$ e $\mathbb P(G \cap V)$.
2. Verificate dalla definizione che $G$ e $V$ sono indipendenti.
3. Calcolate $\mathbb P(V \mid G)$ e confrontatelo con
   $\mathbb P(V)$.
````

````{solution} ex-indip-album-altra-squadra
:class: dropdown

1. Poiché ogni squadra ha $12$ figurine su $48$, si ha
   $\mathbb P(G) = \frac{1}{4}$. Le figurine in $G \cap V$ sono
   le $3$ dei Guardiani con volo cosmico, quindi
   $\mathbb P(G \cap V) = \frac{3}{48} = \frac{1}{16}$.

2. Dalla condizione {eq}`eq-indipendenza`:

```{math}
\mathbb P(G)\,\mathbb P(V)
= \frac{1}{4} \cdot \frac{1}{4} = \frac{1}{16}
= \mathbb P(G \cap V) \enspace. \quad \checkmark
```

3. Si ottiene $\mathbb P(V \mid G) = \frac{3}{12} = \frac{1}{4}
= \mathbb P(V)$: conoscere la squadra non aggiunge informazione
sul possesso del volo cosmico.
````

````{exercise} ••
:label: ex-indip-complemento-album

Nell'{prf:ref}`ex-indip-album`, si consideri l'evento
$\overline A =$ «la figurina _non_ appartiene agli Avengers».

1. Calcolate $\mathbb P(\overline A \cap V)$ direttamente.
2. Verificate dalla definizione che $\overline A$ e $V$ sono
   indipendenti.
3. Ottenete lo stesso risultato applicando il
   {prf:ref}`thm-indip-complemento`.
````

````{solution} ex-indip-complemento-album
:class: dropdown

1. Le figurine in $\overline A \cap V$ sono le $9$ con volo
   cosmico appartenenti alle tre squadre diverse dagli Avengers
   ($3$ per ciascuna), quindi
   $\mathbb P(\overline A \cap V) = \frac{9}{48} = \frac{3}{16}$.

2. Verificando la condizione {eq}`eq-indipendenza`:

```{math}
\mathbb P(\overline A)\,\mathbb P(V)
= \frac{3}{4} \cdot \frac{1}{4} = \frac{3}{16}
= \mathbb P(\overline A \cap V) \enspace. \quad \checkmark
```

3. Poiché $A$ e $V$ sono indipendenti
   (dall'{prf:ref}`ex-indip-album`), il
   {prf:ref}`thm-indip-complemento` garantisce direttamente che
   $\overline A$ e $V$ siano indipendenti.
````

````{exercise} ••
:label: ex-indip-pattuglia

{extlink}`Songbird
<https://marvel.fandom.com/wiki/Melissa_Gold_(Earth-616)>` e
{extlink}`Moon Knight
<https://marvel.fandom.com/wiki/Marc_Spector_(Earth-616)>`
pattugliano indipendentemente due quartieri distinti di New York.
La probabilità che Songbird incontri un criminale durante il turno
è $\frac{1}{3}$; quella di Moon Knight è $\frac{1}{4}$.

1. Qual è la probabilità che entrambi incontrino un criminale?
2. Qual è la probabilità che almeno uno dei due ne incontri uno?
3. Qual è la probabilità che _solo_ Moon Knight incontri un
   criminale?
````

````{solution} ex-indip-pattuglia
:class: dropdown

Siano $S =$ «Songbird incontra un criminale» e
$M =$ «Moon Knight incontra un criminale», con
$\mathbb P(S) = \frac{1}{3}$, $\mathbb P(M) = \frac{1}{4}$,
indipendenti per ipotesi.

1. Per la condizione {eq}`eq-indipendenza`:

```{math}
\mathbb P(S \cap M) = \frac{1}{3} \cdot \frac{1}{4}
= \frac{1}{12} \enspace.
```

2. Per la formula dell'unione:

```{math}
\mathbb P(S \cup M)
= \frac{1}{3} + \frac{1}{4} - \frac{1}{12}
= \frac{4 + 3 - 1}{12} = \frac{1}{2} \enspace.
```

3. L'evento «solo Moon Knight» è $M \cap \overline S$.
   Per il {prf:ref}`thm-indip-complemento`, $M$ e $\overline S$
   sono indipendenti, quindi

```{math}
\mathbb P(M \cap \overline S)
= \mathbb P(M)\,\mathbb P(\overline S)
= \frac{1}{4} \cdot \frac{2}{3} = \frac{1}{6} \enspace.
```
````

````{exercise} •••
:label: ex-indip-darkhawk

{extlink}`Darkhawk
<https://marvel.fandom.com/wiki/Christopher_Powell_(Earth-616)>`
utilizza una tuta controllata da tre amuleti indipendenti, ciascuno
con probabilità $p$ di funzionare correttamente in combattimento.
La tuta è operativa se _almeno due_ dei tre amuleti funzionano.

1. Esprimete $\mathbb P(\text{tuta operativa})$ in funzione di $p$.
2. Per quale valore di $p$ la probabilità di operatività supera
   $\frac{1}{2}$?
3. Confrontate con la probabilità di operatività di una tuta in
   serie con tre componenti identici, ognuno con probabilità $p$.
   Per $p = 0{,}8$, quale architettura è più affidabile?
````

````{solution} ex-indip-darkhawk
:class: dropdown

Siano $A_i =$ «l'amuleto $i$ funziona», con
$\mathbb P(A_i) = p$ per $i = 1, 2, 3$, indipendenti per ipotesi.

1. Gli scenari favorevoli sono «esattamente due funzionano» e
   «tutti e tre funzionano»:

```{math}
\mathbb P(\text{operativa})
= \binom{3}{2}p^2(1-p) + p^3
= 3p^2 - 2p^3 \enspace.
```

2. Si richiede $3p^2 - 2p^3 > \frac{1}{2}$. Valutando in
   $p = \frac{1}{2}$: $3 \cdot \frac{1}{4} - 2 \cdot \frac{1}{8}
   = \frac{1}{2}$. La funzione $f(p) = 3p^2 - 2p^3$ è crescente
   su $[0, 1]$, quindi la probabilità di operatività supera
   $\frac{1}{2}$ se e solo se $p > \frac{1}{2}$.

3. Per una tuta in serie: $\mathbb P(\text{operativa}) = p^3$.
   Per $p = 0{,}8$, la tuta con regola di maggioranza dà

```{math}
3 \cdot 0{,}64 \cdot 0{,}2 + 0{,}512
= 0{,}384 + 0{,}512 = 0{,}896 \enspace,
```

mentre quella in serie dà $0{,}8^3 = 0{,}512$. L'architettura
con regola di maggioranza è decisamente più affidabile: la
ridondanza compensa efficacemente il rischio di guasto di un
singolo amuleto.
````

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


# Combinazioni

Analogamente alle disposizioni, anche le combinazioni descrivono delle
sequenze di lunghezza prefissata costituite da oggetti scelti da un insieme di
partenza. In questo caso, però, le sequenze _non sono ordinate_, e in effetti
è più corretto parlare della costruzione di un _sottoinsieme_ dell'insieme di
partenza. Pertanto nel raggruppamento che corrisponde alle combinazioni
non è rilevante l'ordine, ma possiamo scegliere di potere ripetere gli
oggetti oppure no. Le due categorie di combinazioni risultanti sono descritte
nei paragrafi che seguono.

## Combinazioni semplici

```{margin}
È anche possibile parlare della costruzione di _insiemi_ a partire da un
_universo_ che contiene gli oggetti considerati.
```
Quando non è possibile inserire nella sequenza non ordinata uno stesso oggetto
più di una volta, possiamo a tutti gli effetti dire che vi è corrispondenza
tra le combinazioni, che vengono dette _semplici_, e i sottoinsiemi
dell'insieme di partenza.

````{prf:definition}
:label: def-combinazioni
Consideriamo un insieme $A = \{ a_1, \ldots, a_n \}$ di $n$ oggetti e
fissiamo un numero naturale $k \leq n$. Una _combinazione semplice_ (o più
semplicemente _combinazione_) degli $n$ oggetti in $k$ posti è una sequenza
di questi oggetti che individua un sottoinsieme $B \subseteq A$ di cardinalità
uguale a $k$. Indicheremo con $c_{n, k}$ il numero di differenti combinazioni
semplici di $n$ oggetti in $k$ posti.
````

```{margin}
L'uso delle parentesi graffe è anche direttamente collegato alla sintassi
utilizzata per descrivere gli insiemi in modo estensivo.
```
Indicheremo le combinazioni utilizzando una sintassi simile a quella delle
permutazioni e delle disposizioni, ma in questo caso useremo le parentesi
graffe come delimitatori, per sottolineare che si tratta di sequenze non
ordinate.

````{prf:example} Peter Petrelli
:label: ex-peter-petrelli
Peter Petrelli è uno dei protagonisti della serie Heroes, dotato di una
straordinaria forma di _empatia_ che gli permette di riprodurre i poteri
degli altri supereroi che si trovano nelle sue vicinanze.
Ipotizziamo che questo meta-potere sia limitato, e che Peter sia in grado
di replicare tre superpoteri alla volta: le terne
$\{ \text{psicocinesi}, \text{telepatia}, \text{invisibilità} \}$ e
$\{ \text{telepatia}, \text{invisibilità}, \text{psicocines} \}$ indicano una
medesima sequenza ordinata, e dunque uno stesso sottoinsiemi e
una sola combinazione semplice di $k = 3$ superpoteri. In questo caso l'insieme
da cui estraiamo gli oggetti è l'insieme di tutti i superpoteri, ed è poco
rilevante determinarne la cardinalità $n$.
````

Per calcolare $c_{n, k}$ possiamo utilizzare un ragionamento analogo a quello
seguito per calcolare il numero di permutazioni con ripetizione: basta
osservare che l'insieme delle dispozioni senza ripetizione di $n$ oggetti in
$k$ posti contiene anche tutte le corrispondenti combinazioni, ma ognuna di
queste $c_{n, k}$ combinazioni sarà rappresentata tante volte.
Più precisamente, per ognuna delle combinazioni troveremo $k!$ disposizioni
ottenute permutando i $k$ oggetti coinvolti. Pertanto
$d_{n, k} = c_{n, k} \cdot k!$, da cui si ricava

$$
c_{n, k} = \frac{d_{n, k}}{k}! = \frac{n!}{(n-k)!k!} =\binom{n}{k}.
$$

```{margin}
Come indicato in https://www.superherodb.com/powers/.
```
Riprendendo l'esempio precedente, immaginiamo che vi siano in tutto $n = 477$
possibili superpoteri, e che Peter Petrelli sia in grado di riprodurli tutti.
In un dato istante sarà in grado di «ricordarsi» $\binom(477){3} = 17974950$
diverse configurazioni di tre superpoteri.


## Combinazioni con ripetizione

- Se invece immaginiamo che nel selezionare ciascuno dei $k$ oggetti abbiamo
  a disposizione sempre l'insieme $A$ completo, e quindi il singolo oggetto
  $a_i$ può essere selezionato anche più di una volta, allora parliamo di
  disposizioni o combinazioni _con ripetizione_. Ad esempio, fissato $k=3$,
  la sequenza $(a_r, a_i, a_i)$ è una disposizione con ripetizione perché
  l'oggetto $a_i$ ricorre due volte, e analogamente  $\{a_r, a_i, a_i\}$ è
  una combinazione con ripetizione.



Vediamo ora come calcolare, data una particolare modalità di selezione, il
numero di possibili scelte distinte.




- Si potrebbe infine dimostrare (ma non lo faremo) che il numero  $C_{n,k}$
  di _combinazioni con ripetizione di $n$ oggetti distinti presi $k$ alla
  volta_ è

$$
C_{n, k} = \binom{n+k-1}{k}
$$


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


# Disposizioni e combinazioni

Consideriamo un insieme di $n$ oggetti distinti $A= \{ a_1,\dots a_n \}$ e
selezioniamo $k$ oggetti di questo insieme. Le modalit\`a di selezione
possono essere svariate.

- Se vogliamo distinguere le configurazioni contenenti gli stessi oggetti ma
  estratti in ordine differente allora pariamo di _disposizioni di $n$
  oggetti su k posti_, che sono configurazioni in cui sono importanti sia
  l'oggetto selezionato che la sua posizione. Specifichiamo una disposizione
  indicando tra parentesi tonde gli oggetti estratti. Ad esempio, fissato
  $k=3$, la disposizione $(a_i, a_j, a_r)$ è diversa dalla disposizione
  $(a_r, a_j, a_i)$ perché, sebbene gli oggetti selezionati siano gli stessi,
  essi compaiono in ordine differente.

- Se invece siamo solo interessati a quali oggetti sono stati estratti e non
  alla loro posizione nella sequenza, allora pariamo di _combinazioni di $n$
  oggetti presi $k$ alla volta_. Specifichiamo una combinazione indicando tra
  parentesi graffe gli oggetti estratti. Ad esempio, fissato $k=3$,
  $\{ a_i, a_j, a_r \}$ e $\{ a_r, a_j, a_i \}$ sono la stessa combinazione.

Inoltre:

- Se gli oggetti di $A$ possono essere usati una sola volta, allora parliamo
  di disposizioni o combinazioni _senza ripetizione_. Gli esempi di
  disposizioni o combinazioni visti sopra sono senza ripetizione.

- Se invece immaginiamo che nel selezionare ciascuno dei $k$ oggetti abbiamo
  a disposizione sempre l'insieme $A$ completo, e quindi il singolo oggetto
  $a_i$ può essere selezionato anche più di una volta, allora parliamo di
  disposizioni o combinazioni _con ripetizione_. Ad esempio, fissato $k=3$,
  la sequenza $(a_r, a_i, a_i)$ è una disposizione con ripetizione perché
  l'oggetto $a_i$ ricorre due volte, e analogamente  $\{a_r, a_i, a_i\}$ è
  una combinazione con ripetizione.

Abbiamo dunque quattro possibili modi di selezionare $k$ oggetti da un
insieme di $n$ oggetti, che corrispondono a quattro tipi di configurazioni
diverse:

- le _disposizioni senza ripetizione_, dette anche _disposizioni semplici_,
  che richiedono ovviamente che sia $k\leq n$,
- le _combinazioni senza ripetizione_, dette anche _combinazioni semplici_,
  con $k\leq n$,
- le _disposizioni con ripetizione_,
- le _combinazioni con ripetizione_.

Vediamo ora come calcolare, data una particolare modalità di selezione, il
numero di possibili scelte distinte.

- Per calcolare il numero $d_{n, k}$ di possibili _disposizioni senza
  ripetizione di $n$ oggetti distinti su $k$ posti_ procediamo in modo
  analogo a quanto fatto per le permutazioni semplici, fermandoci però alla
  posizione $k$-esima. L'albero costruito ha profondità $k$ e un numero di
  foglie pari a:

\begin{align}
d_{n, k} &= n (n-1) (n-2) \dots (n-k+1) \\
         &= n (n-1) (n-2) \dots (n-k+1) \cdot
             \left(\frac{(n-k)(n-k-1)\dots1}{(n-k)(n-k-1)\dots1}\right) \\
         &=\frac{n!}{(n-k)!}.
\end{align}

- Si osservi che, per $k=n$, nella disposizione si utilizzano tutti gli
  elementi di $A$, quindi le permutazioni semplici sono un caso particolare
  di disposizioni semplici.

- Per calcolare il numero $c_{n, k}$ di possibili _combinazioni senza
  ripetizione di $n$ oggetti distinti presi $k$ alla volta_ osserviamo che,
  fissati $k$ oggetti, alla combinazione contenente quei $k$ oggetti
  corrispondono $k!$ distinte disposizioni contenenti gli stessi $k$ oggetti.
  Quindi il numero totale di disposizioni semplici è uguale al numero di
  combinazioni moltiplicato per $k!$, cioè $d_{n,k} = c_{n,k} \cdot k!$, da
  cui segue che

$$
c_{n, k} = \frac{d_{n, k}}{k}! = \frac{n!}{(n-k)!k!} =\binom{n}{k}
$$

- Per calcolare il numero $D_{n, k}$ di possibili _disposizioni con
  ripetizione di $n$ oggetti distinti su $k$ posti_ procediamo in modo
  analogo a quanto fatto per le disposizioni senza ripetizione, tenendo
  presente però che in ciascun nodo dell'albero abbiamo sempre $n$ possibili
  oggetti tra i quali scegliere, mentre la profondità dell'albero è, come in
  quel caso, ancora $k$. Quindi avremo

$$
D_{n, k} = \underbrace{n \cdot n \dots \cdot n}_{k \text{ volte}} = n^k.
$$

- Si potrebbe infine dimostrare (ma non lo faremo) che il numero  $C_{n,k}$
  di _combinazioni con ripetizione di $n$ oggetti distinti presi $k$ alla
  volta_ è

$$
C_{n, k} = \binom{n+k-1}{k}
$$

La Tabella seguente contiene uno schema riassuntivo dei casi considerati.

<table style="font-size: 1rem;">
    <tr>
        <th></th>
        <th>sequenze (ordinate)</th>
        <th>insiemi (non ordinati) </th>
    </tr>
    <tr>
        <th>senza ripetizione</th>
        <td>DISPOSIZIONI: $d_{n,k}=\frac{n!}{(n-k)!}$</td>
        <td>COMBINAZIONI: $c_{n,k}=\binom{n}{k}$</td>
    </tr>
    <tr>
        <th>con ripetizione </th>
        <td>DISPOSIZIONI: $D_{n,k}=n^k$</td>
        <td>COMBINAZIONI: $C_{n,k}=\binom{n+k-1}{k}$</td>
    </tr>
</table>

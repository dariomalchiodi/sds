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

(sec_concetti-fondamentali)=
# Concetti fondamentali

Come descritto all'inizio di questo capitolo, alla base di ogni ragionamento
di tipo probabilistico si trova un'esperienza non deterministica che chiameremo
_esperimento casuale_, come formalizzato nella definizione seguente.

```{margin}
Gli esperimenti casuali saranno indicati utilizzando
le lettere maiuscole corsive $\mathscr E$, $\mathscr F$ e così via, scegliendo
possibilmente una lettera legata al significato dell'esperimento stesso.
```
```{prf:definition} Esperimento casuale
:label: def-esperimento-casuale
Definiamo _esperimento casuale_ (o _aleatorio_) una qualsiasi esperienza che
può dare risultati differenti quando essa viene ripetuta più volte partendo da
condizioni iniziali identiche.
```

Immaginiamo di acquistare tutte le settimane un nuovo numero di un fumetto dei
Fantastici 4: ogni volta i contenuti saranno diversi, permettendoci di
considerare per esempio gli esperimenti casuali $\mathscr P =$ controllare se
il numero totale di occorrenze della Donna invisibile è pari, $\mathscr O =$
verificare quale sia il colore degli occhi del primo supereroe che compare nel
numero, $\mathscr C =$ elencare l'ordine di apparizione dei Fantastici 4,
$\mathscr N =$ contare il numero di diversi supereroi presenti e $\mathscr A =$
misurare l'altezza (in cm.) dell'ultimo supereroe che compare nel fumetto.

```{margin}
Denoteremo gli esiti usando le lettere minuscole dell'alfabeto greco,
utilizzando possibilmente $\omega$ (omega minuscola) o alcune sue varianti.
```
```{prf:definition} Esito
:label: def-esito
Ogni possibile risultato $\omega$ di un esperimento casuale $\mathscr E$ prende
il nome di _esito_.
```

Un esempio di esito è $\text{falso}$ per $\mathscr P$, $\text{azzurro}$ per
$\mathscr O$, $(\text{Torcia umana}, \text{Donna invisibile},
\text{Mister Fantastic}, \text{Cosa})$ per $\mathscr C$, $3$ per $\mathscr N$ e
$183$ per $\mathscr A$. L'insieme di tutti gli esiti di un esperimento casuale,
che rappresenta il punto iniziale della modellazione matematica che useremo per
il concetto di probabilità, prende il nome di _spazio degli esiti_.

```{margin}
Lo spazio degli esiti viene spesso anche chiamato _spazio campionario_ o
_insieme universo_, e in letteratura esistono notazioni alternative che lo
denotano usando per esempio le lettere $S$ e $U$.
```

````{prf:definition} Spazio degli esiti
:label: def-spazio-esiti
L'insieme di tutti i possibili esiti di un generico esperimento
casuale $\mathcal E$ viene chiamato _spazio degli esiti_, e lo si denota
usualmente tramite la lettera $\Omega$ (omega maiuscola).
````

La {numref}`tab-esempi-spazi-esiti` descrive lo spazio degli esiti per ognuno
degli esperimenti casuali presi precedentemente in considerazione.

```{margin}
In questo caso, la scelta per $\Omega_\mathscr O$ è arbitraria.
```
````{table} Esempi di spazi degli esiti per gli esperimenti casuali $\mathscr P$, $\mathscr O$, $\mathscr C$, $\mathscr N$ e $\mathscr A$.
:name: tab-esempi-spazi-esiti

| Esperimento | Spazio degli esiti |
|--------------|-----------------------------------|
| $\mathscr P$ | $\Omega_\mathscr P = \{ \text{vero}, \text{falso} \}$ |
| $\mathscr O$ | $\Omega_\mathscr O = \{ \text{azzurro}, \text {marrone}, \text{nero},\text{verde} \}$ |
| $\mathscr C$ | $\Omega_\mathscr C = $ insieme di tutte le permutazioni degli elementi in  $\{ \text{Mister Fantastic}, \text{Donna invisibile}, \text{Torcia umana}, \text{Cosa}\}$|
| $\mathscr N$ | $\Omega_\mathscr N = \mathbb N$ |
| $\mathscr A$ | $\Omega_\mathscr A = \mathbb R^+$ |
````

```{margin}
In alcune fonti il termine _evento elementare_ è sinonimo di _esito_.
```
````{prf:definition} Evento ed evento elementare
:label: def-evento
Fissato uno spazio degli esiti $\Omega$, un _evento_ è un sottoinsieme
$E \subseteq \Omega$. In particolare, se $E = \{ \omega \}$ per qualche
$\omega \in \Omega$ si dice che $E$ è un _evento elementare_. Se dopo che
l'esperimento casuale alla base di $\Omega$ è stato eseguito ed è stato
ottenuto un esito $\omega \in E$, si diche che l'evento si è _verificato_.
In caso contrario si dice che $E$ non si è verificato.
````

Nella {prf:ref}`def-evento` il concetto di sottoinsieme è inteso anche in
senso improprio, includendo cioè $\{\}$ e $\Omega$ tra i possibili
sottoinsiemi. In realtà questi sottoinsiemi individuano due eventi
particolarmente rilevanti:
- $\{\}$ per definizione non contiene alcun esito, dunque rappresenta un
  evento che, indipendentemente dal risultato dell'esperimento casuale, non
  potrà mai verificarsi, e pertanto è detto _evento impossibile_;
- al contrario, $\Omega$ contiene tutti i possibili esiti dell'esperimento,
  e quindi è un evento che si verificherà sempre, detto _evento certo_.

Vedremo nel {ref}`sec_assiomi-kolmogorov` che il calcolo della probabilità
di un evento è legato alla valutazione di una funzione di cui l'evento stesso
è un argomento. Il dominio di questa funzione, che raccoglie dunque gli eventi
di cui vogliamo poter calcolare la probabilità, viene chiamato
_algebra degli eventi_.

```{margin}
$2^\Omega$ denota l'insieme delle parti di $\Omega$, pertanto un'algebra
è un insieme di eventi, o equivalentemente un insieme di sottoinsiemi di
$\Omega$.
```
````{prf:definition} Algebra degli eventi
:label: def-algebra-degli-eventi
Fissato uno spazio degli esiti $\Omega$, si definisce _algebra degli eventi_
una qualsiasi collezione di eventi $\mathsf A \subseteq 2^\Omega$ che:

1. contiene lo spazio degli esiti ($ \Omega \in \mathsf A$),
2. è chiusa rispetto all'operazione di complemento
   ($\forall E \in \mathsf A \; \overline E \in \mathsf A$),
3. è chiusa rispetto all'operazione di unione
   ($\forall E, F \in \mathsf A \; E \cup F \in \mathsf A$).

````

Dunque un'algebra degli eventi è una collezione di eventi chiusa rispetto
alle operazioni di unione e complemento. La {prf:ref}`def-algebra-degli-eventi`
implica una serie di altre proprietà che sono dimostrate di seguito.

````{prf:theorem}
:label: insieme-vuoto-in-algebra
Un'algebra degli eventi contiene sempre l'evento impossibile.
````
````{admonition} _
:class: myproof

Sia $\mathsf A$ un'algebra degli eventi. La {prf:ref}`def-algebra-degli-eventi`
assicura che $\Omega \in \mathsf A$, e applicando la proprietà di chiusura
rispetto al complemento si ottiene $\{\} = \overline \Omega \in \mathsf A$.
````

````{prf:theorem}
:label: teo-chiusura-algebra-eventi
Un'algebra degli eventi è chiusa rispetto:

1. all'unione di un numero finito di eventi,
2. all'intersezione di un numero finito di eventi, e
3. alla differenza tra due eventi.
````
````{admonition} _
:class: myproof

Fissato $n \in \mathbb N$, sia $E_1, \ldots, E_n$ una successione di $n$
eventi nell'algebra $\mathsf A$ considerata.

Per dimostrare primo punto, definiamo $U_r = \cup_{i=1}^r E_i$ per ogni
$r = 1, \ldots, n$ e applichiamo il principio di induzione per dimostrare che
$U_r \in \mathsf A$ per ogni $r$. La base dell'induzione è banalmente vera:
$U_1$ coincide con $E_1$ e dunque appartiene all'algebra. Ipotizziamo ora che
per un generico $r$ valga $U_r \in \mathsf A$: siccome
$U_{r+1} = U_r \cup E_{r+1}$, la chiusura di $\mathsf A$ rispetto all'unione
di due insiemi implica $U_{r+1} \in \mathsf A$.

Il secondo punto si dimostra applicando innanzitutto una delle leggi di De
Morgan agli eventi $E_1$ ed $E_2$, ottenendo

```{math}
E_1 \cap E_2 = \overline{\overline E_1 \cup \overline E_2} \,,
```

e notando che le proprietà di chiusura rispetto a unione e complemento
richieste dalla {prf:ref}`def-algebra-degli-eventi` implicano che
$E_1 \cap E_2 \in \mathsf A$. Per estendere questa proprietà all'intersezione
di un numero finito di eventi si può applicare il principio di induzione in
modo analogo a quanto fatto nella prima parte della dimostrazione.

Infine,la tesi al terzo piunto si ottiene facilmente notando che
$E_1 \backslash E_2 = E_1 \cap \overline E_2$ e ricordando che per quanto
visto finora $\mathsf A$ è chiuso rispetto al complemento e all'intersezione
di eventi.
````

In generale, l'algebra degli eventi deve essere abbastanza grande da
comprendere tutti gli eventi dei quali potremmo volere ragionevolmente
calcolare la probabilità, ma, nel contempo, più l'algebra è grande e più
può diventare difficile associare a tutti i suoi elementi dei valori di
probabilità in modo

- corretto, così da riflettere l'effettiva incertezza degli eventi, e
```{margin}
Vedremo nel {ref}`sec_assiomi-kolmogorov` che il concetto di coerenza è
matematicamente catturato dagli assiomi di Kolmogorov.
```
- coerente con le relazioni che esistono tra gli eventi (per esempio, se
  un evento è molto probabile allora intuitivamente il suo complemento
  dovrà essere poco probabile).

Quando lo spazio degli esiti $\Omega$ è finito, normalmente si utilizza come
algebra degli eventi l'insieme delle parti $2^\Omega$: questo perché se per
ogni $\omega \in \Omega$ si vuole poter calcolare la probabilità dell’_evento
elementare_ $\{ \omega \}$, la sola proprietà di chiusura rispetto all'unione
descritta nella {prf:ref}`def-algebra-degli-eventi` permette di dimostrare che
ogni evento è contenuto in $\mathsf A$.

```{prf:theorem} Algebra degli eventi di uno spazio degli esiti finito
Sia $\mathsf A$ un'algebra degli eventi per uno spazio degli esiti finito
$\Omega$. Se $\mathsf A$ contiene tutti gli eventi elementari allora
$\mathsf A = 2^\Omega$.
```
````{admonition} _
:class: myproof

Un generico evento $E \subseteq \Omega$ deve essere un insieme finito, essendo
$\Omega$ stesso finito. Quindi devono esistere $n$ esiti
$w_1, \ldots, w_n \in \Omega$ tali che $E = \{ w_1, \ldots, w_n \}$. Per
ipotesi, per ogni $i = 1, \ldots, n$ l'evento elementare $\{ w_i \}$ appartiene
ad $\mathsf A$ e dunque

```{math}
E = \bigcup_{i=1}^n \{ E_i \} \in \mathsf A.
```

Riassumendo, ogni $E \subseteq \Omega$ appartiene ad $\mathsf A$, che quindi
deve essere l'insieme delle parti di $\Omega$.
````

Pertanto, gli esperimenti casuali $\mathscr P$, $\mathscr O$ e $\mathscr C$
saranno tipicamente associati a un'algebra degli eventi che coincide con
la famiglia di tutti i possibili insiemi di eventi in $\Omega$. Va sottolineato
che questo non significa che in questi casi $2^\Omega$ sia l'unica algebra
possibile. Per esempio:

```{margin}
Come è facilmente intuibile, $\{ \}$ e $\Omega$ sono rispettivamente l'evento
che non si verifica mai e quello che si verifica sempre.
```
- indipendentemente da $\Omega$, $\mathsf A_0 = \{ \{\}, \Omega \}$ è sempre
  un'algebra degli eventi, probabilmente poco interessante perché si focalizza
  solo su due eventi particolari, ma essa ha la proprietà di essere contenuta
  in tutte le  possibili algebre, e dunque di essere la più piccola algebra
  costruibile;
- se consideriamo l'esperimento casuale $\mathscr O$ e il corrispondente
  spazio degli esiti $\Omega = \{ \text{Azzurro}, \text{Marrone}, \text{Nero},
  \text{Verde}\}$, la collezione di eventi $\mathsf A = \{ \{\},
  \{ \text{Azzurro}, \text{Verde}\}, \{ \text{Marrone}, \text{Nero} \},
  \Omega \}$ è un'algebra, più grande di $\mathsf A_0$ e più piccola di
  $2^\Omega$, che si focalizza sugli eventi relativi a colori chiari e scuri
  degli occhi.

```{margin}
Potremmo, per esempio, considerare $2^\Omega$.
```
Le cose si complicano quando lo spazio degli esiti è infinito, perché in
questo caso è possibile costruire algebre degli eventi che sono anch'esse
infinite. Abbiamo visto che la
{prf:ref}`def-algebra-degli-eventi` implica che queste algebre sono chiuse
rispetto all'unione di un numero finito di eventi, ma la stessa proprietà
potrebbe non valere quando consideriamo l'unione di una _famiglia infinita_ di
eventi, come evidenziato nell'esempio che segue.

````{prf:example}
:label: ex-controesempio-sigma-algebra
Concentriamoci sull'esperimento casuale $\mathscr N$, e dal corrispondente
spazio degli esiti $\Omega = \mathbb N$ costruiamo la seguente collezione di
eventi:

```{math}
\mathsf A = \{ E \subseteq \Omega
\text{ tale che } E \text{ è finito oppure }
\overline E \text{ è finito} \}.
```

Intuitivamente, indicato con $N$ il numero di supereroi diversi che compaiono
in un fumetto, $\mathsf A$ ci permette di ragionare in termini di eventi come
$E = \{ N = 42 \}$ oppure $F = \{ N \leq 4 \}$ (che appartengono all'algebra
perché sono finiti: $E = \{ 42 \}$ e $F = \{ 0, 1, 2, 3, 4 \}$), ma anche
dell'evento $G = \{ N > 10 \}$, in quanto il suo complementare è un evento
finito. Possiamo verificare che $\mathsf A$ è un'algebra degli eventi, come
dettagliato nei punti seguenti.

1. $\Omega = \mathbb N \in \mathsf A$ in quanto il suo complemento è l'insieme
   vuoto, che è un insieme finito;
2. Se $E \in \mathsf A$, per definizione deve valere uno dei due casi seguenti:
   - $E$ è un insieme finito, pertanto il complementare di $\overline E$ è un
     insieme finito, dunque $\overline E \in \mathsf A$,
   - $\overline E$ è un insieme finito, dunque $\overline E \in \mathsf A$,

   dunque $\mathsf A$ è chiusa rispetto all'operazione di complemento.
3. Se $E, F \in \mathsf A$ deve necessariamente essere verificato uno dei
   seguenti tre casi:
   - entrambi gli eventi sono finiti, pertanto lo è anche $E \cup F$;
   - entrambi gli eventi sono infiniti, ma sia $\overline E$ che $\overline F$
     sono finiti, dunque
     $\overline{E \cup F} = \overline E \cap \overline F$,
     essendo interzione di due insiemi finiti, è esso stesso finito;
   - uno dei due eventi è finito e l'altro è infinito, e senza ledere la
     generalità del ragionamento possiamo supporre che $E$ sia finito e $F$
     sia infinito; $\overline F$ deve però essere finito perché
     $F \in \mathsf A$, e siccome
     $\overline{E \cup F} = \overline E \cap \overline F \subseteq \overline F$,
     $\overline{E \cup F}$ è finito perché è sottoinsieme di un insieme finito.

   In tutti i casi abbiamo dimostrato che $E \cup F$ oppure
   $\overline{E \cup F}$ è un insieme finito, pertanto
   $E \cup F \in \mathsf A$, il che significa che $\mathsf A$ è chiusa rispetto
   all'unione.

Consideriamo però la successione di insiemi definita da
$ P_n = \{ 2 i, i = 1, \ldots, n \} $. In generale, $P_n$ è l'evento che
si verifica quando il numero di supereroi nel fumetto è pari e minore o uguale
di $2 n$, e quindi contiene sempre un numero finito di elementi, il che
implica $P_n \in \mathsf A$ per ogni $n$. L'evento
$P = \cup_{n=1}^{+\infty} P_n$ si verifica quindi quando in un fumetto è
presente un numero pari di supereroi, e il suo complemento si verificherà
quando tale numero è dispari. Dunque sia $P$, sia il suo complemento sono
infiniti e dunque $P \not\in \mathsf A$.
````

Per garantire di poter calcolare la probabilità dell'unione di una quantità
infinita numerabile di eventi, è necessario estendere l'algebra degli eventi
in una _sigma-algebra_ come indicato nella definizione che segue.

````{prf:definition} Sigma-algebra degli eventi
:label: def-sigma-algebra-degli-eventi
Ogni algebra degli eventi $\mathsf A$ su uno spazio degli esiti $\Omega$
è una _sigma-algebra_ se rispetta la seguente proprietà oltre a quelle della
{prf:ref}`def-algebra-degli-eventi`: per ogni successione infinita
$E_1, E_2, \ldots$ di eventi in $\mathsf A$, si verifica

```{math}
\bigcup_{n=1}^{+\infty} E_i \in \mathsf A.
```
````

In generale si utilizza il termine _spazio misurabile_ per indicare una
coppia $(\Omega, \mathsf A)$ in cui $\mathsf A$ indica un'algebra o una
sigma-algebra degli eventi.
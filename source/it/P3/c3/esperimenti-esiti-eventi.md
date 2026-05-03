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
# Esperimenti, esiti ed eventi

Come ho descritto all'inizio di questo capitolo, alla base di ogni ragionamento
di tipo probabilistico si trova un _esperimento casuale_: un'esperienza non
deterministica formalizzata nella definizione seguente.

```{margin}
Indicherò gli esperimenti casuali utilizzando le lettere maiuscole corsive,
come $\mathscr E$, $\mathscr F$ e così via, scegliendo ove possibile lettere
legate al significato dell'esperimento stesso.
```
```{prf:definition} Esperimento casuale
:label: def-esperimento-casuale
Un _esperimento casuale_ (o _aleatorio_) è una qualsiasi esperienza che
può dare risultati differenti quando essa viene ripetuta più volte partendo da
condizioni iniziali identiche.
```

```{prf:example}
:label: ex-experiments

Immaginiamo di acquistare tutte le settimane un nuovo numero di un fumetto dei
Fantastici 4: ogni volta i contenuti saranno diversi, permettendoci di
considerare per esempio gli esperimenti casuali che seguono:

- $\mathscr P$: controllare se il numero totale di occorrenze della Donna
  invisibile è pari,
- $\mathscr O$: verificare quale sia il colore degli occhi del primo supereroe
  che compare nel fumetto,
- $\mathscr C$ elencare l'ordine di apparizione dei Fantastici 4,
- $\mathscr N$: contare il numero di diversi supereroi presenti, e
- $\mathscr A$: misurare l'altezza (in cm.) dell'ultimo supereroe che compare
  nel fumetto.

```

```{margin}
Denoterò gli esiti usando le lettere minuscole dell'alfabeto greco,
utilizzando possibilmente $\omega$ (omega minuscola) o alcune sue varianti.
```
```{prf:definition} Esito
:label: def-esito
Ogni possibile risultato $\omega$ di un esperimento casuale $\mathscr E$ prende
il nome di _esito_.
```

```{prf:example}
:label: ex-outcomes

Facendo riferimento agli esperimenti introdotti nell’{prf:ref}`ex-experiments`,
un esempio di esito è «falso» per $\mathscr P$, «azzurro» per $\mathscr O$,
«Torcia umana, Donna invisibile, Mister Fantastic, Cosa» per $\mathscr C$,
$3$ per $\mathscr N$ e $183$ per $\mathscr A$.
```

L'insieme di tutti gli esiti di un esperimento casuale, che rappresenta il
punto iniziale della modellazione matematica che userò per introdurre il
concetto di probabilità, prende il nome di _spazio degli esiti_.

```{margin}
Lo spazio degli esiti viene spesso anche chiamato _spazio campionario_ o
_insieme universo_, e in letteratura esistono notazioni alternative che lo
denotano usando per esempio le lettere $S$ e $U$.
```

````{prf:definition} Spazio degli esiti
:label: def-spazio-esiti
L'insieme di tutti i possibili esiti di un generico esperimento
casuale $\mathscr E$ viene chiamato _spazio degli esiti_, e lo si denota
usualmente tramite la lettera $\Omega$ (omega maiuscola).
````

```{prf:example}
:label: ex-outcome-spaces

La {numref}`tab-esempi-spazi-esiti` descrive lo spazio degli esiti per ognuno
degli esperimenti casuali presi in considerazione
nell’{prf:ref}`ex-experiments`. Va notato che la scelta per
$\Omega_\mathscr O$ è arbitraria.
```

````{table} Esempi di spazi degli esiti per gli esperimenti casuali $\mathscr P$, $\mathscr O$, $\mathscr C$, $\mathscr N$ e $\mathscr A$ precedentemente introdotti.
:name: tab-esempi-spazi-esiti

| Esperimento | Spazio degli esiti |
|--------------|-----------------------------------|
| $\mathscr P$ | $\Omega_\mathscr P = \{ \text{vero}, \text{falso} \}$ |
| $\mathscr O$ | $\Omega_\mathscr O = \{ \text{azzurro}, \text {marrone}, \text{nero},\text{verde} \}$ |
| $\mathscr C$ | $\Omega_\mathscr C = $ insieme di tutte le permutazioni degli elementi in  $\{ \text{Mister Fantastic}, \text{Donna invisibile}, \text{Torcia umana}, \text{Cosa}\}$|
| $\mathscr N$ | $\Omega_\mathscr N = \mathbb N$ |
| $\mathscr A$ | $\Omega_\mathscr A = \mathbb R^+$ |
````


````{prf:definition} Evento ed evento elementare
:label: def-evento
Fissato uno spazio degli esiti $\Omega$, un _evento_ è un sottoinsieme
$E \subseteq \Omega$. In particolare, se $E = \{ \omega \}$ per qualche
$\omega \in \Omega$ si dice che $E$ è un _evento elementare_. Se dopo che
l'esperimento casuale alla base di $\Omega$ è stato eseguito ed è stato
ottenuto un esito $\omega \in E$, si diche che l'evento si è _verificato_.
In caso contrario si dice che $E$ non si è verificato.
````

In questa definizione il concetto di sottoinsieme è inteso anche in senso
improprio, includendo cioè $\varnothing$ e $\Omega$ tra i possibili
sottoinsiemi. In realtà questi sottoinsiemi individuano due eventi
particolarmente rilevanti:

- per definizione, $\varnothing$ non contiene alcun esito, dunque rappresenta un
  evento che, indipendentemente dal risultato dell'esperimento casuale, non
  potrà mai verificarsi, e pertanto è detto _evento impossibile_;
- al contrario, $\Omega$ contiene tutti i possibili esiti dell'esperimento,
  e quindi è un evento che si verificherà sempre, detto _evento certo_.

Il fatto che gli eventi siano definiti come insiemi non è una scelta
arbitraria: permette di ereditare direttamente il vocabolario e gli strumenti
della teoria degli insiemi, che nel contesto della probabilità assumono una
semantica precisa. L'unione corrisponde alla disgiunzione logica: l'evento $E
\cup F$ si verifica quando si verifica almeno uno dei due tra $E$ ed $F$, così
come l'intersezione corrisponde alla congiunzione: $E \cap F$ si verifica solo
al verificarsi di entrambi $E$ ed $F$, con ovvie generalizzazioni al caso di
operatori $n$-ari. Analogamente, $\Omega$ costituisce l'insieme universo e il
complemento individua la negazione logica: $\overline E$ si verifica se e solo
se non si verifica $E$. Infine, la relazione di sottoinsieme cattura
l'implicazione logica: se $E \subseteq F$, allora ogni esito che realizza $E$
deve realizzare anche $F$, pertanto $E \rightarrow F$.

Nella {prf:ref}`def-evento` ho identificato un evento con un sottoinsieme di
$\Omega$. Questa scelta appare del tutto naturale e, nel caso in cui lo spazio
degli esiti sia numerabile, non crea alcuna difficoltà: tutti i sottoinsiemi di
$\Omega$ possono essere considerati eventi. Quando però $\Omega$ non è
numerabile (come accade per esempio nell'esperimento $\mathscr A$), non è più
possibile procedere in questo modo senza rinunciare ad alcune proprietà
naturali della probabilità. Entrare nei dettagli di questo problema richiede un
approccio completamente diverso (e meno immediato) allo studio del calcolo
delle probabilità, basato sulla [teoria della
misura](https://it.wikipedia.org/wiki/Misura_(matematica)). Detto in modo molto
approssimativo, in questi casi non è possibile associare una probabilità a
_tutti_ i possibili sottoinsiemi di $\Omega$ preservando una ragionevole
_proprietà di additività_, per cui la probabilità dell’unione di eventi
disgiunti è sempre uguale alla somma delle probabilità dei singoli eventi,
anche nel caso di unioni numerabili. In pratica, esistono sottoinsiemi così
irregolari da rendere impossibile definire una probabilità su tutti gli eventi
mantenendo questa proprietà. Per questo motivo si introduce una collezione di
sottoinsiemi di $\Omega$, detta _algebra degli eventi_, che descrive l’insieme
degli eventi ai quali vogliamo assegnare una probabilità. Vedremo infatti nel
{ref}`sec_assiomi-kolmogorov` che questa collezione &mdash; o, più
precisamente, una sua estensione &mdash; costituisce il dominio della funzione
che associa a ogni evento la sua probabilità, in modo da garantire che la sopra
menzionata proprietà di additività valga sempre.

```{margin}
$2^\Omega$ denota l'insieme delle parti di $\Omega$, pertanto un'algebra
è un insieme di eventi, o equivalentemente un insieme di sottoinsiemi di
$\Omega$.
```
````{prf:definition} Algebra degli eventi
:label: def-algebra-degli-eventi
Fissato uno spazio degli esiti $\Omega$, un’_algebra degli eventi_ è
una qualsiasi collezione di eventi $\mathsf A \subseteq 2^\Omega$ che:

1. contiene lo spazio degli esiti ($ \Omega \in \mathsf A$),
2. è chiusa rispetto all'operazione di complemento
   ($\forall E \in \mathsf A \; \overline E \in \mathsf A$),
3. è chiusa rispetto all'operazione di unione
   ($\forall E, F \in \mathsf A \; E \cup F \in \mathsf A$).

````

Il terzo punto nella definizione precedente è collegato alla proprietà di
additività: la chiusura rispetto all’unione garantisce che, dati due eventi,
anche la loro unione sia ancora un evento e quindi abbia una probabilità ben
definita. In particolare, nel caso di eventi disgiunti, questa proprietà
permette di estendere il calcolo della probabilità all’unione di un numero
finito di eventi disgiunti, per iterazione.

È lecito chiedersi come mai la {prf:ref}`def-algebra-degli-eventi` richieda la
chiusura rispetto alle operazioni di unione e complemento, ma non rispetto
all'intersezione. In realtà, ciò non è necessario, in quanto è automaticamente
implicato dalla definizione stessa, unitamente ad altre proprietà, dimostrate
di seguito.

````{prf:theorem}
:label: insieme-vuoto-in-algebra
Un'algebra degli eventi contiene sempre l'evento impossibile.
````
````{admonition} _
:class: myproof

Sia $\mathsf A$ un'algebra degli eventi. La {prf:ref}`def-algebra-degli-eventi`
assicura che $\Omega \in \mathsf A$, e applicando la proprietà di chiusura
rispetto al complemento si ottiene $\varnothing = \overline \Omega \in \mathsf A$.
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

Il secondo punto si dimostra partendo dalla legge di De
Morgan $\overline{E_1 \cap E_2} = \overline{E_1} \cup \overline{E_2}$, che
equivale a
$E_1 \cap E_2 = \overline{\overline E_1 \cup \overline E_2}$.
Le proprietà di chiusura rispetto a unione e complemento richieste dalla
{prf:ref}`def-algebra-degli-eventi` implicano pertanto che
$E_1 \cap E_2 \in \mathsf A$. Per estendere questa proprietà all'intersezione
di un numero finito di eventi si può applicare il principio di induzione in
modo analogo a quanto fatto nella prima parte della dimostrazione.

Infine, la tesi al terzo punto si ottiene facilmente notando che
$E_1 \backslash E_2 = E_1 \cap \overline E_2$ e ricordando che per quanto
visto finora $\mathsf A$ è chiusa rispetto al complemento e all'intersezione
di eventi.
````

In generale, l'algebra degli eventi deve essere abbastanza grande da
comprendere tutti gli eventi dei quali potremmo volere ragionevolmente
calcolare la probabilità, ma, nel contempo, più l'algebra è grande e più
può diventare difficile associare a tutti i suoi elementi dei valori di
probabilità in modo corretto e coerente, come ho spiegato sopra.
Quando lo spazio degli esiti $\Omega$ è finito, normalmente si utilizza come
algebra degli eventi l'insieme delle parti $2^\Omega$: questo perché se per
ogni $\omega \in \Omega$ si vuole poter calcolare la probabilità dell’_evento
elementare_ $\{ \omega \}$, la sola proprietà di chiusura rispetto all'unione
descritta nella {prf:ref}`def-algebra-degli-eventi` permette di dimostrare che
ogni evento è contenuto in $\mathsf A$.

```{prf:theorem} Algebra degli eventi di uno spazio degli esiti finito
Sia $\mathsf A$ un'algebra degli eventi per uno spazio degli esiti finito
$\Omega$. Se $\mathsf A$ contiene tutti gli eventi elementari, allora
$\mathsf A = 2^\Omega$.
```
````{admonition} _
:class: myproof

Un generico evento $E \subseteq \Omega$ deve essere un insieme finito, essendo
$\Omega$ stesso finito. Quindi devono esistere $n$ esiti
$w_1, \ldots, w_n \in \Omega$ tali che $E = \{ w_1, \ldots, w_n \}$. Per
ipotesi, per ogni $i = 1, \ldots, n$ l'evento elementare $\{ w_i \}$ appartiene
ad $\mathsf A$ e dunque, per il terzo assioma di Kolmogorov,

```{math}
E = \bigcup_{i=1}^n \{ w_i \} \in \mathsf A \enspace.
```

Riassumendo, ogni $E \subseteq \Omega$ appartiene ad $\mathsf A$, che quindi
deve essere l'insieme delle parti di $\Omega$.
````

Pertanto, gli esperimenti casuali $\mathscr P$, $\mathscr O$ e $\mathscr C$
saranno tipicamente associati a un'algebra degli eventi che coincide con
la famiglia di tutti i possibili insiemi di eventi in $\Omega$. Va sottolineato
che questo non significa che in questi casi $2^\Omega$ sia l'unica algebra
possibile.

```{prf:example}
:label: ex-algebra-min

Indipendentemente da $\Omega$, $\mathsf A_0 = \{ \varnothing, \Omega \}$ è sempre
un'algebra degli eventi, probabilmente poco interessante perché contiene solo
l'evento impossibile e l'evento certo, ma essa ha la proprietà di essere 
ontenuta in tutte le  possibili algebre, e dunque di essere la più piccola
algebra costruibile.
```

```{prf:example}
:label: ex-algebra-sub

Se consideriamo l'esperimento casuale $\mathscr O$ e il corrispondente spazio
degli esiti $\Omega = \{ \text{Azzurro}, \text{Marrone}, \text{Nero},
\text{Verde}\}$, la collezione di eventi $\mathsf A = \{ \varnothing,
\{ \text{Azzurro}, \text{Verde}\}, \{ \text{Marrone}, \text{Nero} \},
\Omega \}$ è un'algebra, più grande di $\mathsf A_0$ e più piccola di
$2^\Omega$, che si focalizza sugli eventi relativi a colori chiari e scuri
degli occhi.
```

L’{prf:ref}`ex-algebra-sub` è in realtà un caso particolare di una costruzione
più generale, che permette di ottenere un'algebra a partire da una partizione
dello spazio degli esiti.

```{prf:definition} Algebra indotta da una partizione
:label: def-algebra-indotta-partizione
Sia $\Omega$ uno spazio degli esiti e sia $\mathcal P = \{ P_1, P_2, \ldots,
P_n \}$ una partizione di $\Omega$, ovvero una famiglia di sottoinsiemi non
vuoti, a due a due disgiunti e tali che $\bigcup_{i=1}^n P_i = \Omega$.
L’_algebra indotta dalla partizione $\mathcal P$_ è la collezione di eventi
$\mathsf A_{\mathcal P}$ costituita da tutte le possibili unioni di elementi
di $\mathcal P$, includendo l'insieme vuoto (interpretato come l'unione di
zero elementi):

$$
\mathsf A_{\mathcal P} = \left\{ \bigcup_{i \in I} P_i \quad \forall I \subseteq
\{1, \ldots, n\} \right\}.
$$
```

È immediato verificare che $\mathsf A_{\mathcal P}$ è un'algebra: essa
contiene $\Omega$ (ottenuto come unione di tutti gli elementi della
partizione), è chiusa rispetto al complemento (dato che il complemento di
un'unione di elementi è l'unione degli elementi rimanenti) e rispetto all'unione
(l'unione di due elementi di $\mathsf A_{\mathcal P}$ è ancora un'unione di
elementi della partizione). L’{prf:ref}`ex-algebra-sub` corrisponde al caso
particolare in cui $\mathcal P = \{ \{ \text{Azzurro}, \text{Verde} \},
\{ \text{Marrone}, \text{Nero} \} \}$.

```{margin}
Potremmo, per esempio, considerare $2^\Omega$.
```
Le cose si complicano quando lo spazio degli esiti è infinito, perché in questo
caso è possibile costruire algebre degli eventi che sono anch'esse infinite.
Abbiamo visto che la {prf:ref}`def-algebra-degli-eventi` implica che queste
algebre sono chiuse
rispetto all'unione di un numero finito di eventi, ma la stessa proprietà
potrebbe non valere quando consideriamo l'unione di una _famiglia infinita_ di
eventi, come evidenziato nell'esempio che segue.

````{prf:example}
:label: ex-controesempio-sigma-algebra

Un insieme si dice _cofinito_ se il suo complementare è finito. Concentriamoci
sull'esperimento casuale $\mathscr N$, e dal corrispondente spazio degli esiti
$\Omega = \mathbb N$ costruiamo la seguente collezione di eventi:

```{math}
\mathsf A = \{ E \subseteq \Omega
\text{ tale che } E \text{ è finito oppure cofinito} \} \enspace.
```

Intuitivamente, indicato con $n$ il numero di supereroi diversi che compaiono
in un fumetto, $\mathsf A$ ci permette di ragionare in termini di eventi come
$E = \{ 42 \}$ oppure $F = \{ n \mid n \leq 4 \}$ (che appartengono all'algebra
perché sono finiti), ma anche di eventi quali $G = \{ n \mid n > 10 \}$, che
è descritto da un insieme cofinito. Possiamo verificare che $\mathsf A$ è
un'algebra degli eventi, come dettagliato nei punti seguenti.

1. $\Omega \in \mathsf A$, in quanto il suo complemento è l'insieme vuoto, che
   è un insieme finito.
2. Se $E \in \mathsf A$, deve essere finito o cofinito: nel primo caso
   $\overline E$ è cofinito, e nel secondo è finito, dunque è garantita la
   chiusura ripetto all'operazione di complemento.
3. Infine, dati $E, F \in \mathsf A$, sussistono i casi seguenti:

   - i due insiemi sono entrambi finiti, e dunque lo è anche $E \cup F$;
   - i due insiemi sono entrambi cofiniti, il che significa che
     $\overline{E \cup F} = \overline E \cap \overline F$ èun insieme finito,
     essendo uguale all'intersezione di due insiemi finiti;
   - uno dei due insiemi è finito, mentre l'altro è cofinito, quindi seguendo
     lo stesso ragionamento del punto precedente si verifica che
     $\overline{E \cup F}$ è l'intersezione tra un insieme infinito e un
     insieme finito, e deve dunque essere finito.

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
quando tale numero è dispari. Dunque $P$ non è né finito, né cofinito, e ciò
implica che questo insieme non può appartenere ad $\mathsf A$.
````

L’esempio precedente mostra che la chiusura rispetto a unioni finite non è
sufficiente quando si considerano famiglie infinite di eventi. In particolare,
a partire da una semplice algebra degli eventi non è garantito che l’unione di
una famiglia numerabile di eventi sia ancora un evento, e quindi che la sua
probabilità sia ben definita in modo coerente con la proprietà di additività.
Per trattare in modo sistematico unioni numerabili di eventi, si introduce una
struttura più ricca, detta $\sigma$-algebra.

````{prf:definition} $\sigma$-algebra degli eventi e spazio misurabile
:label: def-sigma-algebra-degli-eventi
Ogni algebra degli eventi $\mathsf A$ su uno spazio degli esiti $\Omega$
è una _$\sigma$-algebra_ se, oltre a rispettare le proprietà indicate nella
{prf:ref}`def-algebra-degli-eventi`, è anche chiusa rispetto all'unione di
una famiglia numerabile di eventi: per ogni successione $E_1, E_2, \ldots$ di
eventi in $\mathsf A$, si ha

```{math}
\bigcup_{n=1}^{+\infty} E_n \in \mathsf A.
```

una coppia $(\Omega, \mathsf A)$ in cui $\mathsf A$ indica una $\sigma$-algebra
di sottoinsiemi di $\Omega$ viene detta _spazio misurabile_.
````

Ogni algebra di sottoinsiemi può essere estesa a una $\sigma$-algebra.
Intuitivamente, partendo da una famiglia di insiemi chiusa rispetto a un numero
finito di operazioni, è sempre possibile «completarla» aggiungendo tutti gli
insiemi necessari per garantire la chiusura anche rispetto a unioni numerabili.
Il risultato è la più piccola $\sigma$-algebra che contiene la famiglia di
partenza.

## Esercizi

````{exercise} •
:label: ex-shield-esperimenti

La [S.H.I.E.L.D.](https://marvel.fandom.com/wiki/S.H.I.E.L.D.)
monitora quotidianamente le attività degli
[Avengers](https://marvel.fandom.com/wiki/Avengers_(Earth-616)). Per ognuna
delle seguenti situazioni, identificate l'esperimento casuale, gli esiti
possibili e il relativo spazio:

1. osservare quale Avenger risponde per primo a un'emergenza,
2. controllare se Thor usa Mjolnir (il suo martello) durante una missione,
3. contare il numero di cattivi sconfitti in una settimana.

````

```{solution} ex-shield-esperimenti
:class: dropdown

1. L'esperimento è $\mathscr R$ = osservare quale Avenger risponde per primo.
   Se consideriamo la formazione iniziale del Marvel Cinematic Universe (quella
   del primo film, pubblicato nel 2012) gli esiti possibili sono:
   $\text{Iron Man}$, $\text{Capitan America}$, $\text{Thor}$, $\text{Hulk}$,
   $\text{Vedova Nera}$ e $\text{Occhio di Falco}$. Lo spazio degli esiti è
   dunque l'insieme finito $\Omega_{\mathscr R} = \{ \text{Iron Man},
   \text{Capitan America}, \text{Thor}, \text{Hulk}, \text{Vedova Nera}, 
   \text{Occhio di Falco} \}$.

2. L'esperimento è $\mathscr M$ = verificare se Thor usa Mjolnir, dunque gli
   esiti possibili sono $\text{vero}$ e $\text{falso}$, e lo spazio degli esiti
   è $\Omega_{\mathscr M} = \{\text{vero}, \text{falso}\}$.

3. L'esperimento è $\mathscr C$ = contare il numero di cattivi sconfitti, e gli
   esiti possibili sono tutti gli interi non negativi, perché teoricamente non
   c'è un limite superiore al numero di cattivi che possono essere sconfitti, e
   non va esclusa la possibilità che non venga sconfitto alcun cattivo.
   Pertanto, lo spazio degli esiti è
   $\Omega_{\mathscr C} = \mathbb{Z}_{\geq 0}$.
```


```{exercise} •
:label: ex-spazio-esiti-capelli

Considerate l'esperimento di scegliere casualmente un colore dei capelli nel
dataset dei supereroi. Descrivete lo spazio degli esiti $\Omega$ e indicate se
è finito o infinito.
```
<!-- CELL-MARKER-24-START -->
```{code-cell} ipython3
import pandas as pd

heroes = pd.read_csv('data/heroes.csv')
colori = heroes['hair_color'].dropna().unique()
print(f'Numero di colori distinti: {len(colori)}')
print(f'Colori: {sorted(colori)}')
```
<!-- CELL-MARKER-24-END -->

````{solution} ex-spazio-esiti-capelli
:class: dropdown

L'esperimento casuale consiste nella scelta di un colore dei capelli tra
quelli presenti nel dataset. Analizziamo il dataset per determinare i
valori distinti dell'attributo `hair_color`:

<!-- CELL-PLACEHOLDER-24 -->

Lo spazio degli esiti è dunque l'insieme dei colori trovati, e siccome
$|\Omega|$ è un numero finito, lo spazio degli esiti è finito.
````

```{exercise} •
:label: ex-eventi-elementari-jl

Riferendoti allo spazio degli esiti al primo punto
dell’{numref}`ex-shield-esperimenti`, indicate quali tra i seguenti eventi sono
elementari e quali non lo sono:

- $E_1$: «risponde per primo Iron Man,
- $E_2$: «risponde per primo un supereroe che può volare»,
- $E_3$: «risponde per primo un supereroe che è verde»,
- $E_4$: «risponde per primo un supereroe che è nato sulla Terra».
```
```{solution} ex-eventi-elementari-jl
:class: dropdown

- $E_1 = \{ \text{Iron Man} \}$ è un evento elementare perché contiene
  un solo esito.
- $E_2$ contiene $\text{Iron Man}$ e $\text{Thor}$, dunque non è un evento
  elementare perché contiene più di un esito.
- $E_3 = \{ \text{Hulk} \}$ è un insieme singoletto, dunque l'evento
  corrispondente è elementare.
- $E_4 = \{ \text{Iron Man}, \text{Capitan America}, \text{Hulk},
  \text{Vedova Nera}, \text{Occhio di Falco} \}$ non è un evento elementare
  in quanto $| E_4 | > 1$.
```

```{exercise} ••
:label: ex-operazioni-insiemistiche-metropolis

Un supercattivo attacca [Metropolis](https://dc.fandom.com/wiki/Metropolis).
Definiamo l'esperimento come l'osservazione di quale supereroe interviene. Sia
$\Omega = \{\text{Superman}, \text{Batman},
\text{Wonder Woman}, \text{Flash}, \text{Nessuno}\}$. Dati:

- $V = \{\text{Superman}, \text{Wonder Woman}\}$ (eroi in grado di volare),
- $I = \{\text{Batman}, \text{Wonder Woman}\}$ (eroi senza superpoteri innati),

descrivete quali eventi indicano gli insiemi: $V \cup I$, $V \cap I$,
$\overline{V}$, e $V \setminus I$.
```
```{solution} ex-operazioni-insiemistiche-metropolis
:class: dropdown

- $V \cup I = \{ \text{Superman}, \text{Batman}, \text{Wonder Woman} \}$
  è l'evento «interviene un eroe che può volare, oppure un eroe senza
  superpoteri innati» (o entrambe le cose).
- $V \cap I = \{ \text{Wonder Woman} \}$: è l'evento «interviene un eroe
  che può volare e che non ha superpoteri innati». Wonder Woman è l'unica
  a soddisfare entrambe le condizioni.
- $\overline{V} = \{ \text{Batman}, \text{Flash}, \text{Nessuno} \}$:
  è l'evento «non interviene un eroe che sa volare, cioè interviene un eroe che
  non vola oppure non interviene nessuno.
- $V \setminus I = \{ \text{Superman} \}$: è l'evento «interviene un eroe che
  può volare ma che non ha superpoteri innati». Superman è l'unico eroe volante
  con superpoteri innati.
```

```{exercise} ••
:label: ex-algebra-mutante

Sia $\Omega = \{ \text{Fuoco}, \text{Ghiaccio}, \text{Elettricità},
\text{Telepatia} \}$ l'insieme dei poteri che può manifestare un
[mutante](https://marvel.fandom.com/wiki/Mutants_(Homo_superior)).
Verificate se $\mathsf{A} = \{ \varnothing, \{\text{Fuoco}, \text{Ghiaccio},
\{\text{Elettricità} \}, \text{Telepatia} \}, \Omega \}$ è un'algebra degli
eventi su $\Omega$.
```
```{solution} ex-algebra-mutante
:class: dropdown

Verifichiamo le tre proprietà richieste dalla
{prf:ref}`def-algebra-degli-eventi` di algebra degli eventi.

1. Per definizione, $\Omega \in \mathsf{A}$.

2. È facile verificare che il complemento di ogni elemento di $\mathsf{A}$
   appartenga ancora ad $\mathsf{A}$:

   - $\overline{\varnothing} = \Omega \in \mathsf{A}$,
   - $\overline{\Omega} = \varnothing \in \mathsf{A}$,
   - $\overline{ \{\text{Fuoco}, \text{Ghiaccio}, \text{Elettricità} \}} =
     \{ \text{Telepatia}\} \in \mathsf{A}$,
   - $\overline{\{ \text{Telepatia} \}} =
     \{ \text{Fuoco}, \text{Ghiaccio}, \text{Elettricità} \} \in \mathsf{A}$.

3. Infine, per quanto riguarda le possibili unioni di eventi:

   - l'unione di $\varnothing$ con un qualsiasi evento in $\mathsf A$ è uguale
     a quest'ultimo, e dunque apparterrà all'algebra;
   - l'unione di un qualsiasi evento in $\mathsf A$ e $\Omega$ è uguale a
     quest'ultimo, che appartiene all'algebra;
   - $\{ \text{Fuoco}, \text{Ghiaccio}, \text{Elettricità} \} \cup
     \{ \text{Telepatia} \} = \Omega \in \mathsf{A}$.

Tutte le proprietà sono soddisfatte, quindi $\mathsf{A}$ è un'algebra
degli eventi su $\Omega$.

In realtà, questo esercizio si può risolvere molto più rapidamente, notando che
$\mathsf A$ è l'algebra indotta su $\Omega$ dalla partizione $\mathcal P =
\{ \{ \text{Fuoco}, \text{Ghiaccio}, \text{Elettricità} \},
\{ \text{Telepatia}\} \}$.
```

```{exercise} ••
:label: ex-algebra-guardiani

I [Guardiani della
Galassia](https://marvel.fandom.com/wiki/Guardians_of_the_Galaxy_(Earth-616))
(Star-Lord, Gamora, Drax, Rocket e Groot) devono essere suddivisi per una
missione. Costruite l'algebra più piccola che contenga l'evento
$E = \{\text{Rocket}, \text{Groot}\}$.
```
````{solution} ex-algebra-guardiani
:class: dropdown

Lo spazio degli esiti è $\Omega = \{\text{Star-Lord}, \text{Gamora},
\text{Drax}, \text{Rocket}, \text{Groot}\}$.

Per costruire l'algebra più piccola contenente $E = \{\text{Rocket},
\text{Groot}\}$, è necessario includere:

1. $\Omega$ (richiesto dalla definizione di algebra),
2. $\varnothing$ (conseguenza della chiusura rispetto al complemento, dato
   che $\overline{\Omega} = \varnothing$),
3. $E = \{\text{Rocket}, \text{Groot}\}$ (richiesto dall'esercizio),
4. $\overline{E} = \{\text{Star-Lord}, \text{Gamora}, \text{Drax}\}$
   (per la chiusura rispetto al complemento).

Verifichiamo che non servano altri elementi: le unioni con $\varnothing$ o
$\Omega$ non generano nuovi insiemi; a parte queste, la sola unione possibile
è $E \cup \overline{E} = \Omega$ e. Pertanto l'algebra più piccola è:

```{math}
\mathsf{A} = \{ \varnothing, \{\text{Rocket}, \text{Groot}\},
\{\text{Star-Lord}, \text{Gamora}, \text{Drax}\}, \Omega \}.
```

Anche in questo caso, notando che $\{ \{\text{Rocket}, \text{Groot}\},
\{\text{Star-Lord}, \text{Gamora}, \text{Drax}\} \}$ è una partizione di
$\Omega$, si può direttamente dimostrare che $\mathsf A$ è un'algebra, e
in particolare la più piccola algebra contenente $E$.
````

```{exercise} •••
:label: ex-dispositivo-alieno

Un dispositivo alieno genera supereroi, ognuno dei quali possiede un uno o più
superpoteri. Considerate l'esperimento casuale che consiste nell'osservare
il numero di poteri di un supereroe generato dal dispositivo, così che
$\Omega = \mathbb N$. Infine, sia $\mathsf{A}$ la collezione degli insiemi
finiti o cofiniti (cioè con complemento finito) contenuti in $\Omega$.
Dimostrate che:

1. $\mathsf A$ è un'algebra;
2. per ogni $k \in \mathbb N$, l'evento $P_k = \{ k \}$, che si verifica quando
   si osservano esattamente $k$ poteri, appartiene ad $\mathsf{A}$;
3. l'evento $D = \{ 1, 3, 5, 7, \ldots \}$, che si realizza quando si osserva
   un numero dispari di poteri, non appartiene ad $\mathsf{A}$.
```
```{solution} ex-dispositivo-alieno
:class: dropdown

1. $\Omega \in \mathsf A$, in quanto il suo complemento è l'insieme vuoto, che
   è un insieme finito. Se $E \in \mathsf A$, deve essere finito o cofinito:
   nel primo caso $\overline E$ è cofinito, e nel secondo è finito, dunque è
   garantita la chiusura ripetto all'operazione di complemento. Infine, dati
   $E, F \in \mathsf A$, sussistono i casi seguenti:

   - i due insiemi sono entrambi finiti, e dunque lo è anche $E \cup F$;
   - i due insiemi sono entrambi cofiniti, il che significa che
     $\overline{E \cup F} = \overline E \cap \overline F$ èun insieme finito,
     essendo uguale all'intersezione di due insiemi finiti;
   - uno dei due insiemi è finito, mentre l'altro è cofinito, quindi seguendo
     lo stesso ragionamento del punto precedente si verifica che
     $\overline{E \cup F}$ è l'intersezione tra un insieme infinito e un
     insieme finito, e deve dunque essere finito.

   Pertanto, $\mathsf A$ è un algebra di eventi su $\Omega$.

2. Per ogni $k \in \mathbb{N}$, $| P_k | = 1 $, quindi $P_k$ è finito e deve
   appartenere ad $\mathsf{A}$.

3 . L'insieme $D$ contiene tutti i numeri dispari, e dunque $\overline D$
   contiene i numeri pari. Ciò implica che $D$ non sia né finito, né cofinito,
   e non può appartenere all'algebra.

Questo esempio mostra che $\mathsf{A}$ non è una $\sigma$-algebra, perché
$D = \bigcup_{k=0}^{+\infty} P_{2k+1}$ non appartiene ad $\mathsf{A}$, ma è
esprimibile come l'unione numerabile di eventi in essa.
```

```{exercise} ••••
:label: ex-multiverso-spiderman

Considerate l'esperimento casuale che, partendo da un gruppo di universi nel
[Multiverso Marvel](https://marvel.fandom.com/wiki/Multiverse), consiste nel
selezionare a caso un universo e osservare quale versione di Spider-Man vi
appare. Definite:

1. un possibile spazio degli esiti $\Omega$ (considerando almeno cinque
   universi),
2. quattro eventi significativi in questo spazio, che non siano tutti eventi
   elementari,
3. un'algebra $\mathsf{A}$ diversa da $2^\Omega$ che contenga tali eventi,
   verificando esplicitamente le tre proprietà della
   {prf:ref}`def-algebra-degli-eventi`.
```
````{solution} ex-multiverso-spiderman
:class: dropdown

1. Consideriamo ad esempio lo spazio degli esiti che contiene le seguenti sei
   varianti di Spider-Man:
   
   ```{math}
   \Omega = \{ \text{Peter Parker}, \text{Miles Morales},
   \text{Gwen Stacy}, \text{Miguel O'Hara}, \text{Noir},
   \text{Spider-Ham} \} \enspace.
   ```

2. Risulta conveniente ragionare in termini della partizione di $\Omega$
   formata dai seguenti eventi:

   - $E_1 = \{\text{Peter Parker}, \text{Miles Morales}\}$
     (gli Spider-Man della Terra principale, intesa come l'Universo
     [Terra-1610](https://marvel.fandom.com/wiki/Earth-1610)),
   - $E_2 = \{\text{Gwen Stacy}\}$ (Spider-Woman nell'Universo
     [Terra-65](https://marvel.fandom.com/wiki/Earth-65)),
   - $E_3 = \{\text{Miguel O'Hara}\}$ (Spider-Man nell'Universo del futuro
     [Terra-928](https://marvel.fandom.com/wiki/Earth-928)),
   - $E_4 = \{\text{Noir}, \text{Spider-Ham}\}$ (due Spider-Man negli
     Universi alternativi
     [Terra-90214](https://marvel.fandom.com/wiki/Earth-90214) e
     [Terra-8311](https://marvel.fandom.com/wiki/Earth-8311)).

3. Possiamo costruire l'algebra generata dalla partizione $\mathcal P$
   considerata al punto precedente:
   
   $$
   \mathsf{A}_{\mathcal P} = \{ \varnothing, E_1, E_2, E_3, E_4, E_1 \cup E_2,
   E_1 \cup E_3, E_1 \cup E_4, E_2 \cup E_3, E_2 \cup E_4, E_3 \cup E_4, \\
   E_1 \cup E_2 \cup E_3, E_1 \cup E_2 \cup E_4, E_1 \cup E_3 \cup E_4,
   E_2 \cup E_3 \cup E_4, \Omega \} \enspace,
   $$

   che aggrega $|\mathsf{A}| = 2^4 = 16$ elementi ed è dunque più piccola
   dell'insieme delle parti di $\Omega$.
````

```{exercise} ••••
:label: ex-universo-finito

Nell’{prf:ref}`ex-controesempio-sigma-algebra` del testo, l'algebra
$\mathsf{A}$ non è una $\sigma$-algebra. Immaginate un universo parallelo, nel
quale tutti i fumetti hanno sempre un numero finito di supereroi (diciamo, al
massimo $1000$). In questo caso, la stessa costruzione produrrebbe una
$\sigma$-algebra? Giustificate la risposta.
```
```{solution} ex-universo-finito
:class: dropdown

In questo caso la costruzione produrrebbe effettivamente una $\sigma$-algebra.
Lo spazio degli esiti è finito perché $\Omega = \{0, 1, 2, \ldots, 1000\}$,
e pertanto ogni suo sottoinsieme di $\Omega$ è anch'esso finito. Di
conseguenza, l'algebra $\mathsf{A}$ degli insiemi finiti o cofiniti coincide
con l'insieme delle parti di $\Omega$. Infatti:

- ogni $E \subseteq \Omega$ è finito (perché $\Omega$ è finito), quindi
  $E \in \mathsf{A}$;
- $\mathsf{A}$ è finita, quindi le unioni numerabili sono sempre composte da
  un numero finito di eventi, e quindi appartengono sempre ad $\mathsf{A}$.

In altre parole, l'insieme delle parti di un insieme finito è sempre una
$\sigma$-algebra (anzi, è la più grande $\sigma$-algebra possibile su
quell'insieme). Il problema nell’{prf:ref}`ex-controesempio-sigma-algebra`
sorge proprio perché $\Omega = \mathbb{N}$ è infinito: esistono sottoinsiemi
infiniti (come l'insieme dei numeri pari) il cui complemento è anch'esso
infinito, e tali insiemi non appartengono all'algebra degli insiemi finiti o
cofiniti. Quando $\Omega$ è finito, questa situazione non può verificarsi.
```

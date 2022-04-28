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

L'elenco seguente descrive lo spazio degli esiti per ognuno degli esperimenti
casuali presi precedentemente in considerazione.

```{table} Esempi di spazi degli esiti
:name: tab-esempi-spazi-esiti

| Esperimento | Spazio degli esiti |
|--------------|-----------------------------------|
| $\mathscr P$ | $\{ \text{vero}, \text{falso} \}$ |
| $\mathscr O$ | insieme di tutti i colori |
| $\mathscr C$ | insieme di tutte le permutazioni degli elementi in  $\{ \text{Mister Fantastic}, \text{Donna invisibile}, \text{Torcia umana}, \text{Cosa}\}$|
| $\mathscr N$ | insieme $\mathbb N$ di tutti i numeri naturali |
| $\mathscr A$ | insieme $\mathbb R^+$ di tutti i numeri reali positivi |
```

```{margin}
$2^\Omega$ denota l'insieme delle parti di $\Omega$, pertanto un'algebra
è un insieme di eventi, o equivalentemente un insieme di sottoinsiemi di
$\Omega$.
```
````{prf:definition} Algebra degli eventi
:label: def-algebra-degli-eventi
Fissato uno spazio degli esiti $\Omega$, si definisce _algebra degli eventi_
una qualsiasi collezione di eventi $\mathsf A \subseteq 2^\Omega$ che
soddisfa le seguenti proprietà:

$$ \Omega \in \mathsf A; $$

$$ \forall E \in \mathsf A \quad \overline E \in \mathsf A; $$

$$ \forall E, F \in \mathsf A \quad E \cup F \in \mathsf A. $$

````

Dunque un'algebra degli eventi è una collezione di eventi chiusa rispetto
alle operazioni di unione e complemento. La {prf:ref}`def-algebra-degli-eventi`
implica anche le seguenti proprietà:

- tramite il principio di induzione si dimostra facilmente che un'algebra
  degli eventi è chiusa rispetto all'unione di un numero _finito_ di eventi:

  $$ \forall E_1, \ldots, E_n \in \mathsf A \quad
     \bigcup_{i=1}^n E_i \in \mathsf A; $$
- come immediata conseguenza delle leggi di De Morgan si ottiene

  ```{div} my-class
  $$ E \cap F = \overline{\overline E \cup \overline F}, $$   

  dunque un'algebra risulta anche chiusa rispetto all'intersezione di eventi.

  ```

In generale, un'algebra degli eventi rappresenta un insieme di eventi a cui
si è interessati.

Quando lo spazio degli esiti $\Omega$ è finito, l'unica algebra degli eventi
sensata è l'insieme delle parti $2^\Omega$: più precisamente, se per ogni
$\omega \in \Omega$ ha senso (come dovrebbe) ragionare in termini dell'_evento
elementare_ $\{ \omega \}$, la sola proprietà di chiusura rispetto all'unione
descritta nella {prf:ref}`def-algebra-degli-eventi` permette di dimostrare che
ogni evento è contenuto in $\mathsf A$.

```{prf:theorem} Algebra degli eventi di uno spazio degli esiti finito
Sia $\mathsf A$ un'algebra degli eventi per uno spazio degli esiti finito
$\Omega$. Se $\mathsf A$ contiene tutti gli eventi elementari allora
$\mathsf A = 2^\Omega$.
```
```{prf:proof}
Un generico evento $E \subseteq \Omega$ deve essere un insieme finito, essendo
$\Omega$ stesso finito. Quindi devono esistere $n$ esiti
$w_1, \ldots, w_n \in \Omega$ tali che $E = \{ w_1, \ldots, w_n \}$. Per
ipotesi, per ogni $i = 1, \ldots, n$ l'evento elementare $\{ w_i \}$ appartiene
ad $\mathsf A$ e dunque

$$ E = \bigcup_{i=1}^n \{ E_i \} \in \mathsf A. $$

Riassumendo, ogni $E \subseteq \Omega$ appartiene ad $\mathsf A$, che quindi
deve essere l'insieme delle parti di $\Omega$.
```

Pertanto, gli esperimenti casuali $\mathscr P$, $\mathscr O$ e $\mathscr C$
ammettono un'unica algebra degli eventi. Per quanto riguarda $\mathscr N$ e
$\mathscr A$...

Le cose si complicano quando lo spazio degli esiti è infinito, perché in
questo caso è possibile costruire algebre degli eventi che sono anch'esse
infinite (potremmo, per esempio, considerare $2^\Omega$). Abbiamo visto che la
{prf:ref}`def-algebra-degli-eventi` implica che queste algebre sono chiuse
rispetto all'unione di un numero finito di eventi, ma la stessa proprietà
potrebbe non valere quando consideriamo l'unione di una _famiglia infinita_ di
eventi, come evidenziato nell'esempio che segue.

````{prf:example}
:label: ex-controesempio-sigma-algebra
Concentriamoci sull'esperimento casuale $\mathscr N$, e dal corrispondente
spazio degli esiti $\Omega = \mathbb N$ costruiamo l'algebra

$$ \mathsf A = \{ E \subseteq \Omega
\text{ tale che } E \text{ è finito oppure }
\overline E \text{ è finito} \}. $$

e in particolare
sull'evento $P = \{ il numero di supereroi diversi nel fumetto è pari \}$ spazio degli esiti $\Omega = \mathbb N$ e sulla seguente
collezione di eventi in questo spazio:



Si verifica che $\mathsf A$ è un'algebra degli eventi, come dettagliato nei
punti seguenti.

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
$ E_n = \{ 2 i, i = 1, \ldots, n \} $. In generale, $E_n$ è l'insieme dei primi
$n$ numeri pari, e quindi contiene sempre un numero finito di elementi, il che
implica $E_n \in \mathsf A$ per ogni $n$. L'unione
$E = \cup_{n=1}^{+\infty} E_n$ è quindi l'insieme infinito dei numeri pari,
e il suo complemento è l'insieme infinito dei numeri dispari. Pertanto
$E \not\in \mathsf A$.
````

Per garantire di poter calcolare la probabilità dell'unione di una quantità
infinita numerabile di eventi, è necessario estendere l'algebra degli eventi
in una _sigma-algebra_ come indicato nella definizione che segue.

````{prf:definition} Sigma-algebra degli eventi
:label: def-sigma-algebra-degli-eventi
Ogni algebra degli eventi $\mathbb A$ su uno spazio degli esiti $\Omega$
è una _sigma-algebra_ se rispetta la seguente proprietà oltre a quelle della
{prf:ref}`def-algebra-degli-eventi`: per ogni successione infinita
$E_1, E_2, \ldots$ di eventi in $\mathsf A$

$$ \bigcup_{n=1}^{+\infty} E_i \in \mathsf A. $$

````

In generale si utilizza il termine _spazio misurabile_ per indicare una
coppia $(\Omega, \mathsf A)$ in cui $\mathsf A$ indica un'algebra o una
sigma-algebra degli eventi.
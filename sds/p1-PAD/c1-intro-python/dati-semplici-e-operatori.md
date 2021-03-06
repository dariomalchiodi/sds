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

(dati-semplici)=
# Tipi di dati semplici

```{margin}
Il linguaggio è comunque fortemente tipizzato, ma il _type checking_ viene
fatto durante l'esecuzione.
```
In Python non è obbligatorio dichiarare il tipo di una variabile, anzi: nelle
prime versioni del linguaggio la dichiarazione non era neppure possibile
[^type-hinting]. Pertanto, il modo più semplice di procedere quando si vuole
utilizzare una variabile è quello di assegnarle un valore: quest'ultimo
determina automaticamente il tipo, e di conseguenza quali operazioni si possono
effettuare sulla variabile stessa [^duck-typing]. Ovviamente questo vale solo
fino a quando non viene modificato il contenuto della variabile.

I tipi di dati semplici sono quello booleano (`bool`, che fa riferimento alle
costanti `True` e `False`), quello intero (`int`) e quello a virgola mobile
(`float`). Ciò significa dunque che in Python, a differenza di altri
linguaggi, non esiste un tipo semplice per i caratteri: vedremo più avanti che
le stringhe sono direttamente implementate come tipo strutturato. Il tipo di
dato intero permette di memorizzare numeri interi, che si esprimono come
successioni di una o più cifre eventualmente precedute da `+` (che si può
omettere) o da `-` per indicarne il segno. Il tipo di dato a virgola mobile
permette di memorizzare numeri decimali; anche in questo caso si utilizza di
norma la notazione tipica in ambito informatico: si indica il segno, seguito
dalle cifre della parte intera, dal carattere `.` e dalle cifre della parte
decimale (ed è obbligatorio specificare sempre il carattere di punto decimale e
almeno una tra le parti intera e decimale, mentre il resto è opzionale). Nel
caso in cui si debbano specificare dei valori molto grandi o molto piccoli
risulta però più pratico l'utilizzo della notazione _scientifica_ o
_esponenziale:_ si indica un valore di _mantissa_ (con o senza virgola) seguito
dal carattere `E` (o `e`) e da un numero intero detto _esponente;_ tale
espressione genera il valore numerico pari al prodotto della mantissa per `10`
elevato all'esponente. Pertanto `1E9` e `1E-9` indicano rispettivamente un
miliardo e un miliardesimo.

Va sottolineato che in Python non esiste una distinzione tra tipi primitivi e
oggetti, come succede in linguaggi come Java e C++: anche i tipi semplici come
`int` e `float` corrispondono a classi e dunque assegnare, per esempio, `42` a
una variabile implica la creazione di un oggetto e la memorizzazione di un
riferimento a quest'ultimo.

Se avete dubbi sul tipo di un'espressione, la funzione `type` restituisce il
tipo corrispondente.

```{code-cell} ipython3
first_appearance = 1971
type(first_appearance)
```

```{code-cell} ipython3
weight = 71.6
type(weight)
```

```{code-cell} ipython3
type(True)
```

```{margin}
Va osservato che esistono varie convenzioni relative allo stile da adottare
quando si scrive codice Python; questo libro fa riferimento alla [Style Guide
for Python Code](https://www.python.org/dev/peps/pep-0008/).
```

In due delle celle precedenti è possibile vedere come l'assegnamento di un
valore a una variabile segua la stessa sintassi di parecchi linguaggi di
programmazione. Per formare i nomi delle variabili si possono utilizzare i
caratteri alfabetici (maiuscoli o minuscoli, tenendo conto del fatto che
l'intero linguaggio è _case sensitive_), le cifre e il simbolo di _underscore_
(`_`), con l'unico vincolo di non usare una cifra come carattere iniziale del
nome. È inoltre convenzione ampiamente adottata quella di utilizzare per le
variabili i soli caratteri minuscoli, facendo uso dell'_underscore_ per
separare parole diverse in un nome (come in `first_appearance` nella cella
precedente).
```{margin}
Ci sono due importanti eccezioni a questa regola che verranno introdotte più
avanti.
```
L'uso di uno o più _underscore_ all'inizio o alla fine di un nome
è da evitare, perché in alcune situazioni particolari ciò può conferire un
significato specifico al codice: questo non succederebbe in ogni caso negli
esempi contenuti in questo libro, ma è meglio essere particolarmente attenti a
questo aspetto già quando si imparano le basi del linguaggio.

A partire da valori booleani, interi o a virgola mobile è possibile costruire
espressioni arbitrariamente complesse utilizzando degli _operatori_. La maggior
parte di quelli che considereremo è di tipo _binario_ (cioè si applicano a due
argomenti) e  si utilizzano in modalità _infissa_ (il che significa che
l'operatore si indica in mezzo ai suoi due argomenti). Gli operatori vengono
utilizzati nella maggior parte dei linguaggi per codificare le operazioni
aritmetico/logiche e le relazioni aritmetiche (utilizzando `+` per l'addizione,
`!=` per la relazione di non uguaglianza e così via). La
{numref}`elenco-operatori-per-tipi-semplici` riassume i principali simboli
utilizzati in Python per questo tipo di operatori binari.

```{margin}
Va notato che questo libro utilizza un particolare font con
particolari [legature](https://it.wikipedia.org/wiki/Legatura_(tipografia)) per
indicare alcuni operatori nel codice (nello specifico, il font
[Fira code](https://github.com/tonsky/FiraCode)), e quindi alcuni simboli
appaiono in forma diversa rispetto a ciò che è necessario scrivere per
inserirli: per esempio `==`, `!=` e `<=` corrispondono alle sequenze
<code style="font-family: monospace !important;">==</code>,
<code style="font-family: monospace !important;">!=</code> e
<code style="font-family: monospace !important;"><=</code>.
```

```{table} Elenco dei principali operatori per i tipi semplici
:name: elenco-operatori-per-tipi-semplici
:align: center
|  Operazione                  | Sequenza | Legatura |
|:----------------------------:|:--------:|:--------:|
| addizione                    | `+`      |          |
| sottrazione                  | `-`      |          |
| moltiplicazione              | `*`      |          |
| divisione (reale)            | `/`      |          |
| divisione (intera)           | `//`     |          |
| resto (modulo)               | `%`      |          |
| elevamento a potenza         | `**`     |          |
| appartenenza a una struttura | `in`     |          |
| rimozione dalla memoria      | `del`    |          |
| uguale (per riferimento)     | `is`     |          |
| uguale (per contenuto)       | <code style="font-family: monospace !important;">==</code> | `==`    |
| diverso                      | <code style="font-family: monospace !important;">!=</code> | `!=`    |
| minore                       | `<`      |          |
| minore o uguale              | <code style="font-family: monospace !important;"><=</code> | `<=`    |
| maggiore                     | `>`      |          |
| maggiore o uguale            | <code style="font-family: monospace !important;">>=</code> | `>=`    |
| congiunzione logica          | `and`    |          |
| disgiunzione logica          | `or`     |          |
| negazione logica             | `not`    |          |
```

Nella maggior parte dei casi gli operatori usano la stessa sintassi dei loro
equivalenti nei principali linguaggi di programmazione, mantenendo inalterata
anche la semantica. Vanno però fatte alcune importanti osservazioni, elencate
di seguito.

- Esistono due diversi simboli per codificare la divisione tra numeri reali e
  quella tra numeri interi. In altre parole, la valutazione di `/` sarà sempre
  un numero in virgola mobile, anche nel caso in cui i due argomenti dovessero
  essere due interi e il primo fosse un multiplo del secondo. In molti
  linguaggi di programmazione (comprese le versioni di Python precedenti alla
  3.0) viene invece utilizzato il simbolo `/` per entrambe le divisioni, e in
  fase di esecuzione è il tipo degli operandi a stabilire quali delle due verrà
  effettivamente calcolata.
- È presente un operatore specifico per l'elevamento a potenza, che accetta
  anche esponenti negativi e decimali. Pertanto valutando `a ** 0.5` e
  `a ** -1` si calcolano rispettivamente la radice quadrata e l'inverso del
  valore contenuto in `a`.
- L'operatore `is` verifica se due riferimenti puntano allo stesso oggetto,
  mentre `==` verifica l'uguaglianza tra quanto contenuto tra due oggetti,
  anche diversi.
  ```{margin}
  Rimangono invece invariati i simboli `&`, `|` e `!` per riferirsi agli
  operatori binari che vengono applicati "bit per bit" o "componente per
  componente". Questi operatori risultano particolarmente utili da utilizzare
  insieme a pandas (vedi {numref}`Capitolo %s <pandas>`).
  ```
- Gli operatori che corrispondono ai connettivi logici sono codificati tramite
  `and`, `or` e `not`, dunque in modo esplicito rispetto alla sintassi di
  linguaggi come Java o C (che usano invece i simboli `&&`, `||` e `!`).
- Gli operatori `in` e `del`, introdotti per completezza, sono in realtà
  tipicamente utilizzati insieme alle strutture dati (vedi
  {numref}`dati-strutturati`).

Sebbene la maggior parte degli operatori che considereremo sono di tipo
binario, ne esistono anche di altri tipi: il simbolo `-` è un esempio di
operatore _unario_ che cambia il segno dell'espressione numerica che lo segue
(esiste anche l'analogo, ma poco utile, operatore `+`); analogamente, `not` e
`del` sono degli operatori unari. Vedremo più avanti che esiste anche uno
speciale operatore _ternario_.

La conversione tra i tipi semplici si effettua, quando possibile, utilizzando
il nome del tipo come funzione di conversione. Come accennato in precedenza, i
valori dei tipi semplici sono sempre oggetti di una specifica classe, il cui
nome coincide con quello del tipo. Vedremo più avanti come utilizzare gli
oggetti in Python: per il momento è sufficiente dire che il nome di una classe
funge anche da costruttore, e per i tipi semplici questo costruttore accetta
come argomento un'espressione, che _tenta_ di convertire nel tipo in oggetto.
Se la conversione è possibile viene creato un nuovo oggetto, altrimenti viene
emesso un errore. Ciò significa che è possibile usare indirettamente questi
costruttori per convertire tra tipi: per esempio

```{code-cell} ipython3
int(3.14)
```
```{margin}
Ovviamente Python prevede l'uso dei _letterali_ per scrivere i valori dei tipi
fondamentali senza ricorrere esplicitamente all'uso dei costruttori, come
abbiamo visto all'inizio di questo paragrafo.
```
effettua la conversione da `float` a `int`.

[^type-hinting]: A partire dalla versione 3.5 Python permette di indicare il
tipo di alcuni elementi del linguaggio (come ad esempio i parametri formali di
una funzione, o il valore da essa restituito) utilizzando un formalismo
chiamato _type hinting_. Va specificato che la tipizzazione resta comunque
dinamica, ma in questo modo è possibile utilizzare degli strumenti esterni per
effettuare il cosiddetto _type checking_, che consiste nel verificare
_staticamente_ (cioè sulla base di quanto scritto nel codice) che le variabili
vengano utilizzate correttamente. _Editor_ e IDE  possono per esempio trarre
vantaggio dal _type hinting_ per suggerire come completare il codice o per
segnalare dei _warning_. Infine, l'uso del _type hinting_ rappresenta anche un
modo per alleggerire la documentazione.

[^duck-typing]: Se in un linguaggio è necessario dichiarare esplicitamente i
tipi, si dice che la _tipizzazione_ è _statica_ e la dichiarazione determina
che cosa si può fare con un oggetto; per esempio su un oggetto di tipo `Anatra`
sarà possibile invocare i metodi `cammina`, `nuota` e `starnazza`. Senza
entrare troppo nei dettagli, in Python la tipizzazione è _dinamica_ e si
assiste a un rovesciamento del concetto di _semantica_. Ciò è legato al fatto
che sono i metodi invocabili a un dato momento della vita di un oggetto a
individuarne il tipo. Pertanto, se è possibile invocare i metodi `cammina`,
`nuota` e `starnazza` su un oggetto diremo che questo è equivalente a
un'`Anatra`. Questo esempio non è fatto a caso: si utilizza infatti proprio il
termine _duck typing_ per descrivere questo tipo di tipizzazione dinamica,
facendo riferimento a una frase attribuita al poeta americano James Whitcomb
Riley: «when I see a bird that walks like a duck and swims like a duck and
quacks like a duck, I call that bird a duck».
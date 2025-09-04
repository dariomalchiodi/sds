---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
nb_execution: false
---

(sec:dati-semplici)=
# Dati semplici

Come indicato nel precedente paragrafo, i dati semplici permettono di fare
riferimento a entità che non è particolarmente sensato suddividere, vuoi
perché questa cosa non è possibile, vuoi perché non risulta interessante per
i nostri scopi. I tipi di dati semplici sui quali ci concentreremo
principalmente sono quelli numerici (interi, decimali e booleani) e quello che
permette di lavorare con le stringhe, sebbene descriverò brevemente anche altri
tipi di dati.

## Tipi numerici

Tra i tipi che si possono utilizzare per esprimere delle quantità numeriche,
`int` e `float` sono quelli più utilizzati in Python: il primo permette di
memorizzare numeri interi, il secondo numeri decimali (quelli che comunemente
chiamiamo «numeri con la virgola»). Come anticipato nel paragrafo precedente,
`int` e `float` rappresentano due classi, e i numeri corrispondenti ne
costituiscono gli oggetti. Siccome nella programmazione l'uso di costanti
numeriche è particolarmente frequente, Python permette di fare riferimento a
queste costanti senza dover necessariamente creare in modo esplicito i
corrispondenti oggetti. Come quasi in tutti i linguaggi, questo viene fatto
tramite la scrittura di _letterali_ di una particolare grammatica.

```{admonition} Letterali
 Nell'ambito di un fissato linguaggio di programmazione, il termine
_letterale_ indica un valore costante di un dato tipo, espresso secondo
una notazione prefissata. Per esempio, `42` e `3.14` sono due letterali,
rispettivamente di tipo intero e decimale, in praticamente tutti i linguaggi di
programmazione, mentre `'foo'` è un letterale di tipo stringa in Python ma non
in Java oppure in Go. Non tutti i tipi hanno dei letterali (per esempio, i tipi
che corrispondono ai file o alle date non hanno dei letterali associati in
Python&mdash;né probabilmente in alcun altro linguaggio).
```

Il modo più naturale di ottenere un letterale di tipo `int` è quello di
scrivere una sequenza di cifre, eventualmente preceduta da un segno: il
risultato rappresenterà il corrispondente numero intero in base
dieci[^int-prefix]. Va sottolineato che gli interi vengono internamente
rappresentati tramite un formato a _precisione arbitraria_ (o _precisione
infinita_), nel quale non esiste un valore minimo o massimo memorizzabile,
fatta ovviamente salva la quantità di memoria centrale disponibile al processo
in esecuzione[^bigint]. Questo permette di utilizzare numeri
molto grandi e molto piccoli, dei quali diventa però difficile comprendere
l'ordine di grandezza a un primo sguardo (in realtà, ciò già capita delle
decine di migliaia in su). Per aumentare la leggibilità del codice, è
possibile inserire un carattere di _underscore_ (`_`) tra due cifre in un
letterale: in questo modo si possono separare terzetti di cifre, ma anche
evidenziare parti logicamente diverse in una sequenza numerica (come ad
esempio le componenti di un numero di telefono).

Il modo più semplice per scrivere un letterale di tipo `float` è invece quello
di indicare un eventuale segno, seguito dalle cifre della parte intera, dal
carattere `.` e dalle cifre della parte decimale. È obbligatorio specificare
sempre il carattere di punto decimale e almeno una tra le parti intera e
decimale, e anche in questo caso è possibile separare due cifre successive
utilizzando un carattere di _underscore_. Nel caso in cui si debbano
specificare dei valori molto grandi o molto piccoli risulta però più pratico
l'utilizzo della notazione _scientifica_: si indica un valore (intero o
decimale) di _mantissa_, con o senza segno e virgola, seguito da uno dei
caratteri `E` o `e` e da un letterale intero detto _esponente;_ questa
espressione genera il valore numerico pari al prodotto della mantissa
moltiplicato per `10` elevato all'esponente. Pertanto `1E9` e `1E-9` indicano
rispettivamente un miliardo e un miliardesimo. Va notato come Python scelga
automaticamente tra la tradizione tradizionale e quella scientifica per
visualizzare valori `float`, in modo da ottimizzare la leggibilità del
risultato.

```{margin}
Va sottolineato che `inf` e `nan` non sono letterali di tipo `float`: per
riferirsi esplicitamente a essi si deve usare il costruttore della classe
(`float('inf')` e `float('nan')`, rispettivamente), o utilizzare delle
particolari librerie.
```
Il formato adottato per memorizzare i valori decimali fa di solito riferimento
al classico standard a virgola mobile [IEEE
754](https://en.wikipedia.org/wiki/IEEE_754), utilizzando $8$
byte[^double]. Questo formato non è a precisione arbitraria: tutti i numeri che
cadono al di fuori di un prefissato intervallo, i cui estremi corrispondono
all'incirca a `±1.8E308`, vengono convertiti (a seconda del segno) nel `float`
che viene visualizzato come `inf` o `-inf`, delle espressioni speciali
utilizzate per modellare $\pm \infty$. Inoltre, tutti i valori compresi in uno
specifico intorno di zero (approssimativamente tra `5E-324` e il suo opposto)
vengono rappresentati come `0.0`. Infine, è previsto il valore speciale «not a
number», che viene visualizzato come `nan` e che viene utilizzato come
risultato per alcune operazioni aritmetiche indefinite, come calcolare il
logaritmo di un numero negativo (notate che invece la divisione per zero causa
l'emissione di un'eccezione), ma può anche essere impiegato per segnalare
valori mancanti in un _dataset_.

(sec:stranezze)=
````{admonition} Stranezze in virgola mobile
:name: adm:stranezze

La rappresentazione dei numeri decimali usando il formato in virgola mobile
richiede spesso di effettuare delle approssimazioni. Questo fatto è ovvio
se pensiamo per esempio ai numeri irrazionali, mentre è meno intuitivo quando
coinvolge numeri con parte decimale finita. Nella cella che segue si può vedere
un esempio eclatante.

```python
print(0.1 + 0.2)
```

Il risultato non è, come sarebbe logico aspettarsi, $0.3$, ma un numero
leggermente più alto. Questo è dovuto alla differenza tra la base decimale che
noi abbiamo usato per indicare i due addendi e la base binaria che viene
utilizzata per rappresentare i corrispondenti valori `float`. Se usiamo la
notazione $(n)_b$ per indicare la rappresentazione del numero $n$ in base $b$,
si ha infatti che

$$(0.1)_{10} = (0.000\overline{1100})_2 \enspace,$$

a significare che, a destra dell'uguale, la prima cifra binaria dopo il punto
decimale va moltiplicata per $2^{-1}$, la seconda per $2^{-2}$ e così via, e
sommando tutti i prodotti si ottiene il numero indicato a sinistra (per il
quale si potrebbe svolgere un processo analogo, ma l'uso della base decimale fa
sì che il risultato sarebbe esattamente il numero indicato tra parentesi). La
sovralineatura sta a indicare il periodo nella rappresentazione: in altre
parole, la sequenza $1100$ si ripete all'infinito, così come succederebbe con
l'equivalente decimale della frazione $1/3$ espresso in base $10$. Ora, il
formato usato per rappresentare i valori `float` memorizza la mantissa (e anche
l'esponente) esprimendola in base $2$ e utilizzando un numero fisso di bit.
Dunque non è possibile rappresentare $0.1$ in modo preciso. Lo stesso vale per
gli altri due valori coinvolti nell'operazione, perché

$$(0.2)_{10} = (0.00 \overline{1100})_2 \enspace,$$

mentre

$$(0.3)_{10} = (0.0100 \overline{1100})_2 \enspace.$$

Se ipotizziamo per semplicità che vengano utilizzati $11$ bit dopo la virgola
decimale, calcolando la somma delle approssimazioni di $0.1$ e $0.2$ nel
sistema binario otteniamo

    0.00011001100 +
    0.00110011001 =
    -------------
    0.01001100101

che differisce dall'espansione binaria di $0.3$ a partire dalla nona cifra
dopo la virgola, e che corrisponde al valore $0.29931640625$ in base dieci.
Tenendo conto del fatto che Python utilizza $52$ bit per memorizzare il
valore assoluto della mantissa (e di altre peculiarità dello standard IEEE per
la virgola mobile che non approfondisco per brevità), il risultato ottenuto
eseguendo il codice&mdash;pur non essendo corretto&mdash; presenta un errore
di approssimazione estremamente minore, dell'ordine di $10^{-17}$.

In ogni caso, le stranezze non finiscono qui, perché valutando il letterale
`0.1` si ottiene un risultato incoerente con quanto detto finora:

```python
0.1
```

e si può verificare che lo stesso accade per $0.2$ e $0.3$. Ciò è dovuto al
fatto che la rappresentazione in virgola mobile è univoca ma non biunivoca:
fissato un numero, la sua rappresentazione è unica, ma a partire da una
rappresentazione esistono infiniti numeri decimali che le corrispondono.
Pertanto, quando Python deve visualizzare un valore `float`, deve anche
scegliere uno tra questi infiniti numeri. La scelta che viene fatta è quella
ragionevole di considerare quello che ha la rappresentazione più corta in
base dieci.

Riassumendo, quando viene valutata l'espressione `0.1 + 0.2`, nell'ordine:

- vengono creati i valori `float` per gli addendi, e in entrambi i casi
  si introduce un'approssimazione rispetto ai valori originali;
- le due approssimazioni vengono sommate, ottenendo la corrispondente
  rappresentazione in virgola mobile;
- viene visualizzato il numero decimale più corto tra tutti quelli che
  corrispondono alla rappresentazione binaria ottenuta, e questo numero non
  è $0.3$, bensì {py}`0.1 + 0.2`.

````

Il fatto che ogni letterale identifichi l'oggetto di una classe
significa che su questi valori è possibile in teoria invocare dei metodi della
classe stessa. Per esempio, `float` include un metodo `as_integer_ratio` che 
restituisce una coppia di valori interi il cui rapporto è uguale al valore sul
quale il metodo è stato invocato:

```python
3.14.as_integer_ratio()
```

```{margin}
I due valori restituiti dal metodo sono aggregati insieme costruendo una
tupla, un tipo di dati strutturato che vedremo nel Paragrafo {ref}`sec:tuple`.
```

Per questioni di compatibilità, lo stesso metodo è presente anche in
`int`[^int-method]:

```python
(3).as_integer_ratio()
```

Nella pratica comune, però, non succede quasi mai di invocare dei metodi
direttamente su un letterale, e nemmeno di invocare dei metodi su oggetti
di tipo `int` o `float`. Analogamente, la praticità dell'utilizzo del
letterali fa sì che i costruttori di queste due classi non vengano di norma
utilizzati per creare degli oggetti. Vi è però un'importante eccezione:
tutti i costruttori delle che corrispondono ai tipi semplici accettano un
argomento il cui tipo può differire da quello che essi implementano: per
esempio, `int` può ricevere un valore di tipo `float` e viceversa. Durante
la loro esecuzione, questi costruttori _tentano_ di convertire il valore
attuale dell'argomento nel tipo che rappresentano: se la conversione è
possibile viene creato un nuovo oggetto, altrimenti viene lanciata
un'eccezione. Pertanto, la conversione tra i tipi semplici si
effettua&mdash;ove possibile&mdash;utilizzando il nome del tipo di
destinazione come funzione di conversione. Per esempio

```python
int(3.14)
```

effettua una conversione da `float` a `int`, troncando all'intero più vicino da
sinistra. Nello stesso modo è possibile estrarre il valore numerico, intero o
decimale, contenuto in una stringa, a patto che i suoi contenuti siano
interpretabili in tal senso.

### Operatori per i tipi numerici

A partire da riferimenti a oggetti, espressi usando variabili o letterali, è
possibile costruire espressioni arbitrariamente complesse utilizzando degli
_operatori_. Per operatore si intende un tipo particolare di funzione che viene
espressa utilizzando la _notazione infissa_, nella quale gli argomenti (che in
questo contesto si chiamano _operandi_) non vengono indicati tra parentesi,
bensì specificati prima o dopo il simbolo che denota l'operatore/funzione.
L'uso degli operatori permette di scrivere delle espressioni in modo più
succinto e più leggibile rispetto a quello che si otterrebbe utilizzando delle
funzioni, perché si rifà alla notazione aritmetica.

```{table} Elenco dei principali operatori per i tipi numerici
:name: elenco-operatori-per-tipi-numerici
:align: center
| Operazione                   | Operatore |
|:----------------------------:|:---------:|
| addizione                    | `+`       |
| sottrazione                  | `-`       |
| moltiplicazione              | `*`       |
| divisione (decimale)         | `/`       |
| divisione (troncata)         | `//`      |
| resto (modulo)               | `%`       |
| elevamento a potenza         | `**`      |
```

La {numref}`elenco-operatori-per-tipi-numerici` elenca i principali operatori
che si possono applicare a valori numerici, per i quali è importante formulare
alcune osservazioni.

```{margin}
Vedremo più avanti che esiste anche uno speciale operatore _ternario_.
```
- Gli operatori di addizione e sottrazione funzionano in modo sia _binario_,
  sia _unario_. Nel primo caso (che è quello maggiormente utilizzato)
  l'operatore, che serve a denotare la somma o la differenza tra due operandi,
  viene posizionato tra di essi. Nel secondo caso l'operatore viene posizionato
  prima dell'unico operando, e serve a denotare un segno: il suo classico
  utilizzo è quello di cambiare il segno di un valore di un'altra espressione
  senza ricorrere a un'esplicita moltiplicazione per `-1`. Per esempio,
  `-valore` viene valutata come l'opposto del contenuto della variabile
  `valore` (in teoria è possibile usare in modo analogo l'operatore di somma,
  ma non è una cosa particolarmente informativa).
- Addizione, sottrazione, moltiplicazione ed elevamento a potenza si applicano
  a tutti gli operandi di tipo numerico. Se gli operandi sono dello stesso
  tipo, questo sarà anche il tipo del risultato, altrimenti avverrà una
  _promozione_, effettuando la conversione dell'argomento che non comporta
  una perdita di informazione. Per i tipi numerici che abbiamo visto finora, la
  sola promozione possibile è quindi quella da `int` a `float`.
- La divisione decimale `a / b` restituisce il valore `float` che moltiplicato
  per il divisore `b` diventa uguale al dividendo `a`. Va notato che il
  risultato è un `float` anche quando gli operandi sono entrambi interi e il
  dividendo è un multiplo del divisore.
- La divisione troncata `a // b` restituisce il più grande valore intero che
  è minore o uguale ad `a / b`. Se gli operandi hanno lo stesso segno, il
  risultato è analogo al calcolo della divisione decimale arrotondato per
  difetto, altrimenti le cose cambiano: per esempio, dividendo $-10$ per $3$
  il risultato è   $-\frac{10}{3} = -3.\overline{3}$ e dunque `-10 // 3`
  restituisce $-4$, che   è il più grande tra gli interi che sono minori o
  uguali della precedente frazione. Idem per `10 // -3`. Va notato che questo
  operatore restituisce un valore intero quando entrambi gli operandi sono
  interi, altrimenti viene restituito un valore `float` (che però è sempre
  equivalente a un intero, nel senso che la sua parte decimale è nulla).
- L'operatore `%` denota l'operazione di modulo, definita nel modo seguente: il
  modulo tra due valori $a$ e $b$ è il valore $r \in \mathbb N$ compreso tra
  zero e $b$ tale   che $a = b \cdot q + r$, dove $q$ è il valore della divisone
  troncata tra $a$ e $b$. Se `a` e `b` sono entrambi positivi, allora `a % b`
  equivale al resto della divisione intera tra `a` e `b`, altrimenti il
  risultato va calcolato con attenzione. Riprendendo l'esempio del punto
  precedente, `-10 % 3` è uguale a $2$, mentre `10 % -3` è uguale a $-2$. Anche
  in questo caso, l'operatore restituisce un intero quando lo sono anche gli
  operandi coinvolti, altrimenti restituisce un valore `float` con parte
  decimale nulla.
- L'elevamento a potenza accetta operandi sia interi che decimali, e
  restituisce:
  - un valore intero se sia la base che l'esponente sono `int`,
  - un valore decimale se la base o l'esponente sono `float` e la base è
    positiva,
  - un valore complesso (vedi Paragrafo {ref}`sec:altri-tipi`) se la base è
    negativa e non intera.

```{margin}
A differenza di altri linguaggi, non esistono invece in Python gli operatori
unari di _autoincremento_ e _autodecremento_.
```
Va inoltre rimarcato che a ognuna delle operazioni in
{numref}`elenco-operatori-per-tipi-numerici` è associata una specifica variante
dell'operatore di assegnamento, espressa aggiungendo il carattere `=` a destra
del simbolo dell'operazione. La loro semantica è la seguente: dapprima viene
applicata l'operazione ai due operandi, e il risultato viene assegnato alla
variabile che compare a sinistra dell'assegnamento. Pertanto `a += 1` equivale
ad `a = a + 1`, `b %= 2` a `b = b % 2`, `c **= 3` a `c = c ** 3` e così via.
 
## Il tipo booleano

Python implementa attraverso la classe `bool` un tipo booleano, dedicato a
esprimere i due valori di verità nella logica classica: vero e falso, ai quali
corrispondono i letterali `True` e `False`. Tecnicamente, `True` e `False` sono
l'equivalente di due costanti i cui valori sono rispettivamente `1` e `0`, come
si può facilmente verificare per esempio sommando `True` a sé stesso. In altre
parole, `bool` è un _sottotipo_ di `int`, ed è possibile usare operandi di tipo
booleano per tutti gli operatori della
{numref}`elenco-operatori-per-tipi-numerici`.

È possibile convertire qualsiasi oggetto in un valore di verità: questo si può
fare esplicitamente passando per il costruttore `bool`, o implicitamente in
tutti i punti nei quali è richiesto di specificare un valore booleano, come per
esempio all'interno di un'operazione di selezione (vedi il
{ref}`sec:strutture-di-controllo`). Diventano `False` i letterali `False`
(ovviamente) e `None` (vedi il Paragrafo {ref}`sec:none`), i valori nulli dei
tipi numerici (l'intero `0`, il valore decimale `0.0`, ma anche i loro
equivalenti per gli altri tipi numerici di Python) e, in generale, tutti gli
oggetti che si possono pensare come «vuoti» perché non contengono alcunché,
come la stringa vuota o la lista vuota (vedi il Paragrafo {ref}`sec:stringhe` e
il {ref}`sec:dati-strutturati`).

### Operatori logici
La {numref}`elenco-operatori-logici` illustra i principali operatori associati
ai valori booleani. I primi sette accettano operandi di tipo differente e
restituiscono un valore `bool`: in particolare, la differenza e gli operatori
di confronto ordinale hanno una sintassi intuitiva, che è identica a quella di
molti linguaggi di programmazione moderni. Gli ultimi tre operatori
corrispondono ai classici connettivi logici, dunque anche i loro operandi sono
valori di verità. Va notato che questi connettivi presentano una sintassi che
utilizza i termini `and`, `or` e `not` (dunque in modo esplicito rispetto alla
sintassi di linguaggi come Java o C, che usano invece i simboli `&&`, `||` e
`!`). I connettivi logici vengono valutati sfruttando il meccanismo del _corto
circuito_: il secondo operando di `and` e `or` viene valutato solo quando il
primo operando è stato valutato, rispettivamente, come `True` e `False`. Negli
altri casi, l'operatore restituisce il valore del primo operando.
```{margin}
Rimangono invece invariati i simboli `&` e `|` per riferirsi agli operatori
di congiunzione e disgiunzione che vengono applicati alle singole componenti
dei loro operandi, per esempio su ogni bit in un intero o «componente per
componente» in una struttura dati, come un _array_. A questi si aggiunge
l'operatore unario `~` per l'analoga negazione. Nel {ref}`chap:pandas`
vedremo che, in alcune situazioni, questi operatori risultano particolarmente
utili da utilizzare per elaborare un _dataset_.
```

```{table} Elenco dei principali operatori logici
:name: elenco-operatori-logici
:align: center
| Operazione                | Operatore |
|:--------------------------|:----------|
| uguale (per contenuto)    | `==`      |
| uguale (per riferimento)  | `is`      |
| diverso (per contenuto)   | `!=`      |
| diverso (per riferimento) | `is not`  |
| minore                    | `<`       |
| minore o uguale           | `<=`      |
| maggiore                  | `>`       |
| maggiore o uguale         | `>=`      |
| congiunzione              | `and`     |
| disgiunzione              | `or`      |
| negazione                 | `not`     |
```

```{margin}
Gli operatori di confronto sono applicabili solo se i due operandi sono
compatibili. Negli altri casi, viene lanciata un'eccezione `TypeError`.
```

L'uguaglianza tra due operandi può essere valutata in due modi differenti:
per contenuto e per riferimento. L'uguaglianza per contenuto, che corrisponde
all'operatore `==`, coinvolge un confronto tra i valori di due operandi,
mentre `is` restituisce `True` solo quando i riferimenti indicati come operandi
puntano al medesimo oggetto. Per esempio, nel codice seguente

```python
a = int("10_000")
b = int("10_000")
```

il valore `2.71` rappresenta un letterale di tipo `float`, e per ognuna delle
due righe nelle quali occorre è stato creato l'oggetto corrispondente.
Esisteranno dunque due oggetti `float` distinti, pertanto i riferimenti
memorizzati in `a` e `b` saranno diversi, ma questi due oggetti corrispondono
allo stesso numero decimale. Concludendo, i confronti fatti usando `is` e `==`
daranno risultati diversi:

```python
print('Il confronto per riferimento vale', a is b)
print('Il confronto per valore vale', a == b)
```

In generale, ogni volta che viene invocato un costruttore viene dunque creato
un nuovo oggetto, anche se già esiste in memoria centrale un altro oggetto
equivalente. Il motivo dietro questa scelta è legato all'efficienza: il tempo
di esecuzione diventerebbe rapidamente inaccettabile se si operasse altrimenti.
Ci sono però delle eccezioni: semplificando non poco la
questione[^is-behaviour], queste riguardano gli oggetti di `bool` e `int`. Per
quanto riguarda la prima classe, esistono solo due possibili letterali (`True`
e `False`), quindi è molto semplice pre-istanziare i due oggetti corrispondenti
e farli restituire dal costruttore, così che non possano mai esistere due
oggetti `bool` diversi che contengono il medesimo valore di verità[^flyweight].
Per `int` può succedere una cosa simile. Chiaramente, non è possibile creare
preventivamente «tutti» i possibili oggetti (ricordate che Python implementa
gli interi con precisione arbitraria). Però, alcuni particolari letterali
interi tendono a essere usati frequentemente nel codice (indipendentemente dal
linguaggio di programmazione usato): questo capita tipicamente per valori
positivi non troppo grandi e per i primi valori a sinistra dello zero.
Nell'implementazione di Cpython, che è attualmente quella più usata dalla
comunità degli sviluppatori e delle sviluppatrici, viene per esempio garantita
l'esistenza di un unico oggetto per tutti gli interi compresi tra $-5$ e $256$.
Pertanto 

```python
a = 256
b = 256
print(a is b)

a = 257
b = 257
print(a is b)
```

### Regole di precedenza

Quando un'espressione contiene più operatori, può diventare significativo
l'ordine nel quale le operazioni vengono eseguite. Quando gli operatori
coinvolti sono _associativi_, come per esempio in `a + b + c`, il valore
dell'espressione è indipendente da questo ordine, ma in generale questo non è
vero. Considerate per esempio `a / b / c`: se si esegue la prima divisione e
poi la seconda si ottiene il rapporto tra `a` e `b * c`, ma se si inverte
l'ordine si ottiene il rapporto tra `a * c` e ` b`. Lo stesso vale per la
situazione più generale nella quale l'espressione contiene operatori
differenti. Ogni linguaggio stabilisce dunque delle _regole di precedenza_ che
indicano l'ordine preciso nel quale i vari operatori devono essere valutati. La
{numref}`regole-precedenza` elenca gli operatori che ho introdotto finora,
ordinati per precedenza decrescente: quando deve essere valutata
un'espressione, si eseguono prima tutti gli elevamenti a potenza, se presenti,
per poi passare agli operatori di segno, sempre se sono presenti, e così via.
Notate che alcuni operatori appaiono su una stessa riga della tabella, a
indicare che hanno la stessa precedenza. Rimane però il problema di stabilire
l'ordine con il quale devono venire applicate più occorrenze di un medesimo
operatore, o operatori diversi che però hanno la stessa precedenza. In questo
caso, la regola è semplice: si considera l'ordine nel quale gli operatori
compaiono nell'espressione, procedendo da sinistra verso destra. Vi è però
un'eccezione: questa regola non vale per l'elevamento a potenza, le cui
occorrenze vengono valutate da destra verso sinistra.

```{table} Regole di precedenza per gli operatori
:name: regole-precedenza
:align: center
| Operatore                                        | Descrizione                                            |
|:-------------------------------------------------|:-------------------------------------------------------|
| `**`                                             | Elevamento a potenza                                   |
| `+x`, `-x`                                       | Segno unario                                           |
| `*`, `/`, `//`, `%`                              | Moltiplicazione, divisione, divisione troncata, modulo |
| `+`, `-`                                         | Addizione e sottrazione                                |
| `is`, `is not`, `<`, `<=`, `>`, `>=`, `!=`, `==` | Confronto                                              |
| `not`                                            | Negazione                                              |
| `and`                                            | Congiunzione                                           |
| `or`                                             | Disgiunzione                                           |
```

Chiaramente, può capitare di voler valutare un'espressione seguendo un ordine
che non è quello previsto dalle regole di precedenza. Come negli altri
linguaggi, In casi come questi si utilizzano le parentesi tonde per delimitare
le parti dell'espressione che vanno valutate per prime. L'uso delle parentesi è
comunque consigliato anche quando non strettamente necessario, se questo
contribuisce ad aumentare la leggibilità del codice (cosa che tipicamente
avviene per le espressioni non particolarmente semplici). Sempre al fine di
produrre codice facile da leggere, è consigliabile anche inserire gli spazi tra
operandi e operatori in un modo ragionato e coerente. La [Style Guide for
Python Code](https://www.python.org/dev/peps/pep-0008/) (introdotta nel
{ref}`sec:tipi-di-dati`) contiene un
[paragrafo](https://malchiodi.com/sds/short/pep-whitespace) dedicato proprio a
questo argomento, e io mi atterrò alle indicazioni ivi contenute.

Infine, vale la pena ricordare che la {numref}`regole-precedenza` fa
riferimento solo agli operatori che abbiamo visto fino a questo momento (per la
precisione, mancano quelli che operano componente per componente, ai quali ho
solamente accennato). Per una lista completa, come sempre, il punto migliore al
quale fare riferimento è la [documentazione
ufficiale](https://malchiodi.com/sds/short/operator-precedence). Notate che
questa fonte riporta le parentesi tonde come un particolare operatore che ha
precedenza su tutto il resto.

(sec:altri-tipi)=
## Altri tipi
Come già accennato, Python supporta un elevato numero di tipi di dati, alcuni
automaticamente disponibili e altri importabili da moduli di sistema o di
terze parti. In questo paragrafo farò alcuni accenni a dei tipi che si possono
facilmente incontrare quando si lavora con questo linguaggio, vuoi perché si
riferiscono a concetti utili per l'analisi dei dati, vuoi perché potrebbero
essere chiamati in causa da eventuali _bug_[^bug] nel software che scrivete.

### Numeri complessi

Python supporta in modo nativo i numeri complessi, implementati come oggetti
della classe `complex`. I letterali corrispondenti si ottengono in un modo che
ricalca la rappresentazione cartesiana dei numeri complessi: si scrive un
letterale di tipo intero o decimale seguito dal simbolo `j` (o `J`), ed
eventualmente si aggiunge (o si sottrae) un altro letterale intero o decimale.
Sono dunque esempi di letterali complessi `3j`, `5.J-4` e così via. È
importante notare che deve essere sempre presente un letterale prima del
simbolo, altrimenti quest'ultimo viene scambiato dal _parser_ del linguaggio
come il nome di una variabile. Ciò significa che l'unità
immaginaria[^unita-immaginaria] va sempre scritta come `1j` o `1J`.

Gli operatori elencati nella {numref}`elenco-operatori-per-tipi-numerici` e
nella {numref}`elenco-operatori-logici` si possono applicare a operandi
complessi, eccezion fatta per le operazioni che non sono definite in tal senso
(il confronto, la divisione troncata e il modulo).

(sec:none)=
### L'oggetto speciale None

Molti linguaggi hanno un costrutto speciale per indicare una sorta di «valore
nullo», come ad esempio la parola chiave `null` in Java o la costante `NULL` in
C che rappresentano un riferimento che non è associato ad alcunché. Python
utilizza invece la costante predefinita `None`, che viene tipicamente usata
nelle situazioni in cui non si può (o non avrebbe senso) fare riferimento a uno
specifico valore. Questo può capitare, per esempio,
1. quando si inizializza una variabile,
2. quando si vuole utilizzare un valore «speciale» all'interno di una sequenza,
   che deve dunque essere diverso da qualsiasi possibile altro valore,
3. quando una particolare procedura può terminare dando un esito negativo,
   senza che questo implichi l'emissione di un'eccezione: in questi casi,
   il risultato della procedura è `None` quando l'esito è negativo, e un
   valore specifico in tutti gli altri casi,
4. quando una funzione o un metodo non restituiscono un valore.

Nei primi due casi, `None` verrà dunque utilizzato all'interno di un
assegnamento o per creare la sequenza, mentre nel terzo sarà necessario
verificare se l'esito della procedura sia stato `None` oppure no. Questo
aspetto è particolarmente delicato, perché tutti i valori in Python
rappresentano oggetti di una classe, e `None` non fa eccezione: è un oggetto
della classe `NoneType`, o, meglio, è l'_unico_ oggetto di questa classe che
può esistere (nel senso che non è nemmeno possibile invocarne il costruttore
per creare altri oggetti[^singoletto]). Questa peculiarità permette di valutare
se una variabile, diciamo, `a` contiene `None` tramite l'espressione
`a is None`, che è inerentemente più sicura di `a == None`[^aisnone]. Una
cosa simile non sarebbe possibile, per esempio, con `a is 42`, perché possono
esistere più oggetti della classe `int` uguali a `42`.

(sec:numeri-in-base-dieci)=
### Numeri in base dieci
Il modulo `decimal` mette a disposizione la classe `Decimal` che implementa
numeri decimali memorizzati in base dieci. Questa classe non incorre dunque nei
comportamenti controintuitivi illustrati nel riquadro [Stranezze in virgola
mobile](#adm:stranezze). Rappresenta dunque una soluzione efficace quando è
necessario fare riferimento a quantità monetarie, anche perché le espressioni
che coinvolgono oggetti di questa classe venogno valutate preservando tutte le
cifre significative degli operandi. Per esempio, nella cella seguente

```python
from decimal import Decimal

print(Decimal('15.45') + Decimal('0.05'))
```

il risultato è stampato indicando comunque due cifre decimali, anche se la
seconda è uno zero. La [documentazione
ufficiale](https://docs.python.org/3/library/decimal.html) descrive
in dettaglio questa classe.

### Date e istanti
Quando si analizzano dei dati, può capitare che alcuni di questi indichino
delle misurazioni temporali, indicate con una precisione più o meno
elevata: un particolare giorno, o uno specifico secondo all'interno
di una giornata, o di un anno, o ancora la durata di un lasso di tempo
espressa in minuti, e così via. Per far fronte a questa situazione, si può
utilizzare il modulo `datetime`, che mette a disposizione le classi descritte
qui di seguito.

- `date`, i cui oggetti indicano un giorno dell'anno, espressi attraverso le
  variabili di istanza `year`, `month` e `day`, va notato come
  l'informazione contenuta in uno di questi oggetti non possa fare riferimento
  a uno specifico fuso orario, e assuma il calendario Gregoriano come
  riferimento, indipendentemente dal fatto che questo fosse in vigore nella
  data specificata.
- `time`, per indicare un istante all'interno di un giorno non specificato, nei
  termini delle variabili di istanza `hour`, `minute`, `second`, `microsecond`
  e `tzinfo`. L'ultima variabile di istanza permette di specificare il fuso
  orario nel quale l'istante viene indicato.
- `datetime`, che combina insieme le informazioni contenute negli oggetti di
  tipo `date` e `time`. La creazione di un oggetto di questa classe richiede
  di specificare sempre anno, mese e giorno come argomenti al costruttore, e
  assume l'orario di mezzanotte quando non vengono specificati valori per gli
  altri argomenti.
- `timedelta`, le cui istanze indicano un intervallo di tempo, espresso usando
  le variaili di istanza `weeks`, `days`, `hours`, `minutes`, `seconds`,
  `microseconds` e `milliseconds`.
```{margin}
Ci si potrebbe chiedere, giustamente, come mai ho annoverato questi tipi
nella categoria di quelli semplici, essendo per esempio una data scomponibile
in giorno, mese e anno. Ricordate però il criterio che ho utilizzato per
discriminare tra le due possibilità: siccome non è possibile iterare sulle
istanze, considero il tipo di dati come semplice. 
```

```{table} Significato delle principali direttive per la formattazione delle date.
:name: elenco-direttive-strftime
:align: center
| Direttiva | Significato                     |
|:----------|:--------------------------------|
| `%A`      | Nome del giorno della settimana |
| `%d`      | Numero del giorno               |
| `%B`      | Nome del mese                   |
| `%m`      | Numero del mese                 |
| `%y`      | Anno (due cifre)                |
| `%Y`      | Anno (quattro cifre)            |
| `%H`      | Ora (per un periodo di 24 ore)  |
| `%I`      | Ora (per un periodo di 12 ore)  | 
| `%p`      | AM/PM                           |
| `%M`      | Minuti                          |
| `%S`      | Secondi                         |
```

```{margin}
Nel {ref}`sec:funzioni` vedremo come Python adotti una
sintassi alternativa per l'invocazione di metodi e funzioni, basata su
parametri opzionali, che permette in situazioni come questa la scrittura di
codice più snello e più leggibile.
```
La creazione degli oggetti di queste classi permette in alcuni casi di non
indicare tutti o alcuni dei valori per le variabili di istanza. In particolare,
per `date` bisogna invocare il costruttore specificando tutti i valori,
rispettando l'ordine nel quale le variabili di istanza sono state introdotte.
Invece `time` è più flessibile: seppure anche in questo caso l'ordine degli
argomenti sia fissato, è possibile specificarne solo alcuni, e le rimanenti
variabili di istanza verranno impostate a zero, e lo stesso vale per
`timedelta`. Infine, per quanto riguarda `datetime` è sempre necessario
specificare anno, mese e giorno. Per esempio

```python
import datetime

birth = datetime.date(1912, 6, 23)
```

```{margin}
Alan Turing non è nel nostro _dataset_, ma è un supereroe a tutti gli effetti
:-)
```
memorizza in `birth` l'oggetto che corrisponde alla data di nascita di Alan
Turing, mentre

```python
free = datetime.timedelta(14526)
```

salva in `free` l'oggetto che corrisponde a 14526 giorni, che equivale al
periodo che è trascorso tra la nascita di Alan Turing e l'inizio del suo
processo per «indecenza grave» da parte delle autorità britanniche. È
interessante sottolineare che si possono scrivere espressioni matematiche che
hanno oggetti di questo tipo come operandi. Per esempio,

```python
birth + free
```

corrisponde alla data dell'udienza di Turing al suo processo. Analogamente, si
può ottenere un oggetto di tipo `timedelta` sottraendo due date, o sommare tra
loro oggetti di tipo `timedelta` o ancora moltiplicarli per un numero. Più in
generale, le classi del modulo `datetime` permettono di eseguire compiti
particolarmente articolati, che non vale la pena di approfondire qui. Anche in
questo caso, la [documentazione
ufficiale](https://docs.python.org/3/library/datetime.html) è un
ottimo punto di partenza per studiare le funzionalità che esse introducono. Mi
limito qui a parlare solamente di come gli oggetti di queste classi si possano
visualizzare con un notevole grado di flessibilità. L'uso di `print` permette
di stampare date e istanti temporali usando un formato predefinito, che segue
gli standard del mondo anglofono, come si verifica per esempio nella cella
seguente:

```python
print(birth)
```

Si vede come l'output ottenuto indichi la sequenza anno, mese e giorno. Il
metodo `strftime` permette di specificare un formato personalizzato per la
stampa, come nella cella seguente:

```python
print(birth.strftime('%d/%m/%Y'))
```

Il funzionamento del metoodo si basa sull'indicazione di una _stringa di 
formato_, che contiene sia caratteri da includere nella stampa (nel nostro
caso, i separatori `/`), sia _direttive_ che specificano tanto un particolare
componente dell'istante temporale, quanto il modo di stamparlo. La
{numref}`elenco-direttive-strftime` riporta un elenco delle principali
direttive che si possono utilizzare. Si può pertanto verificare che Alan
Turing è nato di domenica:
```{margin}
Il risultato dell'esecuzione dipende strettamente da come è impostato il
_locale_ (l'insieme di parametri che corrisponde a una specifica variante
di una lingua e che definisce, tra le altre cose, i nomi dei giorni e dei
mesi) a cui Python fa riferimento. Per impostare il locale di Python si può
fare riferimento al modulo `locale`.
```

```python
print(birth.strftime('%A'))
```

Infine, le direttive di `strftime` si possono utilizzare anche per effettuare
l'operazione inversa: costruire cioè un oggetto della classe `datetime`
partendo da una stringa che contiene una data espressa in un certo formato,
utilizzando il metodo `strptime`[^class-method]:

```python
datetime.datetime.strptime('10/05/2024', '%d/%m/%Y')
```

## Esercizi

```{exercise} •
La funzione `type` accetta un riferimento e restituisce il tipo corrispondente.
Invocatela passando le seguenti espressioni come argomento, osservando quello
che viene restituito e analizzando il risultato:

- `8`,
- `0.1`,
- `'0.1'`,
- `True`,
- `None`,
- `int`,
- `print`,
- `math` (dopo avere importato il modulo omonimo).

```

```{exercise} •
Considerate ognuna delle seguenti sequenze di carattere, e, per ognuna,
dire se viene interpretata da Python come il letterale di un tipo, specificando
in caso affermativo quale sia questo tipo e quale sia il valore ottenuto.
Sforzatevi di svolgere questo esercizio ragionando per conto vostro, e
valutando le espressioni in Python solo per avere una conferma.

- `536`,
- `000`,
- `+5`,
- `-5`,
- `--5`,
- `0_0_0`,
- `0____________________0`,
- `__0`,
- `_`,
- `3 5`,
- `3_5`,
- `0xF`,
- `E4`,
- `1E4`,
- `0X1E4`,
- `0X1H4`,
- `'0X1H4'`,
- `0b100_001`,
- `1.3`,
- `-1.3E3`,
- `1.3E-3`,
- `1.3E0xAA`,
- `True`,
- `'True'`,
- `Tr__ue`,
- `inf`,
- `nan`,
- `j`,
- `j-1`,
- `3j`,
- `1j`,
- `1j-1`,
- `1j - 1`,
- `1912-06-23`.

```

```{exercise} •
Determinate una coppia di valori `float` il più possibile vicini tra loro,
ma caratterizzati dal fatto che uno viene stampato da Python usando la
notazione scientifica, mentre l'altro no.
```

```{exercise} •
Quali degli operatori introdotti finora sono unari?
```

```{exercise} ••
Determinate tre espressioni che quando vengono valutate producono
rispettivamente come risultato `inf`, `-inf ` e `nan`.
```

```{exercise} •••
Verificate che l'assegnamento `big = 2 ** 40000` sia eseguibile senza che
venga prodotto alcun errore. Provate poi a valutare la semplice espressione
`big`, o a stampare il contenuto della variabile e commentate il risultato
ottenuto (suggerimento: rileggete attentamente la nota [^bigint]).
```

```{exercise} ••
Utilizzando la definizione di divisione troncata, calcolate manualmente il
valore delle espressioni `-10 // 3` e `10 // -3`. Verificate poi che il
risultato ottenuto sia corretto, valutando le stesse espressioni con Python.
```

```{exercise} ••
Ripetete l'esercizio precedente, considerando ora le espressioni `10 % 3`,
`-10 % -3`, `-10 % 3` e `10 % -3`.
```

```{exercise} •
Convertite mentalmente, qualora sia possibile, le seguenti espressioni al tipo
`int`:

- `6`,
- `-6`,
- `3.1`,
- `3.9`,
- `-3.1`,
- `-3.9`,
- `2e3`,
- `2g3`,
- `2.432354e3`,
- `0x2e3`,
- `0x2g3`,
- `inf`,
- `nan`.

Verificate poi che i risultati che avete ottenuto siano in linea con i valori
effettivamente convertiti con Python.
```

```{exercise} •
Ripetete l'esercizio precedente, convertendo però le espressioni in valori
`float`.
```

```{exercise} •
Verificate come sia possibile usare i costruttori di `int` e `float` per
convertire una stringa rispettivamente in un intero o un decimale. Quali
sono i vincoli che la stringa da convertire deve rispettare? Che cosa succede
se questi vincoli non sono rispettati?
```

```{exercise} ••
È possibile usare il costruttore di `bool` per convertire una stringa in valore
booleano? (Suggerimento: provate a valutare l'espressione `bool('False')`.)
```

```{exercise} ••
Sulla base del risultato ottenuto risolvendo l'esercizio precedente, cercate
di spiegare come viene elaborato l'argomento passato al costruttore di `bool`.
```

```{exercise} •••
Ricordando che l'elevamento a potenza con base irrazionale restituisce un
valore `float` solo quando questa base è positiva, valutate con Python
l'espressione `-2.5 ** 3.5`. Il risultato dovrebbe sorprendervi: perché? Come
potete spiegare questo comportamento? E come dovete modificare l'espressione
affinché il risultato della valutazione sia coerente con la definizione di
elevamento a potenza?
```

```{exercise} ••
Scrivete un'espressione che coinvolge un operatore di confronto che è ben
formata ma che genera un'eccezione di tipo `TypeError`, dovuta al fatto che
gli operandi non sono compatibili con l'operazione calcolata.
```

```{exercise} ••
Indicate qual è l'ordine nel quale vengono valutati gli operatori in oguna
delle seguenti espressioni, assumendo che di volta in volta `a`, `b` e `c`
siano variabili contenenti valori che hanno senso per i corrispondenti
operandi:

- `a - b - c`,
- `-a - b - c`,
- ` a ** b ** c`,
- `-a ** b`,
- `a ** -b`,
- `a + b * c`,
- `a % b // c`,
- `a or b and c`,
- `not a != b`,
- `a and not b`,
- `not a and b`,
- `not a is not b`.
```

````{exercise} ••
Implementate le seguenti funzioni, copiandone i contenuti nella cella di un
_notebook_ e valutandola.

```python
def true_function():
  print('in true_function')
  return True

def false_function():
  print('in false_function')
  return False
```

Valutate poi ognuna delle seguenti espressioni, e leggendo l'output prodotto
indicate in quali casi sia stato sfruttato il meccanismo di corto circuito
nella valutazione degli operatori logici.

- `true_function() and true_function()`,
- `true_function() or true_function()`,
- `false_function() and false_function()`,
- `false_function() or false_function()`.

````

```{exercise} ••
Valutate mentalmente il tipo e il valore delle seguenti espressioni, indicando
l'ordine nel quale gli operatori vengono valutati e specificando se
intervengono delle conversioni implicite tra tipi di dati:

- `bool(False) is False`,
- `bool('False') is False`,
- `3 + (4 and 2)`,
- `'3' + 3`,
- `3 + 3.`,
- '3 % True`,
- `3 % False`,
- `'3' and 3`,
- `'3' or 3`,
- `not 3`,
- `3 + 4 < 2 - 8`,
- `3 + (4 < 2) - 8`,
- `2 ** 2 ** 2`,
- `2 ** 2 * 2 ** 2`,
- `2 == 3 is int(4.0)`,
- `type(4.0) is int`,
- `1j / 1j`.

Valutate poi le stesse espressioni usando Python e verificando la validità
dei risultati precedentemente ottenuti.
```


```{exercise} ••
Scrivete un'espressione che non contiene riferimenti espliciti a valori di tipo
`complex` ma che produce un valore di questo tipo quando viene valutata.
```

```{exercise} •
Implemetate una funzione `second_grade_roots(a, b, c)` che interpreta i suoi
parametri come i coefficienti $a$, $b$ e $c$ dell'equazione
$a x^2 + b x + c = 0$ e restituisce le due radici (eventualmente complesse) di
questa equazione. (Suggerimento: l'istruzione `return m, n` permette di
restituire due valori, aggregandoli in una tupla&mdash;un tipo di dati
strutturato che vedremo nel prossimo capitolo.)
```

```{exercise} •••
Riconsiderate l'espressione `print(Decimal('15.45') + Decimal('0.05'))` che
abbiamo valutato nel Paragrafo {ref}`sec:numeri-in-base-dieci`, e notate come
gli argomenti del costruttore `Decimal` siano delle stringhe. Se eliminate gli
apici dall'espressione a la rivalutate, otterrete un risultato diverso.
Descrivete questo risultato e indicate perché, a prima vista, può sembrare
inatteso. Trovate poi una motivazione di questo comportamento.
```

```{exercise} •••
Come è possibile modificare l'espressione nell'esercizio precedente in modo
che non vi compaiano stringhe e che venga valutata nello stesso modo?
```

```{exercise} ••
Impratichitevi a scrivere e valutare delle espressioni che coinvolgono oggetti
di classi definiti nel modulo `datetime`. Per ogni operazione che considerate,
verificate quale deve essere la combinazione di operandi affinché non venga
generata un'eccezione. Quando questo accade, provate a giustificare come mai
l'operazione non possa essere eseguita.
```

```{exercise} •••
Dopo aver letto la
[documentazione](https://docs.python.org/3/library/locale.html) del
modulo `locale`, usate il metodo `setlocale` per impostare il locale sulla
lingua italiana parlata in Italia (la stringa che descrive questo locale è
`'it_IT'`) e verificate come il comportamento di `strftime` e `strptime` viene
influenzato. 
```


[^int-prefix]: La sintassi completa per scrivere un letterale di tipo intero
è leggermente più complessa: è anche possibile specificare il prefisso `0b`,
`0o` o `0x` (con il carattere in minuscolo o maiuscolo) per indicare,
rispettivamente, che l'intero in questione è da inendersi espresso in base
binaria, ottale o esadecimale.

[^bigint]: Può capitare che nonostante un numero intero sia _memorizzabile_,
Python si rifiuti di _visualizzarlo_, o, più precisamente, di convetirlo
esplicitamente o implicitamente in una stringa. Nella versione del linguagio
alla quale faccio riferimento, ciò capita per i numeri di più di $4300$ cifre.
L'idea alla base di questo vincolo è che non ha senso visualizzare numeri così
grandi da non poter essere efficacemente letti a occhio nudo, e, di solito, ciò
capita solo a causa di _bug_ nel codice. In questo modo, questi difetti vengono
possibilmente rilevati e segnalati. Volendo, è possibile aumentare il limite
sulla grandezza degli interi visualizzabili, ma ciò potrebbe generare errori o
malfunzionamenti di altro tipo, tipicamente legati all'enorme quantità di
memoria richiesta per generare la stringa da visualizzare.

[^double]: In realtà determinare il numero esatto di byte usato per
rappresentare un valore decimale non è semplice: in teoria, questo numero
dipende dal tipo di CPU utilizzata e, soprattutto, dalla particolare
implementazione di Python (se non ricordate che cosa si intende per
implementazione di un linguaggio, rileggete il Paragrafo
{ref}`sec:linguaggi-versioni-implementazioni`). A complicare le cose, anche a
parità d implementazione ci possono essere delle variazioni: per esempio,
CPython (l'implementazione di Python probabilmente più utilizzata al momento in
cui scrivo) memorizza i valori `float` utilizzando il tipo `double` del
linguaggio C, e anche per quest'ultimo linguaggio è la particolare
implementazione a stabilire il numero di byte coinvolti. Fortunatamente, le
versioni recenti delle implementazioni più diffuse di Python impongono
l'utilizzo dello standard IEEE 754 basato su otto byte. In ogni caso, conoscere
con esattezza questo tipo di informazione risulta ininfluente per la stragrande
maggioranza di applicazioni per le quali si utilizza Python (sicuramente lo è
per quanto riguarda imparare a padroneggiare i concetti che espongo in questo
libro).

[^int-method]: Per invocare un metodo a partire da un letterale `int` è
necessario racchiudere quest'ultimo tra parentesi tonde. In caso contrario,
viene emesso un errore perché il _parser_ che analizza le istruzioni di Python
interpreta quello che noi intendevamo come il punto della _dot notation_ come
un punto decimale, e si aspetta che i cartteri successivi contribuiscano a
definite un letterale di tipo `float`.

[^is-behaviour]: In realtà, il funzionamento di `is` è molto complicato da
descrivere, perché dipende da vari fattori che non riguardano solo la specifica
implementazione del linguaggio, ma anche per esempio il fatto che l'esecuzione
del codice avvenga nella REPL piuttosto che in un _notebook_ o altrove. Questo
comportamento così articolato fa sì che a volte i risultati della valutazione
di espressioni possano sembrare incoerenti tra loro: per esempio, l'espressione
`float(2.71) is float(2.71)` viene valutata come vera. Questo è dovuto al modo
nel quale Python esegue il codice, organizzandolo in _blocchi_ che vengono
compilati separatamente. A seconda del contesto,diverse occorrenze di un
medesimo letterale vengono fatte riferire in alcuni casi a uno stesso oggetto,
e in altri a oggetti differenti. Una spiegazione detagliata di questo fenomeno
è ampiamente al di fuori dello scopo di questo libro. Se siete abbastanza
coraggiosi, l'argomento è stato per esempio affrontato in modo approfondito su
[Stack Overflow](https://malchiodi.com/sds/short/is-behaviour). La cosa
importante è ricordare che `is` è un operatore peculiare che può produrre dei
comportamenti inattesi, nel caso in cui emergessero dei _bug_ durante
l'esecuzione di codice che lo utilizza.

[^bug]: Gli informatici usano il termine _bug_ (talvolta si usa la dicutura più
specifica _software bug_) per indicare la presenza di qualche tipo di errore,
di norma nel codice sorgente, che fa sì che il risultato dell'esecuzione di un
programma non sia quello atteso. Spesso si fa risalire l'adozione di questo
termine a un preciso momento storico: nel 1947, gli operatori di un computer
dell'Università di Harvard documentarono un fatto particolarmente bizzarro: una
falena era entrata nel calcolatore (a quei tempi l'hardware era di tipo
elettromeccanico, dunque di dimensioni considerevoli), rimanendo intrappolata
in uno dei suoi circuiti. Questo incidente causò un malfunzionamento, ed è
appunto cercando di risolverlo che i tecnici si resero conto di che cosa era
accaduto. Questo fatto venne documentato nel _logbook_ (un registro nel quale
venivano annotati a mano fatti rilevanti che si verificavano durante l'utilizzo
del computer) come «First actual case of bug being found», incollando con del
[nastro adesivo](https://malchiodi.com/sds/short/real-bug) la falena
incriminata, a testimonianza dell'accaduto. Questa fonte suggerisce dunque come
_bug_ fosse già usato nell'accezione moderna: risultava particolarmente
intrigante il fatto che un _bug_ fisico (la falena) avesse causato un _bug_
logico. In effetti, questo termine già veniva utilizzato in ambito
ingegneristico per indicare un malfunzionamento in un sistema: compare, per
esempio, in una lettera scritta da Thomas Edison nel 1878. L'etimologia di
_bug_ viene fatta risalire a «bugbear», un nome che veniva usato nel X secolo
in Inghilterra per indicare spiriti magligni ritenuti responsabili di eventi
infausti, come la rottura di oggetti. Questa credenza rimase diffusa nei secoli
successivi, e con l'introduzione della meccanica e poi dell'ingegneria il
termine _bugbear_ rimase per indicare un problema dovuto all'uso di un
macchinario.

[^flyweight]: Questa funzionalità è tipica di un particolare _pattern_ di
progettazione software, noto come _flyweight_ nella terminologia utilizzata
dagli ingegneri del software.

[^unita-immaginaria]: La notazione matematica adottata per l'unità immaginaria
prevede l'utilizzo del simbolo $i$, e dunque ha senso chiedersi come mai i
letterali complessi si basino su `j` e non su `i`. Questa scelta è stata fatta
nel 1988, quando la versione 1.5 di Python ha introdotto il tipo di dati che
corrisponde ai numeri complessi, ed è legata principalmente all'adozione  della
notazione utilizzata in ambito ingegneristico, nella quale l'unità immaginaria
è denotata da $j$. Ci sono anche altre motivazioni che hanno portato a
preferire `j` a `i`: chi è interessato ad approfondirle può fare riferimento a
una specifica (e lunga)
[discussione](https://bugs.python.org/issue10562) fatta nel 2010 da
un gruppo di sviluppatori del linguaggio.

[^singoletto]: È questa la situazione tipica di una _classe singoletto_, che si
studia quando si approcciano le basi dell'ingegneria del software. 

[^aisnone]: Quando si crea una nuova classe in Python, è possibile ridefinire
l'operatore `==` (così come tutti i rimanenti operatori), e questo può essere
fatto senza garantire la semantica dell'uguaglianza per contenuti. Per esempio,
si può fare in modo che se `o` è un oggetto di questa classe, allora
l'espressione `o == x` viene valutata `True` indipendentemente dal valore di
`x`. Chiaramente, in un caso come questo, `o == None` è vera anche se `o` non
è `None`. Non spiegando in questo libro come creare nuove classi, non mi
addentrerò in questo argomento che è abbastanza avanzato: se siete interessati,
potete leggere i primi capitoli di {cite}`ramalho`.

[^class-method]: Il metodo `strptime` rappresenta un esmepio di _metodo
fabbrica_ (o _factory method_, nella denominazione inglese tipica della
progettazione del software), in quanto il suo scopo è quello di creare un
oggetto a partire da una sua descrizione testuale, senza che venga
esplicitamente invocato il corrispondente costruttore. Chi legge con attenzione
avrà notato che questo metodo ha una caratteristica particolare: è stato
invocato sulla _classe_ `datetime`, e non su una sua istanza, proprio perché
non esiste (ancora) nessuna istanza. Tecnicamente, in casi come questi si dice
che il metodo in questione è un _metodo di classe_, o _metodo statico_.

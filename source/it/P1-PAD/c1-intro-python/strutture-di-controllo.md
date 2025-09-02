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

(sec:strutture-di-controllo)=
# Strutture di controllo

Python gestisce il flusso di esecuzione tramite le tipiche strutture di
controllo di sequenza, selezione e iterazione. La sequenza viene implementata
semplicemente indicando le istruzioni, una per riga, in ordine di esecuzione:
per esempio la cella seguente crea due liste, una con nomi di supereroi e
un'altra con i corrispondenti anni di prima apparizione, e le memorizza nelle
variabili `names` e `years`.

```python
names = ['Aquaman', 'Ant-Man', 'Batman', 'Black Widow',
         'Captain America', 'Daredavil', 'Elektra', 'Flash',
         'Green Arrow', 'Human Torch', 'Hancock', 'Iron Man',
         'Mystique', 'Professor X', 'Rogue', 'Superman',
         'Spider-Man', 'Thor', 'Northstar']

years = [1941, 1962, None, None, 1941,
         1964, None, 1940, 1941, 1961,
         None, 1963, None, 1963, 1981,
         None, None, 1962, 1979]
```

Il valore speciale `None` è stato utilizzato nei casi in cui non risulta
disponibile l'anno di prima apparizione di un supereroe. In queste situazioni
si parla di *valori mancanti* (o si utilizza l'equivalente termine inglese
*missing values*) che di norma vengono indicati con la sigla NA (dall'inglese
"not available"). La scelta di `None` come valore per codificare gli elementi
mancanti è puramente arbitraria: l'eterogeneità delle liste ci avrebbe permesso
di utilizzare per esempio la stringa `'NA'` o altri valori (anche espressioni
numeriche che non indicano un anno). In realtà vedremo più avanti che
esistono altre modalità che permettono di memorizzare ed elaborare i dati in
modo più agevole.

Immaginiamo di voler conteggiare, anno per anno, il numero totale di
apparizioni, calcolando quelle che in statistica vengono chiamate le _frequenze
assolute_ del numero di apparizioni. Un approccio classico è quello di
utilizzare un contatore per ogni anno, scandire la lista delle prime
apparizioni e incrementare di volta in volta il contatore corrispondente
all'anno trovato. Una struttura dati particolarmente adeguata per aggregare i
contatori è un dizionario, in cui le chiavi corrispondono agli anni. La
scansione di una lista viene effettuata in python da una delle due strutture
iterative, il *ciclo for*. A differenza di quanto succede di norma, non si
tratta di un ciclo numerato bensì di un ciclo che esegue il suo corpo in
corrispondenza di ogni elemento di un *oggetto iterabile*. Liste e tuple sono
appunto gli esempi più semplici di oggetti iterabili: immaginando che `lista`
sia una lista da scandire (ma andrebbe bene anche una tupla) e che esista una
funzione `elabora` che accetta un argomento, la sintassi

```
for elemento in lista:
    elabora(elemento)
```

implementa appunto un ciclo for, in cui `elemento` rappresenta una variabile
che conterrà a ogni iterazione uno degli elementi. In particolare, liste e
tuple vengono scandite in ordine di posizione, quindi `elemento` conterrà il
primo elemento di `lista` durante la prima iterazione, il suo secondo elemento
durante la seconda iterazione e così via. Notate anche che le funzioni si
invocano usando la sintassi tipica basata sull'uso di parentesi tonde. Infine,
va sottolineato che la seconda riga inizia più a destra della prima: in molti
linguaggi questa tecnica (detta di _indentazione_) ha lo scopo puramente
visuale di mettere in evidenza l'istruzione o le istruzioni che vengono
ripetute nel ciclo (il _corpo_ del ciclo). In python l'indentazione è invece
obbligatoria per indicare quali sono le istruzioni che compongono il corpo del
ciclo (cosa che negli altri linguaggi viene fatta utilizzando per esempio le
parentesi graffe). Non esiste una regola prefissata che indichi _come_
effettuare l'indentazione: si può usare un carattere di tabulazione, oppure
alcuni caratteri di spazio. l'unica limitazione è quella di mantenere la
stessa scelta una volta che questa è stata fatta: se si decide di indentare
il corpo di un ciclo usando, per esempio, tre spazi, tutte le istruzioni del
corpo dovranno essere indentate di tre spazi.

Tornando al problema di effettuare il conteggio del numero di apparizioni al
variare degli anni, un primo tentativo che utilizza un dizionario per
memorizzare i relativi contatori potrebbe essere il seguente:

```
# non funziona!
counts = {}
for y in years:
    counts[y] += 1
```

In realtà tale codice non funzionerebbe, perché la prima istruzione crea un
dizionario `counts` vuoto, e quindi il primo accesso  che verrebbe fatto
utilizzerebbe una chiave che non esiste, causando il lancio di un'eccezione. È
pertanto necessario verificare di volta in volta che l'anno considerato sia una
chiave esistente (il che significa che l'anno considerato è già stato trovato
precedentemente, e quindi il corrispondente contatore esiste già e va solamente
incrementato) oppure no (e dunque il contatore va inizializzato). È quindi
necessario utilizzare l'operatore `in` unitamente a una struttura di selezione,
e precisamente una if-else. La sintassi di questa struttura è la seguente:

```
if <condizione>:
    <istruzione_se_condizione_vera>
else:
    <istruzione_se_condizione_falsa>
```

e la sua semantica è quella che ci si aspetta: la condizione tra la parola
chiave `if` e il carattere di due punti viene valutata: se risulta vera viene
eseguita l'istruzione alla linea seguente, altrimenti viene eseguita
l'istruzione dopo la parola chiave `else`. Anche in questo caso l'indentazione
permette di identificare quali istruzioni debbano essere eseguite nei due rami
della selezione. La cella seguente contiene un'implementazione (stavolta
  funzionante) del codice che conteggia le apparizioni per anno.

```python
counts = {}
for y in years:
    if y in counts:
        counts[y] += 1
    else:
        counts[y] = 1
```

Il risultato è il seguente:

```python
counts
```

Notate che una coppia fa riferimento alla chiave `None`, che sarà relativa al
numero di casi mancanti. Supponiamo di voler visualizzare i conteggi
visualizzando prima l'anno con il maggior numero di apparizioni, per poi
procedere in ordine decrescente. Un possibile modo di procedere è quello di
"convertire" `counts` nella corrispondente tupla di coppie e poi ordinare
quest'ultima. La prima operazione si effettua facilmente invocando sul
dizionario il metodo `items`. La seconda operazione è più complessa, perché è
necessario basare l'ordinamento sul secondo elemento di ogni coppia. Nella
cella seguente si utilizza l'argomento opzionale `key` della funzione `sorted`
e una funzione anonima per specificare il criterio su cui basare l'ordinamento.
L'esempio utilizza anche l'argomento opzionale `reverse` per ottenere gli anni
ordinati a partire da quello con il maggior numero di apparizioni.

```python
pairs = list(counts.items())
sorted(pairs, key=lambda p:p[1], reverse=True)
```

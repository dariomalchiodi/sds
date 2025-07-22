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

(sec:dati-strutturati)=
#  Dati strutturati

Come indicato nel [Tipi di dati](sec:tipi-di-dati), ho deciso di
definire un tipo di dati come strutturato se i corrispondenti valori
costituiscono un'aggregazione di più tipi di dati __ed__ è possibile iterare
automaticamente sui loro contenuti. Dopo aver spiegato meglio questo concetto,
in questo paragrafo elencherò i tipi strutturati usati maggiormente in Python, 
descrivendo le corrispondenti classi e alcuni aspetti speciali della sintassi
che permettono di accedere ai loro contenuti.

```{admonition} Nomenclatura
Il generico valore di un tipo di dati strutturato è memorizzato appoggiandosi
su di una _struttura dati_, intesa come metodo che permette di organizzare
un particolare tipo di informazione all'interno di un computer. Questo tende
a creare confusione nella terminologia, anche perché sebbene a volte i due
concetti si sovrappongono (come capita per esempio con gli _array_),
normalmente questo non succede. Anzi, di norma è possibile costruire un
medesimo tipo di dati strutturato usando strutture dati diverse: per esempio,
un insieme è un tipo di dati strutturato che può essere basato su un _array_
così come su un albero (sebbene la scelta tra queste due strutture dati abbia
un impatto sull'_efficienza_ delle operazioni che si possono eseguire
sull'insieme). Siccome questo libro non parla delle strutture dati, e tenuto
conto del fatto che la dicitura «generico valore di un tipo di dati
strutturato» è decisamente prolissa, al suo posto userò occasionalmente il
termine _struttura_, confidando che questo non causi confusione in chi
legge.
```

I tipi di dati strutturati che descrivo nei prossimi paragrafi, elencati
nella {numref}`tab:caratteristiche-dati-strutturati`, sono:
```{margin}
Python supporta gli _array_ in un package omonimo, che non supporta però la
corrispondente aritmetica. È per questo motivo che per analizzare dati vengono
quasi sempre usati gli _array_ implementati in numpy.
```

- le stringhe, che abbiamo già parzialmente utilizzato e che descrivono
  sequenze di caratteri;
- gli _array_, che contengono sequenze omogenee di oggetti;
- le liste e le tuple, che implementano sequenze di generici oggetti;
- gli insiemi, che fanno riferimento all'omonimo concetto in matematica;
- i dizionari, che permettono di costruire mappe tra oggetti.

Classificherò questi tipi di dati in funzione di vari criteri, che descrivo
qui sotto.

- La modalità di accesso: quando l'aggregazione viene fatta in modo
  sequenziale, il modo più naturale per riferirsi a un elemento della
  struttura è quello di utilizzare un _indice_ che descrive la sua posizione.
  È questo il caso delle stringhe, delle liste, degli _array_ e delle tuple.
  L'accesso a insiemi e i dizionari, che organizzano i dati in un modo non
  necessariamente ordinato, viene invece fatto in modo differente.
- La staticità/dinamicità della struttura: ci sono dei tipi di dati strutturati
  che non permettono di aggiungere o rimuovere elementi a una struttura dopo
  che questa è stata creata (come le stringhe e le tuple), e altri tipi che
  invece lo consentono (come le liste, gli insiemi e i dizionari).
- La mutabilità degli elementi della struttura: alcuni tipi sono _immutabili_,
  nel senso che gli elementi che aggregano non possono essere modificati,
  mentre altri sono _mutabili_. Tra i tipi che considererò, le stringhe e le
  tuple sono immutabili, mentre tutti gli altri sono mutabili. Chiaramente,
  i tipi immutabili sono necessariamente anche statici, ma il contrario non
  è necessariamente vero.
- L'omogeneità o eterogeneità dei contenuti, a seconda del fatto che gli
  elementi nella struttura debbano essere tutti dello stesso tipo oppure no.

```{table} Proprietà dei tipi di dati strutturati
:name: tab:caratteristiche-dati-strutturati
:align: center
| Tipo strutturato            | Classe     | Posizionale | Dinamico | Mutabile | Omogeneo |
|:----------------------------|:-----------|:-----------:|:--------:|:--------:|:--------:|
| [stringa](sec:stringhe)     | `str`      | ✓           | ✕       | ✕        | ✓        |
| [array](sec:array)          | `np.array` | ✓           | ✕       | ✓        | ✓        |
| [lista](sec:liste)          | `list`     | ✓           | ✓       | ✓        | ✕        |
| [tupla](sec:tuple)          | `tuple`    | ✓           | ✕       | ✕        | ✕        |
| [insieme](sec:insiemi)      | `set`      | ✕           | ✓       | ✓        | ✕        |
| [dizionario](sec:dizionari) | `dict`     | ✕           | ✓       | ✓        | ✕        |
```
```{margin}
Ricordate che `np` è l'_alias_ che viene normalmente usato per importare numpy.
```

(sec:iterare)=
## Accedere a una struttura
Pur facendo riferimento a concetti altamente diversi tra loro, i tipi di dato
strutturati che considererò supportano delle modalità comuni di accesso, e
Python introduce una sintassi unificata per queste operazioni.
La prima di queste modalità riguarda l'aspetto che ho scelto per definire i
dati di tipo strutturato, ed è quella di supportare in modo automatico
l'iterazione sui contenuti di una struttura.

Molti dei linguaggi di programmazione che si rifanno al paradigma imperativo
prevedono tra le strutture di controllo il cosiddetto _ciclo enumerativo_, noto
ai più come «ciclo for» a causa della parola chiave corrispondente. Questa
particolare forma di iterazione è caratterizzata dal fatto di specificare a
priori il numero di volte che il corpo del ciclo deve essere eseguito.
Normalmente, il numero di iterazioni viene indicato in modo più o meno
esplicito, lavorando su una _variabile di ciclo_ [^var-ciclo] che deve assumere
tutti i valori in una sequenza predefinita, e normalmente&mdash;ma non
sempre&mdash;questa sequenza contempla tutti gli interi da $0$ a un valore $n$
prefissato [^for-caveats].
```{margin}
A complicare ulteriormente la nomenclatura, notate come il termine «struttura
di controllo» si riferisca a un ulteriore concetto che è completamente diverso
sia da «tipo di dati strutturato» che da «struttura dati».
```

Python si comporta in un modo completamente diverso:
nella sua forma più semplice, un ciclo for viene introdotto dall'idioma
`for <variabile> in <struttura>:`, dove `<variabile>` è il nome scelto per la
variabile di ciclo e `<struttura>` è il valore di un tipo di dati strutturato.
Le righe di codice che compongono il corpo del ciclo vengono scritte subito
dopo, aumentando il livello di indentazione. L'esecuzione del ciclo avviene nel
modo seguente: tutti gli elementi contenuti in `<struttura>` vengono
considerati separatamente, una e una sola volta, assegnandoli alla variabile
del ciclo ed eseguendo il suo corpo. La differenza fondamentale rispetto al
ciclo enumerativo classico è che in quest'ultimo la variabile di ciclo contiene
di volta in volta un _indice_ da usare per ottenere l'elemento da
elaborare[^foreach], per esempio estraendolo da un _array_, mentre in Python la
variabile di ciclo contiene direttamente l'elemento in questione.

````{prf:example}
L'unico tipo di dati strutturato al quale ho accennato finora sono le stringhe:
eseguire un ciclo for su una di esse equivale a considerare tutti i caratteri
contenuti, nell'ordine naturale che va dal primo all'ultimo:

```python
s = 'Wasp'
for c in s:
    print(c)
```
````

Il nome per la variabile di ciclo viene generalmente scelto in modo da
rispettare due requisiti: deve essere corto e deve ricordare il significato
dei valori che saranno contenuti nella variabile. Nell'esempio precedente
ho usato `c`, in quanto l'iterazione è fatta sui caratteri.

Nonostante la sua semantica diversa, `for` in Python ricade a pieno titolo
nella categoria dei cicli enumerativi: anche in questo caso, la variabile di
ciclo assume i valori di una particolare sequenza, che sono poi i valori
contenuti nella struttura sulla quale viene organizzata l'iterazione. La
descrizione che ho dato di questa semantica, però, non specifica
_in quale ordine_ vengono considerati i vari elementi, perché questo dipende
fortemente dal particolare tipo di dati strutturato che si utilizza di volta
in volta: in alcuni casi, come nell'esempio precedente, questo ordine è
noto a priori, mentre in altri no.


````{admonition} Pattern e antipattern
Quando si studia uno specifico linguaggio di programmazione, si impara
rapidamente a riconoscere degli _schemi_ nel codice che viene prodotto:
una o poche righe di codice la cui struttura è sempre uguale, ma che si
adattano a risolvere parecchie situazioni. Il risultato è l'apprendimento di
quello che viene chiamato un _pattern_ del linguaggio, anche se si tende a
parlare di codice _idiomatico_ o, nel caso specifico di Python,
_pythonico_ [^design-pattern]. L'uso di `for` mostrato sopra per iterare su una
stringa è un esempio di codice pythonico, e rappresenta una soluzione di
carattere generale che va ben oltre il considerare i caratteri che occorono in
una stringa. Infatti, come ho già evidenziato, lo stesso codice idiomatico
permette di iterare su una generica struttura dati, e questo permette di
imparare rapidamente a produrre codice Python di carattere generale, ma anche
a individuare facilmente come comportarsi quando non si conosce in dettaglio
un componente del linguaggio: sempre continuando l'esempio precedente, se
si tratta di una struttura dati e quello che si vuole fare è considerare tutti
gli elementi in essa contenuti, una delle prime cose da considerare è proprio
un ciclo `for`.


Va però anche sottolineato che esistono degli schemi che possono emergere
facilmente, pur non rappresentando codice idiomatico. È questo il caso di
schemi imparati autonomamente, magari adattando codice idiomatico di
altri linguaggi di programmazione, oppure reperiti su fonti di documentazione
relativamente affidabili, come alcuni forum di discussione. A questi schemi si
dà il nome di _antipattern_, per sottolineare il loro aspetto negativo: 
utilizzarli porta infatti a scrivere codice subottimale e che difficilmente si
riesce ad adattare a risolvere altri problemi. Chi conosce già, per esempio,
Java, tenderà a iterare su una stringa ricalcando la struttura del ciclo `for`
basata esplicitamente su una variabile intera che individua le posizioni dei
caratteri, scrivendo codice simile a questo:

```python
for i in range(len(s)):
    print(s[i])
```

Si tratta di un _antipattern_ perché introduce inutile complessità nel
codice, che deve:
- introdurre una variabile intera `i` quando tutto quello che ci
  interessa sono i singoli caratteri della stringa, e non le loro posizioni;
- invocare `range`, che restituisce un particolare oggetto che rappresenta
  una sequenza numerica sulla quale è possibile iterare, producendo come
  risultato le posizioni della stringa;
- calcolare esplicitamente la lunghezza della stringa.

Inoltre questo approccio non si può generalizzare facilmente ad altri tipi di
dati strutturati, come gli [insiemi](#sec:insiemi), i
[dizionari](sec:dizionari) o i file. Infine, è innegabile che il modo
idiomatico sia più semplice da scrivere e dunque anche più facile da leggere.
Chiaramente, possono esistere delle situazioni nelle quali è necessario
accedere sia ai caratteri della stringa, sia al numero che identifica la loro
posizione: in questi casi, però, il modo pythonico di procedere è quello di
utilizzare la funzione `enumerate`:

```python
for i, c in enumerate(s):
    print('Il carattere in posizione ', i, 'è', c)
```
````

Le altre modalità di accesso comuni ai tipi di dati strutturati sono riassunte
nel seguente elenco, e verranno dettagliate nei paragrafi che seguono.

- La funzione `len` restituisce sempre il numero di elementi contenuti nella
  struttura[^data-model]. Nel gergo informatico, ci si riferisce a questo
  numero come alla sua _lunghezza_, anche nel caso in cui questa denominazione
  possa risulta impropria (per esempio, si parla della _cardinalità_ di un
  insieme e non della sua lunghezza).

- Sono quasi sempre disponibili uno o più operatori di _accesso_ che permettono
  di ottenere il valore uno specifico elemento contenuto nella struttura e, se
  questa è mutabile, di moidificarlo. La sintassi di questi operatori è basata
  sull'uso delle parentesi quadre, estendendo l'analogo operatore per gli
  _array_ che è disponibile nella maggior parte dei  linguaggi che mettono a
  disposizione questo tipo di dato.

- L'operatore `in` permette di verificare se una struttura contiene o meno un
  dato elemento.

- L'operatore `del` può essere utilizzato per rimuovere degli elementi nelle
  strutture dinamiche.


(sec:stringhe)=
## Le stringhe

```{margin}
Nei paragrafi seguenti vedremo che esistono altre modalità per
specificare i letterali di tipo stringa.
```
A differenza di altri linguaggi, come per esempio C, in Python non esiste
un tipo di dato che corrisponde ai singoli caratteri. Le stringhe, intese come
sequenze di zero o più caratteri, sono implementate attraverso la classe `str`
che mette a disposizione un tipo omogeneo e ad accesso posizionale, i cui
oggetti sono immutabili. Nella loro versione più semplice, i letterali di
questa classe si costruiscono facendo precedere e seguire i caratteri della
stringa in questione da un delimitatore. Esistono tre tipi di delimitatori:
gli apici singoli, doppi e tripli. L'uso degli apici singoli (`'`) o doppi
(`"`) ricalca la classica sintassi per indicare le stringhe nei linguaggi di
programmazione più diffusi, con la differenza che in Python è possibile
scegliere tra due diversi delimitatori: in altre parole, `'Robin'` e `"Robin"`
identificano la stessa stringa. Questo facilita la creazione di stringhe che
devono contenere apici doppi o singoli, come nella cella seguente:

```python
'Superman proviene da un pianeta chiamato "Krypton".'
"L'altro nome di Superman è Kal-El."
```
```{margin}
Volendo, apici singoli e doppi si possono comunque inserire in un letterale
stringa usando la tecnica di _escaping_, utilizzando rispettivamente le
sequenze `\'` e `\"`.
```

È però necessario chiudere una stringa usando lo stesso tipo di delimitatore
con il quale si è iniziato: sempre due apici singoli, o due doppi apici.
Gli apici tripli permettono di definire delle stringhe che contengono più
righe, senza dover inserire sequenze di _escape_ per i corrispondenti caratteri
di «a capo». Per esempio, il letterale

```{code-block} python
'''Il primo fumetto che ha Storm come protagonista
compare nel numero uno di "Giant-size X-men"
ed è stato pubblicato nel 1977.
'''
```

fa riferimento a una stringa di tre righe. I tre apici per delimitare le
stringhe su più righe possono essere sia singoli che doppi. Anche in questo
caso, è necessaria coerenza tra il delimitatore iniziale e quello finale.

Abbiamo già visto che l'iterazione su di una stringa avviene carattere per
carattere, nell'esatto ordine con cui questi appaiono. E non dovrebbe stupire
nessuno il fatto che `len(s)` restituisca il numero di caratteri della stringa
`s`, né che i letterali `''` e `""` denotino la stringa vuota (la cui
lunghezza è uguale a zero).

L'operatore di accesso richiede un po' più di dettaglio. Risulta naturale
accedere in modo posizionale ai singoli caratteri di una stringa,
specificandone la posizione, pertanto basta specificare dopo una variabile
che la referenzia (ma ovviamente si potrebbe utilizzare anche un letterale)
una coppia di parentesi quadre contenente la posizione, conteggiata a partire
da `0`[^start-from-zero]. In altre parole, si può utilizzare l'operatore di
accesso con la stessa semantica degli _array_. Ma in Python la sintassi è più
estesa: se si specifica un valore negativo per la posizione, a questo viene
automaticamente sommata la lunghezza della lista. Pertanto `-1` identifica
l'ultimo elemento della lista, `-2` il penultimo e così via.


È anche possibile indicare un intervallo di posizioni consecutive per
riferirsi a una sottostringa: questa modalità, che prende il nome
di _slicing_, si effettua indicando tra parentesi quadre la posizione del
primo carattere da includere nella sottostringa, seguita da un carattere di due
punti e dalla posizione del primo carattere da escludere[^substring]. Gli
_slicing_ si possono fare anche usando due indici positivi, oppure due
negativi, o ancora mischiando un indice positivo e uno negativo: la cosa
importante è che la prima posizione preceda la seconda, altrimenti l'operazione
restituisce la stringa vuota.
```{margin}
La sottostringa estratta partirà dal primo carattere della stringa ogni volta
che nello slicing si omette la posizione iniziale, e procederà fino a fine
stringa ogni volta che si omette la posizione finale.
```

In linea di principio, l'operatore `in` dovrebbe permettere di verificare
se un carattere occorre da qualche parte in una stringa oppure no. In realtà
questo comportamento si estende alle sottostringhe: `s in t` restituisce `True`
quando la stringa `s` (che può contenere uno o più caratteri) è una
sottostringa della stringa `t`, e `False` altrimenti.

````{prf:example}
Consideriamo la stringa definita nella cella seguente.

```python
s = '''- Spider-Man: Dev'esserci qualcun altro da chiamare... Per esempio Thor?
- Nick Fury: Fuori portata.
- Spider-Man: Captain Marvel.
- Maria Hill: Indisponibile.
- Spider-Man: Io sono solo un amichevole Spider-Man di quartiere.
- Nick Fury: Ma per favore! Sei stato nello spazio!'''
```
```{raw} html
<py-script>
s = '''- Spider-Man: Dev'esserci qualcun altro da chiamare... Per esempio Thor?
- Nick Fury: Fuori portata.
- Spider-Man: Captain Marvel.
- Maria Hill: Indisponibile.
- Spider-Man: Io sono solo un amichevole Spider-Man di quartiere.
- Nick Fury: Ma per favore! Sei stato nello spazio!'''
</py-script>
```

Le istruzioni qui sotto illustrano come

- calcolare la lunghezza della stringa,
- estrarne il primo e l'ultimo carattere, utilizzando l'operatore di accesso,
- estrarne una sottostringa, combinando operatore di accesso e _slicing_,
- verificare l'eventuale occorrenza di una sottostringa.

```python
print('La stringa contiene', len(s), 'caratteri')
print('inizia per', s[0])
print('e finisce per', s[-1])

start = 67
end = 70
print(s[start:end+1], 'occorre dalla posizione', start, 'alla posizione', end)

hero = 'Aquaman'
print(hero, end=' ')
if hero not in s:
    print('non ', end='')
print('occorre nella stringa')
```
```{raw} html
<div id="stdout-3" class="script-stdout"></div>
<py-script>
output = io.StringIO()
sys.stdout = output

print('La stringa contiene', len(s), 'caratteri')
print('inizia per', s[0])
print('e finisce per', s[-1])

start = 67
end = 70
print(s[start:end+1], 'occorre dalla posizione', start, 'alla posizione', end)

hero = 'Aquaman'
print(hero, end=' ')
if hero not in s:
    print('non ', end='')
print('occorre nella stringa')

display(output.getvalue(), target="stdout-3")
</py-script>
```


````

Come già indicato precdentemente, in Python le stringhe sono immutabili, il
che significa che non è possibile cambiarne i contenuti, per esempio
rimpiazzando un carattere con un altro, oppure appendendo uno o più caratteri.
Per effettuare operazioni di questo tipo è sempre necessario creare una nuova
stringa che vada a rimpiazzare quella di partenza.

La classe `str` implementa vari metodi e operatori specifici per le stringhe;
in particolare vale la pena segnalare che:

- l'operatore `+` concatena due stringhe (e __solo__ due stringhe: è infatti
  necessario convertire esplicitamente eventuali operandi di tipo diverso),
- l'esito della moltiplicazione tra una stringa `s` e un numero intero `i` è
  una nuova stringa ottenuta concatenando `s` con se stessa per `i` volte;
- `s.find(t)` restituisce la posizione a partire dalla quale la sottostringa
  `t` è contenuta nella stringa `s`, se ciò accade, e `-1` negli altri casi.


Per un elenco completo si può consultare la sezione relativa alle stringhe nella
[documentazione ufficiale](https://docs.python.org/3/library/stdtypes.html#string-methods).

(sec:r-string)=
### Letterali stringa grezzi
Ho accennato al fatto che si può generare una stringa utilizzando le sequenze
di _escape_ per fare riferimento a caratteri che altrimenti risulta complesso
o anche impossibile inserire all'interno di un letterale: i casi più frequenti
sono quelli dei caratteri di «a capo» o _newline_ (`\n`), di tabulazione (`\t`)
e, chiaramente, dello stesso _backslash_ (`\\`)[^escape_numeric], che
altrimenti non potrebbe mai comparire all'interno di un letterale stringa. In
alcuni contesti è però necessario creare delle stringhe che contengono parecchi
caratteri di _backslash_: in questi casi, nei quali l'uso delle relative
sequenze di _escape_ renderebbe difficile la lettura del letterale stesso,
si utilizzano i cosiddetti _letterali grezzi_ (in inglese, _raw string
literals_, o, per brevità, _r-string_). In questi letterali, che si inseriscono
prependendo `r` al delimitatore iniziale, le sequenze di _escaping_ non vengono
interpretate.

```{margin}
Se non conoscete $\LaTeX$, vi consiglio caldamente di imparare a usarlo,
perché nonostante sia inizialmente non facilissimo da studiare, permette di
diventare rapidamente veloci nell'ottenere documenti di qualità tipografica
occupandosi solo marginalmente di tutti gli aspetti che riguardano lo stile
della formattazione, avendo nel contempo accesso a strumenti che permettono
di automatizzare la gestione degli indici, dei riferimenti incrociati, della
bibliografia e via discorrendo.
```


````{prf:example} $\LaTeX$
$\LaTeX$ è un linguaggio di marcatura che permette di descrivere
[testi formattati](https://www.latex-project.org/), ampiamente utilizzato in
ambito scientifico per produrre documentazione. Anche in questo libro ho
utilizzato $\LaTeX$ per generare tutte le formule matematiche che compaiono nel
testo, nelle quali i simboli matematici vengono descritti nei termini di una
sintassi simbolica che utilizza ampiamente il carattere di _backslash_. Per
esempio, le espressioni `\pi` e `\int` corrispondono, rispettivamente, a $\pi$
e all'operatore integrale. Nella cella seguente, la funzione `display` e la
classe `Math` del modulo `IPython.display` vengono utilizzate per visualizzare
nella cella di output una formula relativamente complicata:

```python
from IPython.display import display, Math
from js import MathJax

s = r'\Phi(x) = \frac{1}{2 \pi} '
s += r'\int_{-\infty}^{+\infty} \mathrm e^{-\frac{x^2}{2}} \mathrm dx'

display(Math(s))

```
```{raw} html
<div id="out-4" class="script-output"></div>
<py-script>
from pyscript import HTML
from js import MathJax

s = r'$$\Phi(x) = \frac{1}{2 \pi} \int_{-\infty}^{+\infty} \mathrm e^{-\frac{x^2}{2}} \mathrm dx$$'

display(HTML(s), target='out-4')
MathJax.typeset()
</py-script>
```

che descrive una particolare funzione che studieremo nel Paragrafo
@sec:modello-normale. Notate come la stringa utilizzata sia stata costruita
giustapponendo due letterali grezzi tramite l'operatore `+=`, per evitare
di avere una riga di codice eccedente ottanta caratteri.
````


````{prf:example} Espressioni regolari
Le [espressioni regolari](https://it.wikipedia.org/wiki/Espressione_regolare)
sono un formalismo che permette di definire un insieme di stringhe nelle quali
i caratteri devono soddisfare delle particolari regole. Più precisamente, ci
sono alcuni costrutti fondamentali che catturano degli aspetti relativamente
semplici: si può fissare ad esempio la lunghezza della stringa, o richiedere
che questa contenga esclusivamente alcuni caratteri. Componendo questi
costrutti è possibile arrivare a definire delle regole che individuano
famiglie complesse di stringhe, come ad esempio tutti gli indirizzi di posta
elettronica in un certo dominio, o tutte le password di almeno dieci caratteri
che contengono almeno una cifra e caratteri sia minuscoli che maiuscoli.
Tipicamente, data una specifica espressione regolare, si vuole valutare se una
stringa la soddisfi o meno, oppure si vogliono estrarre tutte le sue
sottostringhe che la soddisfano.

Il modulo `re` permette di utilizzare le espressioni regolari in Python,
definendole tramite una sintassi nella quale si fa ampio uso dei caratteri
di _backslash_. Per esempio, `\d` indica una cifra e `+` descrive una sequenza
di una o più occorrenze della regola precedente, così che `\d+` corrisponde a
una sequenza di una o più cifre, e dunque a una stringa che descrive un numero
intero. La funzione `compile` restituisce un oggetto che descrive
un'espressione regolare $s$, partendo da una stringa che la descrive. Su questo
oggetto si possono invocare dei metodi, come ad esempio `findall` che accetta
come argomento una stringa e ne estrare tutte le sottostringhe che soddisfano
$s$. Per esempio, il codice nella cella seguente elenca tutti i numeri che
compaiono in una descrizione dei superpoteri di Elastigirl, presa dalla
relativa pagina su [Wikipedia](https://it.wikipedia.org/wiki/Helen_Parr).

```python
import re

s = "Il superpotere principale di Elastigirl è l'elasticità, che le "
s += "consente di allungare varie parti del suo corpo fino a 300 piedi "
s += "(90 metri) e può essere sottile 1 millimetro."

p = re.compile(r'\d+')
p.findall(s)
```

```{raw} html
<div id="out-5" class="script-output"></div>
<py-script>
import re

s = "Il superpotere principale di Elastigirl è l'elasticità, che le "
s += "consente di allungare varie parti del suo corpo fino a 300 piedi "
s += "(90 metri) e può essere sottile 1 millimetro."

p = re.compile(r'\d+')

display(p.findall(s), target='out-5')
</py-script>
```

Dovreste avere notato qualcosa di nuovo nel valore restituito dal metodo
`findall`: si tratta di un dato strutturato che permette di aggregare
le varie occorrenze individuate nella stringa di partenza. Studieremo tra
breve anche il tipo corrispondente, nel Paragrafo [Le liste](sec:liste). 

````

(sec:f-string)=
### Letterali stringa formattati
Abbiamo visto che è possibile stampare un output mescolando stringhe fisse
e contenuti di variabili, semplicemente usandoli come argomenti della funzione
`print`.

```python
name = 'Brainiac'
month = 'luglio'
year = 1958
magazine = 'Action Comics'
num = 242
print(name, 'ha debuttato nel numero', num, 'di', magazine, 'nel', month, year)
```
```{raw} html
<div id="stdout-6" class="script-stdout"></div>
<py-script>
output = io.StringIO()
sys.stdout = output

name = 'Brainiac'
month = 'luglio'
year = 1958
magazine = 'Action Comics'
num = 242
print(name, 'ha debuttato nel numero', num, 'di', magazine, 'nel', month, year)

display(output.getvalue(), target="stdout-6")
</py-script>
```

È importante sottolineare che in molti linguaggi di programmazione
l'equivalente della funzione `print` accetta un unico argomento, e per
stampare output analoghi a quello precedente si utilizza un _pattern_ preciso:
si usa l'operatore di concatenazione delle stringhe, che _promuove_
automaticamente gli operandi che non sono delle stringhe. Python effettua
però un _type checking_ di tipo forte, il che significa che non ammette
promozioni, e dunque la concatenazione può avvenire solo tra due o più
stringhe. Pertanto, per applicare il _pattern_ precedente sarebbe necessario
convertire esplicitamente a stringa tutti gli operandi della concatenazione che
già non sono di questo tipo, pena l'emissione di un'eccezione. Ciò
renderebbe il codice inutilmente complesso, ed è per ovviare a questo che
`print` accetta più argomenti. Nella pratica comune, però, quando si vuole
emettere degli output complessi che mischiano stringhe fisse con il contenuto
di una o più variabili si preferisce produrre dell'_output formattato_. Questo
si può fare in tre modi diversi: usando l'operatore `%`, invocando il metodo
`format` su una stringa oppure utilizzando dei _letterali stringa formattati_.
Sebbene le prime due modalità siano tutt'ora disponibili, l'ultima (che è
quella che è stata introdotta più recentemente) è quella che fornisce più
controllo sul risultato finale, e nel contempo alleggerisce il codice che viene
prodotto. Un letterale stringa formattato si riconosce perché il suo
delimitatore iniziale è sempre precedeuto da un carattere `f`. Al suo interno
è possibile inserire arbitrarie espressioni Python tra parentesi graffe:
durante l'esecuzione, tali espressioni vengono valutate, e il loro risultato
è inserto al posto della parte di letterale delimitato dalle stesse parentesi.

```python
print(f'{name} ha debuttato nel numero {num} di {magazine} nel {month} {year}')
```
```{raw} html
<div id="stdout-7" class="script-stdout"></div>
<py-script>
output = io.StringIO()
sys.stdout = output

print(f'{name} ha debuttato nel numero {num} di {magazine} nel {month} {year}')

display(output.getvalue(), target="stdout-7")
</py-script>
```

Il vantaggio nell'uso dei letterali formattati, che nella terminologia inglese
vengono spesso indicati, per brevità, come _f-string_, sta nella possibilità
di gestire in modo preciso la quantità di spazi da inserire tra le varie
stringhe ed espressioni che vengono implicitamente concatenate. Per esempio,
terminare la stringa nell'ultima cella con un carattere di punto è immediato,
mentre richiede una certa perizia in quella precedente. È inoltre possibile
specificare con notevole precisione il modo nel quale i valori devono essere
visualizzati, utilizzando un _mini linguaggio_ che indica alcune regole di
formattazione. Più precisamente, prima di chiudere le parentesi graffe è
possibile aggiungere un carattere di due punti e indicare qual è il tipo del
valore mostrato e come questo debba essere visualizzato. Per esempio, nella
cella seguente


```python
a = 0.1
b = 0.2
print(f'{a+b:.1f}')
```
```{raw} html
<div id="stdout-8" class="script-stdout"></div>
<py-script>
output = io.StringIO()
sys.stdout = output

a = 0.1
b = 0.2
print(f'{a+b:.1f}')

display(output.getvalue(), target="stdout-8")
</py-script>
```

`.1f` indica che il valore dell'espressione è di tipo `float`, e va
visualizzato indicando una cifra decimale dopo la virgola. Una versione
semplificata della sintassi da usare per specificare il formato di
visualizzazione per il valore di un'espressione è

`[[fill]align][sign][width][,|_][.precision][type]`

dove:

- `fill` è il carattere (per _default_, uno spazio) da usare per il 
  riempimento;
- `align` individua come allineare il valore: `<`, `>`, `^` e `=`
  indicano, rispettivamente, l'allineamento a sinistra, a destra, centrato e
  organizzato in modo da porre il segno a sinistra e il valore a destra (valido
  solo per valori numerici);
- `sign` specifica come visualizzare l'eventuale segno: `+` lo visualizza
  sempre, anche quando è positivo; `-` lo visualizza solo quando è negativo e
  `␣` visualizza uno spazio per i numeri positivi e `-` per quelli negativi
  (in modo da garantire un corretto allineamento verticale);
- `width` imposta il numero totale di caratteri da utilizzare per la
  visualizzazione;
- `,` o `_` denota il carattere da usare per separare i gruppi di tre cifre nei
  valori numerici;
- `precision` numero di cifre decimali (per i valori `float`) o di caratteri
  (per le stringhe) da visualizzare;
- `type` denota come visualizzare il valore da visualizzare, in funzione di
  un carattere scelto tra quelli indicati nella
  {numref}`tab:tipi-formattazione`.

La sintassi completa del mini lingugaggio di formattazione è leggermente più
complessa, ed è descritta nella
[documentazione ufficiale](https://docs.python.org/3/library/string.html#format-specification-mini-language).


```{table} Modalità di visualizzazione per i letterali stringa formattati, unitamente ai corrispondenti simboli
:name: tab:tipi-formattazione
:align: center
| Carattere | Tipo di visualizzazione             |
| --------- | ----------------------------------- |
| `s`       | Stringa (_default_)                 |
| `d`       | Intero                              |
| `f`       | Decimale (notzione a virgola fissa) |
| `e`       | Decimale (notazione scientifica)    |
| `E`       | Decimale (notazione scientifica)    |
| `g`       | Forma compatta                      |
| `%`       | Percentuale                         |
| `x`       | Esadecimale                         |
| `X`       | Esadecimale                         |
| `b`       | Binario                             |
| `o`       | Ottale                              |
```

(sec:liste)=
## Le liste

Le liste sono strutture dati dinamiche ad accesso posizionale che memorizzano
una sequenza di riferimenti a oggetti di tipo eterogeneo, anche se per brevità
è comune riferirsi a una lista di oggetti, o di valori. Quando una lista
contiene pochi elementi, risulta pratico definirla in modo _estensivo_, cioè
racchiudendo tra parentesi quadre l'elenco di questi elementi, indicati dal
primo all'ultimo e separati tramite virgole. Ciò che si ottiene è un letterale
di tipo `list`, la classe che in Python implementa le liste.


Per esempio, la lista che contiene i quattro quadrati perfetti che si ottengono
contando a partire da zero corrisponde al letterale `[0, 1, 4, 9]`, così come
quella formata dai primi tre numeri dispari positivi è indicata da `[1, 3, 5]`;
analogamente, `[]` rappresenta la lista vuota. Chiaramente, la modalità
estensiva diventa poco pratica per riferirsi a liste contenenti più di una
decina di elementi: queste ultime vengono infatti gestite creandole
dinamicamente, per esempio inserendovi gli elementi via via che essi vengono
generati all'interno di un ciclo, oppure create da opportune funzioni. È però
possibile esprimere una lista anche come il risultato di una trasformazione
applicata agli elementi di un'altra struttura. Tale modalità, che prende il
nome di _list comprehension_, opera dunque con un approccio _intensivo_,
perché si basa sulla specificazione di una proprietà che deve essere
soddisfatta da tutti e soli gli elementi della lista. La sintassi più semplice
di una _list comprehension_ è `[f(e) for e in l]`, dove `f(e)` indica una
funzione o un'espressione che dipende dalla variabile muta `e` e `l` è la
struttura di partenza. Quando l'espressione corrispondente viene valutata, la
struttura `l` viene attraversata, generando tutti i suoi elementi: ogni volta,
l'elemento ottenuto viene usato per valutare la funzione o l'espressione `f`.
Il risultato finale è la lista che aggrega tutti i valori restituti,
nell'ordine in cui questi sono stati generati (che quindi dipende strettamente
dalla struttura `l` di partenza). In altre parole, la _list comprehension_
produce una nuova lista nella quale il primo elemento è il risultato del
calcolo di `f` sul primo elemento di `l`, il secondo è il risultato di `f`
secondo elemento di `l` e così via. Pertanto, la lista dei primi quattro
quadrati perfetti si può esprimere anche come
```{margin}
Quando una lista è utilizzata per dati di tipo omogeneo, vale la pena
considerare di sostituirla con un _array_ per diminuire i tempi di esecuzione
e ridurre la possibilità di introdurre _bug_ nel codice.
```

```python
[i**2 for i in range(4)]
```
```{raw} html
<div id="out-0" class="script-output"></div>
<py-script>
import io, sys
from pyscript import display

display([i**2 for i in range(4)], target="out-0")
</py-script>
```

In una _list comprehension_ è inoltre possibile scartare una parte della
struttura originale: la sintassi `[f(e) for e in l if g(e)]` specifica che
un generico elemento `e` va considerato solo quando esso rende vera
l'espressione `g(e)`. Pertanto

```python
[i for i in range(1, 6) if i % 2 == 1]
```
```{raw} html
<div id="out-1" class="script-output"></div>
<py-script>
display([i for i in range(1, 6) if i % 2 == 1], target="out-1")
</py-script>
```

genera la stessa lista di numeri dispari che ho indicato prima.

````{admonition} Range
In alcuni degli esempi fatti finora, ho utilizzato `range` per ottenere degli
oggetti che rappresentano sequenze di numeri interi equispaziati che variano
tra un valore minimo e un valore massimo. Più precisamente, dati tre valori
interi `m`, `n` e `s`,

- `range(m)` corrisponde alla sequenza di tutti gli interi che vanno da zero a
  `m-1`,
- `range(m, n)` indica la sequenza di tutti gli interi che partono da `m` e
  arrivano a `n-1`,
- `range(m, n, s)` individua la sequenza ottenuta partendo da `m` e aggiungendo
  `s` ogni volta, fermandosi la prima volta che si eccede `n`.

Nelle prime versioni di Python, `range` era una funzione che restituiva una
lista che conteneva una sequenza. Questo approccio era però altamente
inefficiente (e potenzialmente inutilizzabile) quando si volevano memorizzare
sequenze particolarmente lunghe con il solo scopo di iterare sopra di esse, per
esempio in un ciclo. Chiaramente, per eseguire questo compito è sufficiente
mantenere in memoria solo il valore corrente della sequenza e il suo limite
superiore. A partire dalla versione 3 di Python, `range` è diventata una classe
i cui oggetti rappresentano le sequenze usando proprio questo approccio, e con
i quali è possibile interagire in modo simile alle liste. In particolare, gli
oggetti `range` si possono utilizzare in concomitanza con i cicli `for` e
all'interno di _list comprehension_, come ho fatto negli esempi precedenti.
````

La proprietà di eterogeneità delle liste ci permette di utilizzarle per
indicare un _record_, inteso come insieme di informazioni che descrivono un
oggetto complesso o un individuo, come ad esempio un supereroe:

```python
iron_man = ['Iron Man',
            'Tony Stark',
            'Long Island, New York',
            'Marvel Comics',
            198.51,
            191.85,
            'M',
            1963,
            'Blue',
            'Black',
            85,
           'high']
```
```{raw} html
<py-script>
iron_man = ['Iron Man',
            'Tony Stark',
            'Long Island, New York',
            'Marvel Comics',
            198.51,
            191.85,
            'M',
            1963,
            'Blue',
            'Black',
            85,
           'high']
</py-script>
```

```{margin}
Vedremo più avanti che ci sono modi più interessanti di codificare un
_record_ di informazioni.
```

L'operatore di accesso alle liste segue la stessa semantica vista per gli
array e per le stringhe: tra parentesi quadre si specifica una posizione che
individua un oggetto all'interno della sequenza memorizzata nella lista (più
precisamente, un riferimento a questo oggetto), o uno _slicing_ per individuare
una sotto-sequenza.

````{prf:example}
Riconsideriamo la lista memorizzata nella variabile `iron_man`. Valutando le
espressioni `iron_man[1]` e `iron_man[-2]` si ottengono rispettivamente il
secondo e il penultimo dei valori memorizzati nella lista, e cioè la stringa
`'Tony Stark'` e l'intero `85`. Analogamente, si può estrarre la sotto-lista
contenente i colori di occhi e capelli nel modo seguente:

```python
iron_man[-4:-2]
```
```{raw} html
<div id="out-3" class="script-output"></div>
<py-script>
display(iron_man[-4:-2], target="out-3")
</py-script>
```

````
```{margin}
Un'altra differenza tra liste e _array_ è legata al fatto che questi ultimi
rappresentano strutture dati _statiche_, nelle quali non è possibile aggiungere
o rimuovere elementi, ma solo modificare quelli esistenti.
```
Dover specificare la posizione del primo elemento da escludere sembra
controintuitivo rispetto alla scelta più naturale di indicare la posizione
dell'ultimo elemento da includere. In realtà in questo modo risulta più facile
scrivere codice che elabora porzioni successive in una lista. Infine, come già
detto le liste sono strutture dati _dinamiche_, nel senso che oltre a
modificare gli elementi in essa contenuti è anche possibile rimuovere uno o più
di tali elementi, oppure aggiungerne di nuovi.

Sono a disposizione varie operazioni che agiscono sulle liste, e queste
operazioni sono implementate utilizzando diversi elementi del linguaggio:
gli operatori, le funzioni e i metodi. I paragrafi che seguono, lungi
dall'essere esaustivi, introducono alcuni esempi: il loro scopo è
principalmente quello di sottolineare la differenza tra i concetti di
operatore, funzione e metodo in Python. Per degli approfondimenti è possibile
consultare la documentazione ufficiale, che contiene un [documento
introduttivo](https://docs.python.org/3/tutorial/introduction.html#lists) e uno
[più dettagliato](https://docs.python.org/3/tutorial/datastructures.html#)
sull'uso delle liste. Per esemplificare l'uso di questi tre tipi di strumenti
conviene ragionare in termini di una lista utilizzata come se fosse un _array_,
memorizzando dunque una successione di valori dello stesso tipo, per esempio i
nomi di alcuni supereroi:

```python
names = ['Aquaman', 'Ant-Man', 'Batman', 'Black Widow',
         'Captain America', 'Daredavil', 'Elektra', 'Flash',
         'Green Arrow', 'Human Torch', 'Hancock', 'Iron Man',
         'Mystique', 'Professor X', 'Rogue', 'Superman',
         'Spider-Man', 'Thor', 'Northstar']
```
```{raw} html
<py-script>
names = ['Aquaman', 'Ant-Man', 'Batman', 'Black Widow',
         'Captain America', 'Daredavil', 'Elektra', 'Flash',
         'Green Arrow', 'Human Torch', 'Hancock', 'Iron Man',
         'Mystique', 'Professor X', 'Rogue', 'Superman',
         'Spider-Man', 'Thor', 'Northstar']
</py-script>
```


### Operatori

Alcuni degli operatori descritti in @dati-semplici mantengono la loro semantica
quando vengono usate delle liste come operatori: per esempio `==` permette di
verificare se due liste abbiano uguali contenuti (cioè contengano lo stesso
numero di elementi, e gli elementi in una stessa posizione siano uguali). Altri
tra questi operatori assumono invece una semantica diversa: in particolare

- l'operatore `+` permette di concatenare due liste, creando una nuova lista
  che contiene un numero di elementi pari alla somma dei numeri di elementi
  contenuti nelle due liste usate come operando: in particolare, questa nuova
  lista conterrà tutti gli elementi del primo operando in testa e tutti quelli
  del secondo operando in coda;
- per mantenere coerente la relazione tra gli operatori `+` e `*`, se `l` è una
  lista e `n` è un valore intero la valutazione dell'espressione `l * n` ha
  l'effetto di creare una nuova lista ottenuta concatenando `l` con se stessa
  esattamente `n` volte.

```{margin}
Vedremo che `in` e `del` mantengono la loro semantica anche quando vengono
usati con altri tipi di strutture dati.
```
Sempre in @dati-semplici sono stati introdotti gli operatori speciali `in` e
`del`. Il primo implementa essenzialmente la relazione di appartenenza: se `e`
è un'espressione e `l` una lista, l'espressione `e in l` viene valutata come
logicamente vera se il valore dell'espressione occorre in una posizione
qualsiasi della lista, e come logicamente falsa altrimenti:

```python
print('Thing' in names)
print('Human Torch' in names)
```
```{raw} html
<div id="stdout-5" class="script-stdout"></div>
<py-script>
output = io.StringIO()
sys.stdout = output

print('Thing' in names)
print('Human Torch' in names)

display(output.getvalue(), target="stdout-5")
</py-script>
```

L'operatore `del` permette invece di eliminare un elemento da una lista,
indicandone la relativa posizione: per esempio, eseguendo la cella seguente
viene cancellata la stringa contenuta nella prima posizione di `names`:

```python
del names[0]
```
```{raw} html
<py-script>
del names[0]
</py-script>
```

Va sottolineato che `del` è un operatore dal comportamento quantomeno
particolare, in quanto esso non restituisce alcun valore; la sua esecuzione ha
però l'_effetto collaterale_ di eliminare l'elemento nella posizione
specificata della lista usata come operando [^del-behaviour]. Come conseguenza
di questo effetto collaterale, nell'esempio precedente viene eliminato il primo
elemento della lista, così che quello che prima era il secondo elemento diventa
ora il primo, e così via, come si può facilmente verificare:



```python
names[0]
```
```{raw} html
<div id="out-8" class="script-output"></div>
<py-script>
display(names[0], target="out-8")
</py-script>
```

```{admonition} Nota
:class: note
In realtà `del` è un operatore che può essere applicato a una vasta gamma di
operandi, e che permette di eliminare il riferimento a un oggetto, liberando la
memoria che questo occupa quando non ci sono più riferimenti che puntano a
esso. Il fatto che le varie componenti di Python accessibili durante
l'esecuzione di un programma siano più o meno esplicitamente associate a degli
oggetti permette ad esempio di eliminare variabili, parti di strutture dati, ma
anche altri elementi del linguaggio che vedremo più avanti, come funzioni e
moduli.
```


### Funzioni

Alcune delle funzioni nel linguaggio base di Python sono pensate per elaborare
liste. Per esempio `len` restituisce la _lunghezza_ della lista specificata
come argomento, dove per lunghezza si intende il numero di elementi contenuti
nella lista:

```python
len(names)
```
```{raw} html
<div id="out-9" class="script-output"></div>
<py-script>
display(len(names), target="out-9")
</py-script>
```

Anche in questo caso, `len` è una funzione di carattere generale pensata per
calcolare la lunghezza delle varie strutture dati implementate in Python.

### Metodi

Python è un linguaggio di programmazione che implementa (anche) il paradigma
orientato a oggetti, e come abbiamo già visto le liste (così come gli altri
tipi di dati) sono a tutti gli effetti oggetti, e quindi su di esse è possibile
invocare dei metodi. Supponiamo per esempio di voler mettere in ordine
alfabetico i nomi dei supereroi contenuti in `names` (la lista è quasi in
ordine, l'unico elemento fuori posto è l'ultimo): uno dei modi in cui è
possibile eseguire questa operazione è quella di invocare sulla lista il
metodo `sort` (usando la _dot notation tipica_ della programmazione orientata
agli oggetti).

```python
names.sort()
```
```{raw} html
<py-script>
names.sort()
</py-script>
```


Così come l'operatore `del`, questo metodo non restituisce alcun valore, in
quanto l'ordinamento è eseguito _in place_ [^sorted]: l'invocazione di `sort`
ha come effetto collaterale il riposizionamento degli elementi all'interno
della lista in modo da riflettere l'ordinamento [^ordinamento-eterogeneo].
Possiamo convincercene facilmente visualizzando per esempio gli ultimi cinque
elementi di `names`:

```python
names[-5:]
```
```{raw} html
<div id="out-11" class="script-output"></div>
<py-script>
display(names[-5:], target="out-11")
</py-script>
```

In Python è possibile specificare valori per argomenti _opzionali_ quando si
invoca un metodo (o una funzione): si tratta di argomenti identificati da un
nome, che _possono_ essere omessi, e in tal caso assumono un valore predefinito
[^argomenti-opzionali]. Per poter specificare un valore diverso da quello
predefinito è necessario indicare, dopo _tutti_ gli eventuali argomenti non
opzionali, un'espressione del tipo `<nome>=<valore>`, dove `<nome>` indica il
nome dell'argomento opzionale in questione e `<valore>` è il relativo valore.
Per esempio, il metodo `sort` effettua l'ordinamento in verso non decrescente,
e l'argomento opzionale `reversed` permette di invertire tale verso:

```python
names.sort(reverse=True)
```
```{raw} html
<py-script>
names.sort(reverse=True)
</py-script>
```

Un'altra caratteristica di python è quella di poter specificare una funzione
come argomento di un metodo (o di un'altra funzione) [^first-class]; ciò si può
fare indicando il nome della funzione, oppure usando una _funzione anonima_
(vedi il Paragrafo [Funzioni anonime](funzioni-anonime)). Consideriamo ad
esempio l'argomento opzionale `key` del metodo `sort`: esso permette di
indicare un criterio alternativo per eseguire l'ordinamento, specificando come
valore una funzione che trasforma gli elementi della lista in quantità
numeriche su cui basare l'ordinamento (nel senso che elementi trasformati in
numeri più bassi compariranno prima nella lista ordinata rispetto ad altri
elementi trasformati in numeri più alti). Dunque è necessario fornire come
valore di questo argomento opzionale il nome di una funzione che trasforma
stringhe in numeri. Possiamo quindi utilizzare la funzione `len`
precedentemente introdotta:


```python
names.sort(key=len)
```
```{raw} html
<py-script>
names.sort(key=len)
</py-script>
```

Invocare in questo modo il metodo `sort` equivale quindi a:

- associare ogni nome di supereroe alla sua lunghezza,
- ordinare le coppie ottenute in base alla lunghezza,
- considerare solo i nomi, mantenendo questo nuovo ordinamento.

In parole povere, abbiamo ordinato i nomi dal più breve al più lungo, come si
può facilmente verificare:

```python
names
```
```{raw} html
<div id="out-14" class="script-output"></div>
<py-script>
display(names, target="out-14")
</py-script>
```

Nel caso in cui si volessero specificare due o più argomenti opzionali all'atto
dell'invocazione di un metodo, basta separarli usando le virgole esattamente
come si procede per gli argomenti non opzionali. Per esempio

```python
names.sort(key=lambda n:len(n), reverse=True)
```
```{raw} html
<py-script>
names.sort(key=lambda n:len(n), reverse=True)
</py-script>
```

riordina le stringhe contenute in `names` dalla più lunga alla più corta. Va
anche notato che essendo gli argomenti opzionali univocamente individuati dal
loro nome, non è necessario specificarli seguendo un ordine prefissato:
pertanto si potrebbero scambiare le posizioni di `key` e `reverse`
nell'invocazione precedente senza modificare la semantica dell'istruzione.

(sec:tuple)=
## Le tuple

```{margin}
La sintassi per la descrizione delle tuple diventa problematica quando si vuole
indicare una tupla contenente un unico elemento, in quanto per esempio
l'espressione `(1)` viene interpretata come il valore intero `1` racchiuso tra
parentesi tonde, ottenendo dunque il medesimo intero come risultato della
valutazione. In casi come questo la soluzione è quella di fare seguire l'unico
elemento della tupla da una virgola, scrivendo per esempio `(1,)`. Come regola
generale, infatti, è sempre possibile aggiungere una virgola alla fine di una
tupla (o di una lista) senza che ciò ne alteri i contenuti. È invece possibile
utilizzare l'espressione `()` per indicare una tupla vuota.
```
Una tupla è in tutto e per tutto una lista immutabile, nel senso che una volta
che essa è stata creata non è possibile modificare i suoi contenuti. Un
letterale di tipo tupla viene indicato con una sintassi analoga a quella per le
liste, con l'unica differenza che i suoi contenuti sono delimitati da parentesi
tonde.

```python
rogue = ('Rogue',
         'Anna Marie',
         'Caldecott County, Mississippi',
         'Marvel Comics',
         173.1,
         54.39,
         'F',
         1981,
         'Green',
         'Brown / White',
         10,
        'good')
```
```{raw} html
<py-script>
rogue = ('Rogue',
         'Anna Marie',
         'Caldecott County, Mississippi',
         'Marvel Comics',
         173.1,
         54.39,
         'F',
         1981,
         'Green',
         'Brown / White',
         10,
        'good')
</py-script>
```



L'accesso a un elemento di una tupla viene fatto in modo posizionale usando la
medesima sintassi introdotta per le liste, e anche in questo caso è possibile
estrarre delle sotto-tuple utilizzando degli _slicing_. Quando però si tenta di
modificare un elemento contenuto in una tupla, l'esecuzione verrà bloccata
emettendo un errore:

```python
    rogue[-2] = 70
```
```{raw} html
<div id="stderr-17" class="script-stderr"></div>
<py-script>
import traceback

try:
    rogue[-2] = 70
except Exception:
    tb = traceback.format_exc()
    display(tb, target="stderr-17")
</py-script>
```

A seguito di questo errore, la tupla manterrà i suoi valori originali, restando
quindi effettivamente invariata:

```python
rogue
```
```{raw} html
<div id="out-18" class="script-output"></div>
<py-script>
display(rogue, target="out-18")
</py-script>
```

Una tupla può essere utilizzata facendo ri ferimento agli stessi operatori e
alle stesse funzioni messi a disposizione per le liste (come per esempio `in` e
`len`), escludendo ovviamente le operazioni che modificano la tupla stessa
(come `sort`).

L'immutabilità delle tuple le rende da preferire rispetto alle liste in tutti i
casi in cui si vuole impedire che dei dati vengano modificati, per esempio a
causa di un bug; inoltre la loro elaborazione è in molti casi più efficiente di
quella delle liste.

(sec:array)=
## Gli array
Un _array_, o vettore, è una struttura dati statica ad accesso posizionale che
permette di memorizzare una sequenza di valori omogenei.

(sec:insiemi)=
## Gli insiemi
Python implementa direttamente un tipo di dato per gli insiemi, intesi come
collezione finita di elementi tra loro distinguibili e non memorizzati in un
ordine particolare. A differenza delle liste e delle tuple, gli elementi non
sono quindi associati a una posizione e non è possibile che un insieme contenga
più di un'istanza di un medesimo elemento. La descrizione di questo tipo di
dato è posticipata al Paragrafo @insiemi-in-python, dopo avere richiamato le
proprietà matematiche di base degli insiemi.


(sec:dizionari)=
##  I dizionari
I dizionari servono a memorizzare delle associazioni tra oggetti, in analogia
con il concetto matematico di funzione. È quindi possibile pensare a essi come
a insiemi di coppie (chiave, valore), dove una data chiave non occorre più di
una volta, e a ogni chiave corrisponde un unico valore.

Un letterale di tipo dizionario viene descritto indicando ogni coppia separando
chiave e valore con il carattere di due punti, separando le coppie con delle
virgole e racchiudendo l'intero letterale tra parentesi graffe. Possiamo per
esempio usare un dizionario per rappresentare un _record_ in modo più elegante
rispetto a quanto fatto nel Paragrafo @liste utilizzando le liste:

```python
rogue = {'name': 'Rogue',
         'identity': 'Anna Marie',
         'birth_place': 'Caldecott County, Mississippi',
         'publisher': 'Marvel Comics',
         'height': 173.1,
         'weight': 54.39,
         'gender': 'F',
         'first_appearance': 1981,
         'eye_color': 'Green',
         'hair_color': 'Brown / White',
         'strength': 10,
         'intelligence': 'good'}
```
```{raw} html
<py-script>
rogue = {'name': 'Rogue',
         'identity': 'Anna Marie',
         'birth_place': 'Caldecott County, Mississippi',
         'publisher': 'Marvel Comics',
         'height': 173.1,
         'weight': 54.39,
         'gender': 'F',
         'first_appearance': 1981,
         'eye_color': 'Green',
         'hair_color': 'Brown / White',
         'strength': 10,
         'intelligence': 'good'}
</py-script>
```

L'accesso, in lettura o scrittura, agli elementi di un dizionario viene fatto
con una notazione che ricorda quella di liste e tuple: si specifica all'interno
di parentesi quadre la chiave per ottenere o modificare il valore
corrispondente:

```python
rogue['identity']
```
```{raw} html
<div id="out-20" class="script-output"></div>
<py-script>
display(rogue['identity'], target="out-20")
</py-script>
```

È proprio questa modalità di accesso che fa sì che i dizionari rappresentino
una scelta più elegante per memorizzare un record: `rogue['identity']` è
sicuramente più leggibile di `rogue[1]`. Va notato che il prezzo da pagare per
la leggibilità è un'efficienza potenzialmente minore nelle operazioni di
accesso (normalmente le liste sono implementate con una logica simile a quella
degli array e dunque hanno un tempo di accesso costante ai loro elementi,
mentre i dizionari sono implementati tramite tabelle di hash, pertanto
l'accesso è a tempo costante solo se non avvengono collisioni).

Se si tenta di accedere in lettura a un dizionario specificando una chiave
inesistente viene lanciata un'eccezione (`KeyError`), mentre accedendovi in
scrittura la specificazione di una chiave inesistente comporterà l'aggiunta
della corrispondente coppia (chiave, valore) al dizionario.

L'operatore `in` introdotto per le liste può anche essere utilizzato per i
dizionari: più precisamente, l'espressione `k in d` restituisce `True` se `k` è
una chiave valida per il dizionario `d`.

Anche nel caso dei dizionari il linguaggio mette a disposizione una serie di
funzioni specifiche, e si può fare riferimento alla
[documentazione ufficiale](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
di python per approfondire l'argomento.

## Esercizi

Provare a modificare un carattere in una stringa e vedere che cosa succede

Doppio for in list comprehension


[^var-ciclo]: Nel tempo si è consolidato l'uso dei nomi `i`, `j` e `k` per le variabili
usate nei cicli enumerativi. C'è chi sostiene (ma è uno scherzo) che ciò sia un
omaggio dovuto a
[Edsger Dijkstra](https://en.wikipedia.org/wiki/Edsger_W._Dijkstra), uno dei
pionieri dell'informatica, ma l'origine di questi nomi va fatta risalire a uno
dei primi linguaggi di programmazione: il
[Fortran](https://en.wikipedia.org/wiki/Fortran), che utilizzava una
dichiarazione di tipo _implicita_, nella quale la lettera iniziale nel nome di
una variabile ne determinava anche il tipo, e il tipo era intero per le 
variabili nelle quali questa iniziale era compresa tra I e N. Per brevità, e
anche per ricordare la classica notazione usata in matematica per gli indici
muti nelle sommatorie o nelle successioni, venivano quindi usate `I`, `J` e `K`
come variabili di ciclo, e `N` o `M` per indicare eventualmente il valore
finale di queste ultime (notate l'uso delle maiuscole: quando è stato
introdotto il Fortran, si usavano solo quelle per scrivere il codice!). Questa
convenzione viene ampiamente usata anche oggi: qualunque programmatore associa
istintivamente nomi come `i` e `j` alle variabili di ciclo. È per questo che
il loro uso è consigliato anche in Python, anche se vedremo che è relativamente
rara la necessità di dover introdurre variabili di questo tipo.

[^for-caveats]: In realtà è possibile modificare dinamicamente il numero di
iterazioni in un ciclo enumerativo, sia forzandone l'uscita anticipata, sia
modificando alcune informazioni contestuali, come il valore della varaibile di
ciclo nei linguaggi come C o Java, o la modifica del dato strutturato sul quale
si esegue l'iterazione in Python.  Quest'ultima pratica è però decisamente
sconsigliata, perché complica la comprensione del codice ed è normalmente
rimpiazzabile con degli idiomi di programmazione più eleganti, come la sopra
menzionata uscita anticipata.

[^foreach]: Per completezza di informazione, molti altri linguaggi di
programmazione affiancano al ciclo enumerativo (inteso in senso classico) una
struttura di controllo con la semantica analoga a quella di `for` in Python,
usando parole chiave dedicate come `foreach` o `forall`, oppure introducendo
una sintassi alternativa.

[^design-pattern]: L'uso del termine _pattern_ può causare confusione con
l'argomento più generale dei _design pattern_ [@gang-of-four], che descrivono
degli schemi decisamente più complessi di quelli che descrivono codice
idiomatico, e che si possono implementare usando diversi linguaggi di
programmazione. Sono esempi di _design pattern_ i singoletti, i _flyweight_ e i
metodi fabbrica.

[^data-model]: Se avete già studiato un linguaggio di programmazione orientato
agli oggetti, vi starete probabilmente chiedendo perché la lunghezza di una
struttura non si ottenga invocando un metodo su di essa. Questo è in effetti
quello che succede dietro le quinte: tutte le occorrenze di `len(o)` vengono
automaticamente convertite nell'invocazione `o.__len__()`, dove `__len__` è
un metodo implementato in tutti i tipi strutturati (il doppio _underscore_
all'inizio e alla fine del nome del metodo sancisce il fatto che quest'ultimo è
per certi versi speciale, ed è alla base della regola di stile che richiede di
non usare `_` all'inizio e alla fine degli identificatori). Questo permette
agli sviluppatori di scrivere nuove classi i cui oggetti possono essere usati
in modo trasparente come argomenti di `len`. Procedendo in modo analogo si
riesce ad agire praticamente su tutti gli aspetti del linguaggio, costruendo
delle classi i cui oggetti possono venire usati come operandi in espressioni
matematiche, o che possono essere invocati come delle funzioni, o ancora che
supportano l'equivalente degli operatori di accesso. L'idea di base è quella
di usare sempre la stessa sintassi per effettuare una particolare azione,
indipendentemente dallo specifico tipo di dato che viene elaborato (ricordate
uno dei principi esposti nello zen di Python: «There should be one&mdash;and
preferably only one&mdash;obvious way to do it»). Il cosiddetto
[Python data model](https://docs.python.org/3/reference/datamodel.html)
formalizza in modo dettagliato la corrispondenza tra i vari componenti del
linguaggio e i metodi che le classi devono implementare. Un
buon punto di partenza per studiare il Python data model è il primo capitolo
di {cite:p}`ramalho`, sebbene sarebbe prima importante imparare come si
definisce una nuova classe.

[^start-from-zero]: Gli informatici iniziano a contare da zero. Se aveste
qualche dubbio sull'utilità di questa pratica, un breve ma particolarmente
efficace
[manoscritto](https://www.cs.utexas.edu/~EWD/ewd08xx/EWD831.PDF) di Edsger
Dijkstra (vedi anche la precedente nota[^var-ciclo]) descrive i suoi vantaggi.

[^substring]: Dover specificare la posizione del primo carattere da
escludere sembra controintuitivo rispetto a indicare la posizione dell'ultimo
carattere nella sottostringa. In realtà in questo modo risulta più facile
scrivere codice che elabora porzioni successive in una stringa.

[^escape_numeric]: Oltre ad altre sequenze standard di _escaping_ che sono
generalmente utilizzate poco o per nulla, è possibile fare seguire il carattere
di _backslash_ dalla codifica numerica di un carattere qualsiasi,
opportunamente espressa in ottale o esadecimale, così come dal suo nome
simbolico nella codifica Unicode. Per una descrizione più precisa, si può fare
riferimento alla parte della
[documentazione ufficiale](https://docs.python.org/3/reference/lexical_analysis.html#escape-sequences)
che descrive in dettaglio le sequenze di _escaping_.

[^del-behaviour]: I lettori attenti potrebbero avere notato un apparente
incoerenza tra il modo in cui vengono valutate le espressioni e la semantica
appena introdotta per l'operatore `del`. Consideriamo l'espressione
`del names[0]` dell'esempio precedente: se questa fosse valutata in modo
ususale, verrebbe innanzitutto valutato l'operando, dunque l'espressione
`names[0]`. L'operatore `del` verrebbe quindi applicato al valore ottenuto, che
nel nostro caso sarebbe la stringa `'Aquaman'`. Ora, l'istruzione
`del 'Aquaman'` genererebbe un errore, perché `del` si può applicare solo a
riferimenti e non a letterali. In realtà la valutazione di espressioni di
questo tipo viene fatta in un modo diverso, perché `del names[0]` viene i
plicitamente convertita in un'altra espressione che equivale a invocare un
particolare metodo dell'oggetto referenziato da `names`, passando il valore `0`
come argomento. 

[^sorted]: In realtà è disponibile anche la funzione `sorted`, che non modifica
l'argomento e restituisce una nuova lista.

[^ordinamento-eterogeneo]: Tenuto conto del fatto che le liste sono una
struttura dati eterogenea ci si potrebbe chiedere quale sia la relazione
d'ordine a cui fa riferimento Python quando viene invocato il metodo `sort`.
Non approfondiremo questo aspetto: per quanto riguarda gli argomenti qui
trattati è sufficiente dire che quando gli elementi della lista sono tutti
dello stesso tipo viene sfruttata una relazione d'ordine canonica per questo
tipo. Per esempio i valori numerici sono ordinati in modo non decrescente e per
le stringhe viene utilizzato l'ordinamento lessicografico.

[^argomenti-opzionali]: Gli argomenti opzionali vengono tipicamente utilizzati
quando si ha a che fare con metodi o funzioni che implementano operazioni che
prevedono svariate opzioni, sebbene nella maggior parte dei casi ognuna di
queste opzioni venga usata sempre nello stesso modo, modificandone al più una
oppure due. Si pensi al caso della produzione di grafici: sebbene in teoria sia
possibile cambiare il colore o lo spessore degli assi cartesiani, o il corpo
dei caratteri usati per etichettare questi ultimi, difficilmente si ricorre a
tale possibilità. E anche quando si decide di modificare l'aspetto di un
grafico, si agisce di norma solo su alcune delle molteplici possibilità. In
assenza di argomenti opzionali, sarebbe quindi necessario specificare
obbligatoriamente un elevato numero di valori (uno per ogni elemento stilistico
personalizzabile), quasi sempre uguali e ricordandone l'ordine esatto. Vedremo
nel Paragrafo [Disegnare grafici](disegnare-grafici) che le librerie che
useremo per produrre grafici sfruttano proprio gli argomenti opzionali per
permettere di specificare solo le eventuali modifiche da apportare rispetto a
uno stile predefinito per il risultato che si vuole ottenere.

[^first-class]: Nel gergo tecnico in lingua inglese si dice che i nomi di
funzione sono _first-class citizen_ per enfatizzare che vengono trattate in
modo analogo ai nomi delle altre variabili: è possibile per esempio usarli per
specificare argomenti, o come destinazione di un'operazione di assegnamento.



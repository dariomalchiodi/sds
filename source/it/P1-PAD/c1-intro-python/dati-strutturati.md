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

(sec_dati-strutturati)=
#  Dati strutturati

Come anticipato nel {ref}`sec_tipi-di-dati`, considero strutturato un tipo di
dati quando i suoi valori rappresentano un'aggregazione di più elementi, __e__
quando è possibile iterare automaticamente sui suoi contenuti. Dopo aver
chiarito meglio questo concetto, in questo paragrafo presenterò i principali
tipi strutturati disponibili in Python. Di ciascuno descriverò la classe
corrispondente e alcuni aspetti della sintassi che consente di accedere agli
elementi in esso contenuti.

```{admonition} Nomenclatura
Il valore associato a un tipo di dati strutturato viene memorizzato attraverso
una _struttura dati_, cioè un modo per organizzare e gestire un insieme di
informazioni all’interno di un computer. Questa vicinanza terminologica può
generare confusione: talvolta i due concetti coincidono (come nel caso degli
array), ma nella maggior parte delle situazioni restano distinti. In effetti,
uno stesso tipo di dati strutturato può essere implementato utilizzando
strutture dati diverse. Per esempio, un insieme può basarsi tanto su un _array_
quanto su un albero, anche se la scelta dell’una o dell’altra soluzione
influisce sull’_efficienza_ delle operazioni eseguibili. Poiché in questo libro
non entrerò nel merito delle strutture dati, eviterò ove possibile di usare
l’espressione «valore di un tipo di dati strutturato», che risulta piuttosto
macchinosa. Adotterò occasionalmente il termine _struttura_ come abbreviazione,
confidando che il contesto renda chiaro a che cosa mi riferisco.
```

I tipi di dati strutturati che presenterò nei prossimi paragrafi &mdash;
elencati nella {numref}`tab_caratteristiche-dati-strutturati` &mdash; sono i
seguenti:
```{margin}
Python include il modulo `array`, che fornisce un’implementazione degli array
ma che non supporta l’aritmetica vettoriale. Per questo motivo, nell’analisi
dei dati si ricorre quasi sempre agli array forniti da `numpy`.
```
- le stringhe, che abbiamo già utilizzato e che rappresentano sequenze di
  caratteri;
- gli _array_, che contengono sequenze omogenee di oggetti;
- le liste e le tuple, che implementano sequenze di generici oggetti;
- gli insiemi, che corrispondono all'omonimo concetto in matematica;
- i dizionari, che consentono di costruire associazioni &mdash; o _mappe_
  &mdash; tra oggetti.

Classificherò questi tipi di dati secondo alcuni criteri, illustrati di seguito.

- La modalità di accesso: quando l'aggregazione è sequenziale, il modo più
  naturale per riferirsi a un elemento è tramite un _indice_ che ne indica la
  posizione. È questo il caso di stringhe, liste, _array_ e tuple. Insiemi e
  dizionari, invece, organizzano i dati in modo non necessariamente ordinato, e
  l'accesso ai loro elementi segue regole diverse.
- La staticità o dinamicità della struttura: alcuni tipi di dati strutturati
  non consentono di aggiungere o rimuovere elementi dopo la creazione della
  struttura (come stringhe e tuple), mentre altri lo permettono (come liste,
  insiemi e dizionari).
- La mutabilità degli elementi: alcuni tipi sono _immutabili_, nel senso che
  gli elementi che contengono non possono essere modificati, mentre altri sono
  _mutabili_. Tra i tipi che considererò, stringhe e tuple sono immutabili,
  mentre tutti gli altri sono mutabili. I tipi immutabili sono necessariamente
  statici, ma non sempre vale il contrario.
- L'omogeneità o eterogeneità dei contenuti: alcune strutture richiedono che
  tutti gli elementi siano dello stesso, mentre altre accettano elementi
  eterogenei.

La {numref}`tab_caratteristiche-dati-strutturati` riassume i tipi di dati sui
quali mi soffermerò nei prossimi paragrafi, indicando per ciascuno la classe
Python corrispondente e specificando quali delle proprietà appena elencate sono
soddisfatte e quali no.

```{margin}
Ricordate che `np` è l’_alias_ che viene comunement utilizzato per importare il
modulo numpy.
```
```{table} Proprietà dei tipi di dati strutturati
:name: tab_caratteristiche-dati-strutturati
:align: center
| Tipo strutturato            | Classe     | Posizionale | Dinamico | Mutabile | Omogeneo |
|:----------------------------|:-----------|:-----------:|:--------:|:--------:|:--------:|
| [stringa](sec_stringhe)     | `str`      | ✓           | ✕       | ✕        | ✓        |
| [array](sec_array)          | `np.array` | ✓           | ✕       | ✓        | ✓        |
| [lista](sec_liste)          | `list`     | ✓           | ✓       | ✓        | ✕        |
| [tupla](sec_tuple)          | `tuple`    | ✓           | ✕       | ✕        | ✕        |
| [insieme](sec_insiemi)      | `set`      | ✕           | ✓       | ✓        | ✕        |
| [dizionario](sec_dizionari) | `dict`     | ✕           | ✓       | ✓        | ✕        |
```


(sec_iterare)=
## Accedere a una struttura
Sebbene facciano riferimento a concetti anche molto diversi tra loro, i tipi di
dati strutturati che prenderò in esame condividono alcune modalità di accesso
comuni. Python fornisce per queste operazioni una sintassi coerente e
relativamente uniforme. La prima modalità riguarda proprio l’aspetto che ho
scelto per definire i dati strutturati: la possibilità di iterare
automaticamente sui contenuti di una struttura.

Molti linguaggi di programmazione di tipo imperativo includono, tra le
strutture di controllo, il cosiddetto _ciclo enumerativo_, noto ai più come
«ciclo for», dal nome della parola chiave che lo introduce. Questa forma di
iterazione si caratterizza per il fatto che il numero di ripetizioni del corpo
del ciclo è determinato a priori. In genere, tale numero è legato a una
_variabile di ciclo_[^var-ciclo], che assume tutti i valori in una sequenza
predefinita &mdash; normalmente, ma non sempre, gli interi da $0$ fino a un
valore prefissato[^for-caveats].
```{margin}
Vale la pena notare che il termine «struttura di controllo» indica un concetto
completamente distinto sia da «tipo di dati strutturato», sia da «struttura
dati».
```

Python, invece, adotta un approccio del tutto diverso. Nella forma più
semplice, un ciclo viene introdotto dall'idioma `for <variabile> in
<struttura>:`, dove `<variabile>` è il nome assegnato alla variabile di ciclo e
`<struttura>` è il valore di un tipo di dati strutturato. Il corpo del ciclo
segue immediatamente dopo, con un livello di indentazione maggiore.
L’esecuzione procede in modo intuitivo: ciascun elemento contenuto in
`<struttura>` viene considerato a turno, una sola volta, assegnato alla
variabile del ciclo ed elaborato dal suo corpo. La differenza fondamentale
rispetto al ciclo enumerativo classico è che, in quest’ultimo, la variabile di
ciclo rappresenta un _indice_ usato per accedere all’elemento da elaborare —
per esempio, prelevandolo da un _array_ &mdash; mentre in Python la variabile
di ciclo contiene direttamente l’elemento stesso[^foreach].

````{prf:example}
:label: ex-string

L’unico tipo di dati strutturato di cui ho parlato finora sono le stringhe:
eseguire un ciclo for su una di esse significa scorrere tutti i suoi caratteri,
nell’ordine naturale che va dal primo all’ultimo:

```{code-cell} python

s = 'Wasp'
for c in s:
    print(c)
```
````

Il nome della variabile di ciclo viene di solito scelto rispettando due criteri:  
deve essere breve e deve richiamare il significato dei valori che assumerà
durante l’iterazione. Nell’esempio precedente ho usato `c`, poiché il ciclo si
svolge sui caratteri di una stringa.

Nonostante la differenza semantica rispetto ai linguaggi imperativi
tradizionali, il costrutto `for` di Python appartiene comunque alla categoria
dei cicli enumerativi. Anche in questo caso, infatti, la variabile di ciclo
assume, uno dopo l’altro, i valori di una sequenza, che corrispondono agli
elementi contenuti nella struttura su cui si sta iterando. La descrizione di
questa semantica non specifica, però, _in quale ordine_ vengano considerati gli
elementi: ciò dipende dal tipo di dati strutturato utilizzato. In alcuni casi
&mdash; come per le stringhe o le liste &mdash; l’ordine è determinato in modo
prevedibile; in altri, come per gli insiemi o i dizionari, non lo è.


````{admonition} Pattern e antipattern
Quando si studia un linguaggio di programmazione, si impara rapidamente a
riconoscere degli _schemi_ ricorrenti nel codice: piccole sequenze di
istruzioni la cui struttura è sempre simile, ma che possono riutilizzate in
molte altre situazioni. Questi schemi vengono chiamati _pattern_ del
linguaggio, anche se spesso si preferisce parlare di codice _idiomatico_ o, nel
caso specifico di Python, _pythonico_[^design-pattern]. L’uso del ciclo for
per iterare su una stringa, mostrato negli esempi precedenti, è un esempio di
codice pythonico: rappresenta una soluzione generale che va oltre la semplice
iterazione sui caratteri di una stringa. Come già evidenziato, lo stesso
approccio permette di iterare su altre strutture dati come le liste o i
dizionari, aiutando a produrre codice Python generale e a individuare
rapidamente strategie di soluzione anche quando non si conosce in dettaglio un
componente del linguaggio.

Va però sottolineato che esistono schemi che possono emergere facilmente senza
rappresentare codice idiomatico. Sono gli _antipattern_: schemi che, appresi
autonomamente, adattati da altri linguaggi, oppure reperiti su fonti non
sempre affidabili (come i forum di discussione), producono codice poco
efficiente o difficilmente adattabile ad altri problemi. Chi conosce già Java,
per esempio, potrebbe iterare su una stringa ricalcando l'approccio
tradizionale che si basa su una variabile di ciclo associata alle posizioni
dei carateri, scrivendo il codice che segue.

```{interactive-code} python
for i in range(len(s)):
    print(s[i])
```

Il risultato è un _antipattern_ che introduce complessità inutile, obbligando
a:

- definire una variabile intera `i` quando ciò che interessa sono i singoli
  caratteri e non le loro posizioni;
- invocare `range`, che genera un oggetto sul quale è possibile iterare per
  ottenere le posizioni della stringa;  
- calcolare esplicitamente la lunghezza della stringa.

Inoltre, questo metodo non si generalizza facilmente ad altri tipi di dati
strutturati, come [insiemi](#sec_insiemi), [dizionari](sec_dizionari) o file.
L’approccio idiomatico, invece, è più semplice da scrivere e dunque anche più
leggibile. Naturalmente, ci sono situazioni in cui è utile conoscere sia i
caratteri, sia la loro posizione: in questi casi, il modo pythonico di
procedere è utilizzare la funzione `enumerate`:

```{interactive-code} python
for i, c in enumerate(s):
    print('Il carattere in posizione ', i, 'è', c)
```
````

Le altre modalità di accesso comuni ai tipi di dati strutturati sono riassunte
nel seguente elenco, e verranno approfondite nei prossimi paragrafi.

- La funzione `len` restituisce sempre il numero di elementi contenuti nella
  struttura[^data-model]. Nel gergo informatico, questo numero è chiamato
  _lunghezza_, anche se in alcuni casi la denominazione può risultare impropria
  (per esempio, per gli insiemi si dovrebbe parlare più correttamente di
  _cardinalità_).

- Sono quasi sempre disponibili uno o più operatori di _accesso_ che permettono
  di ottenere il valore di un elemento specifico contenuto nella struttura e,
  se questa è mutabile, di modificarlo. La loro sintassi si basa sull’uso delle
  parentesi quadre, estendendo l’operatore di indicizzazione degli _array_
  presente nella maggior parte dei linguaggi di programmazione.

- L’operatore `in` consente di verificare se un elemento appartiene o meno a
  una struttura, mentre l’operatore `del` può essere utilizzato per rimuovere
  elementi da strutture dinamiche.


(sec_stringhe)=
## Le stringhe

```{margin}
Nei paragrafi seguenti vedremo che esistono altre modalità per
specificare i letterali di tipo stringa.
```
A differenza di altri linguaggi, come per esempio C, in Python non esiste
un tipo di dato dedicato ai singoli caratteri. Le stringhe, intese come
sequenze di zero o più caratteri, sono implementate attraverso la classe `str`,
che mette a disposizione un tipo omogeneo e ad accesso posizionale, i cui
oggetti sono immutabili. Nella versione più semplice, i letterali di questa
classe si ottengono racchiudendo i caratteri della stringa tra due delimitatori.
Esistono tre tipi di delimitatori: gli apici singoli, doppi e tripli. L’uso
degli apici singoli (`'`) o doppi (`"`) ricalca la sintassi classica dei
linguaggi di programmazione più diffusi, con la differenza che in Python è
possibile scegliere tra due delimitatori diversi: in altre parole, `'Robin'` e
`"Robin"` identificano la stessa stringa. Questa possibilità facilita la
creazione di stringhe che contengono apici doppi o singoli, come negli esempi
seguenti:

```{code-cell} python
:tags: [remove-output]

'Superman proviene da un pianeta chiamato "Krypton".'
"L'altro nome di Superman è Kal-El."
```
```{margin}
Volendo, apici singoli e doppi si possono comunque inserire in un letterale
stringa usando la tecnica di _escaping_, tramite le sequenze `\'` e `\"`.
```

È però necessario chiudere la stringa con lo stesso tipo di delimitatore con
cui è stata aperta: sempre due apici singoli o due doppi apici. Gli apici
tripli permettono di utilizzare stringhe che si estendono su più righe, senza
dover utilizzare sequenze di _escape_ per i caratteri di «a capo». Per esempio:

```{code-cell} python
:tags: [remove-output]

'''Il primo fumetto che ha Storm come protagonista
compare nel numero uno di "Giant-size X-men"
ed è stato pubblicato nel 1977.
'''
```

definisce una stringa di tre righe. I tre apici possono essere sia singoli sia
doppi, ma anche in questo caso è necessaria coerenza tra il delimitatore
iniziale e quello finale.

Abbiamo già visto che l’iterazione su una stringa avviene carattere per
carattere, nell’ordine in cui questi compaiono. Non sorprende quindi che
`len(s)` restituisca il numero di caratteri della stringa `s`, né che i
letterali `''` e `""` rappresentino la stringa vuota (la cui lunghezza è zero).

L’operatore di accesso merita qualche parola in più. È naturale voler accedere
ai singoli caratteri di una stringa in base alla loro posizione: dopo il nome
della variabile che la referenzia (o il corrispondente letterale), basta
specificare tra parentesi quadre l’indice del carattere desiderato, a partire
da `0`[^start-from-zero]. In altre parole, l’operatore di accesso ha la stessa
semantica degli _array_. Tuttavia, Python ne estende l’uso: se si indica un
valore negativo come indice, a questo viene automaticamente sommata la
lunghezza della stringa, così `-1` identifica l’ultimo carattere, `-2` il
penultimo e così via.

È inoltre possibile indicare un intervallo di posizioni consecutive per
ottenere una sottostringa. Questa modalità, detta _slicing_, si esprime
indicando tra parentesi quadre la posizione del primo carattere da includere,
seguita da due punti e dalla posizione del primo carattere da
escludere[^substring]. Gli _slicing_ possono combinare indici positivi e
negativi, purché la posizione iniziale preceda quella finale; in caso
contrario, l’operazione restituisce la stringa vuota.
```{margin}
Quando si omette la posizione iniziale, la sottostringa parte dall’inizio;
quando si omette quella finale, prosegue fino alla fine della stringa.
```

Infine, l’operatore `in` permette di verificare se un carattere o una
sottostringa è contenuto all’interno di un’altra stringa. In particolare,
`s in t` restituisce `True` se la stringa `s` è una sottostringa di `t`, e
`False` altrimenti.

````{prf:example}
:label: ex-string-2

Consideriamo la stringa definita nella cella seguente.

```{interactive-code} python
s = '''- Spider-Man: Dev'esserci qualcun altro da chiamare... Per esempio Thor?
- Nick Fury: Fuori portata.
- Spider-Man: Captain Marvel.
- Maria Hill: Indisponibile.
- Spider-Man: Io sono solo un amichevole Spider-Man di quartiere.
- Nick Fury: Ma per favore! Sei stato nello spazio!'''
```

Le istruzioni che seguono mostrano come:

- calcolare la lunghezza della stringa;
- estrarne il primo e l’ultimo carattere, utilizzando l’operatore di accesso;
- ottenere una sottostringa, combinando operatore di accesso e _slicing_;
- verificare se una sottostringa è presente all’interno della stringa.

```{interactive-code} python
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

````

Come ho già precedentemente accennato, in Python le stringhe sono immutabili,
cioè non è possibile modificarne il contenuto, ad esempio sostituendo un
carattere con un altro o aggiungendo uno o più caratteri. Per effettuare
operazioni di questo tipo è sempre necessario creare una nuova stringa che
sostituisca quella di partenza.

La classe `str` implementa vari metodi e operatori specifici per le stringhe;
in particolare vale la pena evidenziare che:

- l'operatore `+` concatena due stringhe (e __solo__ due stringhe: è necessario
  convertire in stringa eventuali operandi di tipo diverso);
- la moltiplicazione di una stringa `s` per un numero intero `i` produce una
  nuova stringa ottenuta concatenando `s` con se stessa `i` volte;
- `s.find(t)` restituisce la posizione iniziale della prima occorrenza della
  sottostringa `t` all’interno di `s`, se presente, e `-1` altrimenti.

Per un elenco completo dei metodi disponibili si può consultare la sezione
relativa alle stringhe nella [documentazione
ufficiale](https://docs.python.org/3/library/stdtypes.html#string-methods).


(sec_r-string)=
### Letterali stringa grezzi

Come ho già detto, si può generare una stringa usando sequenze di _escape_ per
inserire caratteri difficili o impossibili da rappresentare direttamente in un
letterale. Nei casi più frequenti, ciò riguarda i caratteri di «a capo»
(_newline_, `\n`), di tabulazione (`\t`) e lo stesso _backslash_
(`\\`)[^escape_numeric], che altrimenti non potrebbe comparire all’interno di
un letterale stringa. In alcuni contesti è necessario creare stringhe
contenenti molti caratteri di _backslash_: in questi casi, l’uso delle sequenze
di _escape_ renderebbe difficile la lettura dei letterali che si otterrebbero.
Per risolvere questo problema, si utilizzano i cosiddetti _letterali grezzi_
(in inglese, _raw string literals_, o, per brevità, _r-string_). In questi
letterali, che si ottengono prependendo `r` al delimitatore iniziale della
stringa,  le sequenze di _escape_ non vengono interpretate.

```{margin}
Se non conoscete $\LaTeX$, vi consiglio caldamente di imparare a usarlo. Anche
se all’inizio non è facilissimo da imparare, permette di redigere documenti di
qualità tipografica, concentrandosi sui loro contenuti e occupandosi solo
marginalmente dei dettagli relativi alla formattazione. Inoltre, offre
strumenti che automatizzano l'inserimento di formule matematiche ela gestione
di indici, riferimenti incrociati, bibliografia e così via.
```


````{prf:example} $\LaTeX$
:label: -latex

$\LaTeX$ è un linguaggio di marcatura che permette di descrivere [testi
formattati](https://www.latex-project.org/), ampiamente utilizzato in ambito
scientifico per produrre documentazione e che ho usato anche per generare tutte
le formule matematiche di questo libro. In $\LaTeX$, i simboli matematici
vengono descritti tramite una particolare sintassi basata sul carattere di
_backslash_: ad esempio, `\pi` e `\int` producono rispettivamente $\pi$ e
l’operatore integrale. Nella cella seguente, la funzione `display` e la classe
`Math` del modulo `IPython.display` vengono utilizzate per visualizzare nella
cella di output una formula relativamente complessa.

```{interactive-code} python
from js import document, katex

s = r'\Phi(x) = \frac{1}{2 \pi} '
s += r'\int_{-\infty}^{+\infty} \mathrm e^{-\frac{x^2}{2}} \, dx'

target = document.getElementById("latex-out")
katex.render(s, target)
```
```{raw} html
<div id="latex-out"></div>
```

Questa formula descrive una particolare funzione che studieremo nel
Paragrafo {ref}`sec_modello-normale`. Notate che ho costruito la stringa
giustapponendo due letterali grezzi tramite l'operatore `+=`, così da evitare
righe di codice più lunghe di ottanta caratteri[^ottanta].
````


````{prf:example} Espressioni regolari
:label: ex-regex

Le [espressioni regolari](https://it.wikipedia.org/wiki/Espressione_regolare)
sono un formalismo che permette di definire insiemi di stringhe che soddisfano
particolari regole. Il punto di partenza di questo formalismo sono dei
costrutti fondamentali che esprimono proprietà relativamente semplici di una
stringa: ad esempio, se ne può fissare la lunghezza, oppure richiedere che essa
contenga esclusivamente determinati caratteri. Componendo questi costrutti è
possibile definire regole complesse, in grado di individuare famiglie
articolate di stringhe &mdash; come tutti gli indirizzi di posta elettronica in
un certo dominio, o tutte le password di almeno dieci caratteri che contengono
una cifra e caratteri sia minuscoli che maiuscoli. Tipicamente, data una
specifica espressione regolare, si vuole valutare se una stringa la soddisfi
oppure no, o estrarre tutte le sue sottostringhe che la rispettano.

Il modulo `re` permette di utilizzare le espressioni regolari in Python,
definendole tramite una sintassi che fa ampio uso dei caratteri di
_backslash_. Per esempio, `\d` indica una cifra e `+` descrive una sequenza di
una o più occorrenze della regola precedente, così che `\d+` corrisponde a una
sequenza di una o più cifre, e dunque a una stringa che rappresenta un numero
intero. La funzione `compile`, definita nel modulo, restituisce un oggetto che
rappresenta un’espressione regolare $s$, costruita a partire da una stringa che
ne descrive la sintassi. Su questo oggetto si possono invocare vari metodi,
come ad esempio `findall`, che accetta una stringa e ne estrae tutte le
sottostringhe che soddisfano $s$. Per esempio, il codice seguente elenca tutti
i numeri che compaiono in una descrizione dei superpoteri di Elastigirl, tratta
dalla relativa pagina su [Wikipedia](https://it.wikipedia.org/wiki/Helen_Parr):

```{interactive-code} python
import re

s = "Il superpotere principale di Elastigirl è l'elasticità, che le "
s += "consente di allungare varie parti del suo corpo fino a 300 piedi "
s += "(90 metri) e può essere sottile 1 millimetro."

p = re.compile(r'\d+')
p.findall(s)
```

Dovreste notare qualcosa di nuovo nel valore restituito dal metodo `findall`:
si tratta di un dato strutturato che aggrega le varie occorrenze individuate
nella stringa di partenza. Studieremo tra breve anche il tipo corrispondente,
nel Paragrafo {ref}`sec_liste`.
````

(sec_f-string)=
### Letterali stringa formattati
Abbiamo visto che è possibile stampare un output mescolando stringhe fisse
e contenuti di variabili, semplicemente passandoli come argomenti alla funzione
`print`.

```{code-cell} python
name = 'Brainiac'
month = 'luglio'
year = 1958
magazine = 'Action Comics'
num = 242
print(name, 'ha debuttato nel numero', num, 'di', magazine, 'nel', month, year)
```

```{margin}
Notate che `print` costruisce il suo output inserendo automaticamente uno
spazio tra ognuna delle stringhe passate come argomento.
```
È importante sottolineare che in molti linguaggi di programmazione
l'equivalente della funzione `print` accetta un unico argomento, e per stampare
un output analogo a quello precedente si segue un _pattern_ preciso: si
utilizza l'operatore di concatenazione delle stringhe, che in alcuni casi
_promuove_ automaticamente gli operandi che non sono di tipo stringa. Python,
invece, effettua un _type checking_ di tipo forte, il che significa che non
ammette conversioni implicite: la concatenazione può avvenire solo tra due o
più stringhe. Pertanto, per applicare il _pattern_ appena descritto sarebbe
necessario convertire esplicitamente in stringa tutti gli operandi che non sono
già di questo tipo, pena l'emissione di un'eccezione. Ciò renderebbe il codice
inutilmente complesso, ed è per questo motivo che `print` accetta più
argomenti.

```{code-cell} python
print(f'{name} ha debuttato nel numero {num} di {magazine} nel {month} {year}')
```

Nella pratica comune, tuttavia, quando si desidera generare un output complesso
che combini stringhe fisse con il contenuto di variabili, si preferisce
produrre un _output formattato_. In Python ciò può essere fatto in tre modi:
utilizzando l'operatore `%`, invocando il metodo `format` su una stringa oppure
ricorrendo ai _letterali stringa formattati_. Sebbene le prime due modalità
siano tuttora disponibili, l'ultima &mdash; introdotta più di recente &mdash; è
quella che fornisce più controllo sul risultato finale e, al tempo stesso,
semplifica il codice. Un letterale stringa formattato si riconosce perché il
suo delimitatore iniziale è preceduto da un carattere `f`. Al suo interno è
possibile inserire arbitrarie espressioni Python racchiuse tra parentesi
graffe: durante l'esecuzione, tali espressioni vengono valutate e il loro
risultato è inserito nel punto della stringa che corrisponde a queste parentesi
quadre.

```{code-cell} python
print(f'{name} ha debuttato nel numero {num} di {magazine} nel {month} {year}')
```

Il vantaggio principale dei letterali formattati &mdash; indicati nella
terminologia inglese, per brevità, come _f-string_ &mdash; consiste nella
possibilità di controllare con precisione la quantità di spazi da inserire tra
le varie stringhe ed espressioni che vengono concatenate in modo implicito.
Per esempio, terminare la stringa nell'ultima cella con un punto è immediato,
mentre ottenere lo stesso risultato nella cella precedente richiede un po’ di
attenzione. Inoltre, le _f-string_ consentono di specificare con notevole
precisione il modo in cui i valori devono essere visualizzati, grazie a un
_mini linguaggio_ che definisce alcune regole di formattazione.  
Più precisamente, prima di chiudere le parentesi graffe è possibile inserire
un carattere di due punti e indicare il tipo di valore mostrato e la modalità
di visualizzazione. Per esempio, nella seguente:

```{code-cell} python
a = 0.1
b = 0.2
print(f'{a+b:.1f}')
```

l’espressione `.1f` indica che il valore calcolato è di tipo `float` e deve
essere mostrato usando una sola cifra decimale dopo la virgola.  
Una versione semplificata della sintassi utilizzata per specificare il formato
di visualizzazione di un valore è la seguente:

`[[fill]align][sign][width][,|_][.precision][type]`

dove:

- `fill` è il carattere utilizzato per assicurare che l'espressione occupi un
  determinato numero di caratteri (per _default_, uno spazio);
- `align` definisce l’allineamento del valore: `<`, `>`, `^` e `=` indicano,
  rispettivamente, l’allineamento a sinistra, a destra, centrato e quello in
  cui il segno è a sinistra e il valore a destra (valido solo per numeri);
- `sign` specifica come rappresentare l’eventuale segno: `+` lo mostra sempre,
  anche per i numeri positivi; `-` lo mostra solo per i negativi; `␣`
  visualizza uno spazio per i numeri positivi e `-` per quelli negativi, in
  modo da mantenere un corretto allineamento verticale;
- `width` imposta la numero totale di caratteri da utilizzare per la
  visualizzazione;
- `,` o `_` indicano il carattere da usare per separare i gruppi di tre cifre
  nei valori numerici;
- `precision` definisce il numero di cifre decimali (per i `float`) o di
  caratteri (per le stringhe) da mostrare;
- `type` specifica la modalità di rappresentazione del valore, scegliendo uno
  dei caratteri elencati nella {numref}`tab_tipi-formattazione`.

La sintassi completa del mini linguaggio di formattazione è leggermente più
complessa, ed è descritta in dettaglio nella
[documentazione ufficiale](https://docs.python.org/3/library/string.html#format-specification-mini-language).


```{table} Modalità di formattazione dei letterali stringa (f-string) e relativi simboli
:name: tab_tipi-formattazione
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

(sec_liste)=
## Le liste

Le liste sono strutture dati dinamiche ad accesso posizionale, utilizzate per
memorizzare sequenze di riferimenti a oggetti di tipo eterogeneo. Quando una
lista contiene pochi elementi, è pratico definirla in modo _estensivo_,
racchiudendo tra parentesi quadre l’elenco dei suoi elementi, indicati
nell’ordine desiderato e separati da virgole. Il risultato è un letterale di
tipo `list`, cioè un’istanza della classe che in Python implementa le liste.
Per esempio, la lista che contiene i primi quattro quadrati perfetti, partendo
da zero, corrisponde al letterale `[0, 1, 4, 9]`, mentre quella composta dai
nomi dei membri fondatori della _Justice League_ nella sua formazione originale
si può esprimere come `['Superman', 'Batman', 'Wonder Woman', 'Flash', 'Green
Lantern', 'Aquaman', 'Martian Manhunter']`. Analogamente, `[]` indica la lista
vuota.

Vale la pena sottolineare che quello che viene memorizzato in una lista sono
solamente i riferimenti agli oggetti, e non gli oggetti stessi. Pertanto, il
letterale `[0, 1, 4, 9]` corrisponde a una lista che nella prima posizione
contiene il riferimento a un oggetto `int` che corrisponde a zero, nella
seconda contiene il riferimento a un altro oggetto `int`, e così via, come
illustrato nella {numref}`fig-list_behavior`. Ciascuno di questi oggetti
risulterà memorizzato in una porzione di memoria diversa da quella dedicata
alla lista. Anche se tecnicamente sarebbe più corretto parlare di «liste di
riferimenti a oggetti», per semplicità &mdash; o anche solo per evitare di
appesantire il discorso &mdash; si parla comunemente di «liste di oggetti» o
«liste di valori», e anche io quasi sempre utilizzerò questa dicitura
sempliicata.

````{customfigure}
:name: fig-list_behavior

```{mermaid}
graph LR
    subgraph lista[" "]
        direction LR
        A0["l[0]"]
        A1["l[1]"]
        A2["l[2]"]
        A3["l[3]"]
    end

    A0 --> B0["0"]
    A1 --> B1["1"]
    A2 --> B2["4"]
    A3 --> B3["9"]

    l --> lista

    classDef list fill:#fff8e1,stroke:#ffb300,stroke-width:2px,color:#333;
    classDef obj fill:#e3f2fd,stroke:#1e88e5,stroke-width:2px,color:#333;
    class A0,A1,A2,A3 list;
    class B0,B1,B2,B3 obj;

```

Rappresentazione grafica dei riferimenti contenuti nella lista.
`l = [0, 1, 4, 9]`.
````

```{admonition} Nomenclatura
:class: naming

Il termine «lista» può trarre in inganno. In informatica viene spesso usato
come abbreviazione di «lista collegata» (traduzione dall'inglese «linked
list»), che è una struttura dati ben precisa. Nella sua forma più semplice,
ogni elemento è collegato a quello successivo, e per accedere a una specifica
posizione bisogna attraversare la struttura, partendo dall'inizio e passando
per tutte le posizioni precedenti. Questo implica che il tempo di accesso ai
contenuti non sono costanti: gli elementi alla fine della lista richiedono più
tempo rispetto a quelli iniziali. D'altro canto, questo tipo di organizzazione
facilita altri tipi di operazioni, come l'inserimento o la cancellazione di un
elemento.

Le specifiche di Python non impongono alcuna rappresentazione interna per gli
oggetti di tipo `list`. Nella pratica, però, tutte le principali
implementazioni adottano una soluzione completamente diversa da quella delle
liste collegate: i riferimenti agli oggetti sono memorizzati in un _array_
dinamico, cioè un’area di memoria contigua che può essere ampliata o ridotta
quando necessario. Questo approccio consente un tempo di accesso costante agli
elementi.

È comunque importante ricordare che una lista in Python non è un _array_ nel
senso tradizionale del termine: infatti, può contenere oggetti eterogenei e
cresce o si restringe a seconda delle operazioni svolte. Si tratta quindi di
una struttura più flessibile rispetto agli array statici di molti altri
linguaggi.

```

```{margin}
In questo caso, «parola» va inteso in senso lato come sequenza massimale di
caratteri preceduta e seguita da uno o più caratteri di spazio.
```
L'approccio estensivo tende a diventare poco pratico per liste che contengono
più di una decina di elementi. In questi casi le liste vengono costruite
dinamicamente, ad esempio usando un ciclo che genera gli elementi uno alla
volta e li aggiunge via via alla lista. Esiste poi la possibilità di creare
liste invocando metodi o funzioni: per esempio il metodo `split`, invocato su
una stringa, restituisce la lista delle parole in essa contenute.

Vi è poi un terzo modo di procedere, che se ben congegnato risulta più
efficiente rispetto all'uso esplicito di cicli: la _list comprehension_.
Fondamentalmente, applica una trasformazione a tutti gli elementi di una
struttura di partenza e raccoglie i risultati in una nuova lista. In un certo
senso, opera un approccio _intensivo_, perché si basa sulla specificazione di
una proprietà che caratterizza gli elementi della lista risultante. Nella sua
forma più semplice, la sintassi per introdurre una _list comprehension_ è
`[f(e) for e in l]`, dove`f(e)` è un’espressione nella quale occorre la
variabile muta `e`, mentre `l` è la struttura di partenza. Durante la
valutazione della _comprehension_, `l` viene attraversata generando tutti i
suoi elementi; ciascuno, a turno, viene temporaneamente referenziato da `e`,
così che risulta possibile valutare `f(e)`. I risultati ottenuti vengono
raccolti in una nuova lista, mantenendo l’ordine nel quale sono stati generati.
In altre parole, il primo elemento della lista è il risultato dell’applicazione
di `f` al primo elemento di `l` che è stato considerato, il secondo è
il risultato di `f` sul secondo elemento, e così via. Se la struttura di
partenza è una lista, questa verrà attraversata dalla prima alla ultima
posizione, e quindi gli elementi di `l` e quelli del risultato ottenuto saranno
allineati. Per esempio, la lista dei primi quattro quadrati perfetti
può essere espressa anche come:

```{margin}
Quando una lista contiene dati omogenei, è sempre opportuno valutare di
sostituirla con un _array_, per diminuire i tempi di esecuzione e ridurre il
rischio di introdurre _bug_ nel codice.
```

```{code-cell} python
[i**2 for i in range(4)]
```

In una _list comprehension_ è possibile non solo trasformare gli elementi di
una struttura, ma anche scartarne una parte, selezionando solo quelli che
soddisfano una certa condizione. La sintassi estesa `[f(e) for e in l if g(e)]`
indica che un elemento `e` della struttura `l` viene considerato (e
trasformato) se e solo se l’espressione logica `g(e)` risulta vera. Pertanto

```{code-cell} python
[i for i in range(1, 6) if i % 2 == 1]
```

genera la lista dei primi tre numeri dispari.

````{admonition} Range
In alcuni degli esempi fatti finora, ho usato `range` per costruire sequenze di
numeri interi equispaziati tra due estremi definiti. Più precisamente, dati tre
valori interi memorizzati in `m`, `n` e `s`:

- `range(m)` individua la sequenza degli interi da zero a `m − 1`;  
- `range(m, n)` rappresenta la sequenza degli interi da `m` a `n − 1`;  
- `range(m, n, s)` indica la sequenza ottenuta partendo da `m` e applicando
  successivi incrementi di `s` unità, fino al primo valore che non supera `n`.

Nelle prime versioni di Python, `range` era una funzione che restituiva la
lista contenente tutti gli elementi della sequenza generata. Questo approccio
risultava tuttavia potenzialmente impraticabile per lavorare con sequenze molto
lunghe. E poteva anche risultare particolarmente inefficiente: era questo il
caso delle sequenze numeriche generate con il solo scopo di iterarvi sopra.
Infatti, per eseguire questo compito è sufficiente mantenere in memoria
soltanto il valore corrente della sequenza, l'incremento e il limite superiore.
A partire da Python 3, `range` è diventata una classe, i cui oggetti
rappresentano le sequenze stesse e ne implementano la generazione nel modo
_pigro_ appena descritto (si parla, in casi come questi, di _lazy evaluation_).
Gli oggetti restituiti da `range` si comportano come sequenze iterabili, e
possono essere utilizzati nei cicli for o nelle _list comprehension_ in modo
estremamente efficiente.
````

```{margin}
In seguito vedremo modi più strutturati e leggibili per codificare un _record_,
ad esempio tramite dizionari o _named tuple_.
```
L’eterogeneità delle liste consente di usarle anche per rappresentare un
_record_, cioè un'aggregazione di informazioni che descrive un’entità
complessa, come ad esempio un supereroe nel codice qui di seguito.

```{code-cell} python
iron_man = ['Iron Man', 'Anthony Edward Stark', 'Tony Stark', 'Good',
            'Long Island, New York',  'Marvel Comics',
            'Earth-616 - Prime Marvel Universe', 1963, 'Blue', 'Black',
            198.1,  192.8,  100,  'High',  100,  85,  80,  90]
```

L’operatore di accesso alle liste segue la stessa semantica già vista per le
stringhe: tra parentesi quadre si specifica una posizione, che individua un
elemento della sequenza (più precisamente, il riferimento a quell’oggetto),
oppure uno _slicing_ per ottenere una sotto-sequenza. 

````{prf:example}
:label: ex-list

Se consideriamo la lista memorizzata in `iron_man`, valutando le espressioni
`iron_man[2]` e `iron_man[-2]` si ottengono rispettivamente il terzo e il
penultimo dei valori presenti nella lista, ossia la stringa 'Tony Stark' e
l'intero `80`. Allo stesso modo, si può estrarre la sotto-lista che contiene i
colori di occhi e capelli usando uno _slicing_ come nella cella che segue.

```{interactive-code} python
:height: 0px
:class: no-output

iron_man = ['Iron Man', 'Anthony Edward Stark', 'Tony Stark', 'Good',
            'Long Island, New York',  'Marvel Comics',
            'Earth-616 - Prime Marvel Universe', 1963, 'Blue', 'Black',
            198.1,  192.8,  100,  'High',  100,  85,  80,  90]
```

```{interactive-code} python
iron_man[8:10]
```
````

Specificare la posizione del primo elemento da escludere può sembrare
controintuitivo rispetto all’approccio, apparentemente più naturale, di
indicare l’ultimo elemento da includere. In realtà, questa scelta rende più
semplice scrivere codice che elabora porzioni successive di una lista in modo
ordinato ed efficiente.

Sono disponibili diverse operazioni che agiscono sulle liste, implementate
tramite elementi distinti del linguaggio: operatori, funzioni e metodi.
Di seguito, senza alcuna pretesa di completezza, introduco alcuni esempi
basandomi sulla seguente lista che contiene i nomi di alcuni supereroi.

```{code-cell} python
names = ['Aquaman', 'Ant-Man', 'Batman', 'Black Widow',
         'Captain America', 'Daredevil', 'Elektra', 'Flash',
         'Green Arrow', 'Human Torch', 'Hancock', 'Iron Man',
         'Mystique', 'Professor X', 'Rogue', 'Superman',
         'Spider-Man', 'Thor', 'Northstar']
```

Come già indicato in precedenza, la funzione `len` può essere utilizzata per
calcolare la lunghezza di un oggetto: nel caso delle liste, tale valore
corrisponde al numero di elementi contenuti.

```{code-cell} python
len(names)
```

Alcuni degli operatori descritti nel {ref}`sec_dati-semplici` mantengono la
stessa semantica anche quando vengono applicati a delle liste. Per esempio,
`==` consente di verificare se due liste contengano gli stessi
elementi, nel medesimo ordine. Altri operatori, invece, assumono un significato
diverso. In particolare:

- L’operatore `+` consente di concatenare due liste, creando una nuova lista
  che contiene tutti gli elementi della prima seguiti da quelli
  della seconda, lasciando inalterato il loro ordine;
- L’operatore `*` permette di concatenare una lista con se stessa più volte;
  più precisamente, se `l` e `n` sono rispettivamente una lista e un intero, `l
  * n` e `n * l` producono una nuova lista formata da `n` ripetizioni dei
  contenuti di `l`, sempre mantenendone l'ordine.

```{margin}
Vedremo che `in` e `del` mantengono la loro semantica anche quando vengono
usati con altri tipi di strutture dati.
```

Sempre nel {ref}`sec_dati-semplici` ho introdotto gli operatori `in` e `del`,
che si applicano in modo naturale anche alle liste. Il primo implementa la
relazione di appartenenza: se `e` è un’espressione e `l` una lista,
l’espressione `e in l` viene valutata come logicamente vera se il valore
dell’espressione occorre in una qualunque posizione della lista, e come
logicamente falsa altrimenti:

```{code-cell} python
print('Thing' in names)
print('Human Torch' in names)
```

L’operatore `del` consente invece di eliminare un riferimento da una lista
specificandone la posizione. Per esempio, eseguendo la cella seguente viene
eliminato dalla lista memorizzata in `names` il riferimento contenuto nella
sua prima posizione:

```{code-cell} python
del names[0]
```

Va sottolineato che `del` è un operatore dal comportamento peculiare, in quanto
non restituisce alcun valore; la sua esecuzione ha però l’_effetto collaterale_
di eliminare il riferimento nella posizione specificata della lista usata come
operando [^del-behaviour]. Come conseguenza di questo effetto collaterale,
nell’esempio precedente viene eliminato il primo elemento della lista, così che
quello che prima era il secondo elemento diventa ora il primo, e così via, come
si può facilmente verificare:

```{code-cell} python
names[0]
```

```{admonition} Nota
:class: note
In realtà `del` è un operatore che può essere applicato a una vasta gamma di
operandi e che consente di eliminare un riferimento a un oggetto. Se dopo
questa operazione non esistono più riferimenti che puntano all’oggetto,
questo verrà rimosso dalla memoria, liberando spazio[^garbage-collector]. Il
fatto che la maggior parte delle componenti di Python accessibili durante
l’esecuzione di un programma siano, in modo più o meno esplicito, associate a
degli oggetti, rende possibile eliminare non solo variabili o parti di
strutture dati, ma anche altri elementi del linguaggio che vedremo più avanti,
come funzioni e moduli.
```








Infine, è possibile usare oggetti della classe `list` invocando su di essi dei
metodi. Prendiamo ad esempio `sort`, che permette di ordinare gli elementi
sulla base di una relazione predefinita. Per quanto riguarda le stringhe,
questa relazione corrisponde all'_ordine lessicografico_, che è una
generalizzazione dell'ordine alfabetico a parole su un qualsiasi alfabeto di
simboli ordinati. In Python, la comparazione tra due stringhe viene fatta
scandendole da da sinistra verso destra, fermandosi alla prima posizione in cui
si trovano due caratteri diversi, che vengono confrontati secondo la loro
codifica Unicode: quello che ha un codice più basso individua la stringa «più
piccola». Se una stringa è un prefisso dell'altra, allora «viene prima»
nell'ordine. Supponiamo per esempio di voler mettere in ordine i nomi dei
supereroi contenuti in `names` (la lista è quasi in ordine, l'unico elemento
fuori posto è l'ultimo): uno dei modi in cui è possibile eseguire questa
operazione è quella di invocare sulla lista il metodo `sort`.

```{code-cell} python
names.sort()
```

Così come l'operatore `del`, questo metodo non restituisce alcun valore, in
quanto l'ordinamento è eseguito _in place_ [^sorted]: l'invocazione di `sort`
ha come effetto collaterale il riposizionamento degli elementi all'interno
della lista in modo da riflettere l'ordinamento [^ordinamento-eterogeneo].
Possiamo convincercene facilmente visualizzando per esempio gli ultimi cinque
elementi di `names`:

```{code-cell} python
names[-5:]
```

In Python è possibile specificare valori per argomenti _opzionali_ quando si
invoca un metodo (o, come vedremo più avanti, una funzione): si tratta di
argomenti identificati da un nome, che _possono_ essere omessi, e in tal caso
assumono un valore predefinito [^argomenti-opzionali]. Per poter specificare un
valore diverso da quello predefinito è necessario indicare, dopo _tutti_ gli
eventuali argomenti non opzionali, un'espressione del tipo `<nome>=<valore>`,
dove `<nome>` indica il nome dell'argomento opzionale in questione e `<valore>`
è il relativo valore. Per esempio, l'argomento opzionale `reversed` del metodo
`sort` permette di invertire il verso dell'ordinamento:

```{code-cell} python
names.sort(reverse=True)
```

Un'altra caratteristica di Python è quella di poter specificare una funzione
come argomento di un metodo (o di un'altra funzione) [^first-class]; ciò si può
fare indicando il nome della funzione, oppure usando una _funzione anonima_
(vedi il Paragrafo {ref}`sec_funzioni-anonime`). Esemplifico anche questa
caratteristica usando il metodo `sort`: il suo argomento opzionale `key`
permette di specificare criteri alternativi per eseguire l'ordinamento,
indicando una funzione che trasforma gli elementi della lista in quantità
numeriche su cui basare l'ordinamento (nel senso che elementi trasformati in
numeri più bassi compariranno prima nella lista ordinata rispetto ad altri
elementi trasformati in numeri più alti). Nell'invocazione seguente

```{code-cell} python
names.sort(key=len)
```

l'ordinamento viene fatto:

- associando il nome di ogni supereroe nella lista alla sua lunghezza,
- ordinando le coppie ottenute in base a questa lunghezza,
- considerando solo i nomi, mantenendo questo nuovo ordinamento,

che corrisponde a riordinare i nomi dal più breve al più lungo, come si
può facilmente verificare:

```{code-cell} python
names
```

Nel caso in cui si volessero specificare due o più argomenti opzionali, basta
separarli usando le virgole esattamente come si procede per gli argomenti non
opzionali. Per esempio

```{code-cell} python
names.sort(key=lambda n:len(n), reverse=True)
```

riordina le stringhe contenute in `names` dalla più lunga alla più corta. Va
anche notato che essendo gli argomenti opzionali univocamente individuati dal
loro nome, non è necessario specificarli seguendo un ordine prefissato:
pertanto si potrebbero scambiare le posizioni di `key` e `reverse`
nell'invocazione precedente senza modificare la semantica dell'istruzione.

Per degli approfondimenti è possibile
consultare la documentazione ufficiale, che contiene un [documento
introduttivo](https://docs.python.org/3/tutorial/introduction.html#lists) e uno
[più dettagliato](https://docs.python.org/3/tutorial/datastructures.html#)
sull'uso delle liste.

(sec_tuple)=
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

```{code-cell} python
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

L'accesso a un elemento di una tupla viene fatto in modo posizionale usando la
medesima sintassi introdotta per le liste, e anche in questo caso è possibile
estrarre delle sotto-tuple utilizzando degli _slicing_. Quando però si tenta di
modificare un elemento contenuto in una tupla, l'esecuzione verrà bloccata
emettendo un errore:

```{code-cell} python
:tags: [raises-exception]

rogue[-2] = 70
```

A seguito di questo errore, la tupla manterrà i suoi valori originali, restando
quindi effettivamente invariata:

```{code-cell} python
rogue
```

Una tupla può essere utilizzata facendo ri ferimento agli stessi operatori e
alle stesse funzioni messi a disposizione per le liste (come per esempio `in` e
`len`), escludendo ovviamente le operazioni che modificano la tupla stessa
(come `sort`).

L'immutabilità delle tuple le rende da preferire rispetto alle liste in tutti i
casi in cui si vuole impedire che dei dati vengano modificati, per esempio a
causa di un bug; inoltre la loro elaborazione è in molti casi più efficiente di
quella delle liste.

(sec_array)=
## Gli array
Un _array_, o vettore, è una struttura dati statica ad accesso posizionale che
permette di memorizzare una sequenza di valori omogenei.

(sec_insiemi)=
## Gli insiemi
Python implementa direttamente un tipo di dato per gli insiemi, intesi come
collezione finita di elementi tra loro distinguibili e non memorizzati in un
ordine particolare. A differenza delle liste e delle tuple, gli elementi non
sono quindi associati a una posizione e non è possibile che un insieme contenga
più di un'istanza di un medesimo elemento. La descrizione di questo tipo di
dato è posticipata al {ref}`sec_insiemi-in-python`, dopo avere richiamato le
proprietà matematiche di base degli insiemi.


(sec_dizionari)=
##  I dizionari
I dizionari servono a memorizzare delle associazioni tra oggetti, in analogia
con il concetto matematico di funzione. È quindi possibile pensare a essi come
a insiemi di coppie (chiave, valore), dove una data chiave non occorre più di
una volta, e a ogni chiave corrisponde un unico valore.

Un letterale di tipo dizionario viene descritto indicando ogni coppia separando
chiave e valore con il carattere di due punti, separando le coppie con delle
virgole e racchiudendo l'intero letterale tra parentesi graffe. Possiamo per
esempio usare un dizionario per rappresentare un _record_ in modo più elegante
rispetto a quanto fatto nel Paragrafo {ref}`sec_liste` utilizzando le liste:

```{code-cell} python
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

L'accesso, in lettura o scrittura, agli elementi di un dizionario viene fatto
con una notazione che ricorda quella di liste e tuple: si specifica all'interno
di parentesi quadre la chiave per ottenere o modificare il valore
corrispondente:

```{code-cell} python
rogue['identity']
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
l'argomento più generale dei _design pattern_ {cite:p}`gang-of-four`, che
descrivono degli schemi decisamente più complessi di quelli che descrivono
codice idiomatico, e che si possono implementare usando diversi linguaggi di
programmazione. Sono esempi di _design pattern_ i singoletti, i _flyweight_ e i
metodi fabbrica ai quali ho precedentemente accennato.

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
Dijkstra (già citato in una nota precedente nota) descrive i suoi vantaggi.

[^substring]: Dover specificare la posizione del primo carattere da
escludere sembra controintuitivo rispetto a indicare la posizione dell'ultimo
carattere nella sottostringa. In realtà in questo modo risulta più facile
scrivere codice che elabora porzioni successive in una stringa.

[^escape_numeric]: Oltre ad altre sequenze standard di _escaping_ che sono
generalmente utilizzate poco o per nulla, è possibile fare seguire il carattere
di _backslash_ dalla codifica numerica di un carattere qualsiasi,
opportunamente espressa in ottale o esadecimale, così come dal suo nome
simbolico nella codifica Unicode. Per una descrizione più precisa, si può fare
riferimento alla parte della [documentazione
ufficiale](https://docs.python.org/3/reference/lexical_analysis.html#escape-sequences)
che descrive in dettaglio le sequenze di _escaping_.

[^ottanta]: Una delle regole di stile documentate nella PEP 8 raccomanda che la
lunghezza delle righe di codice non ecceda questo limite, così da garantirne
una visualizzazione leggibile nelle finestre di un terminale, la cui larghezza
predefinita è, appunto, di ottanta colonne. Questo accorgimento facilita anche
il confronto tra due file di codice, visualizzandoli in terminali distinti o
affiancandoli in un IDE. Io aderisco a questa convenzione, ma va detto che non
esiste un consenso unanime tra gli sviluppatori: i moderni monitor permettono
infatti di visualizzare e affiancare terminali con righe più lunghe senza
compromettere la chiarezza. In molti progetti si adottano quindi soglie più
flessibili &mdash; ad esempio 100 o 120 caratteri &mdash; mantenendo però
l’obiettivo generale di favorire la leggibilità.

[^del-behaviour]: I lettori attenti potrebbero avere notato un apparente
incoerenza tra il modo in cui vengono valutate le espressioni e la semantica
appena introdotta per l'operatore `del`. Consideriamo l'espressione `del
names[0]` dell'esempio precedente: se questa fosse valutata in modo ususale,
verrebbe innanzitutto valutato l'operando, dunque l'espressione `names[0]`.
L'operatore `del` verrebbe quindi applicato al valore ottenuto, che nel nostro
caso sarebbe la stringa `'Aquaman'`. Ora, l'istruzione `del 'Aquaman'`
genererebbe un errore, perché `del` si può applicare solo a riferimenti e non a
letterali. In realtà la valutazione di espressioni di questo tipo viene fatta
in un modo diverso: a causa del Python data model descritto in una nota
precedente, `del names[0]` viene implicitamente convertita nell'espressione
`names.__delitem__(0)`.

[^garbage-collector]: La gestione della memoria, e in particolare il modo in
cui questa viene liberata quando è occupata da oggetti non più utilizzati,
è un argomento decisamente complesso. Il comportamento descritto finora è
legato all'implementazione CPython del linguaggio e non garantisce sempre
la liberazione immediata della memoria inutilizzata. Per esempio, quando
due oggetti contengono ciascuno un riferimento all'altro, la tecnica basata
sul conteggio dei riferimenti non è più sufficiente. In questi casi
interviene un componente particolare dell'interprete Python, chiamato
_garbage collector_, che viene eseguito periodicamente per rilevare e
deallocare automaticamente gli oggetti ciclici, ossia quegli oggetti che si
riferiscono tra loro ma non sono più raggiungibili dal resto del programma.
Questo meccanismo garantisce che la memoria venga recuperata anche in
situazioni in cui il semplice conteggio dei riferimenti fallirebbe.

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
queste opzioni venga usata sempre nello stesso modo, modificandone al più un
numero molto basso. Si pensi al caso della produzione di grafici: sebbene in teoria sia
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



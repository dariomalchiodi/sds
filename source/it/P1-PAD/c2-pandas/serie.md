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

(sec:serie)=
# Serie

Una delle classi principali implementate in pandas è `Series`. Le sue istanze
rappresentano serie di osservazioni di un certo carattere fatto su un insieme
di individui. La cella seguente recupera dalla lista `heroes` precedentemente
creata i nomi dei supereroi e il loro anno di prima apparizione e li utilizza
per creare una serie:

```{code-block} python
import csv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

with open('data/heroes.csv', 'r') as heroes_file:
  heroes_reader = csv.reader(heroes_file, quotechar='"')
  heroes = list(heroes_reader)[1:]

years = [int(h[7]) if h[7] else None for h in heroes]
names = [h[0] for h in heroes]
first_appearance = pd.Series(years, index = names)
```

Nella creazione della lista `year` è stata utilizzata una list comprehension in
cui l'espressione `int(h[7]) if h[7] else None` utilizza un operatore ternario
tramite cui la stringa vuota viene trasformata nel valore speciale `None`,
mentre tutte le altre vengono convertite nel corrispondente intero.

La differenza tra una serie e una lista o una tupla è legata alla possibilità
di invocare su di essa delle funzioni specifiche. Inoltre a ogni serie è
associato un *indice* che permette di identificare ogni elemento osservato.
Nell'esempio sopra riportato, il primo argomento specificato nel costruttore è
una lista (ma sarebbe andata bene anche una tupla) di anni che indicano la
prima apparizione di un supereroe e il secondo rappresenta appunto l'indice,
che in questo caso è la lista dei corrispondenti nomi. Quando si visualizza
una serie, ogni osservazione viene associata al corrispondente elemento usando
appunto l'indice:

```{code-block} python
first_appearance
```

La visualizzazione della serie (che in questo caso riporta solo i primi e gli
ultimi elementi perché la serie è troppo lunga) termina indicando il tipo di
dato usato per rappresentare le varie osservazioni. Nell'esempio precedente
viene utilizzato il tipo `float64` (pandas utilizza internamente gli array di
numpy, in cui è presente un'implementazione dei tipi in virgola mobile diversa
da quella standard di python), nonostante i dati originari fossero numeri
interi. Ciò è dovuto alla presenza di valori mancanti. Di norma vengono
indicati con la sigla NA (dall'inglese "not available"), ma in pandas essi
vengono rappresentati utilizzando il concetto di "not a number" dello standard
IEEE per la virgola mobile: si noti come tutte le occorrenze di `None` nella
lista originale siano state automaticamente convertite in `np.nan`.

L'accesso ai dati contenuti in una serie può avvenire in due modi:
- specificando un valore per l'indice tra parentesi quadre dopo la serie o dopo
  la sua proprietà `loc`:

```{code-block} python
(first_appearance['Wonder Woman'], first_appearance.loc['Wonder Woman'])
```

- indicando un valore per la posizione tra parentesi quadre dopo la serie o
  dopo la sua proprietà `iloc`:

```{code-block} python
(first_appearance[128], first_appearance.iloc[128])
```

```{admonition} Nomenclatura
:class: naming
Se l'indice di una serie è basato su valori interi, i valori tra parentesi
quadre immediatamente dopo la serie faranno riferimento all'indice e non alla
posizione: ciò potrebbe essere fuorviante se gli elementi dell'indice non
partono da zero e non sono consecutivi.
```


È inoltre possibile utilizzare una notazione simile al _list slicing_
specificando valori dell'indice oppure posizioni. Va però notato che gli
_slicing_ basati su indice comprenderanno il primo e l'ultimo valore
specificato:

```{code-block} python
first_appearance['Wonder Girl':'Wonder Woman']
```

mentre gli _slice_ basati su posizione escluderanno l'ultimo elemento:

```{code-block} python
first_appearance[60:63]
```

L'accesso posizionale può anche fare riferimento a numeri negativi, contando in
analogia a liste e tuple a partire dall'ultimo elemento:

```{code-block} python
first_appearance[-5:]
```

È possibile accedere ai primi e ultimi elementi di una serie anche utilizzando
le funzioni `head` e `tail`, che mostrano rispettivamente solo le prime e le
ultime righe:

```{code-block} python
first_appearance.head(7)
```

L'accesso alle liste può anche essere fatto specificando una lista (ma non una
tupla) di posizioni al posto di una sola posizione, con l'effetto di ottenere i
corrispondenti elementi.

```{code-block} python
first_appearance[[1, 42, 709]]
```

Questo tipo di accesso può essere fatto anche specificando una lista di valori
per l'indice. Infine, si può utilizzare una lista di valori booleani in cui
`True` indica gli elementi da estrarre e `False` quelli da filtrare:

```{code-block} python
first_appearance[[1970 <= y <1975 for y in first_appearance]]
```

```{admonition} Nomenclatura
:class: naming
L'uso di questa modalità di accesso richiede che la lista di valori booleani
abbia la stessa lunghezza della serie. L'uso di liste di dimensioni minori
l'accesso, che comporta un filtraggio effettuato solo nei primi elementi della
serie, è deprecato e va quindi evitato.  
```

Infine, è possibile effettuare delle _query_ su una serie specificando tra
parentesi quadre un'espressione logica che indica quali elementi visualizzare,
utilizzando la serie come simbolo che ne indica un suo generico elemento:

```{code-block} python
first_appearance[first_appearance > 2010]
```

```{admonition} Nomenclatura
:class: naming
Tecnicamente, l'espressione `first_appearance > 2010` genera una nuova serie
che ha lo stesso indice di `first_appearance` e in cui i valori sono `True` in
corrispondenza degli anni successivi al 2010 e `False` altrimenti. Questa nuova
serie viene utilizzata per filtrare `first_appearance`.
```

Vediamo ora come utilizzando le serie sia molto più semplice calcolare e
visualizzare le frequenze assolute: il metodo `value_counts` restituisce
un'altra serie in cui gli indici sono i valori osservati e i valori le
corrispondenti frequenze assolute, ordinate in senso non crescente.

```{code-block} python
first_appearance.value_counts()
```

Va notato come il tipo delle frequenze sia, correttamente, intero e come i
valori mancanti siano automaticamente esclusi dal calcolo delle frequenze,
mentre sono sempre presenti gli _outlier_.  Per ottenere una serie i cui
elementi siano ordinati per valore non decrescente della voce nell'indice è
sufficiente invocare il metodo `sort_index`; già che ci siamo, è un buon
momento per eliminare i valori fuori scala dal conteggio effettuando una
_query_ sulla serie:

```{code-block} python
first_app_freq = first_appearance[first_appearance < 2090].value_counts().sort_index()
first_app_freq.head(10)
```

## Visualizzazione grafica di una serie
Pandas mette a disposizione l'oggetto `plot` per visualizzare graficamente i
contenuti di una serie, utilizzando matplotlib dietro le quinte; in
particolare, il metodo `bar` visualizza un grafico a barre:

```{code-block} python
# Don't try this at home (men che meno all'esame!)

first_appearance.plot.bar()
plt.show()
```

Il grafico ottenuto, diciamolo, fa schifo. Questo perché `bar` considera un
punto per ogni elemento della serie, in cui le ascisse corrispondono alla
posizione (zero per la prima osservazione, uno per la seconda e così via,
sebbene nel grafico sull'asse delle ascisse vengano poi visualizzati i valori
dell'indice) e le ordinate al valore osservato. Per ognuno dei punti così
ottenuti viene poi tracciato un segmento che lo congiunge perpendicolarmente
all'asse delle ascisse. Il risultato è decisamente poco informativo, sia da un
punto di vista grafico (le etichette sull'asse delle ascisse si sovrappongono,
così che non si riesce a leggere nulla), sia da un punto di vista analitico: le
barre hanno altezze simili e quindi le loro differenze sono poco apprezzabili a
colpo d'occhio; inoltre il grafico dipende per esempio dall'ordine in cui sono
elencate le osservazioni e non ci permette di solito di trarre alcuna
informazione sulla relazione che lega tra loro le osservazioni.

Si ottengono dei risultati decisamente più interessanti se si visualizza un
grafico analogo per le frequenze assolute:

```{code-block} python
first_app_freq.plot.bar()
plt.show()
```

Il grafico ottenuto è sicuramente migliore di quello precedente, ma rimane il
problema di leggibilità dell'asse delle ascisse. Ciò è dovuto al fatto che
pandas non inserisce le barre sul grafico nelle ascisse corrispondenti agli
anni, ma le posiziona una accanto all'altra, come possiamo renderci conto
visualizzando un po' meglio solo alcune delle etichette (in prima istanza non è
importante capire come venga generato questo grafico, ma se siete curiosi
potete leggere l'approfondimento che trovate dopo il commento al grafico
stesso):

```{code-block} python
years = np.arange(1945, 2010, 10)
index_pos = [first_app_freq.index.get_loc(y) for y in years]
first_app_freq.plot.bar()
plt.xticks(index_pos, years)
plt.ylim((0, 18.5))
plt.show()
```

Si può osservare che tra due valori successivi evidenziati nell'asse delle
ascisse intercorre una distanza di dieci anni, ma le etichette non risultano
equispaziate: ciò è dovuto al fatto che in realtà la prima barra ha ascissa 1,
la seconda ha ascissa 2 e così via, mentre le etichette mostrate sull'asse
delle ascisse corrispondono ai valori degli indici.

```{admonition} Nomenclatura
:class: naming
Per generare il grafico precedente è necessario utilizzare alcune funzionalità
avanzate delle librerie considerate: `np.arange` permette di costruire un array
i cui valori vanno di dieci in dieci partendo da 1945 e arrivando a 2005; la
proprietà `index` di una serie permette di estrarne l'indice e il metodo
`get_loc` di quest'ultimo restituisce la posizione corrispondente a un dato
valore dell'indice. Infine, il metodo `xticks` di matplotlib permette di
specificare quali valori evidenziare sull'asse delle ascisse e quali etichette
utilizzare.
```

Per ottenere un grafico simile in cui le ascisse siano effettivamente gli anni
di prima apparizione è necessario tornare a utilizzare esplicitamente
matplotlib, passando al metodo `bar` rispettivamente l'indice e i valori della
serie, che si ottengono rispettivamente utilizzando la proprietà `index` e
invocando il metodo `get_values`.

```{code-block} python
plt.bar(first_app_freq.index, first_app_freq.values)
plt.xlim((1935, 2015))
plt.ylim(0, 18.5)
plt.show()
```


## Operazioni con le serie
Consideriamo le seguenti domande:

1. Quanti supereroi sono apparsi dopo il 1960?
2. Quanti tra il 1940 e il 1965?
3. Quanti dopo il 1970?

Per rispondere alla prima domanda dobbiamo isolare le frequenze che
corrispondono agli anni di apparizione che vanno dal 1960 in avanti. Notiamo
che l'indice della serie contiene i valori degli anni; è quindi possibile
utilizzare l'accesso tramite *list slicing* per recuperare le frequenze degli
anni di apparizione che vanno dal 1960 in avanti:

```{code-block} python
first_app_freq[1960:]
```

A questo punto è sufficiente invocare la funzione `sum` sulla sotto-serie
individuata per ottenere la somma delle frequenze:

```{code-block} python
sum(first_app_freq[1960:])
```

La seconda domanda trova risposta in modo analogo, filtrando le frequenze degli
anni di apparizione tra il 1940 e il 1966:

```{code-block} python
sum(first_app_freq[1940:1966])
```

Analogamente, all'ultima domanda si risponde selezionando gli anni dal 1970 in
avanti:

```{code-block} python
sum(first_app_freq[:1971])
```

```{admonition} Nomenclatura
:class: naming
La funzione `sum` accetta come argomento liste, tuple e serie: in tutti i casi
restituisce la somma dei valori in esse contenute.
```

Un modo alternativo per calcolare la somma dei valori in una serie è quella di
invocare su di essa l'omonimo metodo `sum`. Le serie sono inoltre in tutto e
per tutto dei vettori, sui quali è possibile effettuare operazioni algebriche.
Consideriamo per esempio le due serie contenenti altezza e peso dei supereroi:

```{code-block} python
height = pd.Series([float(h[4]) if h[4] else None for h in heroes], index=names)
weight = pd.Series([float(h[5]) if h[5] else None for h in heroes], index=names)
```

Una prima categoria di operazioni è quella che si ottiene indicando il nome di
una serie all'interno di un'espressione aritmetica: il risultato è una nuova
serie ottenuta calcolando l'espressione su tutti gli elementi della serie di
partenza. Per esempio, la cella seguente crea la serie contenente l'altezza
degli eroi misurata in metri e ne visualizza i primi dieci elementi:

```{code-block} python
(height/100)[:10]
```

Quando si considerano operazioni più complicate, è possibile utilizzare il
metodo `apply` indicando come suo argomento la funzione da applicare agli
elementi della serie. Per esempio, nella cella seguente viene creata una nuova
serie ottenuta esprimendo le altezze dei supereroi in metri e successivamente
elevando il risultato al quadrato.

```{code-block} python
height.apply(lambda h: (h/100)**2)[:10]
```

Un'altra importante categoria di operazioni è quella che vede due serie
indicate come argomenti di un operatore aritmetico binario. In questo caso
verrà ancora creata una nuova serie, in cui l'operazione viene calcolata
elemento per elemento nelle serie indicate. Per esempio, la cella seguente
crea una nuova serie `bmi` contenente l'indice di massa corporea (BMI) dei
supereroi (ottenuto dividendo il peso specificato in chilogrammi per il
  quadrato dell'altezza misurata in metri), e mostra i quindici supereroi con
  il BMI più elevato.

```{code-block} python
bmi = weight / height.apply(lambda h: (h/100)**2)
bmi.sort_values(ascending=False)[:15]
```

A parte notare Hulk è solo il quindicesimo della classifica, va sottolineato che
le operazioni fatte elemento per elemento allineano i vettori corrispondenti
alle serie in base all'indice (e non alla posizione). Consideriamo per esempio
la seguente cella, in cui vengono selezionati altezze e pesi più o meno
plausibili per un essere umano, calcolando poi i corrispondenti BMI.

```{code-block} python
standard_weight = weight[(weight < 100) & (weight > 40)]
standard_height = height[(height < 210) & (height > 120)]/100
(standard_weight / (standard_height**2))[:15]
```

Si nota un numero relativamente elevato di `NaN`, e ciò è appunto dovuto al
fatto che il rapporto alla base del calcolo del BMI viene fatto usando peso e
altezza di valori che hanno lo stesso indice. Ora, non è detto che un supereroe
che ha un peso plausibile abbia anche un'altezza plausibile, e viceversa.
Quello che succede quando si esegue un'operazione tra due serie e solo una di
essa è definita in corrispondenza di uno specifico valore dell'indice, il
risultato conterrà `NaN` per quel valore.
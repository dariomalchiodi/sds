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

(pandas)=
# Pandas
Vedremo come la libreria pandas faciliti le operazioni viste finora per caricare dati, organizzarli in opportune strutture e analizzarli. Per poter procedere dobbiamo ricaricare le librerie usate finora, nonché il file `heroes.csv`. Useremo anche la _matplotlib magic_ che ci permette di visualizzare i grafici direttamente nel notebook.

```{code-cell} ipython3
import csv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

plt.style.use('sds.mplstyle')

with open('data/heroes.csv', 'r') as heroes_file:
  heroes_reader = csv.reader(heroes_file, delimiter=';', quotechar='"')
  heroes = list(heroes_reader)[1:]
```

Va notato come pandas (così come, in generale, gran parte del software open source dedicato all'analisi dei dati) sia caratterizzato da una comunità di sviluppatori molto attiva. Ciò significa che il tempo tra il rilascio di due release successive sia di norma breve: se avete effettuato l'installazione in modo autonomo è quindi possibile che stiate utilizzando una versione più (o meno) recente di quella più aggiornata quando è stato scritto questo documento. Per verificare quale sia la versione installata è sufficiente accedere alla proprietà `pd.__version__`:

```{code-cell} ipython3
pd.__version__
```

Utilizzando una versione diversa da questa, può capitare che il risultato ottenuto eseguendo alcune celle sia diverso da quello indicato. Alcune funzionalità potrebbero anche non essere implementate, deprecate o perfino rimosse. Se state invece utilizzando l'ambiente fornito tramite immagine Docker o tramite mybinder non dovreste avere problemi di questo genere.

## Serie
Una delle classi principali implementate in pandas è `Series`. Le sue istanze rappresentano serie di osservazioni di un certo carattere fatto su un insieme di individui. La cella seguente recupera dalla lista `heroes` precedentemente creata i nomi dei supereoi e il loro anno di prima apparizione e li utilizza per creare una serie:

```{code-cell} ipython3
years = [int(h[7]) if h[7] else None for h in heroes]
names = [h[0] for h in heroes]
first_appearance = pd.Series(years, index = names)
```

Nella creazione della lista `year` è stata utilizzata una list comprehension in cui l'espressione `int(h[7]) if h[7] else None` utilizza un operatore ternario tramite cui la stringa vuota viene trasformata nel valore speciale `None`, mentre tutte le altre vengono convertite nel corrispondente intero.

La differenza tra una serie e una lista o una tupla è legata alla possibilità di invocare su di essa delle funzioni specifiche. Inoltre a ogni serie è associato un *indice* che permette di identificare ogni elemento osservato. Nell'esempio sopra riportato, il primo argomento specificato nel costruttore è una lista (ma sarebbe andata bene anche una tupla) di anni che indicano la prima apparizione di un supereroe e il secondo rappresenta appunto l'indice, che in questo caso è la lista dei corrispondenti nomi. Quando si visualizza una serie, ogni osservazione viene associata al corrispondente elemento usando appunto l'indice:

```{code-cell} ipython3
first_appearance
```

La visualizzazione della serie (che in questo caso riporta solo i primi e gli ultimi elementi perché la serie è troppo lunga) termina indicando il tipo di dato usato per rappresentare le varie osservazioni. Nell'esempio precedente viene utilizzato il tipo `float64` (pandas utilizza internamente gli array di numpy, in cui è presente un'implementazione dei tipi in virgola mobile diversa da quella standard di python), nonostante i dati originari fossero numeri interi. Ciò è dovuto alla presenza di valori mancanti. Di norma vengono indicati con la sigla NA (dall'inglese "not available"), ma in pandas essi vengono rappresentati utilizzando il concetto di "not a number" dello standard IEEE per la virgola mobile: si noti come tutte le occorrenze di `None` nella lista originale siano state automaticamente convertite in `np.nan`.

L'accesso ai dati contenuti in una serie può avvenire in due modi:
- specificando un valore per l'indice tra parentesi quadre dopo la serie o dopo la sua proprietà `loc`:

```{code-cell} ipython3
(first_appearance['Wonder Woman'], first_appearance.loc['Wonder Woman'])
```

- indicando un valore per la posizione tra parentesi quadre dopo la serie o dopo la sua proprietà `iloc`:

```{code-cell} ipython3
(first_appearance[128], first_appearance.iloc[128])
```

```{admonition} Nomenclatura
:class: naming
Se l'indice di una serie è basato su valori interi, i valori tra parentesi quadre immediatamente dopo la serie faranno riferimento all'indice e non alla posizione: ciò potrebbe essere fuorviante se gli elementi dell'indice non partono da zero e non sono consecutivi.
```


È inoltre possibile utilizzare una notazione simile al _list slicing_ specificando valori dell'indice oppure posizioni. Va però notato che gli _slicing_ basati su indice comprenderanno il primo e l'ultimo valore specificato:

```{code-cell} ipython3
first_appearance['Wonder Girl':'Wonder Woman']
```

mentre gli _slice_ basati su posizione escluderanno l'ultimo elemento:

```{code-cell} ipython3
first_appearance[60:63]
```

L'accesso posizionale può anche fare riferimento a numeri negativi, contando in analogia a liste e tuple a partire dall'ultimo elemento:

```{code-cell} ipython3
first_appearance[-5:]
```

È possibile accedere ai primi e ultimi elementi di una serie anche utilizzando le funzioni `head` e `tail`, che mostrano rispettivamente solo le prime e le ultime righe:

```{code-cell} ipython3
first_appearance.head(7)
```

L'accesso alle liste può anche essere fatto specificando una lista (ma non una tupla) di posizioni al posto di una sola posizione, con l'effetto di ottenere i corrispondenti elementi.

```{code-cell} ipython3
first_appearance[[1, 42, 709]]
```

Questo tipo di accesso può essere fatto anche specificando una lista di valori per l'indice. Infine, si può utilizzare una lista di valori booleani in cui `True` indica gli elementi da estrarre e `False` quelli da filtrare:

```{code-cell} ipython3
first_appearance[[1970 <= y <1975 for y in first_appearance]]
```

```{admonition} Nomenclatura
:class: naming
L'uso di questa modalità di accesso richiede che la lista di valori booleani abbia la stessa lunghezza della serie. L'uso di liste di dimensioni minori l'accesso, che comporta un filtraggio effettuato solo nei primi elementi della serie, è deprecato e va quindi evitato.  
```

Infine, è possibile effettuare delle _query_ su una serie specificando tra parentesi quadre un'espressione logica che indica quali elementi visualizzare, utilizzando la serie come simbolo che ne indica un suo generico elemento:

```{code-cell} ipython3
first_appearance[first_appearance > 2010]
```

```{admonition} Nomenclatura
:class: naming
Tecnicamente, l'espressione `first_appearance > 2010` genera una nuova serie che ha lo stesso indice di `first_appearance` e in cui i valori sono `True` in corrispondenza degli anni successivi al 2010 e `False` altrimenti. Questa nuova serie viene utilizzata per filtrare `first_appearance`.
```

Vediamo ora come utilizzando le serie sia molto più semplice calcolare e visualizzare le frequenze assolute: il metodo `value_counts` restituisce un'altra serie in cui gli indici sono i valori osservati e i valori le corrispondenti frequenze assolute, ordinate in senso non crescente.

```{code-cell} ipython3
first_appearance.value_counts()
```

Va notato come il tipo delle frequenze sia, correttamente, intero e come i valori mancanti siano automaticamente esclusi dal calcolo delle frequenze, mentre sono sempre presenti gli _outlier_.  Per ottenere una serie i cui elementi siano ordinati per valore non decrescente della voce nell'indice è sufficiente invocare il metodo `sort_index`; già che ci siamo, è un buon momento per eliminare i valori fuori scala dal conteggio effettuando una _query_ sulla serie:

```{code-cell} ipython3
first_app_freq = first_appearance[first_appearance < 2090].value_counts().sort_index()
first_app_freq.head(10)
```




<div id="h-2"></div>

## Visualizzione grafica di una serie
Pandas mette a disposizione l'oggetto `plot` per visualizzare graficamente i contenuti di una serie, utilizzando matplotlib dietro le quinte; in particolare, il metodo `bar` visualizza un grafico a barre:

```{code-cell} ipython3
# Don't try this at home (men che meno all'esame!)

first_appearance.plot.bar()
plt.show()
```

Il grafico ottenuto, diciamolo, fa schifo. Questo perché `bar` considera un punto per ogni elemento della serie, in cui le ascisse corrispondono alla posizione (zero per la prima osservazione, uno per la seconda e così via, sebbene nel grafico sull'asse delle ascisse vengano poi visualizzati i valori dell'indice) e le ordinate al valore osservato. Per ognuno dei punti così ottenuti viene poi tracciato un segmento che lo congiunge perpendicolarmente all'asse delle ascisse. Il risultato è decisamente poco informativo, sia da un punto di vista grafico (le etichette sull'asse delle ascisse si sovrappongono, così che non si riesce a leggere nulla), sia da un punto di vista analitico: le barre hanno altezze simili e quindi le loro differenze sono poco apprezzabili a colpo d'occhio; inoltre il grafico dipende per esempio dall'ordine in cui sono elencate le osservazioni e non ci permette di solito di trarre alcuna informazione sulla relazione che lega tra loro le osservazioni.

Si ottengono dei risultati decisamente più interessanti se si visualizza un grafico analogo per le frequenze assolute:

```{code-cell} ipython3
first_app_freq.plot.bar()
plt.show()
```

Il grafico ottenuto è sicuramente migliore di quello precedente, ma rimane il problema di leggibilità dell'asse delle ascisse. Ciò è dovuto al fatto che pandas non inserisce le barre sul grafico nelle ascisse corrispondenti agli anni, ma le posiziona una accanto all'altra, come possiamo renderci conto visualizzando un po' meglio solo alcune delle etichette (in prima istanza non è importante capire come venga generato questo grafico, ma se siete cursosi potete leggere l'approfondimento che trovate dopo il commento al grafico stesso):

```{code-cell} ipython3
years = np.arange(1945, 2010, 10)
index_pos = [first_app_freq.index.get_loc(y) for y in years]
first_app_freq.plot.bar()
plt.xticks(index_pos, years)
plt.ylim((0, 18.5))
plt.show()
```

Si può osservare che tra due valori successivi evidenziati nell'asse delle ascisse intercorre una distanza di dieci anni, ma le etichette non risultano equispaziate: ciò è dovuto al fatto che in realtà la prima barra ha ascissa 1, la seconda ha ascissa 2 e così via, mentre le etichette mostrate sull'asse delle ascisse corrispondono ai valori degli indici.

```{admonition} Nomenclatura
:class: naming
Per generare il grafico precedente è necessario utilizzare alcune funzionalità avanzate delle librerie considerate: `np.arange` permette di costruire un array i cui valori vanno di dieci in dieci partendo da 1945 e arrivando a 2005; la proprietà `index` di una serie permette di estrarne l'indice e il metodo `get_loc` di quest'ultimo restituisce la posizione corrispondente a un dato valore dell'indice. Infine, il metodo `xticks` di matplotlib permette di specificare quali valori evidenziare sull'asse delle ascisse e quali etichette utilizzare.
```

Per ottenere un grafico simile in cui le ascisse siano effettivamente gli anni di prima apparizione è necessario tornare a utilizzare esplicitamente matplotlib, passando al metodo `bar` rispettivamente l'indice e i valori della serie, che si ottengono rispettivamente utilizzando la proprietà `index` e invocando il metodo `get_values`.

```{code-cell} ipython3
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

Per rispondere alla prima domanda dobbiamo isolare le frequenze che corrispondono agli anni di apparizione che vanno dal 1960 in avanti. Notiamo che l'indice della serie contiene i valori degli anni; è quindi possibile utilizzare l'accesso tramite *list slicing* per recuperare le frequenze degli anni di apparizione che vanno dal 1960 in avanti:

```{code-cell} ipython3
first_app_freq[1960:]
```

A questo punto è sufficiente invocare la funzione `sum` sulla sotto-serie individuata per ottenere la somma delle frequenze:

```{code-cell} ipython3
sum(first_app_freq[1960:])
```

La seconda domanda trova risposta in modo analogo, filtrando le frequenze degli anni di apparizione tra il 1940 e il 1966:

```{code-cell} ipython3
sum(first_app_freq[1940:1966])
```

Analogamente, all'ultima domanda si risponde selezionando gli anni dal 1970 in avanti:

```{code-cell} ipython3
sum(first_app_freq[:1971])
```

```{admonition} Nomenclatura
:class: naming
La funzione `sum` accetta come argomento liste, tuple e serie: in tutti i casi restituisce la somma dei valori in esse contenute.
```

Un modo alternativo per calcolare la somma dei valori in una serie è quella di invocare su di essa l'omonimo metodo `sum`. Le serie sono inoltre in tutto e per tutto dei vettori, sui quali è possibile effettuare operazioni algebriche. Consideriamo per esempio le due serie contenenti altezza e peso dei supereroi:

```{code-cell} ipython3
height = pd.Series([float(h[4]) if h[4] else None for h in heroes], index=names)
weight = pd.Series([float(h[5]) if h[5] else None for h in heroes], index=names)
```

Una prima categoria di operazioni è quella che si ottiene indicando il nome di una serie all'interno di un'espressione aritmetica: il risultato è una nuova serie ottenuta calcolando l'espressione su tutti gli elementi della serie di partenza. Per esempio, la cella seguente crea la serie contenente l'altezza degli eroi misurata in metri e ne visualizza i primi dieci elementi:

```{code-cell} ipython3
(height/100)[:10]
```

Quando si considerano operazioni più complicate, è possibile utilizzare il metodo `apply` indicando come suo argomento la funzione da applicare agli elementi della serie. Per esempio, nella cella seguente viene creata una nuova serie ottenuta esprimendo le altezze dei supereroi in metri e successivamente elevando il risultato al quadrato.

```{code-cell} ipython3
height.apply(lambda h: (h/100)**2)[:10]
```

Un'altra importante categoria di operazioni è quella che vede due serie indicate come argomenti di un operatore aritmetico binario. In questo caso verrà ancora creata una nuova serie, in cui l'operazione viene calcolata elemento per elemento nelle serie indicate. Per esempio, la cella seguente crea una nuova serie `bmi` contenente l'indice di massa corporea (BMI) dei supereroi (ottenuto dividendo il peso specificato in chilogrammi per il quadrato dell'altezza misurata in metri), e mostra i quindici supereroi con il BMI più elevato.

```{code-cell} ipython3
bmi = weight / height.apply(lambda h: (h/100)**2)
bmi.sort_values(ascending=False)[:15]
```

A parte notare Hulk è solo il quindicesimo della classifica, va sottolinato che le operazioni fatte elemento per elemento allineano i vettori corrispondenti alle serie in base all'indice (e non alla posizione). Consideriamo per esempio la seguente cella, in cui vengono selezionati altezze e pesi più o meno plausibili per un essere umano, calcolando poi i corrispondenti BMI.

```{code-cell} ipython3
standard_weight = weight[(weight < 100) & (weight > 40)]
standard_height = height[(height < 210) & (height > 120)]/100
(standard_weight / (standard_height**2))[:15]
```

Si nota un numero relativamente elevato di `NaN`, e ciò è appunto dovuto al fatto che il rapporto alla base del calcolo del BMI viene fatto usando peso e altezza di valori che hanno lo stesso indice. Ora, non è detto che un supereroe che ha un peso plausibile abbia anche un'altezza plausibile, e viceversa. Quello che succede quando si esegue un'operazione tra due serie e solo una di essa è definita in corrispondenza di uno specifico valore dell'indice, il risultato conterrà `NaN` per quel valore.


## Dataframe
Un _dataframe_ è una collezione di serie che hanno lo stesso indice, ed è quindi un insieme di osservazioni di vari _caratteri_ per una popolazione di individui. Tra i vari modi che sono disponibili in pandas per creare un _dataframe_, noi faremo riferimento al metodo `read_csv` della classe `pd.DataFrame`, che permette di leggere i contenuti di un file in formato CSV e convertirli automaticamente in un _dataframe_.

```{code-cell} ipython3
heroes = pd.read_csv('data/heroes.csv', sep=';', index_col=0)
```

Usando lo stesso file a cui abbiamo fatto riferimento nei paragrafi precedenti, è stato necessario utilizzare l'argomento opzionle `sep` per indicare il carattere usato per separare i campi in ogni record. La visualizzazione dei dataframe viene automaticamente formattata in un formato tabellare facile da leggere se si utilizza jupyter:

```{code-cell} ipython3
l = ['paperino', 'minnie', 'paperinick', 'zorro']

def ultima_lettera(s):
    return s[-1]

#l.sort(key=ultima_lettera)

l.sort(key=lambda s: s[-1])

l
```

```{code-cell} ipython3

```

```{code-cell} ipython3
heroes
```

Ci riferiremo spesso alle righe e alle colonne di un _dataframe_ per indicare rispettivamente le osservazioni e i caratteri. Per esempio la prima riga si riferisce all'osservazione relativa ad "A-Bomb", mentre la prima colonna corrisponde al carattere "identity". Vi sono molti modi per interagire con un _dataframe_:

- l'insieme degli indici, dei caratteri e dei valori si ottengono, nell'ordine, alle proprietà `index`, `columns` e `values`;
- una serie corrispondente a una colonna/carattere può essere selezionata usando una sintassi simile a quella dei dizionari, specificando il nome del carattere come chiave:

```{code-cell} ipython3
heroes['Gender']
```

```{admonition} Nomenclatura
:class: naming
In alternativa è possibile usare una sintassi basata su _dot notation_ in cui il nome della colonna, senza essere racchiuso tra apici, segue il _dataframe_. In altre parole, `heroes['Gender']` e `heroes.Gender` sono equivalenti. Questa seconda notazione è però utilizzabile solamente se non vi sono spazi nei nomi delle colonne. Nel seguito utilizzeremo quindi sempre la prima delle due notazioni.
```

- tramite uno _slicing_ sulle posizioni o sui valori dell'indice è possibile selezionare un sottoinsieme delle righe del _dataframe_ (e come nel caso delle serie, l'estremo superiore è incluse se si usano gli indici ed escluso se si usano le posizioni):

```{code-cell} ipython3
heroes['Agent 13':'Air-Walker']
```

Queste modalità di accesso possono effettivamente creare confusione: usando una sintassi molto simile, specificando un valore si accede a una colonna e specificando uno _slice_ si accede a un insieme di righe. Per scrivere codice più chiaro è meglio selezionare le righe utilizzando le proprietà `loc` e `iloc` nello stesso modo in cui queste funzionano per le serie, con la differenza che quando queste sono usate specificando un solo valore, viene restituita una serie, e quando sono utilizzate con uno _slice_ o con una lista viene restituito un _dataframe_.

```{code-cell} ipython3
heroes.loc['Professor X']
```

```{code-cell} ipython3
heroes.iloc[42:46]
```

È inoltre possibile selezionare una o più righe e visualizzare solo un sottoinsieme dei caratteri, passando a `loc` o `iloc` un secondo argomento in cui si specificano i caratteri da mostrare, utilizzando anche in questo caso un valore, una lista di valori oppure uno _slice_:

```{code-cell} ipython3
heroes.loc['Professor X', 'Height':'Weight']
```

Va notato che `loc` accetta solo valori simbolici, mentre `iloc` solamente posizioni, e ciò riguarda anche il loro secondo argomento:

```{code-cell} ipython3
heroes.iloc[[106, 103], [3, 4]]
```

Volendo accedere direttamente a un elemento è possibile utilizzare le proprietà `at` e `iat`:

```{code-cell} ipython3
heroes.at['Superman', 'Strength']
```

```{code-cell} ipython3
heroes.iat[500, -1]
```

```{admonition} Nomenclatura
:class: naming
È anche possibile utilizzare `loc` e `iloc` per estrarre un singolo elemento: per esempio, `heroes.loc['Superman', 'Strength']` equivale alla prima delle due istruzioni appena elencate. Tuttavia, `at` e `iat` sono implementate in modo da essere più efficienti.
```

È infine possibile riordinare le righe di un dataframe invocando i metodi `sort_values` e `sort_index`: il primo basa l'ordinamento sul valore di una colonna, il cui nome va specificato tramite l'argomento `by` e il secondo è invece basato sui valori dell'indice. È inoltre possibile indicare un valore booleano per l'argomento `ascending` che permette di ordinare in verso crescente o decrescente.

```{code-cell} ipython3
heroes.sort_values(by='Weight', ascending=False)[:5]
```

```{code-cell} ipython3
heroes.sort_index()[-5:]
```

Va notato che entrmabi i metodi restituiscono una copia del _dataframe_. Anche per i _dataframe_ è possibile utilizzare una lista di valori booleani che identificano le righe da selezionare, e tale lista può essere prodotta effettuando una query. In questo caso però le condizioni possono riguardare le varie colonne, ognuna delle quali va specificata usando una delle due sintassi precedentemente introdotte (quella analoga ai dizionari oppure quella basata su _dot notation_). Per esempio possiamo selezionare gli eroi per cui l'anno di apparizione esiste e rappresenta un valore non fuori scala nel modo seguente:

```{code-cell} ipython3
heroes_with_year = heroes[heroes['First appearance'] > 1900]
heroes_with_year.head()
```

```{code-cell} ipython3

```

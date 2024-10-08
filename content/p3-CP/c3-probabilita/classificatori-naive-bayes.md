## Classificatori naive Bayes

Una semplice applicazione del teorema di Bayes permette di costruire un
particolare classificatore che prende il nome di _classificatore naive Bayes_.
Consideriamo il caso più semplice possibile in cui abbiamo osservato in una
serie di individui la presenza o l'assenza di una determinata proprietà,
ottenendo per ognuno di essi un'osservazione $x_i \in \{ 0, 1 \}$. Ipotizziamo
inoltre di avere associato a ogni individuo un'etichetta $y_i \in \{ 0, 1 \}$
che denota l'appartenenza o meno a una data classe. Prendendo ad esempio il
dataset dei supereroi, supponiamo che la proprietà osservata faccia riferimento
all'avere oppure no gli occhi neri (indicando con $x_i = 1$ il fatto di avere
gli occhi neri e con $x_i = 0$ il fatto di averli di un altro colore), e la
classe considerata indichi se l'editore corrispondente sia o meno la Marvel
Comics (anche in questo caso, denotando con $y_i = 1$ il fatto di essere un
supereroe Marvel e con $y_i = 0$ il fatto di non esserlo).

Indichiamo inoltre con $N$ l'evento «un supereroe preso a caso ha gli occhi
neri» e con $M$ l'evento «un supereroe preso a caso è un supereroe Marvel»:
grazie al teorema di Bayes sappiamo che vale

$$
\mathrm P(M|N) = \frac{\mathrm P(N|M) \mathrm P(M)}{\mathrm P(N)}.
$$

Ora, se a partire dal dataset fosse possibile ottenere una stima delle
probabilità che compaiono al secondo membro di questa equazione, sarebbe quindi
immediato ottenere una stima di $\mathrm P(M|N)$ da utilizzare per dire
qualcosa sul fatto che un generico supereroe con gli occhi neri sia oppure no
un supereroe Marvel. In particolare, se il valore ottenuto fosse
sufficientemente alto potremmo spingerci oltre e dire che d'ora in avanti
potremo _classificare_ tutti i supereroi con gli occhi neri di cui non
conosciamo l'editore come supereroi Marvel. Allo stesso modo, se il valore
ottenuto fosse particolarmente basso potremmo comportarci in modo analogo,
concludendo però che gli occhi neri indicano un editore diverso dalla Marvel.

Il fatto di poter azzardare l'editore potrebbe sembrare poco utile, visto che
in fondo si tratta di una colonna del nostro dataset e quindi noi già sappiamo
quali siano i valori per questo attributo. In realtà sappiamo che ci potrebbero
essere dei valori mancanti, oppure potremmo in futuro avere a disposizione
nuovi dati per i quali questa informazione non è disponibile.

```{admonition} Nota
:class: naming
Va notato che la scelta di usare il colore degli occhi come proprietà osservata
e la casa editrice come classe è assolutamente arbitraria. In modo analogo
avremmo potuto ragionare in termini di come il fatto di essere un supereroe
Marvel possa essere utilizzato per azzardare il colore degli occhi, scambiando
gli eventi $M$ e $N$ nelle formule.
```

Un modo semplice per stimare le probabilità indicate è quello di osservare con
che frequenza gli eventi associati si verificano nel dataset a nostra
disposizione. In particolare,

- la probabilità $\mathrm P(N|M)$ può essere approssimata calcolando la
  frequenza relativa con cui un supereroe Marvel del dataset ha gli occhi neri;
- la probabilità $\mathrm P(M)$ può essere approssimata calcolando la frequenza
  relativa con cui un supereroe del dataset è edito dalla Marvel;
- la probabilità $\mathrm P(N)$ può essere approssimata calcolando la frequenza
  relativa con cui un supereroe del dataset ha gli occhi neri.

Attrezziamoci quindi per poter calcolare queste frequenze, caricando il dataset
e importando le librerie che utilizzeremo.

```{code-cell} ipython3
import pandas as pd
import numpy as np

heroes = pd.read_csv('data/heroes.csv', sep=';', index_col=0)
```

Possiamo ora approssimare la probabilità dell'evento $M$ come la frequenza
relativa del medesimo evento sul dataset, e quindi calcolando il rapporto tra
il numero di supereroi Marvel e il totale dei supereroi.

```{code-cell} ipython3
marvel_heroes = heroes[heroes['Publisher']=='Marvel Comics']
p_marvel = len(marvel_heroes) / len(heroes)
p_marvel
```

Allo stesso modo, la probabilità $\mathrm P(N)$ si approssima facilmente
calcolando la frazione di supereroi del dataset che hanno gli occhi neri.

```{code-cell} ipython3
black_eyes_heroes = heroes[heroes['Eye color']=='Black']
p_blackeyes = len(black_eyes_heroes) / len(heroes)
p_blackeyes
```

Infine, una stima della probabilità $\mathrm P(N|M)$ si ottiene dividendo il
numero di supereroi Marvel che hanno gli occhi neri per il numero totale di
supereroi Marvel.

```{code-cell} ipython3
blackeyes_and_marvel_heroes = heroes[(heroes['Publisher']=='Marvel Comics') & \
                                     (heroes['Eye color']=='Black')]

p_blackeyes_given_marvel = len(blackeyes_and_marvel_heroes) / len(marvel_heroes)
p_blackeyes_given_marvel
```

Applicando il teorema di Bayes si ottiene quindi che la probabilità di trovarsi
di fronte a un supereroe Marvel, dato che questo ha gli occhi neri, può essere
approssimata come segue.

```{code-cell} ipython3
p_blackeyes_given_marvel * p_marvel / p_blackeyes
```

Dunque sembrerebbe che gli occhi neri siano leggermente più probabili nei
supereroi **non** Marvel. Ovviamente avremmo ottenuto un risultato coerente se
avessimo applicato lo stesso procedimento per stimare la probabilità
$\mathrm(\overline M|N)$.

```{code-cell} ipython3
nonmarvel_heroes = heroes[heroes['Publisher']!='Marvel Comics']
blackeyes_and_nonmarvel_heroes = heroes[(heroes['Publisher']!='Marvel Comics') & \
                                        (heroes['Eye color']=='Black')]

p_notmarvel = len(nonmarvel_heroes) / len(heroes)
p_blackeyes_given_notmarvel = len(blackeyes_and_nonmarvel_heroes) / len(nonmarvel_heroes)

p_blackeyes_given_notmarvel * p_notmarvel / p_blackeyes
```

Visto che le due probabilità ottenute sono molto vicine a $\frac{1}{2}$, ha
senso valutare se l'uso di diverse proprietà da osservare _congiuntamente_ ci
possa portare a una procedura più precisa. Per esempio potremmo tener conto sia
del colore degli occhi, sia di quello dei capelli, senza fissare un colore
specifico. Consideriamo pertanto tutti i possibili valori
$\{ o_1, o_2, \dots, o_n \}$ per i colori degli occhi e scriviamo $O = o_i$ per
indicare l'evento «un supereroe a caso ha gli occhi del colore $o_i$».
Procediamo in modo analogo per l'evento $C = c_j$ che equivale a «un supereroe
a caso ha i capelli del colore $c_j$», dove i valori possibili ora
corrispondono all'insieme $\{ c_1, c_2, \dots, c_m \}$. Il teorema di Bayes
permette in questo caso di scrivere

$$
\mathrm P(M|O = o_i \cap C = c_j) = \frac{\mathrm P(O = o_i \cap C = c_j | M)
                              \mathrm P(M)}{\mathrm P((O = o_i \cap C = c_j)}.
$$

Pertanto si può pensare di estendere il ragionamento visto precedentemente:
dato un supereroe di cui si conoscono i colori $o_i$ e $c_j$ di occhi e
capelli, si approssimano le probabilità al secondo membro dell'equazione e in
funzione del valore ottenuto si classifica il supereroe come «Marvel» oppure
come «non Marvel». I classificatori _naive Bayes_ semplificano il lavoro
approssimando $\mathrm P(O = o_i \cap C = c_j | M)$ con la quantità
$\mathrm P(O = o_i | M) \mathrm P(C = c_j | M)$. Procedendo in questo modo, nel
numeratore della frazione si calcoleranno al più $m + n$ diverse probabilità al
posto di $m n$ (più avanti vedremo come evitare l'analogo problema quando si
calcola il denominatore). L'aggettivo _naive_ nel nome del classificatore
sottolinea la semplicità dell'ipotesi adottata (_naive_ significa infatti
«ingenuo» in inglese).

Concentriamoci per esempio su un supereroe con occhi e capelli neri: la
probabilità che esso sia un supereroe Marvel sarà quindi calcolata da un
classificatore naive Bayes come

$$
\mathrm P(M|O = \text{neri} \cap C = \text{neri}) \approx
\frac{\mathrm P(O = \text{neri} | M) \mathrm P(C = \text{neri} | M)
\mathrm P(M)}{\mathrm P((O = \text{neri} \cap C = \text{neri})}.
$$

Alcune delle probabilità coinvolte sono già state calcolate. Nella cella
seguente quelle mancanti sono derivate in modo analogo, ottenendo come
risultato una bassa probabilità di avere a che fare con un supereroe Marvel se
i suoi occhi e i suoi capelli sono neri.

```{code-cell} ipython3
black_eyes_and_hair_heroes = heroes[(heroes['Eye color']=='Black') & \
                                    (heroes['Hair color']=='Black')]

p_blackeyes_and_black_hair = len(black_eyes_and_hair_heroes) / len(heroes)

blackhair_and_marvel_heroes = heroes[(heroes['Publisher']=='Marvel Comics') & \
                                     (heroes['Hair color']=='Black')]
p_blackhair_given_marvel = len(blackhair_and_marvel_heroes) / len(marvel_heroes)

p_blackeyes_given_marvel * p_blackhair_given_marvel * p_marvel \
     / p_blackeyes_and_black_hair
```

Consideriamo infine il caso più generale in cui vi sono più di due classi su
cui suddividere gli individui. Nell'esempio che stiamo considerando stiamo
quindi dicendo che vi sono valori diversi $\{ e_1, \dots, e_o \}$ per
l'editore, e quindi saremo interessati a eventi della forma $E = e_k$.
Idealmente, una volta osservato un supereroe di cui $o_j$ e $c_j$ indicano
rispettivamente il colore di occhi e capelli sarà necessario calcolare
$\mathrm P(E = e_k | O = o_i \cap C = c_j)$ per tutti i possibili $e_k$: il più
alto ottenuto individuerà l'editore da associare al supereroe. È però possibile
semplificare ulteriormente il procedimento, notando che esso consiste nel
determinare, al variare di $k$, il più alto tra i valori

$$
\mathrm P(E = e_k|O = o_i \cap C = c_j) \approx
\frac{\mathrm P(O = o_i | E = e_k) \mathrm P(C = c_j | E = e_k)
\mathrm P(E = e_k)}{\mathrm P((O = o_i \cap C = c_j)}.
$$

Ora, il denominatore è indipendente da $k$ e quindi la classificazione si può
effettuare trovando il valore $k$ che massimizza la quantità

$$
\mathrm P(O = o_i | E = e_k) \mathrm P(C = c_j | E = e_k) \mathrm P(E = e_k).
$$

Riformuliamo il ragionamento effettuato in modo da renderlo il più generale
possibile: immaginiamo che per un dato individuo si osservino congiuntamente i
valori $x_1, \dots, x_n$ per $n$ proprietà $X_1, \dots, X_n$, e denotiamo con
$X_1 = x_1, \dots, X_n=x_n$ gli eventi corrispondenti. Supponiamo inoltre che
vi siano $m$ possibili classi che corrispondono agli eventi
$Y = y_1, \dots, Y = y_m$. Per ognuna di queste classi vorremo calcolare

$$
\mathrm P(Y=y_k | X_1=x_1, \dots, X_n=x_n) =
      \frac{\mathrm P(X_1=x_1, \dots, X_n=x_n | Y=y_k) \mathrm P(Y=y_k)}
           {\mathrm P(X_1=x_1, \dots, X_n=x_n)}
$$

e assegnare l'individuo alla classe per cui tale probabilità è massima.
L'approssimazione alla base del classificatore naive Bayes ci permette di
scrivere

$$
\mathrm P(Y=y_k | X_1=x_1, \dots, X_n=x_n) \approx \frac{\mathrm P(Y=y_k)
  \displaystyle\prod_{i=1}^n\mathrm P(X_i=x_i | Y=y_k)}
                {\mathrm P(X_1=x_1, \dots, X_n=x_n)},
$$

e tenuto conto che anche in questo caso il denominatore non dipende da $k$,
potremo associare l'individuo alla classe $y_{k^*}$, dove

$$
k^* = \arg\max_k \mathrm P(Y = y_k) \prod_{i=1}^n
      \mathrm P(X_i = x_i | Y = y_k).
$$

In realtà non è necessario effettuare «a mano» i calcoli legati a un
classificatore naive Bayes. Come già visto per gli alberi di decisione, la
libreria sklearn mette a disposizione delle classi che permettono di ottenere
direttamente un classificatore a partire dai dati iniziali. Per esemplificarne
il funzionamento, estraiamo dal nostro dataset alcune colonne ed eliminiamo
tutte le righe in cui occorre almeno un valore mancante.

```{code-cell} ipython3
features = ['Height', 'Weight', 'Gender', 'First appearance',
            'Hair color', 'Eye color', 'Strength', 'Intelligence']
heroes_cleaned = heroes.dropna()
X = heroes_cleaned[features].copy()
```

Per gli stessi motivi visti quando abbiamo lavorato con gli alberi di
decisione, è necessario utilizzare solamente dati numerici. Possiamo convertire
gli attributi categorici che corrispondono a genere e colore di occhi e capelli
riutilizzando le classi `LabelEncoder`. Procediamo poi a convertire i valori
degli attributi rimanenti nel modo che segue: dividiamo innanzitutto
l'intervallo di variazione dei corrispondenti valori in quattro intervalli,
utilizzando i quattro quartili come estremi; associamo successivamente un
diverso valore numerico a ogni intervallo ottenuto e trasformiamo ogni
osservazione nel numero che corrisponde all'intervallo individuato. Questa
operazione viene effettuata automaticamente dalla funzione `pd.qcut`, a cui
passiamo le osservazioni, il numero di intervalli da considerare e i valori
numerici da associare a questi ultimi.

```{code-cell} ipython3
from sklearn.preprocessing import LabelEncoder

n = 4
X['Height'] = pd.qcut(X['Height'], n, labels=range(n))
X['Weight'] = pd.qcut(X['Weight'], n, labels=range(n))

gender_encoder = LabelEncoder()
gender_encoder.fit(X['Gender'])
X['Gender'] = gender_encoder.transform(X['Gender'])

X['First appearance'] = pd.qcut(X['First appearance'],
                                n,
                                labels=range(n))

hair_encoder = LabelEncoder()
hair_encoder.fit(X['Hair color'])
X['Hair color'] = hair_encoder.transform(X['Hair color'])

eye_encoder = LabelEncoder()
eye_encoder.fit(X['Eye color'])
X['Eye color'] = eye_encoder.transform(X['Eye color'])

X['Strength'] = pd.qcut(X['Strength'], n, labels=range(n))

intelligence_encoder = LabelEncoder()
intelligence_encoder.fit(X['Intelligence'])
X['Intelligence'] = intelligence_encoder.transform(X['Intelligence'])
```

L'ultimo ingrediente mancante è l'insieme dei valori per le classi. Per
semplificarci la vita, ritorniamo alla classificazione binaria inizialmente
considerata: anche in questo caso è necessario lavorare con valori numerici,
quindi costruiamo una serie i cui valori sono `1` in corrispondenza dei
supereroi Marvel e `0` per tutti gli altri casi.

```{code-cell} ipython3
Y = (heroes_cleaned['Publisher']=='Marvel Comics').apply( \
         lambda x: 1 if x else 0)
```

In realtà sklearn implementa diverse varianti del classificatore naive Bayes,
ognuna delle quali stima in modo diverso le probabilità
$\mathrm P(X_i = x_i | Y = y_k)$. Consideriamo per esempio la classe
`GaussianNB`, che ipotizza che tali probabilità si possano calcolare
utilizzando una distribuzione gaussiana (uno dei modelli teorici che vedremo
tra qualche lezione). La costruzione del classificatore viene fatta usando lo
stesso procedimento visto per gli alberi di decisione: si crea un oggetto della
classe `GaussianNB`, e poi si invoca su di esso il metodo `fit` specificando
come argomenti le osservazioni e le corrispondenti etichette. Dopo sarà
sufficiente invocare il metodo `predict` passando una lista di oggetti da
classificare. Ricordando che per avere una valutazione imparziale di un
classificatore è necessario utilizzare dati non utilizzati per costruire il
classificatore stesso, per semplicità limitiamoci a verificare che cosa succeda
con le osservazioni in `X`.

```{code-cell} ipython3
from sklearn.naive_bayes import GaussianNB

model = GaussianNB()
model.fit(X, Y)

model.predict(X)
```

Il risultato non pare molto confortante, in quanto quasi tutti i casi vengono
associati alla Marvel. Per analizzare meglio i risultati, vediamo separatamente
come vengono classificati i supereroi delle due classi.

```{code-cell} ipython3
model.predict(X[Y==0])
```

```{code-cell} ipython3
model.predict(X[Y==1])
```

A partire dai vettori ottenuti è facile calcolare separatamente il numero di
veri positivi, falsi positivi, falsi negativi e veri negativi. È anche
possibile costruire un dataframe che contenga la corrispondente matrice di
confusione.

```{code-cell} ipython3
tp = sum(model.predict(X[Y==1]))
fn = len(model.predict(X[Y==1])) - tp
fp = sum(model.predict(X[Y==0]))
tn = len(model.predict(X[Y==0])) - fp
pd.DataFrame([[tp, fn],
              [fp, tn]],
              index=['Etichetta positiva', 'Etichetta negativa'],
              columns=['Classif. positiva', 'Classif. negativa'])
```

La matrice evidenzia una buona classificazione dei supereroi Marvel e una
performance molto bassa per quel che riguarda i rimanenti supereroi. Volendo
riassumere in un unico indice la bontà del risultato ottenuto è possibile
calcolare la percentuale di dati corretti.

```{code-cell} ipython3
(tp + tn) / len(X)
```

Tale percentuale di per sé ci dice che poco meno dell'80% dei casi è stata
classificata correttamente. Ciò è dovuto al fatto che nel dataset considerato
vi sono in proporzione molti più supereroi Marvel rispetto a quelli delle altre
case editrici.

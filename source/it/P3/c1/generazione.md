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

(sec_generazione-combinatoria)=
# Enumerazione combinatoria

In Python è abbastanza facile generare tutti i tipi di raggruppamenti visti
finora. In particolare, il modulo `itertools`, fornisce iteratori efficienti
che permettono di generare in sequenza tutti i possibili raggruppamenti di un
dato tipo, senza mai mantenerli tutti insieme in memoria.

```{admonition} Iteratori e memoria
:class: tip
Le funzioni di `itertools` restituiscono _iteratori_, non liste. Gli
elementi vengono generati uno alla volta solo quando richiesti, senza
mai caricare l'intera sequenza in memoria. Questo è particolarmente
vantaggioso quando $n$ e $k$ sono grandi: per esempio, scegliere tutte le
squadre da 5 eroi tra i 50 personaggi del Marvel Cinematic Universe
produrrebbe $c_{50,5} = $ <span style="word-spacing: -0.1rem">2 118 760</span>
combinazioni. Nell'ipotesi che la descrizione di una squadra richieda di
specificare un identificatore intero per ogni membro, materializzare tutte
le squadre possibili in una lista richiederebbe verosimilmente alcune decine di
megabyte di RAM, mentre l'approccio basato su iteratore manterrebbe di volta in
volta in memoria un'unica squadra &mdash; e per questo basterebbero una
ventina di byte!

Se tuttavia un'applicazione richiedesse di salvare in memoria tutte
le descrizioni, per esempio perché si deve svolgere un'elaborazione delle
squadre che non può essere fatta in modo sequenziale, gli iteratori possono
essere convertiti esplicitamente in list usando `list`.
```

## Permutazioni semplici

Gli oggetti della classe `itertools.permutations` sono degli iteratori che,
quando vengono attraversati, generano tutte le permutazioni semplici degli
elementi contenuti nell'oggetto usato per istanziare la classe stessa. Per
esempio, eseguendo la cella seguente si ottiene un elenco delle possibili
permutazioni dei Fantastici 4, analogo a quello della
{numref}`permutazioni-fantastici-quattro`:

```{code-cell} python
import itertools as it

fantastic_4 = ['f', 'i', 't', 'c']
for i, p in enumerate(it.permutations(fantastic_4)):
    print(p, end='\n' if (i+1) % 3 == 0 else '  ')
```

In altre parole, il codice precedente genera tutte le $p_4 = 24$ permutazioni
dei quattro membri della squadra.

## Permutazioni con ripetizione

Il modulo `itertools` non offre la possibilità di generare direttamente tutte
le permutazioni con ripetizione di un insieme di oggetti distinguibili a
gruppi. È però abbastanza facile ottenere queste permutazioni partendo da
quelle semplici e filtrando i doppioni[^sympy], per esempio inserendo le
permutazioni in un insieme, così da potere ignorare le loro successive
occorrenze. La cella seguente utilizza un approccio di questo tipo per produrre
un elenco simile a quello della {numref}`permutazioni-oggetti-indistinguibili`:

```{code-cell} python

clones = ['k', 'k', 'p', 'p', 'p']
seen = set()
for t in it.permutations(clones):
    if t not in seen:
        print(t, end='\n' if (len(seen)+1) % 3 == 0 else '  ')
        seen.add(t)
```

## Disposizioni con ripetizione

È facile rendersi conto che le disposizioni con ripetizione degli oggetti di un
insieme $A$ in $k \in \mathbb N$ sono esattamente gli elementi del prodotto
cartesiano

```{math}
A^k = \underbrace{A \times A \times \cdots \times A}_{\text{$k$ volte}} \enspace,
```

e che quindi si possono ottenere direttamente generando gli elementi del
prodotto cartesiano iterato, cosa che si ottiene facilmente usando l'iteratore
restituito da `itertools.product`, che quando viene invocato usando il
parametro opzionale `repeat` permette appunto di calcolare il prodotto di
un insieme con se stesso per un dato numero di volte. La cella seguente
mostra come riprodurre in tal modo le disposizioni con ripetizione della
{numref}`tab-disposizioni-con-ripetizione`.

```{code-cell} python
alpha_flight = ['g', 's', 'n', 'a']
for i, d in enumerate(it.product(alpha_flight, repeat=3)):
    print(d, end='\n' if (i+1) % 4 == 0 else '  ')
    if i == 15:
        break
```

Questo codice non stampa tutte le $D_{4, 3} = 64$ disposizioni con ripetizione,
perché viene forzata l'uscita dal ciclo for dopo averne considerato $16$, per
evitare un output inutilmente lungo.

## Disposizioni senza ripetizione

In virtù della relazione che sussiste tra le permutazioni semplici e le
disposizioni senza ripetizione, queste ultime possono essere generate
utilizzando `itertools.permutations`, specificando un secondo argomento che
indica il numero di posti. Ad esempio, nella cella seguente vengono prodotte
tutte le $d_{4, 3} = 24$ disposizioni semplici evidenziate in grassetto nella
{numref}`tab-disposizioni-con-ripetizione`.

```{code-cell} python

for i, d in enumerate(it.permutations(alpha_flight, 3)):
    print(d, end='\n' if (i+1) % 4 == 0 else '  ')
```

## Combinazioni

Il modulo `itertools` contiene due classi `combinations` e
`combinations_with_replacement` i cui oggetti sono iteratori sulle
combinazioni, rispettivamente semplici e con ripetizione. Per esempio, la
cella seguente stampa le combinazioni semplici di tre poteri di Peter Petrelli
(vedi {prf:ref}`ex-peter-petrelli`), nel caso questi possano essere
selezionati da un gruppo di cinque superpoteri.

```{code-cell} python
powers = ['telepatia','invisibilità', 'psicocinesi',
          'rigenerazione', 'precognizione']
for c in it.combinations(powers, 3):
    print(c)
```

Analogamente, il codice qui sotto genera tutte le combinazioni con ripetizione
considerate nella {numref}`tab-combinazioni-DK-MP`.

```{code-cell} python
for c in it.combinations_with_replacement(['k','p'], 4):
    print(c)
```



[^sympy]: In teoria, un approccio leggermente più efficiente è quello di
iterare su `dict.fromkeys(it.permutations(clones))`, che è un dizionario
fittizio creato al volo usando come chiavi le tuple che descrivono le
permutazioni, associandole tutte a `None`. In questo modo, i doppioni vengono
automaticamente esclusi, sovrascrivendo di volta in volta le coppie (chiave,
valore). Se l'implementazione di Python utilizzata è, per esempio, scritta in
C, la creazione del dizionario richiede meno tempo rispetto alla creazione e
all'utilizzo dell'insieme che va a contenere le tuple distinte. In realtà,
entrambi gli approcci hanno un'efficienza molto bassa quando il numero di
oggetti è molto elevato, ma nel contempo vi sono pochi oggetti distinti. Ciò è
dovuto al fatto che `it.permutations` genera in ogni caso _tutte_ le
permutazioni semplici, per poi filtrarle. Per ovviare a questo inconveniente,
il modulo `sympy.utilities.iterables` contiene il generatore
`multiset_permutations` che enumera efficientemente solo le permutazioni
distinte.

## Esercizi

````{exercise} •
:label: ex-gen-titans-turni

Generate e stampate tutti modi in cui è possibile assegnare tre turni di
pattuglia ai cinque [Teen Titans](https://dc.fandom.com/wiki/Teen_Titans)
(Robin, Starfire, Raven, Beast Boy, Cyborg), eventualmente assegnando a uno
stesso supereroe anche più di un turno. Contate e stampate inoltre il numero
totale di turnazioni possibili.
````
````{solution} ex-gen-titans-turni
:class: dropdown

Ogni assegnamento corrisponde a una disposizione con ripetizione dei cinque
Teen Titans in tre posti: lo stesso supereroe può coprire più turni (da cui la
necessità di considerare le ripetizioni), e l'ordine dei turni conta — essere
assegnati al primo turno è diverso dall'essere assegnati al secondo o al terzo
(da cui l'uso delle disposizioni).

```{code-cell} python
titans = ['Robin', 'Starfire', 'Raven', 'Beast Boy', 'Cyborg']
count = 0
for t in it.product(titans, repeat=3):
    print(t)
    count += 1
print(f'In tutto ci sono {count} modi diversi di assegnare i turni.')
```
````

````{exercise} •
:label: ex-gen-titans-conta

Se nell'esercizio precedente l'unica richiesta fosse stata quella di contare
il numero di turnazioni differenti, senza stamparle, esisterebbero dei modi
più efficienti di rispondere alla domanda?
````
````{solution} ex-gen-titans-conta
:class: dropdown

Siccome stiamo considerando le disposizioni con ripetizione di cinque oggetti
in tre posti, sappiamo che ne esistono esattamente $D_{5, 3} = 5^3 = 125$.
Questo ragionamento permette di rispondere alla domanda calcolando un solo
elevamento a potenza.
````

````{exercise} •
:label: ex-gen-watchmen-coppie

Generate e stampate tutte le possibili coppie formate dai sei membri dei
[Watchmen](https://dc.fandom.com/wiki/Watchmen) (Rorschach, Nite Owl, Silk
Spectre, Ozymandias, Dottor Manhattan, Comedian).
````
````{solution} ex-gen-watchmen-coppie
:class: dropdown

```{code-cell} python
watchmen = ['Rorschach', 'Nite Owl', 'Silk Spectre',
            'Ozymandias', 'Dr Manhattan', 'Comedian']

for c in it.combinations(watchmen, 2):
    print(c)
```
````

````{exercise} •
:label: ex-gen-dk-mp-ripetizione

Calcolate quante tra le combinazioni con ripetizione di Dupli-Kate e Multi-Paul
in quattro posti contengono almeno un clone di Kate.
````
````{solution} ex-gen-dk-mp-ripetizione
:class: dropdown

```{code-cell} python
count = 0
for c in it.combinations_with_replacement(['k', 'p'], 4):
    if 'k' in c:
        count += 1
print(f'Esattamente {count} combinazioni contengono almeno un clone di Kate.')
```
````

````{exercise} •
:label: ex-gen-dk-mp-ripetizione-comp

Riconsiderate l'esercizio precedente, risolvendolo usando una _list
comprehension_.
````
````{solution} ex-gen-dk-mp-ripetizione-comp
:class: dropdown

```{code-cell} python
count = len([1 for c in it.combinations_with_replacement(['k', 'p'], 4)
               if 'k' in c])
print(f'Esattamente {count} combinazioni contengono almeno un clone di Kate.')
```
````

````{exercise} •
:label: ex-gen-iter-vs-lista

Contate quante disposizioni con ripetizione dei $21$ membri regolari della
[Legion of
Super-Heroes](https://dc.fandom.com/wiki/Legion_of_Super-Heroes_(Earth-Prime))
in $3$ posti soddisfano la condizione che il primo e il terzo posto siano
occupati dallo stesso eroe, senza memorizzare l'intera lista.
````
````{solution} ex-gen-iter-vs-lista
:class: dropdown

```{code-cell} python
count = sum(1 for d in it.product(range(21), repeat=3) if d[0] == d[2])
print(f'In esattamente {count} casi uno stesso eroe compare in prima '
      'e ultima posizione.')
```

Il risultato è $21^2 = 441$: il primo posto ha $21$ scelte, il secondo pure,
mentre il terzo è vincolato a coincidere con il primo.
````

````{exercise} ••
:label: ex-gen-alpha-flight-senza-guardian

Quante sono le disposizioni semplici dei quattro membri degli Alpha
Flight (vedi l’{prf:ref}`ex-disposizioni-con-ripetizione-1`) in tre posti che
non includono Guardian? Verificate sperimentalmente la risposta a questa
domanda generando tutte le disposizioni e contando quelle che lo escludono.
````
````{solution} ex-gen-alpha-flight-senza-guardian
:class: dropdown

Escludere Guardian equivale a non considerare uno dei possibili oggetti, e
quindi a focalizzarsi sulle disposizioni semplici di tre oggetti in tre posti,
che sono $d_{3, 3} = 6$, come confermato dal codice che segue.

```{code-cell} python
alpha_flight = ['g', 's', 'n', 'a']
no_g = [d for d in it.permutations(alpha_flight, 3) if 'g' not in d]
print(f'Il numero di disposizioni che non include Guardian è {len(no_g)}')
```
````

````{exercise} ••
:label: ex-verifica-formula

Scrivete una funzione `compute_combinatorics(n, k)` che, usando gli iteratori
di `itertools`, conta il numero di disposizioni con ripetizione,
disposizioni semplici e combinazioni semplici di `n` oggetti in `k` posti. La
funzione deve restituire un dizionario le cui chiavi sono le stringhe `'D'`,
`'d'` e `'c'`, associate rispettivamente alle disposizioni con ripetizione,
alle disposizioni semplici e alle combinazioni. Verificate che la funzione si
comporti correttamente nel caso in cui gli argomenti `n` e `k` sono
rispettivamente uguali a $5$ e $3$.
````
````{solution} ex-verifica-formula
:class: dropdown

Sebbene i valori richiesti si possano calcolare direttamente, viene richiesto
esplicitamente di utilizzare gli iteratori. È quindi possibile usare dei
generatori a partire da questi ultimi, che producono il valore costante $1$ per
ogni raggruppamento considerato. Sommando i valori generati si ottengono i
conteggi richiesti.

Il testo dell'esercizio non specifica quali oggetti considerare, ma solo
quanti. Siccome il calcolo degli indici combinatorici non dipende dalla
specifica natura degli oggetti, possiamo usare gli interi da $0$ al valore
contenuto in `n`, che vengono prodotti da `range` in modo efficiente.

```{code-cell} python
def compute_combinatorics(n, k):
    objects = range(n)
    disp_repeat = sum(1 for _ in it.product(objects, repeat=k))
    disp_simple = sum(1 for _ in it.permutations(objects, k))
    comb = sum(1 for _ in it.combinations(objects, k))
    return {'D': disp_repeat, 'd': disp_simple, 'c': comb}
```

Applicando le formule corrispondenti ai due tipi di disposizione e alle
combinazioni, si ottiene facilmente che $D_{5, 3} = 125$, $d_{5, 3} = 60$ e
$c_{5, 3} = 10$, cosa che possiamo verificare tramite delle semplici
asserzioni.

```{code-cell} python
result = compute_combinatorics(5, 3)

assert result['D'] == 125
assert result['d'] == 60
assert result['c'] == 10
```
````

````{exercise} ••
:label: ex-gen-cloni-dk-anagrammi

Generate tutte le permutazioni degli oggetti nel multiinsieme che contiene
due cloni di Dupli-Kate e tre di Multi-Paul, inserendo in un insieme tutte
le permutazioni semplici.
````
````{solution} ex-gen-cloni-dk-anagrammi
:class: dropdown

Nel paragrafo sulle permutazioni con ripetizione, le permutazioni venivano
inserite in un insieme _dopo_ essere state utilizzate, per evitare di
riconsiderarle in seguito. Qui, invece, viene richiesto di utilizzarlo per
aggregare le permutazioni, magari per un utilizzo futuro. Il modo più
intuitivo di procedere è quello di enumerare le permutazioni semplici,
inserendole tutte nell'insieme: questa operazione gestisce automaticamente
la presenza di doppioni, perché l'inserimento in un insieme di un elemento che
già vi appartiene non ha alcun effetto.

```{code-cell} python
clones = ['k', 'k', 'p', 'p', 'p']
distinct = set()
for p in it.permutations(clones):
    distinct.add(p)
print(distinct)
```

In realtà, è possibile riscrivere questo codice in modo molto più succinto.
Infatti, i costruttori di quasi tutti i tipi di dati strutturati che abbiamo
considerato accettano come argomenti anche degli iteratori, che vengono
automaticamente attraversati, inserendo via via gli elementi generati nella
struttura. Nel nostro caso, ciò permette di riscrivere la cella precedente nel
modo indicato di seguito.

```{code-cell} python
clones = ['k', 'k', 'p', 'p', 'p']
distinct = set(it.permutations(clones))

print(distinct)
```
````

````{exercise} ••
:label: ex-gen-doom-patrol-islice

Leggete la
[documentazione](https://docs.python.org/3/library/itertools.html#itertools.islice)
della classe `itertools.islice`, e utilizzatela per generare e stampare
solamente dieci permutazioni semplici dei cinque membri dei
[Doom Patrol](https://dc.fandom.com/wiki/Doom_Patrol) (Robotman, Negative Man,
Elasti-Girl, Crazy Jane, Flex Mentallo), senza generare né scorrere le
restanti $5! - 10 = 110$ permutazioni.
````
````{solution} ex-gen-doom-patrol-islice
:class: dropdown

La classe `islice` costruisce un iteratore a partire da un altro iteratore,
estrandone una sottosequenza. Nella sua forma più semplice, il costruttore
accetta l'iteratore di partenza e un numero intero $n$: l'iteratore
restituito produrrà solamente i primi $n$ elementi di quello originale.

```{code-cell} python
doom_patrol = ['Robotman', 'Negative Man', 'Elasti-Girl',
               'Crazy Jane', 'Flex Mentallo']
for p in it.islice(it.permutations(doom_patrol), 10):
    print(p)
```
````

````{exercise} ••
:label: ex-gen-peter-poteri-incompatibili

Stampate tutte le combinazioni di tre superpoteri, scelti tra telepatia,
invisibilità, psicocinesi, rigenerazione e precognizione, escludendo quelle
che contengono simultaneamente telepatia e psicocinesi. Quante sono queste
combinazioni?
````
````{solution} ex-gen-peter-poteri-incompatibili
:class: dropdown

```{code-cell} python
powers = ['telepatia', 'invisibilità', 'psicocinesi',
          'rigenerazione', 'precognizione']
valid = [c for c in it.combinations(powers, 3)
          if not ('telepatia' in c and 'psicocinesi' in c)]
print(f'Vi sono {len(valid)} combinazioni valide.')
```

Il numero di combinazioni valide si può ottenere anche ragionando nel modo
seguente: partendo dalle $c_{5, 3} = 10$ combinazioni totali, vanno sottratte
tutte quelle nelle quali due dei tre posti sono occupati da telepatia e
psicocinesi; siccome l'unico posto rimanente potrà contenere uno tra i
superpoteri restanti, vi sono esattamente tre combinazioni da rimuovere.
Pertanto, avremo sette combinazioni valide.

````

````{exercise} •••
:label: ex-gen-young-avengers-squadre

Scrivete un generatore Python che, dato un elenco di eroi e un
intero $k$, produca tutte le coppie di squadre disgiunte di $k$ eroi ciascuna.
Verificate il comportamento del generatore utilizzando i nove
[Young Avengers](https://marvel.fandom.com/wiki/Young_Avengers) (Patriot,
Hulkling, Wiccan, Speed, Stature, Vision, Kate Bishop, Noh-Varr e Jonas) e
$k = 2$, tenendo conto che il numero di coppie di squadre &mdash; in questo
caso &mdash; deve essere uguale a $c_{9,2} \cdot c_{7,2} = 36 \cdot 21 = 756$.
````
````{solution} ex-gen-young-avengers-squadre
:class: dropdown

```{code-cell} python
def disjoint_teams(heroes, k):
    for team_1 in it.combinations(heroes, k):
        remaining = [e for e in heroes if e not in team_1]
        for team_2 in it.combinations(remaining, k):
            yield team_1, team_2

young_avengers = ['Patriot', 'Hulkling', 'Wiccan', 'Speed',
                  'Stature', 'Vision', 'Kate Bishop', 'Noh-Varr', 'Jonas']
num_pairs = sum(1 for _ in disjoint_teams(young_avengers, 2))
assert num_pairs == 756
```
````
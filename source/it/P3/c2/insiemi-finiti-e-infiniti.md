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

(sec_insiemi-finiti-e-infiniti)=
# Insiemi finiti e infiniti
Non è difficile pensare a insiemi che contengono un numero finito di elementi,
come ad esempio l'insieme dei membri della Justice League, quello dei giorni
della settimana e quello dei numeri primi minori di $100$. Diciamo che insiemi di questo tipo sono _finiti_. Esistono però anche insiemi che non contengono un
numero finito di elementi, come l'insieme di tutte le frazioni o quello dei
punti del piano. Per questi insiemi _infiniti_ si distinguono due casi:

```{margin}
In matematica si dice semplicemente _numerabile_ ogni insieme i cui elementi
possono essere elencati in una sequenza finita o infinita; gli insiemi finiti
sono quindi anch'essi numerabili.
```
- si dice che un insieme è _infinito numerabile_ quando risulta possibile
  costruire una sequenza (infinita) $x_1, x_2, \dots$ che contiene in qualche
  posizione ognuno dei suoi elementi: l'insieme $D$ dei numeri dispari, che
  introdurrò tra poco, è un esempio di insieme infinito numerabile;
- in tutti gli altri casi si dice che l'insieme è _infinito non numerabile:_
  l'insieme dei punti di una retta e l'insieme dei numeri reali sono entrambi
  infiniti e non numerabili.

La modalità di descrizione estensiva non è, strettamente parlando, adottabile
per gli insiemi infiniti, visto che per definizione non è possibile elencare
tutti i loro elementi. Quando però un insieme infinito numerabile è associabile
a una sequenza che si può intuitivamente continuare dopo avere visto solo
alcuni tra i suoi elementi iniziali, risulta accettabile estendere la
descrizione estensiva elencando solo questi elementi, aggiungendo poi dei punti
di sospensione per enfatizzare il carattere infinito dell'insieme. Ad esempio,
sebbene la descrizione intensiva

```{math}
D = \{ 2n+1 \mid n \in \mathbb N \}
```

sia quella più precisa per indicare l'insieme dei numeri dispari, in molti
contesti viene utilizzata anche la formulazione estensiva
$D = \{1, 3, 5, 7, 9, \dots \}$. Va però tenuto presente che una sequenza
parziale non può identificare un insieme in modo univoco: nel caso precedente,
i primi termini $1, 3, 5, 7, 9$ potrebbero in linea di principio riferirsi
anche all'insieme dei numeri dispari minori di $100$, oppure a una qualsiasi
altra successione che coincide con quella dei dispari sui primi elementi ma poi
diverge. I puntini di sospensione suggeriscono quali siano gli elementi
restanti, ma non li definiscono in modo rigoroso, e per questo la descrizione
intensiva rimane quella formalmente corretta. A maggior ragione, le descrizioni
estensive non riescono a cogliere la complessità degli insiemi infiniti non
numerabili, per i quali sono generalmente utilizzabili solo descrizioni di tipo
intensivo.

## Esercizi

````{exercise}
:label: ex-suicide-squad

La [Suicide Squad](https://dc.fandom.com/wiki/Suicide_Squad_(Prime_Earth)) è
composta da sei membri: Emerald Empress, Doctor Polaris, Johnny Sorrow, Lobo,
Rustam e Cyclotron, ciascuno dei quali può essere operativo oppure fuori
combattimento. Lo stato del gruppo è descritto da un vettore
$(x_1, x_2, x_3, x_4, x_5, x_6)$, dove per ogni $i = 1, \dots 6$, $x_i$ è
uguale a $1$ se l'$i$-esimo membro (nell'ordine precedente) è operativo, e $0$ altrimenti. Rispondete alle seguenti domande.

1. Da quanti elementi è formato l'insieme di tutti i possibili stati del
   gruppo?
2. Sia $A$ l'insieme degli stati in cui almeno uno tra i membri $1$ e $2$ sono
   operativi, e almeno uno tra i membri $3$ e $4$ sono operativi. Scrivete del
   codice Python che elenca tutti gli elementi di $A$.
3. Sia $B$ l'insieme degli stati in cui i membri $1$ e $3$ sono entrambi fuori
   combattimento. Quanti elementi contiene $B$?
````
````{solution} ex-suicide-squad
:class: dropdown

1. Indipendentemente da $i$, ogni componente $x_i$ può assumere due valori
   distinti, quindi il principio fondamentale del calcolo combinatorio ci
   permette di dire che l'insieme di tutti gli stati ha $2^6 = 64$ elementi.

2. Deve risultare $(x_1=1 \vee x_2=1)$ e $(x_3=1 \vee x_4=1)$.
   Le coppie $(x_1, x_2)$ che soddisfano la prima condizione sono tre:
   $(1,0),(0,1),(1,1)$. Analogamente, esistono tre configurazioni per
   $(x_3, x_4)$. Al contrario, $(x_5, x_6)$ può assumere tutte le quattro
   configurazioni possibili. Sempre per il principio fondamentale del calcolo
   combinatorio, avremo $|A| = 3 \times 3 \times 4 = 26$, e
   gli elementi di $A$ sono tutti e soli i vettori con $(x_1, x_2) \neq (0,0)$
   e $(x_3, x_4) \neq (0,0)$, come confermato dall'output del codice che segue.

```{code-cell} python
import itertools as it

v = (0, 1)
teams = [t for t in it.product(v, repeat=6)
           if (t[0] or t[1]) and (t[2] or t[3])]
for t in teams:
    print(t)
```

3. Fissati $x_1=0$ e $x_3=0$, le rimamenti componenti $x_2$, $x_4$, $x_5$ e
   $x_6$ sono libere, quindi $|B| = 2^4 = 16$.
````

````{exercise}
:label: ex-new-warriors

I [New Warriors](https://marvel.fandom.com/wiki/New_Warriors_(Earth-616)) sono
un gruppo di supereroi Marvel composto, in una delle loro formazioni, da sei
membri: Night Thrasher, Firestar, Justice, Namorita, Speedball e Nova. Per
ciascuno dei seguenti insiemi, stabilite se è finito, infinito numerabile
oppure infinito non numerabile, motivando la vostra risposta.

1. L'insieme $W$ dei sei membri dei New Warriors.
2. L'insieme $M$ dei possibili numeri di missione assegnati progressivamente
   al gruppo a, partire da $1$, cioè $M = \{1, 2, 3, 4, \dots\}$.
3. L'insieme $C$ di tutte le coppie $(i, n)$ dove
   $i \in [1 .. 6]$ indica uno dei sei membri e $n \in \mathbb{N}$ indica il
   numero della missione che guida.
4. L'insieme $V$ di tutti i possibili valori reali (in km/h) della velocità
   con cui Nova può volare, sapendo che la velocità è compresa nell'intervallo
   $[0, 10^6]$.
````
````{solution} ex-new-warriors
:class: dropdown

1. $W$ è finito: contiene esattamente $6$ elementi, uno per ciascun membro
   elencato.
2. $M$ è infinito numerabile: siccome non è noto a priori il numero totale di
   missioni che i New Warriors faranno, ogni numero naturale è un possibile
   numero di missione. Dunque $M = \mathbb{N}$, che è per definizione
   numerabile.
3. $C$ è infinito numerabile. Per ogni $i$ fissato, esistono infiniti valori
   di $n$, quindi $C$ è infinito. Per mostrare la numerabilità, si costruisce
   la sequenza $(1,1), (1,2), (1,3), \dots, (2,1), (2,2), \dots$ che, una volta
   terminati gli elementi con $i = j$, passa a $i = j+1$. Poiché si
   concatenano sei sequenze, e ciascuna di queste è numerabile, il risultato è
   ancora una sequenza numerabile che elenca tutti gli elementi di $C$.
4. $V$ è infinito non numerabile: i possibili valori reali di velocità
   appartengono all'intervallo $[0, 10^6]$ formano un sottoinsieme di
   $\mathbb{R}$, e ogni intervallo di numeri reali non è numerabile.
````

````{exercise}
:label: ex-great-lakes-avengers

I [Great Lakes
Avengers](https://marvel.fandom.com/wiki/Great_Lakes_Avengers_(Earth-616))
sono un eccentrico gruppo Marvel composto da sei membri: Big Bertha,
Doorman, Flatman, Mr. Immortal, Dinah Soar e Grasshopper. Prima di ogni
missione, il gruppo assegna tre ruoli distinti &mdash; leader, tattico e
ricognitore &mdash; a tre membri distinti. L'ordine dei ruoli è significativo
(ricoprire il ruolo di leader è diverso dall'essere tattico). Sia $R$
l'insieme di tutte le possibili assegnazioni di ruoli.

1. Quanti elementi contiene $R$?
2. Sia $D$ l'insieme delle assegnazioni in cui Doorman ricopre uno dei tre
   ruoli. Quanti elementi contiene $D$?
3. Scrivete del codice Python che elenca tutti gli elementi di $R$ e verificate
   i risultati dei punti 1 e 2.
````
````{solution} ex-great-lakes-avengers
:class: dropdown

1. Dobbiamo scegliere, in ordine, tre membri distinti tra sei, dunque stiamo
   considerando le disposizioni semplici di sei oggetti (gli eroi) in
   tre posti (i ruoli). Dunque $|R| = d_{6, 3} = 6 \times 5 \times 4 = 120$.

2. Doorman può ricoprire uno qualsiasi dei tre ruoli. Una volta scelto il ruolo
   di Doorman, i due ruoli restanti vengono assegnati selezionando due diversi
   tra i cinque membri rimanenti, cosa che si può fare in
   $d_{5, 2} = 5 \times 4 = 20$ modi. Quindi $|D| = 3 \times d_{5, 2} = 60$.

3. Nella cella seguente, per brevità, indico i supereroi come BB (Big Bertha),
   DM (Doorman), FM (Flatman), MI (Mr. Immortal), DS (Dinah Soar) e GH
   (Grasshopper). Usando `it.permutations' si possono generare tutte le
   disposizioni che corrispondono agli elementi di $R$, e selezionare tutte
   quelle che individuano le assegnazioni in $D$, stamparle e contarle.


```{code-cell} python
import itertools as it

members = ['BB', 'DM', 'FM', 'MI', 'DS', 'GH']
roles  = ['leader', 'tattico', 'ricognitore']

R = it.permutations(members, 3)

D = [t for t in R if 'DM' in t]

print('Elementi di D:')
for i, a in enumerate(D):
    print('-'.join(a), end=', ' if (i+1) % 6 else '\n')

print(f"\n|D| = {len(D)}")
```
````

````{exercise}
:label: ex-doom-patrol

La [Doom Patrol](https://dc.fandom.com/wiki/Doom_Patrol_(New_Earth)) è una
squadra di supereroi emarginati, tra cui Robotman, Negative Man, Elasti-Girl
e Crazy Jane. Il loro archivio storico etichetta ogni scontro con una coppia di
numeri naturali positivi $(v, s)$, dove $v$ indica il numero di un fumetto ed
$s$ il numero dello scontro all'interno di quel fumetto. Sia
$A = \{ (v, s) : v, s \in \mathbb{N} \}$ l'insieme di tutte le possibili
etichette di scontro.

1. Dimostrate che $A$ è infinito.
2. Dimostrate che $A$ è numerabile costruendo esplicitamente una sequenza
   $a_1, a_2, a_3, \dots$ che elenca ogni elemento di $A$ in qualche posizione,
   e ricavate la formula per la posizione di un generico elemento $(v, s)$.
3. In quale posizione si trova $(3, 2)$ nella sequenza del punto precedente?
````
````{solution} ex-doom-patrol
:class: dropdown

1. Non esiste un «ultimo» numero, in linea di principio, dei fumetti. Quindi
   $A$ contiene tutte le coppie $(v, i)$, per $v \in \mathbb N$, ed è dunque
   un insieme infinito.

2. Si adotta la classica _enumerazione diagonale_: si considera la
   scomposizione $A = \cup_{k=2}^{+\infty} D_k$, dove 
   $D_k = \{ (v,s) \in A : v + s = k \}$ indica una _diagonale_ che contiene
   esattamente $k-1$ coppie, ordinate come
   $(1, k-1), (2, k-2), \dots, (k-1, 1)$. Ogni coppia $(v, s)$ appartiene
   a una e una sola diagonale, dunque considerando tutte le diagonali nel
   loro ordine ed enumerando i loro elementi, dopo un numero finito di passi
   si deve ottenere $(v, s)$. $A$ è quindi numerabile.

3. Per $(3, 2)$ si ha $k = 3 + 2 = 5$, dunque la coppia appartiene a $D_5$.
   Generando gli elementi della sequenza che corrispondono alle prime tre
   diagonali si verifica come $(3, 2)$ occorra in nona posizione:
   
   ```{math}
   \underbrace{(1,1)}_{D_2},
   \underbrace{(1,2), (2,1)}_{D_3},
   \underbrace{(1,3), (2,2), (3,1)}_{D_4},
   \underbrace{(1,4), (2,3), (3,2), (4, 1)}_{D_5} \enspace.
   ```

````

````{exercise}
:label: ex-estensiva-intensiva

Per ognuno dei seguenti insiemi, espressi in forma intensiva, scrivete &mdash;
ove possibile &mdash; la corrispondente descrizione estensiva, e indicate se
questa è precisa oppure solo parziale.

1. $A = \{ n \in \mathbb{N} \mid n^2 \leq 25 \}$.
2. $B = \{ n \in \mathbb{Z} \mid -3 \leq n \leq 3 \}$.
3. $C = \{ n \in \mathbb{N} \mid n \text{ è un multiplo di } 3 \}$.
4. $D = \{ x \in \mathbb{R} \mid 1 \leq x \leq 2 \}$.
````
````{solution} ex-estensiva-intensiva
:class: dropdown

1. $A = \{ 1, 2, 3, 4, 5 \}$. L'insieme è finito, quindi la descrizione
   estensiva è precisa: elenca esattamente tutti e soli gli elementi di $A$.

2. $B = \{ -3, -2, -1, 0, 1, 2, 3 \}$. Anche in questo caso l'insieme è finito
   e la descrizione estensiva è precisa.

3. Una possibile descrizione estensiva è $C = \{0, 3, 6, 9, \dots\}$. $C$
   è infinito numerabile, quindi la descrizione estensiva è solo parziale: i puntini di sospensione suggeriscono il pattern, ma non lo definiscono in
   modo rigoroso. In questo caso, per esempio, i quattro valori indicati
   individuano anche l'inizio della sequenza dei numeri composti dalle cifre
   in $\{ 0, 3, 6, 9 \}$, che continuerebbe con $30, 33, 36, 39, 60$ e così
   via.

4. $D$ è un intervallo di numeri reali, quindi è infinito non numerabile, e la
   descrizione estensiva non è utilizzabile. Non è possibile stilare un elenco
   parziale dei suoi elementi che sia significativo.
````

````{exercise}
:label: ex-intensiva-estensiva

Per ognuno dei seguenti insiemi, espressi in forma estensiva, scrivete una
descrizione intensiva equivalente.

1. $A = \{ \text{Thor}, \text{Iron Man}, \text{Captain America},
   \text{Hulk}, \text{Black Widow}, \text{Hawkeye} \}$.
2. $B = \{ 2, 4, 6, 8, \dots \}$.
3. $C = \{ 1, 4, 9, 16, 25, \dots \}$.
4. $D = \{ 0, 1 \}$.
````
````{solution} ex-intensiva-estensiva
:class: dropdown

1. Una possibile descrizione intensiva è
   $A = \{ x \mid x \text{ è un Avenger della formazione originale} \}$.

2. La sequenza indicata sugerisce che l'insieme contenga i numeri pari. In
   tal caso, due possibili descrizioni intensive sono
   $B = \{ n \in \mathbb N  \mid n \text{ è pari} \}$ e
   $B = \{ 2k \mid k \in \mathbb N \}$ (ma la stessa sequenza potrebbe
   continuare in modi diversi, ad esempio elencando tutti i numeri pari con
   le cifre uguali).

3. L'interpretazione più semplice suggerisce che nella descrizione estensiva
   siano indicati i primi quadrati perfetti (ma, anche in questo caso, ci
   possono essere altre interpretazioni). In tal caso, si può utilizzare la
   formulazione intensiva $C = \{ n^2 \mid n \in \mathbb N \}$, oppure
   $C = \{ n \in \mathbb N \mid \sqrt{n} \in \mathbb{N} \}$.

4. $D = \{ n \in \mathbb Z \mid 0 \leq n \leq 1 \}$, oppure
   $D = \{ x \in \mathbb R \mid x^2 = x \}$, o più semplicemente
   $D = \{ x \in \mathbb R \mid x = 0 \vee x = 1 \}$.
````
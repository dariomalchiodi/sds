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

(sec_assiomi-kolmogorov)=
# Assiomi di Kolmogorov 

Nel paragrafo precedente ho introdotto le algebre degli eventi, anticipando che
esse costituiscono il dominio di una funzione che associa a ciascun evento un
valore numerico, rappresentante la sua probabilità. L'approccio didattico
comunemente adottato per definire questa funzione opera in modo indiretto.
Invece di procedere in modo operativo, rifacendosi a una delle possibili
interpretazioni del concetto di probabilità (vedi il
{ref}`sec_concetto-probabilita`), si preferisce partire da una domanda più
generale: quali proprietà vanno rispettate quando si associa un numero a un
evento, se tale valore deve essere interpretato, in modo coerente e non
ambiguo, come una probabilità? La risposta a questa domanda è fornita dal
sistema assiomatico proposto da Andrej Nikolaevič Kolmogorov[^kolmogorov] nel
1933, che costituisce ancora oggi il fondamento della teoria della probabilità
moderna. 


```{figure} https://upload.wikimedia.org/wikipedia/commons/4/43/Andrej_Nikolajewitsch_Kolmogorov.jpg
---
figclass: margin
name: fig_kolmogorov
width: 200px
align: left
---
Ritratto di Andrej Nikolaevič Kolmogorov (Fotografia di Konrad Jacobs, © Mathematisches Forschungsinstitut Oberwolfach (MFO). Licenza CC BY-SA 2.0 DE. Fonte: [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Andrej_Nikolajewitsch_Kolmogorov.jpg)).
```
````{prf:definition} Assiomi di Kolmogorov
:label: def-assiomi-kolmogorov
Dato uno spazio degli esiti $\Omega$ su cui è definita un'algebra $\mathsf A$,
una _funzione di probabilità_ è qualsiasi funzione
$\mathbb P: \mathsf A \rightarrow \mathbb R$ che soddisfa i seguenti
_assiomi di Kolmogorov_:

1. la probabilità associata a un evento è sempre non negativa:
   ```{math}
   :label: kolmogorov-axiom-1
   \forall E \in \mathsf A \quad \mathbb P(E) \geq 0,
   ```
2. la probabilità associata allo spazio degli esiti è uguale a $1$:
   ```{math}
   :label: kolmogorov-axiom-2
   \mathbb P(\Omega) = 1,
   ```
3. la probabilità associata all'unione di due eventi disgiunti è uguale alla
   somma delle probabilità associate ai due eventi:
   ```{math}
   :label: kolmogorov-axiom-3
   \forall E, F \in \mathsf A \quad E \cap F = \varnothing \rightarrow
   \mathbb P(E \cup F) = \mathbb P(E) + \mathbb P(F).
   ```

Nel caso in cui $\mathsf A$ sia una sigma-algebra, quest'ultimo assioma si
estende a ogni successione infinita di eventi:

```{math}
:label: kolmogorov-axiom-3-sigma-algebra
\forall E_1, E_2, \ldots \in \mathsf A
\quad (\forall i \neq j \; E_i \cap E_j = \varnothing)
\rightarrow \mathbb P \left( \bigcup_{i=1}^{+\infty} E_i \right)
= \sum_{i=1}^{+\infty} \mathbb P (E_i).
```

La terna $(\Omega, \mathsf A, \mathbb P)$ viene detta _spazio di probabilità_.

````

<!-- CELL-MARKER-19-START -->
```{code-cell} python

import pandas as pd

heroes = pd.read_csv('data/heroes.csv')

heroes_aligned = heroes[heroes['alignment'].isin(['Good', 'Bad', 'Neutral'])]
n = len(heroes_aligned)

good = len(heroes_aligned[heroes_aligned['alignment'] == 'Good'])
bad = len(heroes_aligned[heroes_aligned['alignment'] == 'Bad'])
neutral = len(heroes_aligned[heroes_aligned['alignment'] == 'Neutral'])

print(f'Numero totale di supereroi con allineamento noto: {n}')
print(f'- Eroi (Good): {good} → P(G) = {good}/{n} = {good/n:.2f}')
print(f'- Cattivi (Bad): {bad} → P(B) = {bad}/{n} = {bad/n:.2f}')
print(f'- Neutrali (Neutral): {neutral} → P(N) = {neutral}/{n} = {neutral/n:.2f}')
print(f'\nVerifica: P(G) + P(B) + P(N) = {(good+bad+neutral)/n:.2f}')
```
<!-- CELL-MARKER-19-END -->

````{prf:example} Esempio: l'universo dei supereroi
:label: ex-frequentista

Consideriamo un esperimento casuale in cui si estrae a caso un supereroe dal
database dei supereroi usato nel libro, considerando solo i personaggi per i
quali è noto l'allineamento. Lo spazio degli esiti $\Omega$ è l'insieme di
tutti questi supereroi. Definiamo gli eventi $G$, $b$ e $N$ che si verificano
rispettivamente quando l'allineamento del supereroe osservato è buono, cattivo
e neutrale. Consideriamo poi l'algebra $\mathsf A$ indotta su $\Omega$ da
questi tre eventi, e su questa definiamo inizialmente $\mathbb P$ come la
funzione che associa a ogni evento la sua probabilità intesa in senso
frequentistico, cioè espressa dal rapporto tra il numero di casi favorevoli
nel dataset e il numero totale di casi.

<!-- CELL-PLACEHOLDER-19 -->

Se consideriamo l'unione di due eventi in $\mathsf A$, per esempio $G \cup B$,
è naturale estendere $\mathbb P$ in modo che l'interpretazione frequentista
valga anche per questo nuovo evento, così che $\mathbb P(G \cup B)$ sia uguale
alla frequenza con cui nel dataset considerato si trovi un supereroe con
allineamento morale buono o cattivo. Il fatto che questi due eventi siano
disgiunti (ogni supereroe ha un unico allineamento morale), permette di
scrivere $\mathbb P(G \cup B) = \mathbb P(G) + \mathbb P(B)$. Procedendo in
questo modo, è possibile estendere $\mathbb P$ a tutti gli eventi dell'algebra.
Questa costruzione garantisce la validità degli assiomi di Kolmogorov:

- tutti i valori di $\mathbb P$ sono maggiori o uguali di zero, essendo
  delle frequenze relative;
- $\mathbb P(\Omega) = \mathbb P(G) + \mathbb P(B) + \mathbb P(N) = 1$ per
  definizione;
- sempre per definizione, la probabilità dell'unione di eventi disgiunti in
  $\mathsf A$ è uguale alla somma della probabilità dei singoli eventi.
````

Grazie agli assiomi di Kolmogorov, $\mathbb P$ viene caratterizzata
esclusivamente attraverso le proprietà formali che essa deve rispettare:
qualunque funzione che soddisfi tali proprietà è una funzione di probabilità,
indipendentemente dal _significato_ che viene dato al concetto stesso di
probabilità, garantendo al contempo che agli eventi vengano assegnate delle
probabilità secondo uno schema _coerente_.


````{admonition} Probabilità e percentuali
:name: adm-percentuali

Gli assiomi di Kolmogorov richiedono che i valori di probabilità siano numeri
reali compresi tra $0$ e $1$. Nella pratica, tuttavia &mdash; e soprattutto nel
linguaggio comune &mdash; è molto frequente esprimere le probabilità in termini
di percentuali, su una scala da $0$ a $100$. Una percentuale si interpreta
sempre in modo relativo: è definita rispetto a una popolazione di riferimento
e, quando esprime una probabilità, fa implcitamente riferimento all'esperimento
casuale che consiste nell'estrarre a caso un individuo da tale popolazione.
Dire, ad esempio, che un evento ha probabilità del $30\%$ significa affermare
che, se si dovessero osservare $100$ individui, mediamente $30$ di questi
verificherebbero l'evento. Equivalentemente, eseguendo un numero elevato di
osservazioni, la frequenza relativa con cui si verifica l'evento si avvicina a
$0.3$, così che questo modo di ragionare rispecchia l'interpretazione
frequentista del concetto di probabilità. In ogni caso, al di là
dell'interpretazione adottata, ciò che conta è che la probabilità rimanga
all'interno di un intervallo prefissato: usare la scala $[0,1]$ o la scala
$[0,100]$ non ne altera il significato matematico, ma soltanto la
rappresentazione numerica.
````


A partire dagli assiomi di Kolmogorov è possibile derivare, per via puramente
deduttiva, un insieme di teoremi di carattere generale, la cui validità è
indipendente dall'interpretazione che si attribuisce al concetto di
probabilità.

````{prf:theorem} Probabilità dell'evento complementare
:label: probabilita-evento-complementare

```{math}
\forall E \subseteq \Omega \quad \mathbb P(\overline E) = 1 - \mathbb P(E).
```
````
````{admonition} _
:class: myproof

Dato un generico $E \subseteq \Omega$, si ha $E \cup \overline E = \Omega$ e
$E \cap \overline E = \varnothing$, pertanto

```{math}
1 = \mathbb P(\Omega) = \mathbb P(E \cup \overline E)
  = \mathbb P(E) + \mathbb P(\overline E),
```
dove il primo e l'ultimo passaggio sono basati sul secondo e terzo assioma di
Kolmogorov, rispettivamente. La tesi si ottiene ricavando
$\mathbb P(\overline E)$.

````

<!-- CELL-MARKER-20-START -->
```{code-cell} python

n = len(heroes)
marvel = len(heroes[heroes['creator'] == 'Marvel Comics'])

print(f'Numero di supereroi Marvel: {marvel}')
print(f'Numero totale di supereroi: {n}')
print(f'P(M) = {marvel}/{n} = {marvel / n:.2f}')
```
<!-- CELL-MARKER-20-END -->

````{prf:example} Esempio: supereroi non Marvel
:label: ex-non-marvel

Proseguendo l’{prf:ref}`ex-frequentista`, consideriamo l'evento $M$ che
corrisponde all'osservazione di un supereroe Marvel e calcoliamone la
probabilità.

<!-- CELL-PLACEHOLDER-20 -->

L'evento complementare $\overline M$ rappresenta l'osservazione di un
supereroe non Marvel &mdash; quindi appartenente a un altro universo, come
quello DC Comics, o è un personaggio indipendente. Per il teorema sulla
probabilità dell'evento complementare, si ha

$$\mathbb P(\overline M) =
1 - \mathbb P(M) = 1 - 0.18 = 0.82 \enspace.$$

Questo significa che c'è l’$82\%$ di probabilità di estrarre un supereroe
che non appartenga all'universo Marvel.

````

````{prf:corollary} Probabilità dell'evento impossibile
:label: probabilita-evento-impossibile

```{math}
\mathbb P(\varnothing) = 0
```
````
````{admonition} _
:class: myproof

La tesi si ottiene dal {prf:ref}`probabilita-evento-complementare`,
quando $E = \Omega$.
````

````{prf:theorem} Probabilità dell'unione di eventi
:label: probabilita-unione-eventi

```{math}
\forall E, F \subseteq \Omega \quad \mathbb P(E \cup F) =
\mathbb P(E) + \mathbb P(F) - \mathbb P(E \cap F).
```
````
````{admonition} _
:class: myproof

Per la distributività dell'intersezione rispetto all'unione si ha

```{math}
(E \cap \overline F) \cup (E \cap F) = E \cap (\overline F \cup F)
= E \cap \Omega = E,
```

inoltre sfruttando le proprietà di associatività, commutatività e idempotenza
si ottiene

```{math}
(E \cap \overline F) \cap (E \cap F) =
(E \cap E) \cap (F \cap \overline F) = E \cap \varnothing = \varnothing.
```

Per il terzo assioma di Kolmogorov, si ha dunque
$\mathbb P(E) = \mathbb P(E \cap \overline F) + \mathbb P (E \cap F)$, e in
modo analogo si dimostra che
$\mathbb P(F) = \mathbb P(\overline E \cap F) + \mathbb P (E \cap F)$, che
equivale a
$\mathbb P(\overline E \cap F) = \mathbb P(F) - \mathbb P (E \cap F)$ (vedi
{numref}`fig_venn-union-theorem`).


Si verifica facilmente che $E \cap \overline F$, $E \cap F$ e
$\overline E \cap F$ sono a due a due disgiunti e che la loro unione coincide
con $E \cup F$, pertanto per l'estensione del terzo assioma di Kolmogorov
all'unione di tre insiemi disgiunti si ha

```{math}
\mathbb P(E \cup F) =
\underbrace{\mathbb P(E \cap \overline F) + \mathbb P(E \cap F)}_{\mathbb P(E)}
+
\underbrace{\mathbb P(\overline E \cap F)}_{\mathbb P(F) - \mathbb P(E \cap F)}
```
da cui segue la tesi.
````

```{code-cell} python
:tags:  [hide-input]

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib_venn import venn2_circles, venn2

venn_set_edge = '#333333'
background_color = '#eaf3f5'
font_size = 7



# Three distinct blue shades
color_E_only    = '#AED6F1'  # light blue  → E \ F  (region '10')
color_intersect = '#2E86C1'  # medium blue → E ∩ F  (region '11')
color_F_only    = '#1A5276'  # dark blue   → F \ E  (region '01')

fig, ax = plt.subplots()

# Set both the axes and figure background
ax.set_facecolor(background_color)
fig.patch.set_facecolor(background_color)

# Rectangle for the universal set Ω
r = patches.Rectangle((-0.75, -0.6), 1.5, 1.1,
                       edgecolor=venn_set_edge,
                       facecolor=background_color, alpha=1, lw=0.7)
ax.add_patch(r)

v = venn2(subsets=(3, 3, 1), set_labels=(r'$E$', r'$F$'), ax=ax)
c = venn2_circles(subsets=(3, 3, 1), ax=ax)

for l in v.set_labels:
    l.set_fontsize(font_size)

for contour in c:
    contour.set_lw(0.7)
    contour.set_edgecolor(venn_set_edge)

# Color each region with a distinct blue shade
v.get_patch_by_id('10').set_color(color_E_only)     # E \ F
v.get_patch_by_id('10').set_alpha(1)

v.get_patch_by_id('11').set_color(color_intersect)  # E ∩ F
v.get_patch_by_id('11').set_alpha(1)

v.get_patch_by_id('01').set_color(color_F_only)     # F \ E
v.get_patch_by_id('01').set_alpha(1)

v.get_label_by_id('10').set_text(r'$E \cap \overline{F}$')
v.get_label_by_id('10').set_fontsize(font_size)

v.get_label_by_id('11').set_text(r'$E \cap F$')
v.get_label_by_id('11').set_fontsize(font_size)

v.get_label_by_id('01').set_text(r'$\overline{E} \cap F$')
v.get_label_by_id('01').set_fontsize(font_size)

ymin, ymax = ax.get_ylim()
ax.set_ylim(ymin - 0.1, ymax)
ax.text(0.55, 0.4, r'$\Omega$', fontsize=font_size)

plt.show()
```
````{customfigure}
:name: fig_venn-union-theorem

Il diagramma di Venn che illustra la scomposizione di $E \cup F$ nell'unione
disgiunta di $E \cap \overline F$, $E \cap F$ ed $\overline E \cap F$.
````

<!-- CELL-MARKER-21-START -->
```{code-cell} python

strong_filter = (heroes['strength'] >= 80)
strong = len(heroes[strong_filter])

intelligent_filter = (heroes['intelligence'] == 'High')
intelligent = len(heroes[intelligent_filter])
intersection_filter = strong_filter & intelligent_filter

both = len(heroes[intersection_filter])

print(f'Numero di supereroi forti: {strong}')
print(f'P(F) = {strong / n :.2f}')

print(f'Numero di supereroi intelligenti: {intelligent}')
print(f'P(I) = {intelligent / n :.2f}')

print(f"Numero di supereroi nell'intersezione: {both}")
print(f'P(F ∩ I) = {both / n :.2f}')
```
<!-- CELL-MARKER-21-END -->

<!-- CELL-MARKER-22-START -->
```{code-cell} python
heroes[intersection_filter].sample(5)['name'].tolist()
```
<!-- CELL-MARKER-22-END -->

````{prf:example} Esempio: supereroi con superforza o superintelligenza
:label: ex-union

Nel nostro database di supereroi, definiamo due eventi $F$ e $I$, che si
verificano rispettivamente quando viene osservato un supereroe con un indice di
forza maggiore o uguale a $80$ (un supereroe «forte») e con un livello di 
intelligenza uguale a `'High'` (un supereroe «intelligente»). Come nei due
esempi precedenti, calcoliamo la probabilità di $F$, $I$ e $F \cap I$ usando
l'interpretazione frequentista.

<!-- CELL-PLACEHOLDER-21 -->

Vi sono dunque più di tremila supereroi che sono sia forti che intelligenti,
come esemplificato dal codice seguente.

<!-- CELL-PLACEHOLDER-22 -->

Per calcolare la probabilità che un supereroe estratto a caso sia forte
oppure intelligente, possiamo applicare il
{prf:ref}`probabilita-unione-eventi`, ottenendo

$$\mathbb P(F \cup I) = \mathbb P(F) + \mathbb P(I) - \mathbb P(F \cap I) =
0.31 + 0.27 - 0.18 = 0.4 \enspace.$$

Se non avessimo sottratto $\mathbb P(F \cap I)$, avremmo contato due volte i
supereroi che possiedono entrambe le caratteristiche.

````
Quando i due eventi sono disgiunti, la tesi del
{prf:ref}`probabilita-unione-eventi` coincide con il terzo assioma di
Kolmogorov. Il teorema seguente estende il calcolo della probabilità
dell'unione a un numero arbitrario di eventi, enunciando il cosiddetto
_principio di inclusione-esclusione_.

````{prf:theorem} Principio di inclusione-esclusione
:label: teo-inclusione-esclusione

Dati tre eventi $E, F, G \in \mathsf A$, si ha
```{math}
\mathbb P(E \cup F \cup G) = \mathbb P(E) + \mathbb P(F) + \mathbb P(G)
- \mathbb P(E \cap F) - \mathbb P(E \cap G) - \mathbb P(F \cap G)
+ \mathbb P(E \cap F \cap G) \enspace.
```

Più in generale, dati $n$ eventi $E_1, \dots, E_n$,

```{math}
\mathbb P(E_1 \cup \dots \cup E_n) = \sum_{i=1}^n \mathbb P(E_i) -
\sum_{i < j} \mathbb P(E_i \cap E_j) \\ +
\sum_{i < j < k} \mathbb P(E_i \cap E_j \cap E_k) + \dots + (-1)^{n+1}
\mathbb P(E_1 \cap \dots \cap E_n) \enspace,
```

  o, in forma più compatta,

```{math}
\mathbb P \left(\bigcup_{i=1}^n E_i\right) =
\sum_{\emptyset \neq S \subseteq \{1, \dots, n\}} (-1)^{|S|+1}
\mathbb P\left(\bigcap_{i \in S} E_i\right) \enspace.
```
````
````{admonition} _
:class: myproof

La prima formula è un caso particolare della seconda, che si può dimostrare
usando il procedimento di induzione matematica (vedi
{ref}`ex-inclusione-esclusione`).
````

````{prf:theorem}
:label: teo_prob_sottoinsiemi

```{math}
\forall E, F \subseteq \Omega \quad E \subseteq F \rightarrow
\mathbb P(E) \leq \mathbb P(F).
```
````
````{admonition} _
:class: myproof

Siccome $F = E \cup (F \cap \overline E)$ ed $E$ e $F \cap \overline E$ sono
disgiunti, come evidenziato nella {numref}`fig_venn-subset-theorem`, per il terzo
assioma di Kolmogorov si ha
$\mathbb P(F) = \mathbb P(E) + \mathbb P(F \cap \overline E) \geq \mathbb P(E)$.
````

```{code-cell} python
:tags:  [hide-input]

import matplotlib.pyplot as plt
import matplotlib.patches as patches

venn_set_edge = '#333333'
background_color = '#eaf3f5'
font_size = 7

# Two distinct blue shades
color_E = '#2E86C1'          # medium blue → E
color_F_minus_E = '#AED6F1'  # light blue  → F \ E

fig, ax = plt.subplots()

# Set both the axes and figure background
ax.set_facecolor(background_color)
fig.patch.set_facecolor(background_color)

# Rectangle for the universal set Ω
r = patches.Rectangle((-0.75, -0.6), 1.5, 1.1,
                       edgecolor=venn_set_edge,
                       facecolor=background_color, alpha=1, lw=0.7)
ax.add_patch(r)

# Outer circle F (larger)
circle_F = patches.Circle((0, 0), 0.4, edgecolor=venn_set_edge,
                            facecolor=color_F_minus_E, lw=0.7)
ax.add_patch(circle_F)

# Inner circle E (smaller, subset of F)
circle_E = patches.Circle((-0.1, 0), 0.2, edgecolor=venn_set_edge,
                           facecolor=color_E, lw=0.7)
ax.add_patch(circle_E)

# Labels
ax.text(-0.1, 0, r'$E$', fontsize=font_size, ha='center', va='center')
ax.text(0.2, 0.15, r'$F\, \cap \overline{E}$', fontsize=font_size,
        ha='center', va='center')
ax.text(-0.35, 0.35, r'$F$', fontsize=font_size, ha='center', va='center')
ax.text(0.55, 0.4, r'$\Omega$', fontsize=font_size)

ax.set_xlim(-0.8, 0.8)
ax.set_ylim(-0.65, 0.55)
ax.set_aspect('equal')
ax.axis('off')

plt.show()
```
````{customfigure}
:name: fig_venn-subset-theorem

Il diagramma di Venn che illustra la scomposizione $F = E \cup (F \cap
\overline E)$ quando $E \subseteq F$: l'evento $F$ è l'unione disgiunta
degli eventi $E$ ed $F \cap \overline E$.
````

<!-- CELL-MARKER-23-START -->
```{code-cell} python

import re

xmen_names = ['Wolverine', 'Cyclops', 'Storm', 'Beast', 'Rogue', 'Gambit', 
              'Nightcrawler', 'Colossus', 'Iceman', 'Angel', 'Jean Grey', 
              'Professor X', 'Magneto', 'Mystique', 'Psylocke', 'Jubilee',
              'Shadowcat', 'Kitty Pryde', 'Cable', 'Bishop', 'Havok',
              'Polaris', 'Emma Frost', 'X-23', 'Banshee', 'Phoenix',
              'Marvel Girl', 'Apocalypse', 'Mister Sinister']

pattern = '|'.join([f'^{re.escape(name)}' for name in xmen_names])

marvel_filter = (heroes['creator'] == 'Marvel Comics')
xmen_filter = marvel_filter & heroes['name'].str.match(pattern, case=False, na=False)

marvel_count = len(heroes[marvel_filter])
xmen_count = len(heroes[xmen_filter])

print(f'Supereroi Marvel: {marvel_count}')
print(f'X-Men: {xmen_count}')
print(f'Numero totale di supereroi: {n}')
print()
print(f'P(M) = {marvel_count}/{n} = {marvel_count/n:.2f}')
print(f'P(X) = {xmen_count}/{n} = {xmen_count/n:.2f}')
print()
print(f'Verifica X ⊆ M: P(X) ≤ P(M)? {xmen_count/n:.3f} ≤ {marvel_count/n:.2f} → {xmen_count <= marvel_count}')
```
<!-- CELL-MARKER-23-END -->

````{prf:example} Esempio: X-Men e supereroi Marvel
:label: ex-prob-subsets

Continuando gli esempi precedenti, consideriamo gli eventi:

- $M$: «il supereroe appartiene all'universo Marvel»,
- $X$: «il supereroe è un X-Man».

Poiché tutti gli X-Men sono personaggi Marvel, abbiamo $X \subseteq M$.
Calcoliamo le probabilità usando il dataset: per identificare gli X-Men,
consideriamo i supereroi Marvel il cui nome corrisponde a uno dei membri
classici del gruppo.[^xmen-nota]

<!-- CELL-PLACEHOLDER-23 -->

Per il {prf:ref}`teo_prob_sottoinsiemi`, $\mathbb P(X) \leq \mathbb P(M)$, e
questo è confermato dai dati. Intuitivamente, la probabilità di estrarre un
X-Man non può superare quella di estrarre un supereroe Marvel, perché ogni
X-Man è un supereroe Marvel.
````

[^xmen-nota]: Questa identificazione è necessariamente approssimativa: il
dataset non contiene un campo esplicito per l'appartenenza agli X-Men, e
alcuni nomi (come Storm o Angel) potrebbero corrispondere a personaggi
non correlati al gruppo mutante.

[^kolmogorov]: Ho scelto di fare riferimento allo standard [ISO
9](https://it.wikipedia.org/wiki/Traslitterazione_scientifica_del_cirillico)
per traslitterare dall'alfabeto cirillico a quello latino, così che il nome
originale Андре́й Никола́евич Колмого́ров diventa Andrej Nikolaevič Kolmogorov.
In realtà, esistono varie forme di traslitterazione, che dipendono anche dalla
lingua di destinazione. Per questo motivo, nella letteratura e nei testi di
riferimento si possono trovare denominazioni differenti dello stesso autore:
per esempio, nel momento in cui scrivo questa nota (aprile 2026),
[Wikipedia](https://wikipedia.org) utilizza Andrey Nikolaevich Kolmogorov nella
versione in inglese, Andreï Nikolaïevitch Kolmogorov in quella francese, Andrei
Nikolajewitsch Kolmogorow in quella tedesca e Andrej Nikolaevič Kolmogorov in
quella italiana.



## Esercizi

In tutti gli esercizi che seguono, ove non esplicitamente indicato,
presuppongo che sia stato fissato uno spazio $(\Omega, \mathsf A, \mathbb P)$
nel quale considerare i vari eventi. 

````{exercise} ••
:label: ex-sub-additivity
Dimostrate che vale la seguente proprietà di _sub-additività_ per la funzione
di probabilità:

```{math}
\forall E_1, \dots, E_n \quad \mathbb P \left( \bigcup_{i=1}^n E_i  \right)
\leq \sum_{i=1}^n \mathbb P(E_i) \enspace.
```
````
````{solution} ex-sub-additivity
:class: dropdown

Procediamo per induzione su $n$.

__Caso base__ ($n = 2$). Per il {prf:ref}`probabilita-unione-eventi`,
$\mathbb P(E_1 \cup E_2) = \mathbb P(E_1) + \mathbb P(E_2) -
\mathbb P(E_1 \cap E_2)$. Per il primo assioma di Kolmogorov,
$\mathbb P(E_1 \cap E_2) \geq 0$, così che
$\mathbb P(E_1 \cup E_2) \leq \mathbb P(E_1) + \mathbb P(E_2)$.

__Passo induttivo__. Supponiamo che la proprietà valga per $n-1$ eventi.
Allora:

$$\mathbb P \left( \bigcup_{i=1}^n E_i \right) =
\mathbb P \left( \left(\bigcup_{i=1}^{n-1} E_i\right) \cup E_n \right)
\leq \mathbb P \left( \bigcup_{i=1}^{n-1} E_i \right) + \mathbb P(E_n)
\leq \sum_{i=1}^{n-1} \mathbb P(E_i) + \mathbb P(E_n) =
\sum_{i=1}^n \mathbb P(E_i) \enspace.$$

````

````{exercise} •
:label: ex-heroes-complement
Usando gli [Sling Ring](https://marvel.fandom.com/wiki/Sling_Ring),
[Doctor Strange](https://marvel.fandom.com/wiki/Doctor_Strange) è in grado di
aprire dei portali dimensionali, ma se si trova in situazioni di stress o se i
suoi poteri sono ridotti, non sempre questo potere ha effetto. Se la
probabilità con cui Doctor Strange riesce ad attivare gli Sling Ring è 0.63,
qual è la probabilità con cui l'attivazione non ha effetto?
````
````{solution} ex-heroes-complement
:class: dropdown

Se indichiamo con $S$ l'evento «gli Sling Ring aprono un portale dimensionale»,
così che $\mathbb P(S) = 0.63$, la probabilità richiesta si ottiene facilmente
grazie al {prf:ref}`probabilita-evento-complementare`:

```{math}
\mathbb P(\overline S) = 1 - \mathbb P(S) = 1 - 0.63 = 0.37 \enspace.
```
````

````{exercise} ••
:label: ex-heroes-union
[Dupli-Kate](https://comicvine.gamespot.com/dupli-kate/4005-41136/)
(vedi {prf:ref}`dupli-kate-multi-paul`) è in missione e deve affrontare due
ondate di nemici. La probabilità che riesca a duplicarsi abbastanza rapidamente
da bloccare la prima ondata è $0.85$, mentre la probabilità che riesca a farlo
per la seconda ondata è $0.7$.
Poiché le due ondate si verificano in rapida successione, i duplicati già
generati durante la prima ondata possono aiutare nella seconda: la probabilità
che Dupli-Kate blocchi entrambe le ondate contemporaneamente è $0.6$.
Calcolate le probabilità dei seguenti eventi:

1. Dupli-Kate riesce a bloccare almeno una delle due ondate,
2. Dupli-Kate non riesce a bloccare nessuna delle due ondate.
````
````{solution} ex-heroes-union
:class: dropdown

Se $P$ e $S$ indicano gli eventi che si verificano, rispettivamente, quando
Dupli-Kate riesce a bloccare la prima e la seconda ondata, avremo
$\mathbb P(P) = 0.85$, $\mathbb P(S) = 0.7$ e $\mathbb P(P \cap S) = 0.6$.
Applicando il {prf:ref}`probabilita-unione-eventi`, la probabilità di bloccare
almeno un'ondata sarà

```{math}
\mathbb P(P \cup S) = \mathbb P(P) + \mathbb P(S) - \mathbb P(P \cap S)
 = 0.85 + 0.70 - 0.60 = 0.95 \enspace.
 ```

La probabilità che Dupli-Kate non riesca a bloccare nessuna delle due ondate è
invece

```{math}
\mathbb P\left(\overline{P \cup S}\right) = 1 - P(P \cup S) =
1 - 0.95 = 0.05 \enspace.
```
````

````{exercise} •
:label: ex-heroes-disjoint
[Hourman](https://dc.fandom.com/wiki/Hourman) è un supereroe che ha scoperto un
farmaco, chiamato [Miraclo](https://dc.fandom.com/wiki/Miraclo) che gli
conferisce forza e velocità sovrumane, ma i cui effetti durano solo per un'ora.
Grazie a questi poteri, e dovendo impedire la fuga di un criminale che si è
nascosto nel porto di New York, che ha due uscite. Hourman stima che le
probabilità che il fuggitivo imbocchi l'uscita a nord e a est siano,
rispettivamente, $0.45$ e $0.3$. In alternativa, il fuggitivo
potrebbe decidere di restare nascosto nel porto, e in tal caso non sarebbe
possibile intercettarlo. Hourman ha piazzato trappole su entrambe le uscite
prima che il Miraclo esaurisse i suoi effetti. Calcolate:

1. la probabilità che Hourman riesca a intrappolare il criminale,
2. la probabilità che il criminale decida di restare nascosto nel porto.
````
````{solution} ex-heroes-disjoint
:class: dropdown

Definiamo i seguenti eventi:

- $N$: «il criminale tenta la fuga usando l'uscita a nord», con
  $\mathbb P(N) = 0.45$;
- $E$: «il criminale tenta la fuga usando l'uscita a est», con
  $\mathbb P(E) = 0.3$;
- $P$: «il criminale resta nascosto nel porto».

Questi tre eventi sono mutuamente esclusivi, dunque la prima probabilità si
ottiene applicando direttamente il terzo assioma di Kolmogorov:

```{math}
\mathbb P(N \cup E) = \mathbb P(E) + \mathbb P(N) = 0.45 + 0.3 = 0.75 \enspace.
```

Inoltre, l'unione dei tre eventi è $\Omega$, pertanto la seconda probabilità
si ottiene applicando il {prf:ref}`probabilita-evento-complementare`:

```{math}
\mathbb P(P) = 1 - \mathbb(N \cup E) = 1 - 0.75 = 0.25 \enspace.
```
````

````{exercise} •••
:label: ex-formule-prob

Dimostrate che
$\mathbb P(E \cap \overline F) = \mathbb P(E) - \mathbb P(E \cap F)$.
````
````{solution} ex-formule-prob
:class: dropdown

Si ha che $E = (E \cap F) \cup (E \cap \overline F)$, dove i due insiemi
considerati nell'unione sono disgiunti. Per il terzo assioma di Kolmogorov,
segue $\mathbb P(E \cap \overline F) = \mathbb P(E) - \mathbb P(E \cap F)$.
````

````{exercise} •••
:label: ex-diff-simmetrica

La differenza simmetrica tra due insiemi $E$ ed $F$ è l'insieme

```{math}
E \Delta F = (E \cap \overline F) \cup (\overline E \cap F)
```

formato da tutti e soli gli elementi appartengono a uno e uno solo dei due
insiemi.

1. Dimostrate che se $E, F \in \mathsf A$, allora $E \Delta F \in \mathsf A$.
2. Indicate quando l'evento $E \Delta F$ si verifica.
3. Dimostrate che, per ogni $E, F \in \mathsf A$, vale
   $\mathbb P(E \Delta F) = \mathbb P(E) + \mathbb P(F)-
   2 \, \mathbb P(E \cap F)$.
````
````{solution} ex-diff-simmetrica
:class: dropdown

1. $E \Delta F$ è definito in termini delle operazioni di unione, intersezione
   e complemento applicate a $E$ ed $F$, che sono contenuti in $\mathsf A$.
   Quest'ultima è chiusa rispetto a tali operazioni, dunque $E \Delta F \in
   \mathsf A$.
2. L'evento $E \Delta F$ si verifica se e solo se si verifica esattamente uno
   tra i due eventi $E$ ed $F$.
3. Siccome $E \cap \overline F$ ed $\overline E \cap F$ sono disgiunti, per il
   terzo assioma di Kolmogorov si ha $\mathbb P(E \Delta F) =
   \mathbb P(E \cap \overline F) + \mathbb P(\overline E \cap F)$. Applicando
   a queste due ultime probabilità il risultato dell’{ref}`ex-formule-prob`
   si ottiene:
   ```{math}
   \mathbb P(E \Delta F) = \mathbb P(E) - \mathbb P(E \cap F) +
                \mathbb P(F) - \mathbb P(E \cap F) =
                \mathbb P(E) + \mathbb P(F) - 2 \mathbb P(E \cap F) \enspace.
   ```
````

````{exercise} •••
:label: ex-intersezione-complementi

Dimostrate che, per ogni coppia di eventi $E$ ed $F$, si ha 
$\mathbb P(\overline E \cap \overline F) = 1 - \mathbb P(E) - \mathbb P(F) +
\mathbb P(E \cap F)$.
````
````{solution} ex-intersezione-complementi
:class: dropdown

$\overline E \cap \overline F = \overline{E \cup F}$ per le leggi di De
Morgan, pertanto

```{math}
\mathbb P(\overline E \cap \overline F)
= 1 - \mathbb P(E \cup F)
= 1 - \mathbb P(E) - \mathbb P(F) + \mathbb P(E \cap F) \enspace.
```

````

````{exercise} ••••
:label: ex-inclusione-esclusione

Dimostrate per induzione il {prf:ref}`teo-inclusione-esclusione`.

````
````{solution} ex-inclusione-esclusione
:class: dropdown

Vogliamo dimostrare che, per ogni successione di eventi $E_1, \dots, E_n$,

```{math}
:label: eq-inclusione-esclusione
\mathbb P \left(\bigcup_{i=1}^n E_i\right) =
\sum_{\emptyset \neq S \subseteq \{1, \dots, n\}} (-1)^{|S|+1}
\mathbb P\left(\bigcap_{i \in S} E_i\right) \enspace.
```

Procediamo per induzione su $n$.

__Caso base__ ($n = 2$). Il principio di inclusione-esclusione assume la forma

```{math}
\mathbb P(E_1 \cup E_2) = \mathbb P(E_1) + \mathbb P(E_2) -
\mathbb P(E_1 \cap E_2) \enspace,
```

che è l'enunciato del {prf:ref}`probabilita-unione-eventi`, e dunque abbiamo
già mostrato.

__Passo induttivo__. Supponiamo vero il principio per $n-1$ eventi e
dimostriamolo per $n$ eventi. Poniamo $F = E_1 \cup \dots \cup E_{n-1}$,
in modo che

```{math}
\bigcup_{i=1}^n E_i = F \cup E_n \enspace.
```

Quest'ultima equazione riguarda l'unione di due eventi, per cui possiamo
applicare il caso base, ottenendo

```{math}
\mathbb P(F \cup E_n) = \mathbb P(F) + \mathbb P(E_n) -
\mathbb P(F \cap E_n) \enspace.
```

D'altra parte, $F \cap E_n = (E_1 \cup \dots \cup E_{n-1}) \cap E_n =
(E_1 \cap E_n) \cup \dots \cup (E_{n-1} \cap E_n)$ coinvolge l'unione di
$n - 1$ eventi, il che permette di applicare l'ipotesi induttiva, ottenendo

```{math}
:label: eq-hp-induttiva

\mathbb P(F \cap E_n) = \sum_{\emptyset \neq S \subseteq \{1, \dots, n-1\}}
(-1)^{|S|+1} \mathbb P\left(\bigcap_{i \in S} (E_i \cap E_n)\right)
= \sum_{\emptyset \neq S \subseteq \{1, \dots, n-1\}} (-1)^{|S|+1}
\mathbb P\left(E_n \cap \bigcap_{i \in S} E_i\right) \enspace.
```

L'ipotesi induttiva si può applicare anche a $F$, in questo quest'ultimo è
uguale all'unione di $n - 1$ eventi:

```{math}
\mathbb P(F) = \sum_{\emptyset \neq S \subseteq \{1, \dots, n-1\}} (-1)^{|S|+1}
\mathbb P\left(\bigcap_{i \in S} E_i\right).
```

Sostituendo in {eq}`eq-hp-induttiva`, si ottiene:

```{math}
:label: eq-gruppi
\mathbb P\left(\bigcup_{i=1}^n E_i\right) =
\underbrace{
  \sum_{\emptyset \neq S \subseteq \{1, \dots, n-1\}} (-1)^{|S|+1}
  \mathbb P\!\left(\bigcap_{i\in S} E_i\right)
}_{\text{gruppo A}}
+ \underbrace{\mathbb P(E_n)}_{\text{gruppo B}}
- \underbrace{
  \sum_{\emptyset \neq S \subseteq \{1, \dots, n-1\}} (-1)^{|S|+1}
  \mathbb P\!\left(E_n \cap \bigcap_{i\in S} E_i\right)
}_{\text{gruppo C (da verificare)}} \enspace.
```

Per terminare la dimostrazione, osserviamo che ogni sottoinsieme non vuoto di
$\{1, \dots, n\}$, che individua uno degli addendi in
{eq}`eq-inclusione-esclusione`, appartiene a uno e uno solo dei tre gruppi che
seguono:

1. gruppo A: tutti i sottoinsiemi $S$ tali che
   $\emptyset \neq S \subseteq \{ 1, \dots, n-1 \}$;
2. gruppo B: il sottoinsieme $\{ n \}$;
3. gruppo C: tutti i sottoinsiemi della forma $S \cup \{ n \}$, dove $S$ è tale
   che $\emptyset \neq S \subseteq \{ 1, \dots, n-1 \}$.


I contributi dei gruppi A e B coincidono con i termini corrispondenti in
{eq}`eq-gruppi`. Rimane da verificare il gruppo C: per ogni insieme in questo
gruppo, in {eq}`eq-inclusione-esclusione` è presente il coefficiente
moltiplicativo
$(-1)^{|S \cup \{n\}|+1}$. Poiché $n \notin S$, si ha $|S \cup \{n\}| = |S|+1$,
quindi:

```{math}
(-1)^{|S \cup \{n\}|+1} = (-1)^{|S|+2} = -(-1)^{|S|+1} \enspace.
```

Il contributo del gruppo C nella formula obiettivo è dunque:

```{math}
\sum_{\emptyset \neq S \subseteq \{1,\dots,n-1\}} (-1)^{|S|+2}\,
\mathbb P\!\left(\bigcap_{i \in S\cup\{n\}} E_i\right)
= -\sum_{\emptyset \neq S \subseteq \{1,\dots,n-1\}} (-1)^{|S|+1}\,
\mathbb P\!\left(E_n \cap \bigcap_{i\in S} E_i\right) \enspace,
```

che coincide esattamente con il terzo termine della formula ottenuta. I tre
contributi combaciano, e la dimostrazione è completa.
````

````{exercise} •••
:label: ex-heroes-three-events
[Bloodshot](https://comicvine.gamespot.com/bloodshot/4005-5569/) viene inviato
in missione in un complesso militare sorvegliato da tre sistemi di sicurezza
indipendenti: un rilevatore di calore, un sistema di riconoscimento facciale e
una rete di sensori al suolo. Il suo corpo è potenziato con dei dispositivi
nanotecnologici, detti _naniti_, che possono interferire con ciascun sistema,
ma non sempre con successo: la probabilità di disattivare il rilevatore di
calore è $0.7$, quella di disattivare il riconoscimento facciale è $0.5$, e
quella di disattivare i sensori al suolo è $0.6$. La probabilità di disattivare
contemporaneamente il rilevatore di calore e il riconoscimento facciale è
$0.35$, quella di disattivare contemporaneamente il rilevatore di calore e i
sensori al suolo è $0.40$, e quella di disattivare contemporaneamente il
riconoscimento facciale e i sensori al suolo è $0.20$. La probabilità di
disattivare tutti e tre i sistemi contemporaneamente è $0.08$.

Calcolate la probabilità che Bloodshot riesca a disattivare almeno uno dei tre
sistemi di sorveglianza.
````
````{solution} ex-heroes-three-events
:class: dropdown

Se definiamo gli eventi:

- $C$ = «i naniti disattivano il rilevatore di calore»,
- $F$ = «i naniti disattivano il riconoscimento facciale»,
- $S$ = «i naniti disattivano i sensori al suolo»,

il testo del problema dice che $\mathbb P(C) = 0.7$, $\mathbb P(F) = 0.5$,
$\mathbb P(S) = 0.6$, $\mathbb P(C \cap F) = 0.35$,
$\mathbb P(C \cap S) = 0.40$, $\mathbb P(F \cap S) = 0.20$ e
$\mathbb P(C \cap F \cap S) = 0.08$. L'evento al quale siamo interessati
è $C \cup F \cup S$, e la sua probabilità si può calcolare applicando il
principio di inclusione-esclusione:

```{math}
\mathbb P(C \cup F \cup S) =
\mathbb P(C) + \mathbb P(F) + \mathbb P(S) -
\mathbb P(C \cap F) - \mathbb P(C \cap S) - \mathbb P(F \cap S) +
\mathbb P(C \cap F \cap S) = 0.7 + 0.5 + 0.6 - 0.35 - 0.40 - 0.20 + 0.08
= 0.93 \enspace.
```
````

````{exercise} ••
:label: ex-heroes-subset-1
Osservando che i membri degli Avengers sono anche supereroi Marvel, sia $A$
l'evento «è un Avenger» e $M$ l'evento «è un supereroe Marvel». Utilizzando
l'interpretazione frequentista e prendendo a riferimento il database che
utilizziamo, supponiamo che questo contenga $3200$ personaggi, $7$ dei quali
siano degli Avengers. È possibile che $\mathbb P(M) = 0.004$?
````
````{solution} ex-heroes-subset-1
:class: dropdown

L'interpretazione frequentista ci permette di definire
$\mathbb P(A) = \frac{7}{1200} = 0.006$. Siccome $A \subseteq M$, per il
{prf:ref}`teo_prob_sottoinsiemi` deve valere
$\mathbb P(M) \geq \mathbb P(A) = 0.006$, pertanto non è possibile che la
probabilità di $M$ sia uguale a $0.004$.
````

````{exercise} ••
:label: ex-heroes-subset-2
Riconsiderate l'esercizio precedente, dove ora $\mathbb P(M) = 0.12$.
Calcolate:
1. $\mathbb P(M \cap \overline A)$, ovvero la probabilità di estrarre un
   supereroe Marvel che non sia un Avenger;
2. $\mathbb P(\overline M \cap A)$, ovvero la probabilità di estrarre un
   Avenger che non sia un supereroe Marvel.
````
````{solution} ex-heroes-subset-2
:class: dropdown

1. Per calcolare $\mathbb P(M \cap \overline A)$, osserviamo che siccome
   $A \subseteq M$, l'insieme $M$ può essere scomposto nell'unione
   di $A$ e $M \cap \overline A$, che sono due eventi disgiunti. Per il terzo
   assioma di Kolmogorov si ha $\mathbb P(M) = \mathbb P(A) +
   \mathbb P(M \cap \overline A)$, da cui

   ```{math}
   \mathbb P(M \cap \overline A) = \mathbb P(M) - \mathbb P(A) =
   0.12 - 0.006 = 0.114 \enspace.
   ```
2. $A \subseteq M$ implica $A \cap \overline M = \varnothing$, dunque
   $\mathbb P(\overline M \cap A) = \mathbb P(\varnothing) = 0$.
````

````{exercise} ••••
:label: ex-heroes-bounds
Dimostrate che, per ogni $E, F \in \mathsf A$,

```{math}
\max(0, \mathbb P(E) + \mathbb P(F) - 1) \leq \mathbb P(E \cap F) \leq
\min(\mathbb P(E), \mathbb P(F)).
```

Utilizzate poi questo risultato per rispondere alla seguente domanda: gli
eventi $V$ = «un supereroe può volare» e $M$ = «un supereroe porta il mantello»
sono tali che $\mathbb P(V) = 0.4$ e $\mathbb P(M) = 0.5$. Qual è il valore
minimo per la probabilità di osservare un supereroe che vola e porta il
mantello? E qual è il suo valore massimo?
````
````{solution} ex-heroes-bounds
:class: dropdown

Poiché $E \cap F \subseteq E$, ma anche $E \cap F \subseteq F$, per il
{prf:ref}`teo_prob_sottoinsiemi` abbiamo
$\mathbb P(E \cap F) \leq \mathbb P(E)$ e
$\mathbb P(E \cap F) \leq \mathbb P(F)$. Da queste due relazione si ottiene
$\mathbb P(E \cap F) \leq \min(\mathbb P(E), \mathbb P(F))$, il che dimostra
la validità del limite superiore.

Per quanto riguarda invece il limite inferiore, dal
{prf:ref}`probabilita-unione-eventi` possiamo derivare
$\mathbb P(A \cap B) = \mathbb P(A) + \mathbb P(B) - \mathbb P(A \cup B)$, e
siccome $\mathbb P(A \cup B) \leq 1$, abbiamo
$\mathbb P(A \cap B) \geq \mathbb P(A) + \mathbb P(B) - 1$.
Inoltre, per il primo assioma di Kolmogorov, $\mathbb P(A \cap B) \geq 0$.
Quindi $\mathbb P(A \cap B) \geq \max(0, \mathbb P(A) + \mathbb P(B) - 1)$.

Applicando questi due limiti al caso descritto, si ottiene che:
- il valore minimo per $\mathbb P(V \cap M)$ è $\max(0, 0.4 + 0.5 - 1) = 0$,
- il suo valore massimo è invece $\min(0.4, 0.5) = 0.4$.
````
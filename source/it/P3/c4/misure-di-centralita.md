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

(sec-misure-di-centralita)=
# Misure di centralità

Nel {ref}`sec_va-discrete` abbiamo visto che la funzione di massa di
probabilità descrive completamente una variabile aleatoria discreta: una
volta nota $p_X$, possiamo in linea di principio ricavare tutto ciò che c'è da
sapere su $X$. Spesso, però, non vogliamo lavorare con l'intera distribuzione,
ma preferiamo concentrarci su alcuni suoi aspetti specifici, quantificandoli
tramite degli indici che permettono di riassumere la distribuzione stessa
tramite pochi numeri, facili da interpretare e da confrontare. Il primo aspetto
che viene introdotto riguarda la _centralità_ della distribuzione, anche noto
come tendenza centrale o posizione, e che si può informalmente definire come
la collocazione dei valori della variabile rispetto all'intero asse reale.
Poter quantificare questa informazione permette di valutare per esempio di
quanto il reddito degli abitanti di una nazione superi la soglia di povertà, o
di confrontare il livello di forza tra gli eroi Marvel e DC, o di modellare il
carico di un server in determinate condizioni. Sebbene esistano vari modi di
misurare la centralità di una distribuzione, quelli più utilizzati nei testi
introduttivi sono il _valore atteso_, la _mediana_ e la _moda_, a cui sono
dedicati i paragrafi successivi.

## Valore atteso

```{margin}
Il valore atteso è il primo _indice di sintesi_ di una variabile aleatoria
che incontriamo: un singolo numero che ne riassume la posizione tipica,
riducendo l'intera funzione di massa a un solo numero.
```
Tra gli indici che misurano la centralità di una distribuzione, il
_valore atteso_ è quello che viene tradizionalmente introdotto per primo, e al
quale viene dedicato più spazio. Questo indice permette di rispondere a una domanda molto naturale: se la variabile aleatoria tante volte, attorno a che
quantità tenderebbero a posizionarsi i valori ottenuti? 

````{prf:definition} Valore atteso
:label: def-valore-atteso-discreto

Sia $X$ una variabile aleatoria discreta con supporto $S_X$ e funzione di massa
di probabilità $p_X$. Il _valore atteso_ di $X$ (detto anche _media_ o
_aspettazione_) è il numero

```{math}
:label: eq-valore-atteso

\mathbb E(X) = \sum_{x \in S_X} x\, p_X(x) \enspace,
```

definito ogni volta che la serie a destra converge assolutamente. Quando ciò
non si verifica, si dice che $X$ non ammette valore atteso.
````

Il valore atteso è quindi una funzione che associa un numero a una variabile
aleatoria, dunque è la funzione di una funzione. In casi come questi (un altro
esempio è quello dell'integrale definito), si usa spesso parlare di
_operatori_, per enfatizzare che gli argomenti coinvolti non sono numeri, ma oggetti matematici più complessi.

```{figure} https://upload.wikimedia.org/wikipedia/commons/2/29/Karl_Pearson%2C_1910_%28cropped%29.jpg
---
figclass: margin
name: fig_pearson
width: 200px
align: left
---
Ritratto di Karl Pearson (Fotografia di autore sconosciuto, 1910. Immagine di
pubblico dominio. Fonte: [Wikimedia Commons](https://upload.wikimedia.org/wikipedia/commons/2/29/Karl_Pearson%2C_1910_%28cropped%29.jpg)).
```

```{admonition} _
:class: naming

Esattamente come per $\mathbb P$, l'uso di $\mathbb E$ per indicare l'operatore
di valore atteso è soltanto una tra le scelte possibili: nei testi di
probabilità sono comunemente adottate anche notazioni alternative, come
$\mathbf{E}$, $\mathrm E$ oppure $E$. Anche in questo caso, inoltre,
l'argomento dell'operatore è talvolta racchiuso tra parentesi quadre, scrivendo
per esempio $\mathbb{E}[X]$, anziché tra parentesi tonde. Io ho scelto di
utilizzare queste ultime, per mantenere una notazione coerente con quella
impiegata per altri operatori, come la varianza, che sarà introdotta nel
paragrafo seguente.

Il valore atteso di $X$ viene spesso indicato anche con il simbolo $\mu_X$, e
quando la variabile aleatoria a cui ci si riferisce è chiara dal contesto, il
pedice viene omesso e si scrive semplicemente $\mu$. Questa notazione è
decisamente più leggera, ma presenta alcuni inconvenienti. L'espressione
$\mu_X$ indica infatti una quantità associata alla variabile aleatoria,
«nascondendo» il particolare operatore che vi è stato applicato; risulta quindi
meno naturale quando l’argomento è un’espressione composta, come $X+Y$ o
$a X + b$. Inoltre, vedremo che la lettera $\mu$ può essere impiegata per
denotare un parametro di una distribuzione, e ciò può generare ambiguità. Nel
seguito, farò riferimento a entrambe le notazioni, scegliendo di volta in volta
tra $\mathbb E(X)$, $\mu_X$ e $\mu$ in funzione di quella che ritengo la
soluzione nel contempo più chiara ed elegante.

Vale la pena richiamare all'attenzione l'origine storica di questo tipo di
notazione. Come per $\mathbb P$, l'uso di $\mathbb E$ e delle sue varianti è
anche dettato dagli strumenti tipografici e alla loro evoluzione nel tempo. Le
prime tracce risalgono all'inizio del $1900$, con l'uso dello stile
calligrafico $\mathcal E$, poi mutato in $E$, $\mathbf E$ e via discorrendo,
per arrivare solo recentemente a $\mathbb E$. La scelta della lettera E è
verosimilmente dovuta a una comunanza nelle terminologie in lingua inglese
(_expectation_), francese (_expérance mathématique_) e tedesca (_Erwartung_).

Per quanto riguarda $\mu$, invece, il percorso è diverso: questo simbolo fu
introdotto da Karl Pearson nella fine del $1800$ per indicare i momenti
di una distribuzione (vedi {ref}`sec_momenti`), presumibilmente per
assonanza tra la lettera greca e l'iniziale di _moment_, e solo verso la metà
del $1900$ si iniziò a diffondere il suo uso specificamente per indicare il
valore atteso (che, come vedremo, è un particolare momento). 
```

````{admonition} Valore atteso e misurabilità
:class: note

Vale la pena di osservare che la definizione di valore atteso coinvolge soltanto
il supporto $S_X$ e la funzione di massa $p_X$, e non lo spazio campionario
$\Omega$ da cui $X$ ha origine. Possiamo procedere così perché ogni scrittura
della forma $\{ X = x \}$ individua davvero un evento, dotato di una
probabilità: è precisamente ciò che garantisce la condizione di _misurabilità_
richiesta dalla {prf:ref}`def-variabile-aleatoria`. È dunque la misurabilità a
permetterci di «dimenticare» $\Omega$ e di riassumere una variabile aleatoria
attraverso grandezze (come, appunto, il valore atteso) calcolate direttamente
sulla sua distribuzione. Nel caso discreto questa condizione è sempre
soddisfatta, ma è su di essa che si regge l'intera costruzione.
````

Quando $X$ può assumere un numero relativamente basso di valori e la sua
funzione di massa di probabilità è nota, risulta agevole calcolare
$\mathbb E(X)$ applicando direttamente la definizione precedente, come
nell'esempio che segue.

````{prf:example} Un passaggio sotto la porta
:label: ex-ea-flatman

{extlink}`Flatman
<https://marvel.fandom.com/wiki/Val_Ventura_(Earth-616)>`, dei {extlink}`Great
Lakes Avengers
<https://marvel.fandom.com/wiki/Great_Lakes_Avengers_(Earth-616)>`, prova ad
appiattirsi per infilarsi sotto una porta blindata. L'operazione riesce con
probabilità $p \in (0, 1)$ e fallisce con probabilità $1 - p$. Se indichiamo
con $X$ la variabile aleatoria che vale $1$ se Flatman passa e $0$ altrimenti,
avremo $p_X(1) = p$ e $p_X(0) = 1 - p$. Applicando la
{prf:ref}`def-valore-atteso-discreto`,

```{math}
\mathbb E(X) = 0 \cdot (1 - p) + 1 \cdot p = p \enspace.
```

Ogni volta che una variabile assume solo i valori $0$ e $1$, il suo valore
atteso coincide dunque con la probabilità di valere $1$: se $p = \tfrac{1}{2}$,
allora $\mathbb E(X) = \tfrac{1}{2}$; se $p = \tfrac{2}{3}$, allora
$\mathbb E(X) = \tfrac{2}{3}$ e così via. Ciò significa che, a parte i casi
degeneri in cui $p = 0$ oppure $p = 1$, il valore atteso non è una
realizzazione della variabile aleatoria: $X$ può assumere soltanto i valori
$0$ e $1$, mentre $\mathbb E(X)$ può essere qualunque numero reale compreso
tra questi due estremi.
````

Quando il numero di realizzazioni cresce, l'applicazione diretta di
{eq}`eq-valore-atteso` può diventare più complicata. Non sempre, però, è
necessario procedere in tal senso: a volte il valore atteso si può calcolare
senza nemmeno sommare, riconoscendo una simmetria nella distribuzione, come nel
caso dell'esempio seguente.

````{prf:example} Una distribuzione simmetrica
:label: ex-ea-simmetria

Riprendiamo la variabile $X$ dell'{prf:ref}`ex-va-discreta-scoiattoli`, la
differenza tra i punteggi di due dadi equilibrati, con supporto
$S_X = [-5 .. 5]$ e funzione di massa

```{math}
p_X(x) = \tfrac{6 - |x|}{36} \mathbb 1_{S_X}(x) \enspace.
```

Questa funzione è _simmetrica_ rispetto all'origine, nel senso che
$p_X(-x) = p_X(x)$ per ogni $x$. Nel calcolo di

```{math}
\mathbb E(X) = \sum_{x = -5}^{5} x\, p_X(x)
```

ogni addendo relativo a un valore positivo $x$ è bilanciato esattamente
dall'addendo opposto $-x$, che ha la stessa massa, e quindi i due termini si
cancellano a vicenda. Quindi, ciò che resta è solo il termine che corrisponde
a $x = 0$, che è anch'esso nullo. Senza bisogno di svolgere i conti in modo
esplicito, si ha dunque $\mathbb E(X) = 0$. Più in generale, si può dimostrare
che il valore atteso di una variabile la cui massa di probabilità è simmetrica
attorno a un punto $c$ vale proprio $c$.
````

````{admonition} Valore atteso e convergenza assoluta
:class: warning

Quando il supporto $S_X$ è finito, {eq}`eq-valore-atteso` esprime la somma di
un numero finito di addendi, che esiste sempre. Se invece $S_X$ è infinito
numerabile, la faccenda è più delicata: è necessario calcolare il valore di una
serie, e non è affatto garantito che questa converga. Da una parte, c'è la
possibilità che il risultato diverga a più o meno infinito. Dall'altra, i
termini dipendono dai valori dei punti di massa, quindi possono essere sia
positivi, sia negativi, con effetti potenzialmente sorprendenti: cambiando
l'ordine degli addendi, la serie può convergere a valori diversi, divergere o
anche risultare indefinita. Per garantire che $\mathbb E(X)$ sia be definito,
la {prf:ref}`def-valore-atteso-discreto` richiede quindi la
_convergenza assoluta_ della serie, cioè

```{math}
\sum_{x \in S_X} |x|\, p_X(x) \in \mathbb R \enspace.
```

Ciò garantisce anche la convergenza semplice della serie, implicando che il
valore atteso sia univocamente determinato.

Esistono variabili aleatorie perfettamente legittime per cui questa condizione
non vale[^va-inesistente] e per cui il valore atteso semplicemente non è
definito[^va-inesistente-terminologia]. Negli esempi che proporrò in questo
libro, però, la convergenza non sarà mai un problema: lo segnalo qui una volta
per tutte, così da poter procedere con la coscienza a posto.
````

````{prf:example}
:label: ex-va-va-infinita

Consideriamo la variabile aleatoria $N$ avente $S_N = \mathbb N \cup \{0 \}$
come supporto e funzione di massa di probabilità definita nel modo seguente:

```{margin}
Applicando {eq}`eq-e-mclaurin`, si verifica che $\sum_{n \in S_N}p_N(n) =
\tfrac{1}{\mathrm e}\sum_{n=0}^{+\infty}\tfrac{1}{n!} = 1$.
```
```{math}
p_N(n) = \frac{1}{\mathrm e n!} \mathbb 1_{S_N}(n) \enspace. 
```

L'applicazione della {prf:ref}`def-valore-atteso-discreto` per ottenere
$\mathbb E(N)$ richiede in questo caso di calcolare il valore di una serie:

```{margin}
Nel penultimo passaggio è stata applicata all'indice della sommatoria la
trasformazione $n \mapsto m + 1$, che equivale a $m \mapsto n - 1$.
```
```{math}
\mathbb E(N) = \sum_{n=0}^{+\infty} \frac{n}{\mathrm e n!}
= \sum_{n=1}^{+\infty} \frac{n}{\mathrm e n!}
= \mathrm e \sum_{n=1}^{+\infty} \frac{1}{(n-1)!}
= \mathrm e \sum_{m=0}^{+\infty} \frac{1}{m!} = 1 \enspace.
```

````


I termini «valore atteso» e «aspettazione» possono trarre in inganno, perciò
conviene fissarne subito il significato: ricordando che i valori di probabilità
sono non negativi e che la loro somma è uguale a uno, $\mathbb E(X)$ non è
altro che una _media pesata_ dei valori di $X$, in cui il peso di ciascuna
realizzazione è la probabilità con cui essa si presenta. Pertanto $\mathbb
E(X)$ indica il _baricentro_ delle osservazioni di $X$, espresso in funzione
delle masse di probabilità corrispondenti, non un valore che è ragionevole
ottenere quando si osserva $X$.
```{margin}
È importante sottolineare una cosa: il fatto che i valori di $X$ si trovino in
un intorno di $\mathbb E(X)$ non implica assolutamente che essi
_si concentrino_ attorno a esso: a seconda dei casi, i valori possono essere
più o meno vicini (o lontani) dal valore atteso.
```
L'informazione contenuta in $\mathbb E(X)$
riguarda invece la centralità della distribuzione: come già messo in
evidenza nell'{prf:ref}`ex-ea-flatman`, può benissimo capitare che il valore
atteso non appartenga nemmeno al supporto di $X$, proprio perché si tratta di
un indice di posizione che esprime quanto i valori osservati tendano a essere
grandi (o piccoli). In altre parole, $\mathbb E(X)$ rappresenta un numero
attorno al quale si dispongono i valori di $X$.

````{prf:example}
:label: ex-ea-dado

Sia $X$ la variabile aleatoria che indica il punteggio ottenuto lanciando un
dado bilanciato a sei facce. La sua funzione di massa di probabilità è tale che
$p_X(x) = \tfrac{1}{6} \mathbb 1_{[1 .. 6]}(x)$, e il suo valore atteso è

```{math}
\mathbb E(X) = \sum_{i = 1}^{6} i \cdot \frac{1}{6}
             = \frac{1}{6} \sum_{i = 1}^{6} i
             = \frac{1}{6} \cdot \frac{6 \cdot 7}{2}
             = \frac{7}{2} \enspace.
```

Questo conferma, ancora una volta, che il valore atteso non va inteso come il risultato che ci si aspetta di ottenere &mdash; non esiste alcuna faccia con
$3.5$ pallini &mdash; bensì come il baricentro della distribuzione. In questo
caso, $\mathbb E(X)$ si posiziona esattamente a metà tra la più piccola e la
più grande delle realizzazioni: ciò è conseguenza del fatto che tutti i punti
di massa hanno la stessa probabilità. Se $\mathbb E(X)$ fosse più grande di
$\tfrac{7}{2}$, ciò significherebbe che il dado tende a cadere più spesso
mostrando un punteggio elevato; se fosse più piccolo di $\tfrac{7}{2}$,
sarebbero i punteggi più bassi a essere osservati più frequentemente. In
entrambi i casi, ciò sarebbe in contrasto con il fatto che il dado è
bilanciato.
````

Il valore atteso è sempre espresso nella stessa unità di misura dei valori
della corrispondente variabile aleatoria, come esemplificato di seguito.

````{prf:example}
:label: ex-ex-unita-misura

Sia $X$ la variabile aleatoria che indica l'altezza del supereroe che compare
per primo in una serie consigliata da un sistema di _streaming_. Se i valori di
$X$ sono espressi in centimetri, allora $\mathbb E(X)$ è una lunghezza espressa
nella stessa unità di misura.  
````


Non è un caso che, nello studio delle variabili aleatorie discrete, ricorrano
termini come _massa di probabilità_ e concetti come _baricentro_. Questa
nomenclatura, adottata fin dalle origini della teoria delle
probabilità[^prob-meccanica], riflette un profondo parallelismo con la
meccanica: come ho già osservato nel {ref}`sec_va-discrete`, una distribuzione
di probabilità può essere interpretata come una distribuzione di massa
totale unitaria, il cui baricentro coincide con il valore atteso.
```{margin}
Vale la pena notare che questa interpretazione non si limita alle variabili
aleatorie discrete, come vedremo nel {ref}`sec_va-continue`.
```
Il grafico nella {numref}`fig_ex-barycenter-balance` rende visibile un altro
aspetto di questa corrispondenza, concentrandosi su una variabile aleatoria $X$
simile e quella dell'esempio precedente, nel senso che essa descrive l'esito
del lancio di un dado. Se immaginiamo la retta reale come un asse e collochiamo
in ogni punto $x \in S_X$ una massa di valore $p_X(x)$, allora il valore atteso
coincide con la posizione del baricentro del sistema anche da un punto di vista
fisico: se l'asse fosse appoggiato su un cuneo posizionato in $\mathbb E(X)$,
resterebbe in equilibrio. Il grafico permette di modificare sia le singole
masse di probabilità sia la posizione del cuneo. L'inclinazione dell'asse viene
aggiornata di conseguenza e il cuneo cambia colore quando il sistema è in
equilibrio.


````{customfigure}
:name: fig_ex-barycenter-balance
:class: left-align

```{raw} html
<div class="plot-container plot-container--top" style="float: none; clear: both; max-width: 100%; width: min(100%, 760px); margin: 0 auto 1rem;">
   <div style="display: grid; grid-template-columns: repeat(6, minmax(0, 1fr)); gap: 0.5rem 0.75rem; align-items: end; width: 100%;">
      <div class="model-slider-container">
         <input type="range" id="mass-weight-1" min="0.2" max="3.0" value="1.0" step="0.1" style="width: 100%;" />
         <div>\(p_1 = \)<span id="mass-prob-1">0.167</span></div>
      </div>
      <div class="model-slider-container">
         <input type="range" id="mass-weight-2" min="0.2" max="3.0" value="1.0" step="0.1" style="width: 100%;" />
         <div>\(p_2 = \)<span id="mass-prob-2">0.167</span></div>
      </div>
      <div class="model-slider-container">
         <input type="range" id="mass-weight-3" min="0.2" max="3.0" value="1.0" step="0.1" style="width: 100%;" />
         <div>\(p_3 = \)<span id="mass-prob-3">0.167</span></div>
      </div>
      <div class="model-slider-container">
         <input type="range" id="mass-weight-4" min="0.2" max="3.0" value="1.0" step="0.1" style="width: 100%;" />
         <div>\(p_4 = \)<span id="mass-prob-4">0.167</span></div>
      </div>
      <div class="model-slider-container">
         <input type="range" id="mass-weight-5" min="0.2" max="3.0" value="1.0" step="0.1" style="width: 100%;" />
         <div>\(p_5 = \)<span id="mass-prob-5">0.167</span></div>
      </div>
      <div class="model-slider-container">
         <input type="range" id="mass-weight-6" min="0.2" max="3.0" value="1.0" step="0.1" style="width: 100%;" />
         <div>\(p_6 = \)<span id="mass-prob-6">0.167</span></div>
      </div>
   </div>
</div>
```

```{interactive-code} python
:tags: [toggle-code]

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, Polygon
from pyscript import display
from pyscript.web import page, when


mass_positions = np.arange(1, 7, dtype=float)
weight_ids = [f'#mass-weight-{index}' for index in range(1, 7)]
probability_ids = [f'#mass-prob-{index}' for index in range(1, 7)]
fig_balance, ax_balance = plt.subplots(figsize=(7, 3.8))
beam_height = 0.0
mass_radius_scale = 0.29
graph_height = '230px'


def rotate_points(x_values, y_values, pivot_x, angle):
   x_values = np.asarray(x_values, dtype=float)
   y_values = np.asarray(y_values, dtype=float)
   cos_angle = np.cos(angle)
   sin_angle = np.sin(angle)
   shifted_x = x_values - pivot_x

   rotated_x = pivot_x + cos_angle * shifted_x - sin_angle * y_values
   rotated_y = sin_angle * shifted_x + cos_angle * y_values
   return rotated_x, rotated_y


def get_probabilities():
   relative_weights = np.array([float(page[weight_id][0].value)
                                for weight_id in weight_ids])
   probabilities = relative_weights / relative_weights.sum()
   return probabilities


def update_probability_labels(probabilities):
   for probability_id, probability in zip(probability_ids, probabilities):
      page[probability_id][0].innerHTML = f'{probability:.3f}'


def render_balance():
   ax_balance.clear()
   graph_container = page['#graph-%this%'][0]
   graph_container.style.display = 'flex'
   graph_container.style.justifyContent = 'center'
   graph_container.style.alignItems = 'center'
   graph_container.style.height = graph_height
   graph_container.style.overflow = 'hidden'
   graph_container.parentElement.style.float = 'none'
   graph_container.parentElement.style.margin = '0 auto'
   graph_container.parentElement.style.width = '100%'
   graph_container.parentElement.style.height = graph_height
   graph_container.parentElement.style.overflow = 'hidden'

   pivot = float(page['#balance-pivot'][0].value)
   probabilities = get_probabilities()
   expected_value = np.dot(mass_positions, probabilities)
   mass_radii = mass_radius_scale * np.sqrt(probabilities)

   page['#balance-pivot-value'][0].innerHTML = f'{pivot:.2f}'
   page['#balance-expected-value'][0].innerHTML = f'{expected_value:.2f}'
   update_probability_labels(probabilities)

   is_balanced = abs(pivot - expected_value) < 0.05
   if is_balanced:
       angle =  0.0
   else:
       angle = np.clip(0.22 * (pivot - expected_value), -0.45, 0.45)
   wedge_color = '#c17f24' if is_balanced else '#6085a6'

   wedge = np.array([
      [pivot - 0.28, -0.65],
      [pivot + 0.28, -0.65],
      [pivot, 0.0],
   ])
   ax_balance.add_patch(Polygon(wedge, closed=True, facecolor=wedge_color,
                                edgecolor='none', zorder=1))

   beam_x, beam_y = rotate_points([0.5, 6.5], [beam_height, beam_height],
                                  pivot, angle)
   ax_balance.plot(beam_x, beam_y, color='#010177',
                   linewidth=4, solid_capstyle='round', zorder=2)

   tick_bottom_x, tick_bottom_y = rotate_points(mass_positions,
                        np.full(6, beam_height - 0.08), pivot, angle)

   tick_top_x, tick_top_y = rotate_points(mass_positions,
                        np.full(6, beam_height + 0.08), pivot, angle)

   for x0, y0, x1, y1 in zip(tick_bottom_x, tick_bottom_y,
                             tick_top_x, tick_top_y):
      ax_balance.plot([x0, x1], [y0, y1],
                      color='#010177', linewidth=1.2, zorder=2)

   label_x, label_y = rotate_points(mass_positions,
                        np.full(6, beam_height - 0.28), pivot, angle)

   for value, x_coord, y_coord in zip(range(1, 7), label_x, label_y):
      ax_balance.text(x_coord, y_coord, f'{value}',
                      ha='center', va='center', fontsize=10, color='#010177')

   mass_x, mass_y = rotate_points(mass_positions,
                                  beam_height + mass_radii, pivot, angle)

   for x_coord, y_coord, mass_radius in zip(mass_x, mass_y, mass_radii):
      ax_balance.add_patch(Circle((x_coord, y_coord), mass_radius,
                                  facecolor='#006699', edgecolor='white', linewidth=1.5, zorder=3))

   ax_balance.set_xlim(0.2, 6.8)
   ax_balance.set_ylim(-1.1, 1.1)
   ax_balance.set_aspect('equal', adjustable='box')
   ax_balance.axis('off')
   display(fig_balance, target='graph-%this%', append=False)

ids = '#balance-pivot, ' + ', '.join([f'#mass-weight-{i}' for i in range(1, 7)])

#@when("input", "#balance-pivot, #mass-weight-1, #mass-weight-2, #mass-weight-3, #mass-weight-4, #mass-weight-5, #mass-weight-6")
@when('input', ids)
def update_balance(event):
   render_balance()


render_balance()
```

```{raw} html
<div class="plot-container" style="float: none; clear: both; max-width: 340px; width: fit-content; margin: 1rem auto 0;">
   <div class="model-slider-container">
      <input type="range" id="balance-pivot"
            min="1.0" max="6.0" value="3.5" step="0.01" aria-label="Posizione del cuneo" />
   </div>
   <div class="model-slider-container">
      <span>Posizione del cuneo: </span>
      <span id="balance-pivot-value">3.50</span>
   </div>
   <div class="model-slider-container">
      <span>\(\mathbb E(X) = \, \)</span>
      <span id="balance-expected-value">3.50</span>
   </div>
</div>
```

Sei cerchi che rappresentano masse appoggiate su un asse, in corrispondenza
delle realizzazioni della variabile aleatoria $X$ che indica il risultato nel
lancio di un dado. Il pannello superiore permette di modificare le masse dei
cerchi, mentre quello inferiore sposta il cuneo sul quale è appoggiato l'asse.
Il cuneo cambia colore quando il sistema si trova in equilibrio, evidenziando
come ciò capiti quando il pungo di appoggio dell'asse coincide con
$\mathbb E(X)$.
````

Una delle denominazioni alternative per il valore atteso è _media_, richiamando
l'attenzione su un parallelismo con il concetto di _media campionaria_. In
effetti, si tratta in entrambi i casi di indici di posizione che calcolano un
baricentro: delle osservazioni di un campione, in un caso, e dei punti
di massa di una variabile aleatoria, nell'altro. È possibile spingere oltre
questo parallelismo, introducendo un'interpretazione frequentista del valore
atteso. Immaginiamo di fissare una variabile aleatoria discreta $X$ tale che
$S_X = \{ x_1, \dots, x_n \}$, e di osservarla per $m$ volte in condizioni di
indipendenza, ottenendo un campione.
```{margin}
È importante sottolineare che $\{ x_1, \dots, x_n \}$ indica il supporto di
$X$ e non il campione che stiamo considerando. Quest'ultimo conterrà, in linea
di principio, più occorrenze di ognuna delle realizzazioni.
```
Per $i = 1, \dots, n$, indichiamo con $m_i$ il numero di volte che è stato
osservato il valore $x_i$. La media campionaria corrispondente sarà ugugale a

```{math}
\frac{m_1 x_1 + m_2 x_2 + \dots + m_n x_n}{m}
   = \sum_{i = 1}^{n} \frac{m_i}{m}\, x_i \enspace.
```

```{margin}
In realtà, questo risultato prescinde dalla particolare interpretazione del
concetto di probabilità che si preferisca adottare. Vedremo nel
{ref}`legge-grandi-numeri` che è possibile dimostrare che, sotto opportune
ipotesi, la frequenza relativa di un evento tende alla sua probabilità.
```
Quando $m$ diventa grande, nell'interpretazione frequentista la frequenza
relativa $\tfrac{m_i}{m}$ con cui osserviamo il valore $x_i$ fornisce una buona
approssimazione della probabilità $p_X(x_i)$. Di conseguenza, la media
campionaria osservata tende a

```{math}
\sum_{i = 1}^{n} p_X(x_i)\, x_i = \mathbb E(X) \enspace.
```

In altre parole, il valore atteso può essere visto come il limite a cui tende
la media aritmetica dei valori assunti dalla variabile aleatoria $X$ al
crescere del numero di osservazioni. In tal senso, se $\mathbb E(X) = \mu$,
spesso si dice che la variabile aleatoria $X$ vale _in media_ $\mu$.


````{prf:example} L'armatura di Mach-X, di nuovo
:label: ex-ea-mach-x

Riprendiamo la variabile $X$ dell'{prf:ref}`ex-va-mach-x`, che conta il numero
di sottosistemi funzionanti nell'armatura di Mach-X, con funzione di massa
$p_X(0) = 0.09$, $p_X(1) = 0.42$ e $p_X(2) = 0.49$. Il suo valore atteso è

```{math}
\mathbb E(X) = 0 \cdot 0.09 + 1 \cdot 0.42 + 2 \cdot 0.49 = 1.4 \enspace.
```

In media, dunque, $1.4$ sottosistemi su due risultano operativi. Anche qui il
valore atteso non è un esito possibile (i sottosistemi funzionanti sono $0$,
$1$ oppure $2$), eppure riassume bene la situazione: l'armatura tende a
funzionare quasi sempre, ma non perfettamente.
````

```{margin}
Questo è un primo esempio del legame che unisce la statistica descrittiva e il
calcolo delle probabilità: la media campionaria e il valore atteso misurano
entrambe la centralità, rispettivamente di un insieme di dati e di una
distribuzione.
```
Il grafico interattivo nella {numref}`fig_ex-convergence` illustra come la
media campionaria tenda al valore atteso al crescere del numero di
osservazioni. Ognuna delle $t$ traiettorie mostrate è ottenuta osservando per
$2\,000$ volte una variabile aleatoria $X$ che descrive il risultato del lancio
di un dado bilanciato, aggiornando ogni volta  il valore della media
campionaria. Ogni singola traiettoria oscilla inizialmente, ma si assesta
presto attorno a $\mathbb E(X) = \tfrac{7}{2}$, indicato dalla linea
tratteggiata arancione. Modificando la barra di scorrimento è possibile
cambiare il numero $t$ di traiettorie, e cliccando sul pulsante «Rigenera» è
possibile ricalcolare tutte le traiettorie, simulando automaticamente
l'osservazione di $t$ nuove realizzazioni di $X$.

````{customfigure}
:name: fig_ex-convergence
:class: left-align


```{interactive-code} python
:tags: [toggle-code]

# import asyncio
import matplotlib.pyplot as plt
import numpy as np

# from js import document
from pyscript import display
from pyscript.web import page, when


def trajectory(n, rng):
  result = rng.integers(1, 7, size=n)
  average = np.cumsum(result) / np.arange(1, n + 1)
  return average

rng = np.random.default_rng(42)
n = 2000

def render_trajectories():
    fig_traj, ax_traj = plt.subplots()
    num_traj = int(page['#num-traj'][0].value)
    page['#num-traj-value'][0].innerHTML = f'{num_traj}'

    for _ in range(num_traj):
        traj = trajectory(n, rng)

        ax_traj.plot(np.arange(1, n + 1), traj, color='C0', alpha=0.2)

    ax_traj.axhline(3.5, color='C1', linestyle='--')
    ax_traj.set_xscale('log')
    ax_traj.set_ylim(1, 6.5)
    display(fig_traj, target='graph-%this%', append=False)

@when("input", "#num-traj")
def ex_plot(event):
   render_trajectories()

@when("click", "#regen-traj")
def regenerate_plot(event):
   render_trajectories()

render_trajectories()
```

```{raw} html
<div class="plot-container">
    <div class="model-slider-container">
        <label for="num-traj">\(t\): </label>
        <input type="range" id="num-traj"
               min="5" max="50" value="20" step="5" />
        <span id="num-traj-value">50</span>
      <button type="button" id="regen-traj">Rigenera</button>
    </div>
</div>
```

Spezzate blu: grafici delle traiettorie descritte dalla media campionaria dei
valori osservati di una variabile aleatoria $X$ che descrive l'esito del lancio
di un dado bilanciato, al variare del numero $t$ di osservazioni da $1$ a $2\,000$.
Linea tratteggiata arancione: valore atteso $\mathbb E(X)$.
````

L'{prf:ref}`ex-ea-flatman` può essere riformulato in modo generale, legando
insieme un evento, la corrispondente variabile indicatrice e il valore atteso
di quest'ultima.

````{prf:theorem} Valore atteso di una variabile indicatrice
:label: teo-valore-atteso-indicatrice

Sia $A$ un evento e $\mathbb 1_A$ la sua variabile indicatrice. Allora
$\mathbb E(\mathbb 1_A) = \mathbb P(A)$.

````
````{sds-proof}
Come indicato nella {prf:ref}`def-indicatrice`, la variabile $\mathbb 1_A$
assume il valore $1$ quando $A$ si verifica e il valore $0$ altrimenti, quindi
$\mathbb P(\mathbb 1_A = 1) = \mathbb P(A)$ e
$\mathbb P(\mathbb 1_A = 0) = 1 - \mathbb P(A) = \mathbb P(\bar A)$. Pertanto

```{math}
\mathbb E(\mathbb 1_A) = 0 \cdot \mathbb P(\bar A) + 1 \cdot \mathbb P(A)
                       = \mathbb P(A) \enspace.
```
````

Questo risultato, semplice ma prezioso, dice che calcolare una probabilità è
un caso particolare di calcolare un valore atteso. È un ponte tra i due
concetti che useremo spesso.

````{prf:example} 
:label: ex-ea-indicatrice-armatura

Riprendendo l'{prf:ref}`ex-indic`, sia $A$ l'evento «l'armatura di Mach-X è
operativa», ovvero $\{X \geq 1\}$, e sia $\mathbb 1_A$ la corrispondente
variabile indicatrice. Sappiamo che $\mathbb P(A) = p_X(1) + p_X(2) = 0.91$,
dunque per il {prf:ref}`teo-valore-atteso-indicatrice`

```{math}
\mathbb E(\mathbb 1_A) = \mathbb P(A) = 0.91 \enspace.
```

Il valore atteso della variabile indicatrice è quindi semplicemente la
probabilità che l'armatura funzioni.
````

## Funzioni di variabili aleatorie

Capita spesso di essere interessati non tanto a una variabile aleatoria $X$ in
quanto tale, quanto a una sua trasformazione $Y = g(X)$: il danno inflitto da
un superpotere in funzione della sua intensità, il tempo necessario per
ricaricare un'abilità speciale in funzione della forza corrente, ma anche il
carico di un server in funzione del numero di richieste ricevute.
```{margin}
Quando considereremo le variabili aleatorie continue, il discorso si
complicherà: in questo caso, sarà necessario estendere alle funzioni il
concetto di misurabilità.
```
Se $X$ è discreta, in particolare, si può prendere in considerazione qualsiasi
funzione $g \colon \mathbb R \to \mathbb R$: per ogni $y \in \mathbb R$,
l'evento $\{ g(X) \leq y \}$ è sempre contenuto nella stessa sigma-algebra in
cui è definita $X$, e quindi $Y$ risulta automaticamente essere una variabile
aleatoria[^gX-definition]. Il modo più immediato di calcolarne il valore atteso
consiste nel ricavare prima la funzione di massa di $Y$, per poi applicare la
{prf:ref}`def-valore-atteso-discreto`.


````{prf:example} L'energia dello scarabeo
:label: ex-ea-energia-scarabeo

Quando si attiva, lo scarabeo di {extlink}`Blue Beetle
<https://dc.fandom.com/wiki/Jaime_Reyes_(New_Earth)>` si carica su uno di
quattro livelli, prediligendo quelli intermedi. Possiamo modellare questa
situazione desrivendo il livello dello scarabeo tramite una variabile
aleatoria $X$ il cui supporto è $S_X = \{1, 2, 3, 4\}$, e la funzione di massa
di probabilità è indicata nelle prime due colonne della tabella che segue.

| $x$ |    $p_X(x)$    | $y = x^2$ |    $p_Y(y)$    |
| :-: | :------------: | :-------: | :------------: |
| $1$ | $\tfrac{1}{8}$ |     $1$   | $\tfrac{1}{8}$ |
| $2$ | $\tfrac{1}{4}$ |     $4$   | $\tfrac{1}{4}$ |
| $3$ | $\tfrac{1}{2}$ |     $9$   | $\tfrac{1}{2}$ |
| $4$ | $\tfrac{1}{8}$ |    $16$   | $\tfrac{1}{8}$ |

Ipotizziamo che l'energia del raggio emesso dallo scarabeo cresca con il
quadrato del livello, cioè sia descritta da una nuova variabile aleatoria
$Y = g(X) = X^2$. La terza colonna della tabella indica quali sono le
realizzazioni di $Y$ che corrispondono a quelle di $X$. Poiché $g$ è una
funzione iniettiva, ogni livello $x$ produce un unico valore $y = x^2$ per
l'energia, e gli eventi $\{ Y = y \}$ e $\{ X = x \}$ coincidono, dunque
$p_Y(y) = p_Y(g(x)) = p_X(x)$. In altre parole, nel passaggio da $X$ a $Y$ il
supporto diventa $S_Y = \{1, 4, 9, 16\}$, mentre i valori di probabilità
rimangono invariati, come evidenziato nell'ultima colonna della tabella, che
insieme alla penultima descrive completamente la distribuzione di $Y$. Ciò
permette di calcolare il valore atteso di $Y$ applicando direttamente la sua
definizione:

```{math}
\mathbb E(X^2) =
\mathbb E(g(X)) = \mathbb E(Y) = 1 \cdot \tfrac{1}{8} + 4 \cdot \tfrac{1}{4}
                  + 9 \cdot \tfrac{1}{2} + 16 \cdot \tfrac{1}{8}
                = \frac{61}{8} = 7.625 \enspace.
```
````

In realtà non è necessario ricavare separatamente la distribuzione di $g(X)$,
perché $\mathbb E(g(X))$ può essere calcolato usando direttamente la funzione
di massa di probabilità di $X$, come dimostrato nel prossimo teorema.

```{margin}
In alcune fonti, {eq}`eq-lotus` viene introdotta come una definizione del
valore atteso di una funzione di variabile aleatoria. In realtà, ciò non è
necessario: basta applicare la definizione di valore atteso a $g(X)$, sotto le
opportune ipotesi dell'esistenza di quest'ultimo. Nella letteratura anglofona,
con una punta di ironia, questo risultato è noto come
{extlink}`law of the unconscious statistician
<https://en.wikipedia.org/wiki/Law_of_the_unconscious_statistician>`
(spesso abbreviato nell'acronimo LOTUS). In italiano, una traduzione possibile
è _legge dello statistico inconsapevole_, poiché questa formula consente di
calcolare $\mathbb E(g(X))$ utilizzando direttamente la distribuzione di $X$,
senza determinare esplicitamente quella di $g(X)$.
```
````{prf:theorem} Valore atteso di una funzione di variabile aleatoria
:label: teo-lotus

Siano $X$ una variabile aleatoria discreta con funzione di massa di probabilità
$p_X$ e $g \colon \mathbb R \to \mathbb R$ una funzione. Allora la variabile
aleatoria $Y = g(X)$ ha valore atteso

```{math}
:label: eq-lotus

\mathbb E(g(X)) = \sum_{x \in S_X} g(x)\, p_X(x) \enspace,
```

purché la serie converga assolutamente.
````
````{sds-proof}

Il supporto di $Y = g(X)$ è $S_Y = \{ g(x) \quad \forall x \in S_X \}$.
Fissato un valore $y \in S_Y$, l'evento $\{ Y = y \}$ si verifica se e solo se
$X$ assume uno dei valori $x \in S_X$ tali che $g(x) = y$, cioè

```{math}
\{ Y = y \} = \bigcup_{x \, : \, g(x)=y} \{ X = x \} \enspace.
```

Gli eventi all'interno di questa unione sono mutuamente esclusivi: per il
{prf:ref}`thm-eventi-singoletto`, dunque,

```{math}
p_Y(y) = \mathbb P(Y = y) = \sum_{x \, : \, g(x)=y} \mathbb P(X = x)
       = \sum_{x \, : \, g(x)=y} p_X(x) \enspace.
```

Sostituendo nella definizione di valore atteso e riorganizzando la doppia
somma, si ottiene

```{math}
\mathbb E(Y) = \sum_{y \in S_Y} y p_Y(y)
             = \sum_{y \in S_Y} y \, \sum_{x : g(x) = y} p_X(x)
             = \sum_{y \in S_Y} \sum_{x : g(x) = y} g(x)\, p_X(x) \enspace,
```

Per concludere, basta osservare che ogni $x \in S_X$ occorre una e una sola
volta all'interno della doppia sommatoria, che quindi equivale a sommare
per tutti gli elementi del supporto di $X$:

```{math}
\mathbb E(Y) = \sum_{y \in S_Y} \sum_{x : g(x) = y} g(x)\, p_X(x)
               \sum_{x \in S_X} g(x)\, p_X(x) \enspace.
```

Pertanto, se quest'ultima serie converge assolutamente, il valore atteso di
$Y$ è ben definito secondo quanto richiesto dalla
{prf:ref}`def-valore-atteso-discreto`, e la tesi è dimostrata.

````

````{prf:example} L'energia dello scarabeo, di nuovo
:label: ex-ea-lotus-scarabeo

Riprendiamo lo scarabeo di Blue Beetle dell'{prf:ref}`ex-ea-energia-scarabeo`,
con $X \in \{1, 2, 3, 4\}$ e $Y = X^2$. Riprendendo l'ultima formula di questo
esercizio, basta notare che

```{math}
\mathbb E(X^2) = 1 \cdot \tfrac{1}{8} + 4 \cdot \tfrac{1}{4}
                  + 9 \cdot \tfrac{1}{2} + 16 \cdot \tfrac{1}{8}
               = 1^2 \cdot \tfrac{1}{8} + 2^2 \cdot \tfrac{1}{4}
                  + 3^2 \cdot \tfrac{1}{2} + 4^2 \cdot \tfrac{1}{8}
               = \sum_{x=1}^4 x^2 p_X(x) \enspace,
```

che mostra come il {prf:ref}`teo-lotus` ci permette di calcolare
$\mathbb E(X^2)$ senza dover ricavare pria la distribuzione di $Y$.
````

Nell'esempio precedente la funzione $g$ era iniettiva, e ogni valore di $Y$
proveniva da un solo valore di $X$. Il {prf:ref}`teo-lotus` vale però per ogni
funzione $g \colon \mathbb R \to \mathbb R$, ed è particolarmente comodo quando
questa funzione _non_ è iniettiva. Infatti, in casi come questo, ricavare la
funzione di massa di probabilità di $Y$ richiederebbe di accorpare più valori
di $X$, mentre {eq}`eq-lotus` fornisce lo stesso risultato, considerando
direttamente la distribuzione della variabile aleatoria di partenza.

````{prf:example} L'entità di uno scarto
:label: ex-ea-lotus-modulo

Riprendiamo ancora la variabile $X$ dell'{prf:ref}`ex-va-discreta-scoiattoli`,
che esprime la differenza tra i punteggi di due dadi bilanciati, con
$S_X = [-5 .. 5]$ e $p_X(x) = \tfrac{6 - |x|}{36} \mathbb 1_{S_X}$.
Nell'{prf:ref}`ex-ea-simmetria` abbiamo visto che $\mathbb E(X) = 0$, a causa
della simmetria di $p_X$: ciò significa che in media le differenze positive e
quelle negative si compensano. Se però si è interessati a _quanto_ i due dadi
differiscono, a prescindere dal segno, bisogna considerare la variabile
aleatoria $\lvert X \rvert$. La funzione $x \mapsto \lvert x \rvert$ non è
iniettiva: per definizione le immagini di $x$ e $-x$ coincidono; ricavare
esplicitamente la massa di probabilità di $\lvert X \rvert$ richiederebbe di
sommare i contributi di valori opposti, ma il {prf:ref}`teo-lotus` ci permette
di evitare del tutto questo passaggio:

```{math}
\mathbb E(\lvert X \rvert) = \sum_{x = -5}^{5} \lvert x \rvert\, p_X(x)
   = 2 \sum_{x = 1}^{5} x \cdot \frac{6 - x}{36}
   = \frac{2}{36} (5 + 8 + 9 + 8 + 5) = \frac{35}{18} \enspace,
```

tenuto conto del fatto che che $x$ e $-x$ forniscono uno stesso contributo (da
cui proviene la moltiplicazione per $2$ della somma) e che quando $x = 0$ il
termine nella sommatoria è nullo. In media, dunque, i due dadi differiscono di
$\tfrac{35}{18} \approx 1.94$ punti.
````

## Valore atteso e trasformazioni affini

Tra le varie funzioni che potremmo applicare a una variabile aleatoria, vale la
pena focalizzare l'attenzione su quelle _affini_, della forma $x \mapsto a x +
b$, dove $a, b \in \mathbb R$ sono due costanti. Applicando il
{prf:ref}`teo-lotus` a questo tipo di funzioni si ottengono alcune proprietà
che &mdash; come vedremo &mdash; sono ampiamente usate in tutta la teoria della
probabilità.

```{margin}
Vedremo più avanti che questo teorema pone la base per dimostrare che il
valore atteso è un _operatore lineare_ che agisce su variabili aleatorie.
```
````{prf:theorem}
:label: teo-valore-atteso-trasf-affini

Siano $X$ una variabile aleatoria discreta con valore atteso finito e
$a, b \in \mathbb R$. Allora

```{math}
:label: eq-val-atteso-affine

\mathbb E(a X + b) = a\, \mathbb E(X) + b \enspace.
```
````
````{sds-proof}
Applicando il {prf:ref}`teo-lotus` alla funzione definita da $g(x) = a x + b$
e distribuendo le somme, si ottiene:

```{math}
\mathbb E(a X + b)
   = \sum_{x \in S_X} (a x + b)\, p_X(x)
   = \sum_{x \in S_X} a x\, p_X(x) + \sum_{x \in S_X} b\, p_X(x) \enspace.
```

```{margin}
Anche in questo caso, emerge l'analogia con la media campionaria, per la quale
valeva un'analoga proprietà.
```
Portando le costanti al di fuori delle sommatorie, si ottiene

```{math}
\mathbb E(a X + b)
   = a \sum_{x \in S_X} x\, p_X(x) + b \sum_{x \in S_X} p_X(x)
   = a\, \mathbb E(X) + b \enspace,
```

in virtù della {prf:ref}`def-valore-atteso-discreto` e del
{prf:ref}`teo-proprieta-massa`, rispettivamente per quanto riguarda la prima
e la seconda sommatoria.

````

````{prf:example} Il compenso di Songbird
:label: ex-ea-linearita-songbird

{extlink}`Songbird
<https://marvel.fandom.com/wiki/Melissa_Gold_(Earth-616)>` viene ingaggiata per
una missione e modella un numero aleatorio $X$ di costrutti sonori, con valore
atteso $\mathbb E(X) = 3$. Il contratto prevede un compenso fisso di $200$
crediti, più $50$ crediti per ciascun costrutto generato; il compenso totale è
quindi descritto dalla variabile $Y = 50 X + 200$. Per il
{prf:ref}`teo-valore-atteso-trasf-affini`,

```{math}
\mathbb E(Y) = 50\, \mathbb E(X) + 200 = 50 \cdot 3 + 200 = 350 \enspace.
```

In media, Songbird incassa $350$ crediti a missione, e abbiamo ottenuto il
risultato senza dover ricavare la funzione di massa di $Y$.
````

Dal teorema precedente si ricavano immediatamente alcune regole che
utilizzeremo spesso per semplificare il calcolo dei valori attesi.

````{prf:corollary}
:label: cor-ev-degenere

Per ogni $b \in \mathbb R$ si ha $\mathbb E(b) = b$.
````
````{sds-proof}
La tesi si ottiene ponendo $a = 0$ nel
{prf:ref}`teo-valore-atteso-trasf-affini`.
````

L'enunciato del corollario precedente può sembrare strano, in quanto il valore
atteso è un operatore che lavora con variabili aleatorie, non con valori
costanti. In realtà, ha perfettamente senso considerare una variabile aleatoria
_degenere_ che restituisce sempre lo stesso valore ogni volta che viene
osservata.

````{prf:definition}
:label: def-va-degenere

Una variabile aleatoria discreta $X$ si dice _degenere_ quando
$\lvert S_X \rvert = 1$.
````

Una variabile aleatoria $X$ di questo tipo deve avere come supporto un insieme
singoletto, sul cui elemento viene concentrata tutta la massa di
probabilità. Alla luce di questa definizione, il {prf:ref}`cor-ev-degenere`
dice che $b \in \mathbb R$, inteso come variabile aleatoria degenere con
dominio $S_b = \{ b \}$ e funzione di massa di probabilità definita da
$p_b(x) = \mathbb 1_{\{b\}}(x)$, è chiaramente centrata sull'unico valore che
può assumere.

````{prf:corollary}
:label: cor-ev-scalatura
Per ogni $a \in \mathbb R$ si ha $\mathbb E(aX) = a \mathbb E(X)$.
````
````{sds-proof}
La tesi si ottiene ponendo $b = 0$ nel
{prf:ref}`teo-valore-atteso-trasf-affini`.
````

Grazie a questo risultato, è possibile «estrarre» i coefficienti moltiplicativi
dall'operatore di valore atteso, in analogia a quanto si fa, per esempio, con
sommatorie e integrali. Ricordando la semantica del valore atteso, il
corollario dice semplicemente che moltiplicare una variabile aleatoria per un
fattore ha l'effetto di riscalare di quello stesso fattore il centro della
distribuzione. Un caso speciale è rappresentato dalla trasformazione dell'unità
di misura nella quale sono espressi i valori della variabile aleatoria: il
valore atteso continua a rappresentare la medesima grandezza, ma il suo valore
numerico cambia in accordo con il fattore di conversione.

````{prf:example} Cambiare unità di misura
:label: ex-ea-cambio-unita

Supponiamo che $X$ rappresenti la distanza, in chilometri, percorsa da
Songbird durante una missione, e che $\mathbb E(X) = 3.5$. La variabile
aleatoria $Y = 1000X$ esprime la stessa grandezza, ma misurata in metri.
Per il {prf:ref}`cor-ev-scalatura`, si può calcolare direttamente il valore
atteso della distanza in metri:

```{math}
\mathbb E(Y) = \mathbb E(1000X) = 1000\, \mathbb E(X) = 1000 \cdot 3.5 = 3500
\enspace.
```

Il significato fisico non cambia: stiamo ancora descrivendo la distanza media
percorsa in una missione. Cambia soltanto l'unità di misura, e quindi cambia
di conseguenza anche il valore numerico del valore atteso.
````

````{prf:corollary}
:label: cor-ev-traslazione
Per ogni $b \in \mathbb R$ si ha $\mathbb E(X + b) = \mathbb E(X) + b$.
````
````{sds-proof}
La tesi si ottiene ponendo $a = 1$ nel
{prf:ref}`teo-valore-atteso-trasf-affini`.
````

````{prf:example} Dalla scala Celsius alla scala Kelvin
:label: ex-ea-traslazione-kelvin

Supponiamo che $X$ rappresenti la temperatura, in gradi Celsius, del nucleo di
un laboratorio e che $\mathbb E(X) = 22$. Se vogliamo esprimere la stessa
temperatura in kelvin, dobbiamo considerare la variabile $Y = X + 273.15$.
Per il {prf:ref}`cor-ev-traslazione`, il valore atteso della temperatura nella
nuova scala si ottiene traslando di $273.15$ anche il valore atteso:

```{math}
\mathbb E(Y) = \mathbb E(X + 273.15) = \mathbb E(X) + 273.15 = 295.15
\enspace.
```

La grandezza fisica descritta non cambia: cambia solo il punto di origine
della scala, e quindi il valore atteso viene semplicemente traslato della
stessa quantità fissa.
````

Quando una variabile aleatoria assume valori enormi, ma la sua variabilità
intrinseca è governata da termini piccoli e ben modellati, conviene isolare la
parte costante e concentrare il calcolo solo sulla componente aleatoria, come
nell'esempio seguente.

````{prf:example} Il cannone entropico di Egghead
:label: ex-egghead-cannone

Immaginiamo che {extlink}`Egghead 
<https://marvel.fandom.com/wiki/Elihas_Starr_(Earth-616)>`, lo scienziato pazzo
nemesi di {extlink}`Ant-Man
<https://marvel.fandom.com/wiki/Henry_Pym_(Earth-616)>`, abbia costruito un
cannone a raggi entropici che minaccia New York. Il cannone ha un livello di
carica base fissato a $c = 10^8$ megajoule, un numero enorme, frutto di anni di
calcoli deliranti. Il problema è che il condensatore centrale è difettoso: a
ogni attivazione, il cannone rilascia una carica addizionale $Y$, che dipende
da quante valvole termoioniche decidono di funzionare correttamente quel
giorno. Più precisamente, $Y$ è una variabile aleatoria discreta, anch'essa
misurata in megajoule, con supporto $\{0,1,2,3,4,5\}$ ed equiprobabile su
questi valori. L'energia totale rilasciata è quindi $X = c + Y$.

Calcolare $\mathbb E(X)$ in modo esplicito richiederebbe di sommare delle
quantità dell'ordine delle centinaia di milioni di megajoule, il che è scomodo 
e inutilmente laborioso. Infatti, basta notare che

```{math}
\mathbb E(X) = \mathbb E(c + Y) =  c + \mathbb E(Y)
  = 10^8 + \frac{0+1+2+3+4+5}{6}
  = 10^8 + 2.5 \text{ megajoule}.
```

````

Un'altra applicazione dell'ultimo corollario, che incontreremo spesso, consiste
nel _centrare_ una variabile, cioè nel sottrarle il proprio valore atteso.

````{prf:example} Centrare una variabile
:label: ex-ea-centratura

Riprendiamo ancora una volta l'armatura di Mach-X dell'{prf:ref}`ex-ea-mach-x`,
per cui $\mathbb E(X) = 1.4$, e definiamo lo _scarto dalla media_
$Y = X - \mathbb E(X) = X - 1.4$. Questa nuova variabile misura quanto, di
volta in volta, il numero di sottosistemi attivi si discosta dal proprio valore
atteso. Applicando il {prf:ref}`teo-valore-atteso-trasf-affini`, con $a = 1$ e
$b = -1.4$, si ottiene

```{math}
\mathbb E(Y) = \mathbb E(X - 1.4) = \mathbb E(X) - 1.4 = 1.4 - 1.4 = 0
\enspace.
```

Lo si può verificare anche a mano: $Y$ assume i valori $-1.4$, $-0.4$ e $0.6$
con probabilità $0.09$, $0.42$ e $0.49$, e infatti
$-1.4 \cdot 0.09 - 0.4 \cdot 0.42 + 0.6 \cdot 0.49 = 0$.
````

È facile verificare che, in generale, ogni variabile aleatoria centrata ha
valore atteso nullo: la somma degli scostamenti dalla media, pesati con le
rispettive probabilità, è sempre nulla. Si tratta di una conseguenza del fatto
che $\mathbb E(X)$ è il baricentro della distribuzione di $X$, ed è anche alla
base della proprietà illustrata nella {numref}`fig_ex-barycenter-balance`, in
cui l'equilibrio dell'asse è dovuto all'annullamento del momento statico delle
masse rispetto al punto di appoggio. In entrambi i casi, infatti, gli
scostamenti dalla posizione di equilibrio, opportunamente pesati, si compensano
esattamente. Questa idea tornerà preziosa quando vorremo misurare la
dispersione di una variabile attorno al suo valore atteso.

## Altre misure di centralità

Il valore atteso non è l'unico modo di descrivere la centralità di una
distribuzione. Le altre due misure di centralità più importanti sono la
_mediana_ e la _moda_, anche in questo caso in analogia con quanto abbiamo già
visto nella parte sulla statistica descrittiva.

```{margin}
Ometterò il pedice, scrivendo semplicemente $m$ per indicare la mediana, quando
la variabile aleatoria di riferimento sarà chiara dal contesto. In letteratura
esistono anche altre convenzioni, in particolare $\operatorname{Med}(X)$, o
altre notazioni basate sui quantili (vedi {ref}`sec:quantili`). 
```
````{prf:definition} Mediana di una variabile aleatoria discreta
:label: def-mediana-va-discreta

La _mediana_ di una variabile aleatoria discreta $X$, indicata con $m_X$, è il
più piccolo valore reale tale che $\mathbb P(X \leq m_X) \geq 0.5$.
````

In altre parole, la mediana di una variabile aleatoria discreta è il più
piccolo valore reale alla cui sinistra si trova almeno metà della massa di
probabilità. Vale la pena osservare che, con questa definizione[^def-mediana],
la mediana di una variabile aleatoria discreta esiste sempre, ma non deve per
forza coincidere con un valore del supporto.

````{prf:example}
:label: ex-ea-mediana-supp

Consideriamo la variabile aleatoria $X$ che descrive il numero di Sling Ring
che {extlink}`Dr. Strange
<https://marvel.fandom.com/wiki/Stephen_Strange_(Earth-616)>`
riesce ad attivare contemporaneamente, e supponiamo che

```{math}
\mathbb P(X=0)=0.2 \qquad \mathbb P(X=1)=0.6 \qquad \mathbb P(X=2)=0.2
\enspace.
```

La mediana di $X$ è $m_X = 1$, perché $\mathbb P(X \leq 1)=0.8 \geq 0.5$ e
$\mathbb P(X \geq 1)=0.8 \geq 0.5$. Inoltre, se $x < 1$, allora
$\mathbb P(X \leq x) \leq 0.2 < 0.5$, mentre se $x > 1$, allora
$\mathbb P(X \geq x) \leq 0.2 < 0.5$. Dunque la mediana corrisponde a uno dei
valori di $X$.
````

````{prf:example}
:label: ex-ea-mediana-nosupp

Consideriamo una variabile aleatoria discreta $X$ tale che

```{math}
\mathbb P\left(X = 1 - \frac{1}{n}\right) = \frac{1}{2^{n+1}}
\quad\forall n  \in \mathbb N \enspace,
```

e $\mathbb P(X = 2) = \frac{1}{2}$. Il supporto sarà dunque l'insieme

```{math}
S_X = \left\{ 1-\frac{1}{n} \, n \in \mathbb N  \right\} \cup \{ 2 \} \enspace,
```

che contiene un'infinità numerabile di valori strettamente minori di $1$, oltre
all'intero $2$. Siccome

```{margin}
$\sum_{n=1}^{\infty} \frac{1}{2^{n+1}} =
\frac{1}{2} \sum_{n=1}^{\infty} \left(\frac{1}{2}\right)^n$, e la serie
geometrica di ragione $\tfrac{1}{2}$ converge a $1$.
```
```{math}
\mathbb P(X < 1) = \sum_{n=1}^{\infty} \frac{1}{2^{n+1}} = \frac{1}{2} \enspace,
```

per ogni $x < 1$, $\mathbb P(X \leq x) < \mathbb P(X < 1) = \frac{1}{2}$. Ciò
implica che la mediana di $X$ è $m_X = 1$, e dunque $m_X \notin S_X$.
````

````{prf:definition} Moda di una variabile aleatoria discreta
:label: def-moda-va-discreta

Sia $X$ una variabile aleatoria discreta con supporto $S_X$ e funzione di massa
di probabilità $p_X$. Un valore $x^\star \in S_X$ si dice _moda_ di $X$ se

```{math}
p_X(x^\star) \geq p_X(x)
\qquad \forall x \in S_X \enspace.
```
````

Una moda è quindi una specificazione che massimizza la funzione
di massa di probabilità, e ciò implica che per una data distribuzione possano
esistere più mode, come esemplificato di seguito.

````{prf:example} 
:label: ex-ea-moda-unica-multipla

Indichiamo con $X$ la variabile aleatoria che descrive il numero di duplicati
corporei che {extlink}`Multiple Man
<https://marvel.fandom.com/wiki/James_Madrox_(Earth-616)>` riesce a generare e
tenere simultaneamente in azione, con $S_X = \{0, 1, 2\}$. Se

```{math}
\mathbb P(X=0)=0.2 \qquad \mathbb P(X=1)=0.5 \qquad \mathbb P(X=2)=0.3
\enspace,
```

la moda è unica ed è uguale a $1$, perché $p_X(1)=0.5$ è strettamente maggiore
di tutti gli altri valori di massa di probabilità. Se invece

```{math}
\mathbb P(X=0)=0.4 \qquad \mathbb P(X=1)=0.2 \qquad \mathbb P(X=2)=0.4
\enspace,
```

la distribuzione ha le due mode $0$ e $2$, perché entrambi questi valori
massimizzano $p_X$.
````

La mediana e la moda non coincidono necessariamente con il valore atteso:
mentre $\mathbb E(X)$ tiene conto di tutte le specificazioni e delle loro
distanze, la mediana dipende soprattutto da come la probabilità si accumula
lungo la retta reale, e la moda individua semplicemente la specificazione più
probabile. Per questo motivo, quando una distribuzione è molto asimmetrica o
contiene valori estremi rari ma molto grandi, mediana, moda e valore atteso
possono raccontare aspetti diversi dello stesso fenomeno.

````{prf:example} Media, mediana e moda possono divergere
:label: ex-ea-mediana-moda

Supponiamo che $X$ descriva il numero di sigilli dimensionali che
{extlink}`Magik <https://marvel.fandom.com/wiki/Illyana_Rasputina_(Earth-616)>`
riesce a mantenere stabili durante un rituale, e che la sua distribuzione sia
data da

```{math}
\mathbb P(X=1)=0.6 \qquad \mathbb P(X=2)=0.3 \qquad \mathbb P(X=10)=0.1
\enspace.
```

La moda è uguale a $1$, perché è il valore più probabile, ed è anche la mediana
di $X$, perché $\mathbb P(X \leq 1) = 0.6 \geq 0.5$ e $
\mathbb P(X \geq 1) = 1 \geq 0.5$. Il valore atteso, però, è

```{math}
\mathbb E(X) = 1 \cdot 0.6 + 2 \cdot 0.3 + 10 \cdot 0.1 = 2.2 \enspace.
```

In questo caso, dunque, mediana e moda coincidono, ma il valore atteso è più
grande perché su di esso influiscono i pesi dei rimanenti valori di $X$.
````

Quando invece la distribuzione di una variabile aleatoria $X$ tende a essere
simmetrica rispetto a un valore centrale $c$, i contributi a $\mathbb E(X)$ dei
valori posti alla sinistra e alla destra di $c$ tendono a compensarsi, e questo
fa sì che $\mathbb E(X)$ e $c$ siano vicini tra loro (e coincideranno in caso
di perfetta simmetria). Per ragioni analoghe, $c$ tende frequentemente a essere
anche una mediana. Per la moda, però, la sola simmetria non basta: essa dipende
dalla localizzazione dei massimi della funzione di massa, e quindi può anche
non coincidere con gli altri due indici. Se alla simmetria si aggiunge anche
l'unimodalità, cioè la presenza di un unico picco centrale, allora valore
atteso, mediana e moda tendono molto più spesso ad allinearsi, e in molti casi
coincidono.

Nel seguito il valore atteso resterà la misura di centralità più importante,
perché si combina molto bene con le trasformazioni e con il calcolo algebrico.
Mediana e moda, però, rimangono strumenti preziosi: la prima è spesso più
robusta rispetto ai valori estremi, mentre la seconda individua il valore più
tipico o più frequente della distribuzione.


[^va-inesistente]: Chi dovesse avere la curiosità di vedere un esempio di
variabile aleatoria che non ammette valore atteso, può considerare la funzione
di massa di probabilità sul supporto $\mathbb N$ definita da $\mathbb
P(X=n)=\frac{6}{\pi^2}\frac{1}{n^2}$, i cui valori sommano a uno &mdash; perché
$\sum_{i=1}^{+\infty} 1/n^2 = \pi^2 / 6$. In questo caso si verifica
immediatamente che $\mathbb E(X)$ è uguale al valore della serie armonica, che
notoriamente diverge.

[^va-inesistente-terminologia]: Alcuni testi distinguono il caso in cui la
serie che definisce il valore atteso converge a un numero reale da quelli in
cui essa diverge a $\pm\infty$, oppure non determina alcun valore, neppure
infinito. Ciò permette di avere tre situazioni: (i) il valore atteso _esiste ed
è finito_; (ii) è definito in senso esteso, e vale più o meno infinito; (iii)
non è definito. Per non complicare la trattazione, ho deciso di considerare
semplicemente variabili aleatorie che ammettono valore atteso, intendendo con
ciò che esso esiste ed è finito, e variabili che non lo ammettono, unificando
le ultime due precedenti situazioni in un'unica categoria.

[^prob-meccanica]: Storicamente, il concetto di valore atteso viene fatto
risalire al XVII secolo, nell'ambito della teoria dei giochi d'azzardo. Esso
veniva infatti definito come il _valore equo_ di una scommessa: il prezzo che
sarebbe stato ragionevole pagare per partecipare a un gioco aleatorio. Sviluppi
successivi della disciplina hanno riconosciuto la coincidenza formale tra il
valore atteso e il baricentro di una distribuzione di masse, da cui derivano
termini come _massa di probabilità_. La successiva assiomatizzazione della
probabilità proposta da Andrej Nikolaevič Kolmogorov nel 1933, fondata sulla
teoria della misura, rese questa corrispondenza parte integrante della
struttura matematica della disciplina: una distribuzione di probabilità è una
misura di massa totale unitaria e il valore atteso coincide con il suo centro
di massa.

[^gX-definition]: Precisamente, per ogni $y \in \mathbb R$ si ha
```{math}
Y^{-1}(y) = \{ \omega \in \Omega \colon Y(\omega) \leq y \} 
= \{ \omega \in \Omega \colon g(X(\omega)) \leq y \} 
= \bigcup_{x \in S_X \colon g(x) \leq y} \{ X = x \} \enspace.
```
Notando che l'ultimo insieme ottenuto è l'unione al più numerabile di eventi,
si ottiene che $Y^{-1}(y)$ è sempre contenuto nella sigma-algebra alla base di
$X$, e ciò dimostra che $Y = g(X)$ soddisfa quanto richiesto nella
{prf:ref}`def-variabile-aleatoria`, ed è dunque una variabile aleatoria.

[^def-mediana]: In letteratura si incontrano diverse convenzioni per definire
la mediana. In particolare, un'alternativa consiste nel definirla come un
qualunque valore $m$ per il quale $\mathbb P(X\leq m)\geq 0.5$ e
$\mathbb P(X\geq m)\geq 0.5$, e dunque come il valore che lascia almeno metà
della massa di probabilità sia alla sua sinistra che alla sua destra. Questa
convenzione è per certi versi più naturale, ma non garantisce l'unicità della
mediana. Le due definizioni coincidono in molti casi, in particolare per
distribuzioni continue con funzione di ripartizione strettamente crescente, ma possono produrre risultati diversi in presenza di distribuzioni discrete o di intervalli sui quali la funzione di ripartizione è costante.


## Vero o falso?

Analizzate ciascuna delle seguenti affermazioni, che riguardano una variabile
aleatoria discreta $X$ con valore atteso finito, e dite se è vera o falsa,
motivando il vostro ragionamento. Cliccate su di essa per visualizzare la
risposta corretta.

````{tf-item}
Il valore atteso $\mathbb E(X)$ è sempre uno dei valori che $X$ può assumere.
+++
**Falsa**. Il valore atteso è il baricentro della distribuzione e può cadere
fuori dal supporto. Lo abbiamo visto con il dado bilanciato
dell'{prf:ref}`ex-ea-dado`, il cui valore atteso $3.5$ non è un esito
possibile.
````

````{tf-item}
Il valore atteso $\mathbb E(X)$ è espresso nella stessa unità di misura dei
valori di $X$.
+++
**Vera**. Nella somma $\sum_x x\, p_X(x)$ i valori $x$ portano l'unità di
misura, mentre le probabilità $p_X(x)$ sono numeri puri; il risultato eredita
quindi l'unità di misura di $X$.
````

````{tf-item}
Se $X \geq 0$ con probabilità $1$, allora $\mathbb E(X) \geq 0$.
+++
**Vera**. Tutti i punti di massa $x \in S_X$ sono non negativi e le
probabilità $p_X(x)$ pure; una somma di prodotti di quantità non negative è non
negativa, dunque $\mathbb E(X) \geq 0$.
````

````{tf-item}
Per ogni variabile aleatoria $X$ vale $\mathbb E(X^2) = (\mathbb E(X))^2$.
+++
**Falsa**. In generale le due quantità sono diverse: per lo scarabeo di Blue
Beetle (vedi l'{prf:ref}`ex-ea-lotus-scarabeo`) si ha $\mathbb E(X^2) = 7.625$
ma $(\mathbb E(X))^2 \approx 6.89$. L'uguaglianza vale solo in casi
particolari, per esempio quando $X$ è costante.
````

````{tf-item}
Per una costante $c$ si ha $\mathbb E(c) = c$.
+++
**Vera**. È fondamentalmente l'enunciato del 
{prf:ref}`teo-valore-atteso-trasf-affini`. Una variabile aleatoria degenere
assume sempre lo stesso valore, quindi la sua media non può che essere quel
valore.
````

````{tf-item}
Per ogni $a, b \in \mathbb R$ vale $\mathbb E(a X + b) = a\, \mathbb E(X) + b$.
+++
**Vera**. È esattamente l'enunciato del
{prf:ref}`teo-valore-atteso-trasf-affini`.
````

````{tf-item}
Per la variabile indicatrice $\mathbb 1_A$ di un evento $A$ vale
$\mathbb E(\mathbb 1_A) = \mathbb P(A)$.
+++
**Vera**. È il contenuto del {prf:ref}`teo-valore-atteso-indicatrice`:
calcolare la probabilità di un evento equivale a calcolare il valore atteso
della sua variabile indicatrice.
````

````{tf-item}
Ogni variabile aleatoria discreta ha valore atteso ben definito.
+++
**Falsa**. Quando il supporto è infinito numerabile la serie in
{eq}`eq-valore-atteso` può non convergere assolutamente; in tal caso il valore
atteso non esiste. Per i supporti finiti, invece, è sempre ben definito.
````

````{tf-item}
Se una variabile aleatoria discreta ha valore atteso uguale alla propria
mediana, allora la sua distribuzione è necessariamente simmetrica.
+++
**Falsa**. L'uguaglianza tra media e mediana, da sola, non basta a garantire
la simmetria. Per esempio, se $X$ assume i valori $0$, $1$ e $3$ con
probabilità rispettivamente $0.4$, $0.4$ e $0.2$, allora
$\mathbb E(X) = 0 \cdot 0.4 + 1 \cdot 0.4 + 3 \cdot 0.2 = 1$, e anche $1$ è
una mediana perché $\mathbb P(X \leq 1)=0.8 \geq 0.5$ e
$\mathbb P(X \geq 1)=0.6 \geq 0.5$; tuttavia la distribuzione non è simmetrica
rispetto a $1$.
````

````{tf-item}
Per una variabile aleatoria discreta, mediana e moda sono sempre uniche.
+++
**Falsa**. La {prf:ref}`def-mediana-va-discreta` individua la mediana in modo
univoco, ma ciò non è vero per la moda. In particolare,
l'{prf:ref}`ex-ea-moda-unica-multipla` mostra una distribuzione con due mode.
````

## Esercizi

````{exercise} •
:label: ex-ea-squirrel

Per compiere una missione, {extlink}`Squirrel Girl
<https://marvel.fandom.com/wiki/Doreen_Green_(Earth-616)>` chiama in aiuto un
numero aleatorio $N$ di scoiattoli, con $N \in \{1, 2, 3, 4\}$ e funzione di
massa

```{math}
p_N(1) = 0.1, \quad p_N(2) = 0.2, \quad p_N(3) = 0.3, \quad p_N(4) = 0.4
\enspace.
```

1. Verificate che $p_N$ è una funzione di massa di probabilità.
2. Calcolate il numero atteso di scoiattoli $\mathbb E(N)$.
````
````{solution} ex-ea-squirrel
:class: dropdown

1. Le masse sono tutte non negative e
   $0.1 + 0.2 + 0.3 + 0.4 = 1$, quindi per il
   {prf:ref}`thm-caratterizzazione-massa` $p_N$ è una funzione di massa di
   probabilità.

2. Applicando la {prf:ref}`def-valore-atteso-discreto`,
   ```{math}
   \mathbb E(N) = 1 \cdot 0.1 + 2 \cdot 0.2 + 3 \cdot 0.3 + 4 \cdot 0.4
                = 0.1 + 0.4 + 0.9 + 1.6 = 3 \enspace.
   ```
   In media Squirrel Girl raduna pertanto $3$ scoiattoli.
````

````{exercise} ••
:label: ex-ea-quadrato

Con riferimento alla variabile $N$ dell'{ref}`ex-ea-squirrel`:

1. Usando il {prf:ref}`teo-lotus`, calcolate $\mathbb E(N^2)$.
2. Confrontate $\mathbb E(N^2)$ con $\mathbb E(N)^2$ e commentate il risultato
   che osservate.
````
````{solution} ex-ea-quadrato
:class: dropdown

1. Per la legge dello statistico inconsapevole,
   ```{math}
   \mathbb E(N^2) = 1^2 \cdot 0.1 + 2^2 \cdot 0.2 + 3^2 \cdot 0.3
                  + 4^2 \cdot 0.4 = 0.1 + 0.8 + 2.7 + 6.4 = 10 \enspace.
   ```

2. Si ha $\mathbb E(N)^2 = 3^2 = 9 \neq 10 = \mathbb E(N^2)$. Le due quantità
   sono diverse, e in particolare il valore atteso del quadrato supera il
   quadrato del valore atteso. Nel prossimo paragrafo vedremo che la differenza
   $\mathbb E(N^2) - \mathbb E(N)^2 = 1$ misura quanto $N$ tende a
   discostarsi dalla propria media.
````

````{exercise} ••
:label: ex-ea-linearita

Sempre con la variabile $N$ dell'{ref}`ex-ea-squirrel`, supponete che ogni
scoiattolo consumi $2$ nocciole e che Squirrel Girl ne tenga da parte altre
$5$ come riserva, indipendentemente dal numero di scoiattoli. Sia
$C = 2 N + 5$ il numero totale di nocciole necessarie per portare a termine la
missione.

1. Calcolate $\mathbb E(C)$ usando {eq}`eq-val-atteso-affine`.
2. Verificate il risultato calcolando direttamente la funzione di massa di $C$
   e applicando la definizione.
````
````{solution} ex-ea-linearita
:class: dropdown

1. Per il {prf:ref}`teo-valore-atteso-trasf-affini`,
   ```{math}
   \mathbb E(C) = \mathbb E(2 N + 5) = 2\, \mathbb E(N) + 5
                = 2 \cdot 3 + 5 = 11 \enspace.
   ```

2. La funzione $n \mapsto 2 n + 5$ è iniettiva, quindi $C$ assume i valori
   $7, 9, 11, 13$ con le stesse probabilità $0.1, 0.2, 0.3, 0.4$ di $N$.
   Allora
   ```{math}
   \mathbb E(C) = 7 \cdot 0.1 + 9 \cdot 0.2 + 11 \cdot 0.3 + 13 \cdot 0.4
                = 0.7 + 1.8 + 3.3 + 5.2 = 11 \enspace,
   ```
   in accordo con il punto precedente.
````

````{exercise} •••
:label: ex-ea-gioco-equo

{extlink}`Mr. Immortal
<https://marvel.fandom.com/wiki/Craig_Hollis_(Earth-616)>`sfrutta la propria
immortalità per giocare innumerevoli volte a un gioco rischioso. A ogni partita
paga una quota d'ingresso di $c$ crediti e vince una somma descritta da una
variabile aleatoria $W$, con $W \in \{0, 2, 10\}$ e funzione di massa di
probabilità

```{math}
p_W(0) = 0.5, \qquad p_W(2) = 0.4, \qquad p_W(10) = 0.1 \enspace.
```

Il guadagno netto di una partita è $G = W - c$.

1. Calcolate $\mathbb E(W)$.
2. Determinate la quota $c$ che rende il gioco _equo_, cioè tale che
   $\mathbb E(G) = 0$.
3. Se la quota richiesta fosse $c = 1.5$, a Mr. Immortal converrebbe giocare a
   lungo termine?
````
````{solution} ex-ea-gioco-equo
:class: dropdown

1. Applicando la definizione di valore atteso,
   ```{math}
   \mathbb E(W) = 0 \cdot 0.5 + 2 \cdot 0.4 + 10 \cdot 0.1
                = 0.8 + 1 = 1.8 \enspace.
   ```

2. Per il {prf:ref}`teo-valore-atteso-trasf-affini`,
   $\mathbb E(G) = \mathbb E(W) - c$. Imponendo $\mathbb E(G) = 0$ si ottiene
   $c = \mathbb E(W) = 1.8$ crediti.

3. Con $c = 1.5$ si ha $\mathbb E(G) = 1.8 - 1.5 = 0.3 > 0$. Il guadagno netto
   atteso per partita è positivo, e applicando l'interpretazione frequentista
   possiamo asserire che su un numero elevato di partite la media dei guadagni
   tende a $0.3$ crediti a partita: a Mr. Immortal, che di tempo ne ha in abbondanza, conviene giocare.
````

````{exercise} •
:label: ex-ea-doorman

Riprendete la variabile $X$ dell'{prf:ref}`ex-va-doorman`, che indica il piano
su cui Doorman fa materializzare i compagni, con
$p_X(1) = \tfrac{1}{2}$, $p_X(2) = \tfrac{1}{3}$ e $p_X(3) = \tfrac{1}{6}$.
Calcolatene il valore atteso.
````
````{solution} ex-ea-doorman
:class: dropdown

Applicando la {prf:ref}`def-valore-atteso-discreto`,

```{math}
\mathbb E(X) = 1 \cdot \tfrac{1}{2} + 2 \cdot \tfrac{1}{3}
               + 3 \cdot \tfrac{1}{6}
             = \tfrac{5}{3} \approx 1.67 \enspace.
```

Come già visto in altri esempi, il valore atteso $\tfrac{5}{3}$ non indica un
piano esistente dell'edificio. Applicando l'interpretazione frequentista, si
può dire che, in media, i compagni atterrano poco sopra il primo piano. 
````

````{exercise} ••
:label: ex-ea-indicatrice-doorman

Sempre con la variabile $X$ dell'{prf:ref}`ex-va-doorman`, sia $A$ l'evento
«il teletrasporto finisce su un piano dispari», cioè $A = \{X \in \{1, 3\}\}$,
e sia $\mathbb 1_A$ la sua variabile indicatrice.

1. Calcolate $\mathbb E(\mathbb 1_A)$.
2. Spiegate a parole perché il risultato coincide con una probabilità già
   calcolata nel capitolo precedente.
````
````{solution} ex-ea-indicatrice-doorman
:class: dropdown

1. Per il {prf:ref}`teo-valore-atteso-indicatrice`,
   $\mathbb E(\mathbb 1_A) = \mathbb P(A)$, e per il
   {prf:ref}`thm-eventi-singoletto`,

   ```{math}
   \mathbb E(\mathbb 1_A) = \mathbb P(X \in \{1, 3\})
      = p_X(1) + p_X(3) = \tfrac{1}{2} + \tfrac{1}{6} = \tfrac{2}{3} \enspace.
   ```

2. Il risultato coincide con il valore ottenuto
   nell'{prf:ref}`ex-va-doorman-singoletto`, proprio perché calcolare il valore
   atteso della variabile indicatrice di un evento equivale a calcolare la
   probabilità che quest'ultimo si verifichi. La variabile indicatrice codifica
   semplicemente con un numero la risposta alla domanda «l'evento si è
   verificato?».
````

````{exercise} ••
:label: ex-prg-ex

Scrivete una funzione `expected_value` che accetta come argomenti:

- una lista di valori,
- una lista di masse di probabilità che ha la stessa lunghezza dell'argomento
  precedente e i cui elementi sommano a $1$,

e che restituisce il valore atteso della corrispondente variabile aleatoria.
Verificate il funzionamento di questa funzione su:

- una variabile aleatoria degenere che è sempre uguale a $1$,
- una variabile aleatoria che assume solamente le specificazioni $0$ e
  $1$ con uguale probabilità,
- una variabile aleatoria che assume solamente le specificazioni $0$ e
  $1$, rispettivamente con probabilità $\tfrac{3}{5}$ e $\tfrac{2}{5}$,
- la variabile aleatoria che indica il risultato del lancio di un dado
  bilanciato a sei facce.

````
````{solution} ex-prg-ex
:class: dropdown

La cella seguente contiene una possibile implementazione della funzione, che
verifica i prerequisiti indicati e che applica successivamente la
{prf:ref}`def-valore-atteso-discreto`. Vengono poi eseguiti i test indicati.

```{code-cell} python
import numpy as np

def expected_value(x, p):
    assert len(x) == len(p), "x and p must have the same length"
    assert abs(sum(p) - 1) < 1e-6, "Probabilities must sum to 1"
    return sum(x_i * p_i for x_i, p_i in zip(x, p))

assert expected_value([1], [1]) == 1
assert expected_value([0, 1], [0.5, 0.5]) == 0.5
assert expected_value([0, 1], [3/5, 2/5]) == 0.4
assert expected_value(np.arange(1, 7), [1/6] * 6) == 3.5
```

````

````{exercise} ••
:label: ex-ea-boomboom

{extlink}`Boom-Boom
<https://marvel.fandom.com/wiki/Tabitha_Smith_(Earth-616)>` semina nell'arena
un numero aleatorio $X$ di sfere esplosive, con $X \in \{0, 1, 2, 3\}$ e
funzione di massa

```{math}
p_X(0) = 0.4, \quad p_X(1) = 0.3, \quad p_X(2) = 0.2, \quad p_X(3) = 0.1
\enspace.
```

Quando due sfere entrano in risonanza si amplificano a vicenda, e il numero di
coppie risonanti è $g(X) = X (X - 1) / 2$.

1. Osservate che $g$ non è iniettiva su $S_X$: individuate due valori di $X$
   che danno lo stesso numero di coppie.
2. Usando il {prf:ref}`teo-lotus`, calcolate il numero atteso di coppie
   risonanti.
````
````{solution} ex-ea-boomboom
:class: dropdown

1. Si ha $g(0) = g(1) = 0$, perché chiaramente partendo da zero o da una sfera
   non è possibile formare alcuna coppia, dunque $g$ non è iniettiva.

2. Calcoliamo $g$ su ciascun valore: $g(0) = 0$, $g(1) = 0$, $g(2) = 1$,
   $g(3) = 3$. Per la legge dello statistico inconsapevole,
   ```{math}
   \mathbb E(X(X - 1)) = 0 \cdot 0.4 + 0 \cdot 0.3 + 1 \cdot 0.2
                       + 3 \cdot 0.1 = 0.2 + 0.3 = \frac{1}{2} \enspace.
   ```
   In media si formerebbe quindi una coppia risonante ogni due volte che
   Boom-Boom posiziona le sfere.
````

````{exercise} ••••
:label: ex-monotonicita-e

Sia $X$ una variabile aleatoria discreta, e siano $f$ e $g$ due funzioni aventi
$\mathbb R$ come dominio e come codominio, caratterizzate dal fatto che per
ogni $x \in \mathbb R$ vale $f(x) \leq g(x)$. Dimostrate che
$\mathbb E(f(X)) \leq \mathbb E(g(X))$.
````
````{solution} ex-monotonicita-e
:class: dropdown

Indicati con $D_X$ e $p_X$ rispettivamente il dominio e la funzione di
massa di probabilità di $X$, si avrà

```{math}
\mathbb E(f(X)) = \sum_{x \in D_X} f(x) p_X(x) \leq
                  \sum_{x \in D_X} g(x) p_X(x) = \mathbb E(g(X)) \enspace.
```
````

````{exercise} ••
:label: ex-ea-centratura-prova

Sia $X$ una variabile aleatoria discreta con valore atteso finito
$\mu = \mathbb E(X)$, e definite la variabile centrata $Y = X - \mu$.
Dimostrate che $\mathbb E(Y) = 0$, indipendentemente dalla distribuzione di
$X$.
````
````{solution} ex-ea-centratura-prova
:class: dropdown

Poiché $\mu$ è una costante, possiamo applicare il
{prf:ref}`teo-valore-atteso-trasf-affini` con $a = 1$ e $b = -\mu$:

```{math}
\mathbb E(Y) = \mathbb E(X - \mu) = \mathbb E(X) - \mu = 0
\enspace.
```

Il risultato non dipende dalla particolare funzione di massa di $X$: ogni
variabile centrata ha valore atteso nullo, come già osservato
nell'{prf:ref}`ex-ea-centratura`. Intuitivamente, sottraendo la media si sposta
l'origine proprio nel baricentro della distribuzione.
````

````{exercise} •••
:label: ex-ea-geometrica

{extlink}`Flatman
<https://marvel.fandom.com/wiki/Flatman_(Matt)_(Earth-616)>` si ostina a
infilarsi sotto la stessa porta finché non riesce a passare. La variabile
aleatoria $X$ che indica il numero di tentativi necessari per riuscire ad
attraversare la porta ha quindi come supporto $\mathbb N$.

1. Verificate che la funzione descritta da
   $p_X(k) = \left( \tfrac{1}{2} \right)^k$ è una funzione di massa di
   probabilità per $X$.
2. Calcolate il numero atteso di tentativi $\mathbb E(X)$.

````
````{solution} ex-ea-geometrica
:class: dropdown

1. I valori di $p_X$ sono sempre positivi, e sommandoli per tutti gli argomenti
   $k \in \mathbb N$ si ottiene una serie geometrica di ragione $\tfrac{1}{2}$,
   contando a partire da $k = 1$. Per {eq}`eq-serie-geometrica-da-uno`,
   ```{math}
   \sum_{k = 1}^{\infty} \left( \tfrac{1}{2} \right)^k
      = \frac{\tfrac{1}{2}}{1 - \tfrac{1}{2}} = 1 \enspace,
   ```
   quindi $p_X$ è una funzione di massa di probabilità.

2. Tutti gli addendi sono positivi, dunque il valore atteso di $X$ è ben
   definito se la serie $\sum_{k=1}^{+\infty} k \, p_X(k)$ converge. Poniamo

   ```{math}
   :label: eq-sum-geo-sx

   S = \mathbb E(X) = \sum_{k=1}^{+\infty} k \, p_X(k)
     = \sum_{k=1}^{+\infty} \frac{k}{2^k}.
   ```

   Dividendo entrambi i membri per $2$ si ottiene

   ```{math}
   :label: eq-sum-geo-dx

   \frac{S}{2} = \sum_{k=1}^{+\infty} \frac{k}{2^{k+1}}
               = \sum_{h=2}^{+\infty} \frac{h-1}{2^h} \enspace,
   ```

   dove nell'ultimo passaggio è stato effettuato il cambiamento $h = k+1$ per
   l'indice di sommatoria. Sottraendo membro a membro {eq}`eq-sum-geo-dx` da
   {eq}`eq-sum-geo-sx` si ottiene

   ```{math}
   S - \frac{S}{2}
   = \sum_{k=1}^{+\infty} \frac{k}{2^k} -\sum_{h=2}^{+\infty}\frac{h-1}{2^h}
   = \sum_{k=1}^{+\infty} \frac{k}{2^k} -\sum_{h=2}^{+\infty}\frac{h}{2^h}
     + \sum_{h=2}^\infty\frac{1}{2^h}
   = \frac{1}{2} + \sum_{k=2}^\infty\frac{1}{2^k} \enspace.
   ```

   L'ultima sommatoria corrisponde alla serie geometrica di ragione
   $\tfrac{1}{2}$, contando a partire da $2$, per cui

   ```{math}
   \sum_{k=2}^\infty\frac{1}{2^k}
   = \sum_{k=1}^\infty\frac{1}{2^k} - \frac{1}{2} = 1 - \frac{1}{2}
   = \frac{1}{2} \enspace.
   ```

   Pertanto $\tfrac{S}{2} = \tfrac{1}{2} + \tfrac{1}{2} = 1$, e quindi
   $\mathbb E(X) = S = 2$. Ciò significa che, in media, Flatman riesce ad
   attraversare la porta al secondo tentativo.
````

````{exercise} •••
:label: ex-ea-decisione

{extlink}`Moonstone
<https://marvel.fandom.com/wiki/Karla_Sofen_(Earth-616)>`, sempre calcolatrice,
deve scegliere come farsi ricompensare per un colpo. Le vengono proposti tre
schemi:

- schema $A$: riceve $6$ crediti con certezza;
- schema $B$: lancia un dado bilanciato e riceve in crediti il punteggio
  ottenuto;
- schema $C$: con probabilità $0.3$ riceve $15$ crediti, altrimenti nulla.

1. Calcolate il valore atteso della ricompensa per ciascuno schema.
2. Quale schema conviene a Moonstone se vuole massimizzare la ricompensa
   media?
3. Le viene infine proposto uno schema $D$: con probabilità $\tfrac{1}{2}$
   riceve $v$ crediti, altrimenti $2$ crediti. Per quale valore di $v$ lo
   schema $D$ ha lo stesso valore atteso dello schema $A$?
````
````{solution} ex-ea-decisione
:class: dropdown

1. Indichiamo con $W_A$, $W_B$, $W_C$ le variabili aleatorie che indicano le
   ricompense secondo i tre schemi.
   - Nello schema $A$ il compenso è costante e $\mathbb E(W_A) = 6$.
   - Nello schema $B$, il compenso medio si calcola esattamente come
     nell'{prf:ref}`ex-ea-dado`, dunque $\mathbb E(W_B) = 3.5$.
   - Per lo schema $C$, la ricompensa è $W_C = 15 \cdot \mathbb 1_C$ dove $C$ è
     un evento che si verifica con probabilità $0.3$; per il
     {prf:ref}`cor-ev-scalatura` e il {prf:ref}`teo-valore-atteso-indicatrice`,
     $\mathbb E(W_C) = 15 \, \mathbb E(\mathbb 1_C) = 15 \cdot 0.3 = 4.5$.

2. Confrontando i tre valori attesi ottenuti al punto precedente si verifica
   immediatamente che lo schema $A$ offre la ricompensa media più alta.

3. Indicando con $W_D$ la variabile aleatoria che descrive il compenso per lo
   schema $D$ e applicando la {prf:ref}`def-valore-atteso-discreto`, si ha
   ```{math}
   \mathbb E(W_D) = \tfrac{1}{2} v + \tfrac{1}{2} \cdot 2 = \tfrac{v}{2} + 1
   \enspace.
   ```
   Imponendo $\mathbb E(W_D) = \mathbb E(W_A) = 6$ si ottiene
   $\tfrac{v}{2} + 1 = 6$, da cui $v = 10$ crediti.
````

````{exercise} •
:label: ex-ea-mediana-moda-base

{extlink}`Jubilee <https://marvel.fandom.com/wiki/Jubilation_Lee_(Earth-616)>`
genera un numero aleatorio $X$ di fuochi pirotecnici in miniatura, con

```{math}
\mathbb P(X=1)=0.2, \qquad \mathbb P(X=2)=0.5, \qquad \mathbb P(X=3)=0.3
\enspace.
```

1. Determinate le mode di $X$.
2. Determinate la mediana di $X$.
3. Stabilite se almeno una moda coincide con la mediana.
````
````{solution} ex-ea-mediana-moda-base
:class: dropdown

1. La variabile aleatoria ha una sola moda, in corrispondenza di $2$, perché
   $p_X(2)=0.5$ è la massa di probabilità più grande.

2. Per ogni $x < 2$, si ha $\mathbb P(X \leq x) \leq 0.2$, quindi $1$ non può
   essere una mediana. Invece $\mathbb P(X \leq 2) \geq 0.5$ e
   $\mathbb P(X \geq 2) \geq 0.5$, quindi $2$ è una mediana.
   Infine, per ogni $x > 2$, $\mathbb P(X \geq x) \leq 0.3$, quindi non ci
   possono essere altre mediane.

3. Per quanto ottenuto nei punti precedenti, la moda è unica e coincide con la
   mediana.
````

````{exercise} ••
:label: ex-ea-mediana-varchi

{extlink}`Cloak <https://marvel.fandom.com/wiki/Tyrone_Johnson_(Earth-616)>`
apre un numero aleatorio $Y$ di varchi d'ombra, con

```{math}
\mathbb P(Y=0)=0.5, \qquad \mathbb P(Y=4)=0.5 \enspace.
```

1. Mostrate che ogni $x \geq 0$ è un candidato a essere la mediana di $Y$.
2. Calcolate la mediana di $Y$.
2. Determinate le mode di $Y$.
````
````{solution} ex-ea-mediana-varchi
:class: dropdown

1. Se $x$ è non negativo, allora $\mathbb P(Y \leq x) \geq 0.5$,
   perché almeno una delle due masse da $0.5$ cade sempre a sinistra di $x$, o
   coincide con esso.

2. La mediana di $Y$ è il più piccolo tra i valori individuati al punto
   precedente, dunque $m_Y = 0$.

3. Le mode sono $0$ e $4$, perché entrambe massimizzano la funzione di massa,
   avendo probabilità uguale a $0.5$.
````

````{exercise} •••
:label: ex-ea-media-mediana-moda

{extlink}`Forge <https://marvel.fandom.com/wiki/Forge_(Earth-616)>` collauda
un dispositivo che produce un numero aleatorio $Z$ di impulsi energetici, con

```{math}
\mathbb P(Z=1)=0.6, \qquad \mathbb P(Z=2)=0.3, \qquad \mathbb P(Z=10)=0.1
\enspace.
```

1. Calcolate la mediana di $Z$.
2. Mostrate che la moda di $Z$ è unica, e calcolatela.
3. Calcolate $\mathbb E(Z)$.
4. Commentate la relazione tra questi tre indici di centralità.
````
````{solution} ex-ea-media-mediana-moda
:class: dropdown

1. Un qualsiasi valore $z < 1$ non può essere una mediana, perché
   $\mathbb P(Z \leq z) = 0$. Invece $\mathbb P(Z \leq 1) \geq 0.5$, da cui si
   ricava $m_Z = 1$.

2. La funzione di massa di probabilità di $Z$ ha un unico valore massimo, in
   corrispondenza di $p_Z(1)=0.6$. Pertanto la moda è unica ed è uguale a $1$.

3. Applicando la {prf:ref}`def-valore-atteso-discreto`,
   ```{math}
   \mathbb E(Z)=1 \cdot 0.6 + 2 \cdot 0.3 + 10 \cdot 0.1 = 2.2 \enspace.
   ```

4. In questo caso mediana e moda coincidono, ma il valore atteso è più grande,
   perché risente del fatto che i valori $2$ e $10$ hanno probabilità non
   nulla.
````

## Concetti fondamentali

Pensate ai concetti fondamentali illustrati in questo paragrafo ed elencateli.
Nella lista qui sotto sono già presenti gli stessi concetti, ma nascosti.
Cliccate sul pulsante per mostrarli sotto forma di parole chiave, quindi
confrontateli con la vostra lista. Provate infine a descrivere ciascun concetto
con parole vostre.

````{sds-wordcloud}
Valore atteso
Media pesata
Baricentro della distribuzione
Interpretazione frequentista
Funzione di una variabile aleatoria
Valore atteso di una funzione di variabile aleatoria
Legge dello statistico inconsapevole
Trasformazioni affini
Valore atteso di trasformazioni affini
Centratura di una variabile aleatoria
Mediana
Moda
````

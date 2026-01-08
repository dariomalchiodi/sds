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

(sec_principio-fondamentale-combinatorica)=
# Principio fondamentale

Lo so che può sembrare impossibile, ma in alcuni casi Batman ha scelto
di indossare dei costumi molto più sgargianti rispetto a quello grigio
dei fumetti originali e a quello nero dei film più recenti. Per esempio,
nel numero 241 di _Detective Comics_ l'uomo-pipistrello decide di combattere
il crimine alternando tra le altre tenute arancioni, verdi e rosa al fine
di attirare l'attenzione su se stesso piuttosto che su una ferita al braccio
di Robin che avrebbe potuto destare sospetti essendo ovviamente uguale a
quella che aveva riportato la sua identità segreta Dick Grayson {cite}`robb`.

Modificando leggermente il contenuto di questo fumetto, immaginiamo che
per differenziare ancora maggiormente la varietà dei propri costumi, Batman
possa contare su di un guardaroba contenente quattro mantelli, rispettivamente
di colore rosa, verde, rosso e marrone, e tre costumi dei quali il primo è
giallo, il secondo azzurro e il terzo nero. In quanti modi diversi si possono
abbinare insieme un costume e un mantello? La {numref}`fig_principio-fondamentale`
illustra come rispondere a questa domanda: siccome per ognuno dei quattro
mantelli è possibile scegliere tre diversi costumi, il numero totale dei
possibili abbinamenti è $4 \times 3 = 12$.

Una semplice illustrazione del principio fondamentale del calcolo combinatorio:
avendo quattro opzioni possibili per una prima scelta e tre opzioni per una
seconda scelta, si hanno dodici scelte combinate in tutto.

```{figure} ../../_static/img/superhero-grid.png
:width: 50%
:name: fig_principio-fondamentale

Illustrazione del principio fondamentale del calcolo combinatorio
(immagine creata ex novo dall'autore tramite IA (ChatGPT) e post-produzione
grafica).
```


Generalizzando questo ragionamento si arriva al cosiddetto
_principio fondamentale del calcolo combinatorio_: se ci sono $s_1$ modi per
operare una scelta e, per ciascuno di essi, ci sono $s_2$ modi per operare
una seconda scelta e, per ciascuno di essi ci sono $s_3$ modi per operare una
terza scelta e così via fino a $s_t$ modi per operare la $t$-esima scelta,
allora il numero delle sequenze di possibili scelte è pari a

$$s_1 \cdot \ldots \cdot s_t = \prod_{i=1}^t s_i.$$

Osserviamo che questo risultato corrisponde a calcolare il numero delle
foglie di un albero di profondità $t$ il cui primo livello ha $s_1$ nodi,
ciascuno dei quali ha $s_2$ figli, ciascuno dei quali ha $s_3$ figli e così
via, come evidenziato nella {numref}`fig_tree`.


```{figure} ../../_static/img/superhero-tree.png
:width: 100%
:name: fig_tree

L'albero che corrisponde alle scelte possibili nella
{numref}`fig_principio-fondamentale` ((immagine creata ex novo dall'autore
tramite IA (ChatGPT) e post-produzione grafica).
```


È importante notare come l'applicazione del principio fondamentale del
calcolo combinatorio prescinda dal tipo degli oggetti considerati, siano essi
mantelli, costumi, verdure, strumenti finanziari o altro. Se nell'esempio
precedente avessimo dovuto abbinare tre colori a quattro modelli di automobile
avremmo ottenuto lo stesso risultato numerico. In altre parole, i risultati
che si ottengono applicando le regole del calcolo combinatorio prescindono
dalla _natura_ degli oggetti, bensì dipendono solamente dalla loro numerosità
ed eventualmente dal numero di posti da tenere in considerazione. Si parla
infatti, ad esempio, delle _permutazioni_ di $n$ oggetti o delle
_combinazioni_ di $n$ oggetti in $k$ posti. Nei paragrafi che seguono, in
ogni caso, faremo spesso riferimento a oggetti specifici, per esemplificare
i concetti che verranno man mano esposti.
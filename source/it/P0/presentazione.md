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

(par:franklin-law)=
# Presentazione

> In questo mondo nulla si può dire certo,<br/>
> tranne la morte e le tasse
>
> -- Benjamin Franklin

La citazione che inizia questo paragrafo è tradotta da una lettera scritta nel
1789 da Benjamin Franklin (vedi {numref}`benjamin-franklin`), uno dei padri
fondatori degli Stati Uniti d'America. Se accettiamo questa massima, a cui
spesso si fa riferimento chiamandola la _legge di Franklin_
[^citazione-franklin], vale la pena studiare l'incertezza, perché
praticamente tutto è incerto (ironicamente, la validità della stessa legge di
Franklin non è da dare per scontata: basti pensare, per esempio, al fenomeno
dell'evasione fiscale, o al fatto che chi risiede nel Principato di Monaco non
paga le tasse).


```{figure} https://live.staticflickr.com/2869/9544834557_b844c48e78_b.jpg
:width: 70%
:name: benjamin-franklin

Raffigurazione di Benjamin Franklin sulle banconote da 100 dollari statunitensi
(immagine di E. Strauhmanis, distribuita sotto licenza
  [CC BY 2.0](https://creativecommons.org/licenses/by/2.0/))
```

In realtà il concetto di _incertezza_ è particolarmente difficile da definire,
perché è particolarmente sfaccettato e assume sfumature diverse a seconda del
contesto. In questo libro ci concentreremo su una particolare incarnazione di
questo concetto, che chiameremo _casualità_.
In termini semplici (e quindi decisamente perfettibili), possiamo identificare
la casualità come la proprietà che caratterizza una qualsiasi esperienza che,
anche se ripetuta con le medesime modalità, non ha un risultato determinabile a
priori. In modo (per ora) informale, chiamiamo _eventi_ delle affermazioni
che riguardano i risultati di queste esperienze. Il valore di verità di queste
affermazioni sarà dunque incerto.
Un classico esempio di evento è quello relativo all'esito del lancio di un dado
quando si gioca a Monopoli. Un altro esempio, altrettanto classico ma più
moderno, riguarda il valore di chiusura di un indice di borsa. Se riflettiamo
più a fondo ci vengono però in mente molti altri esempi: se scrutando il cielo
la mattina vediamo delle nuvole all'orizzonte, oggi pioverà ? Quanti nipoti
avrà la sorella del mio vicino di casa? L'anno prossimo riuscirò a passare la
brutta stagione prendendo l'influenza al massimo una volta? In effetti, non è
difficile convincerci del fatto che la casualità (o, se preferite, il
non-determinismo) permea la nostra esistenza, al punto di avere un ruolo
fondamentale nella descrizione di alcuni aspetti fondamentali della Natura,
come la teoria dell'evoluzione o la meccanica quantistica.

Nonostante ciò, le persone imparano più o meno in fretta a convivere abbastanza
bene con l'incertezza: uscendo di casa, la maggior parte delle volte sappiamo
quando conviene portare con noi un ombrello, e alcune persone riescono anche a
speculare con successo giocando in borsa. Ciò succede perché siamo in grado di
_valutare_ l'incertezza di parecchi eventi, accettando il _rischio_ che la
nostra valutazione comporta (tornando all'esempio del cielo nuvoloso, il
rischio è quello di portare con noi un ombrello inutilmente, oppure di non
portarlo e finire sotto la pioggia). Quasi sempre, facciamo tutto questo in
modo ampiamente soggettivo, sulla base della nostra _esperienza_. La matematica
ci fornisce però degli strumenti qualitativi e quantitativi per affrontare
questo problema in modo rigoroso. In particolare, combinando il
_calcolo delle probabilità_ e la _statistica_ possiamo modellare l'incertezza
degli eventi ed effettuarne una valutazione utilizzando l'esperienza che
abbiamo acquisito.

Lo scopo di questo libro è proprio quello di fornire le basi di queste due
branche della matematica, usando un approccio interattivo e incentrato
sull'analisi dei dati, adatto soprattutto a studenti che abbiano già maturato
competenze nella programmazione dei calcolatori. In particolare, il contenuto è
stato pensato per gli studenti dei corsi di laurea in area informatica, ma è
sicuramente adatto a tutti i contesti educativi che prevedono almeno un
insegnamento obbligatorio di programmazione.

Il lavoro è organizzato in quattro parti:

- nella prima viene introdotto il linguaggio di programmazione Python e le
  principali librerie attualmente utilizzate per analizzare i dati (il
  cosiddetto _Python data science stack_);
- le seconda affronta il tema della _statistica descrittiva_, che possiamo
  informalmente ricollegare al problema di organizzare le osservazioni di
  fenomeno, per poi analizzarle al fine di estrarre _informazione_ (la base
  dell'esperienza sopra menzionata);
- la terza introduce i fondamenti del _calcolo delle probabilità_, intesa
  come disciplina che permette di valutare in modo quantitativo l'incertezza
  degli eventi;
- la quarta si focalizza infine sulle basi della _statistica inferenziale_,
  al fine di fornire strumenti che permettano di prendere decisioni
  in condizioni di incertezza, utilizzando gli strumenti introdotti nei capitoli
  precedenti.

Ognuna di queste parti, considerata da sola, riempirebbe un intero libro di
testo&mdash;anche più di uno! Pertanto, sebbene il materiale sia fruibile
senza bisogno di ricorrere a fonti esterne, il libro permette molto spesso di
affrontare solo i concetti fondamentali delle discipline considerate.
Nonostante ciò, ove possibile vengono brevemente descritti alcuni strumenti
avanzati, tipici del _machine learning_, che si basano sull'applicazione di
concetti e strumenti descritti nel libro.


[^citazione-franklin]: Nella fonte originale (una lettera di B. Franklin al
fisico francese Jean-Baptiste Le Roy) questa affermazione compare in realtà
come parte finale della frase: «... in this world nothing can be said to be
certain, except death and taxes». Va comunque sottolineato che, sebbene la
paternità di questo detto sia fatta risalire a Benjamin Franklin, esistono
[fonti antecedenti](https://en.wikipedia.org/wiki/Death_and_taxes_(idiom))
che ne riportano alcune varianti.

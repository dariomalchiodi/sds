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

(chap:introduzione)=
# Introduzione

(par:franklin-law)=
> In questo mondo nulla si può dire certo,<br/>
> tranne la morte e le tasse
>
> -- Benjamin Franklin

La citazione che apre questo paragrafo è tratta da una lettera scritta nel 1789
da Benjamin Franklin (vedi {numref}`benjamin-franklin`), uno dei padri
fondatori degli Stati Uniti d'America. Se accettiamo questa massima, spesso
chiamata _legge di Franklin_ [^citazione-franklin], vale la pena studiare
l'incertezza, perché praticamente tutto è incerto. Ironicamente, la validità
della stessa legge di Franklin non è scontata: basti pensare, per esempio, al
fenomeno dell'evasione fiscale, o al fatto che chi risiede nel Principato di
Monaco non paga le tasse.


```{figure} https://live.staticflickr.com/2869/9544834557_b844c48e78_b.jpg
:width: 70%
:name: benjamin-franklin

Raffigurazione di Benjamin Franklin sulle banconote da 100 dollari statunitensi
(immagine di E. Strauhmanis, distribuita sotto licenza
<a href="https://creativecommons.org/licenses/by/2.0/"
target="_blank">CC BY 2.0</a>)
```

In realtà il concetto di _incertezza_ è difficile da definire, perché presenta
molte sfaccettature e assume significati diversi a seconda del contesto. In
questo libro mi concentrerò su una sua specifica accezione,
spesso indicata con il termine _casualità_. In termini semplici (e quindi
decisamente perfettibili), possiamo identificare la casualità come la proprietà
che caratterizza un'esperienza che, anche se ripetuta nelle stesse condizioni,
produce un risultato non prevedibile a priori. In modo (per ora) informale,
chiamiamo _eventi_ delle affermazioni che riguardano i risultati di queste
esperienze. Il loro valore di verità sarà dunque incerto. Un esempio classico
di evento riguarda il risultato del lancio di un dado durante una partita a
Monopoli. Un altro esempio, altrettanto classico ma più moderno, considera il
valore di chiusura di un indice di borsa. Ma potremmo aggiungerne molti altri:
oggi pioverà, se scrutando il cielo al mattino vediamo nuvole all'orizzonte?
Quanti nipoti avrà la sorella del mio vicino di casa? L'anno prossimo riuscirò
a superare la stagione influenzare ammalandomi al massimo una volta? In
effetti, non è difficile rendersi conto del fatto che la casualità (o, se
preferite, il non-determinismo) permea la nostra vita quotidiana. E ha anche un
ruolo essenziale nella descrizione di alcuni aspetti fondamentali della Natura,
come la teoria dell'evoluzione o la meccanica quantistica.

Nonostante ciò, impariamo presto a convivere abbastanza bene con l'incertezza:
uscendo di casa, sappiamo quasi sempre se conviene portare con noi un ombrello,
e alcune persone riescono anche a speculare con successo giocando in borsa.
Questo accade perché siamo in grado di _valutare_ l'incertezza di parecchi
eventi, accettando il _rischio_ che la nostra valutazione comporta. Tornando
all'esempio del cielo nuvoloso, il rischio è quello di portare un ombrello
inutilmente, oppure di finire sotto la la pioggia senza averlo con sé. Di
solito, le decisioni che prendiamo si basano su criteri ampiamente soggettivi,
fondati sulla nostra _esperienza_. La matematica ci fornisce però degli
strumenti per affrontare questo problema in modo rigoroso. In particolare,
combinando il _calcolo delle probabilità_ e la _statistica_ possiamo modellare
l'incertezza degli eventi ed effettuarne una valutazione utilizzando
l'esperienza che abbiamo acquisito.

Lo scopo di questo libro è proprio quello di fornire le basi di queste due
branche della matematica, adottando un approccio interattivo e incentrato
sull'analisi dei dati, pensato per studenti che abbiano già maturato competenze
nella programmazione dei calcolatori. Il contenuto è stato pensato per studenti
dei corsi di laurea in area informatica, ma è sicuramente adatto a tutti i
percorsi formativi che prevedono almeno un insegnamento obbligatorio di
programmazione.

Il lavoro è organizzato in quattro parti:

- la prima introduce il linguaggio di programmazione Python e il relativo
  _data science stack_, cioè l'insieme delle principali librerie per
  l'analisi dei dati;
- la seconda affronta il tema della _statistica descrittiva_, che ci fornisce
  strumenti per organizzare e analizzare le osservazioni di
  fenomeno, allo scopi di estrarre _informazione_ (la base
  dell'esperienza sopra menzionata);
- la terza descrive i fondamenti del _calcolo delle probabilità_, intesa come
  disciplina che permette di quantificare l'incertezza
  degli eventi;
- la quarta e ultima parte si concentra sulle basi della _statistica
  inferenziale_, fornendo strumenti che supportano le decisioni in condizioni
  di incertezza, sfruttando gli strumenti introdotti nelle parti precedenti.

Ognuna di queste parti, considerata da sola, riempirebbe un intero libro di
testo&mdash;anche più di uno! Per questo motivo, mi limiterà ad affrontare i
concetti fondamentali delle discipline considerate, limitando gli
approfondimenti e garantendo comunque che il libro resti fruibile senza
ricorrere a fonti esterne. Ove possibile, presenterò anche alcuni aspetti
avanzati, tipici del _machine learning_, basati sui concetti e sugli strumenti
descritti nei capitoli precedenti.


[^citazione-franklin]: Nella fonte originale (una lettera di B. Franklin al
fisico francese Jean-Baptiste Le Roy) questa affermazione compare in realtà
come parte finale della frase: «... in this world nothing can be said to be
certain, except death and taxes». Va comunque sottolineato che, sebbene la
paternità di questo aforisma sia attribuita a Benjamin Franklin, esistono
{extlink}`fonti
antecedenti<https://en.wikipedia.org/wiki/Death_and_taxes_(idiom)>` che ne
riportano alcune varianti.

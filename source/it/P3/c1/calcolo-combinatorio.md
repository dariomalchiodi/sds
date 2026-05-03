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

(chap_calcolo-combinatorio)=
# Calcolo combinatorio

Il _calcolo combinatorio_ è la branca della matematica che si occupa di
determinare il numero di modi in cui è possibile raggruppare o ordinare gli
elementi di un insieme finito. Come si può intuire, questo numero non dipende 
dalla natura degli oggetti considerati: che si tratti di elementi tangibili 
(come frutti o biciclette) o di entità astratte (come poteri di un supereroe o
colori per le pareti di un ufficio), la logica necessaria per contarne le
configurazioni rimane invariata.

Per affrontare correttamente un problema di conteggio, è importante rispondere
a tre domande fondamentali:

- È possibile scegliere uno stesso elemento più di una volta?
- Gli elementi di partenza sono tutti distinti o alcuni sono _indistinguibili_
  tra loro?
- L'ordine in cui gli elementi vengono selezionati è rilevante, oppure no?

Una volta chiariti questi aspetti, il numero di configurazioni possibili 
dipende in genere da due soli parametri: la numerosità $n$ dell'insieme di 
partenza e il numero $k$ di elementi che intendiamo selezionare.

Una metafora particolarmente efficace è la seguente: immaginiamo di 
dover assegnare $n$ _oggetti_ (tangibili oppure no) a $k$ _posti_ disponibili.
Nei paragrafi che seguono, analizzerò le principali modalità di raggruppamento
e di ordinamento e, per ciascuna di esse, mostrerò come ricavare la formula
per calcolare il numero di casi possibili.

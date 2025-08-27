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

(cap:calcolo-combinatorio)=
# Calcolo combinatorio

Il _calcolo combinatorio_ è la parte della matematica che studia come
contare i modi in cui possiamo raggruppare elementi presi da un
insieme finito. Un fatto interessante che riguarda le formule che useremo è
che queste non dipendono dalla natura concreta degli elementi che
consideriamo. Che si tratti di cose tangibili (come abiti, frutti o
biciclette) o di concetti astratti (come supereroi, abilità di un personaggio
in un video gioco o software da installare su un computer), il ragionamento
da fare sarà lo stesso. È invece importante è rispondere alle seguenti
domande.

- Si può scegliere uno stesso elemento più di una volta?
- Gli elementi nell'insieme sono tutti diversi tra loro o ce ne sono alcuni
  _indistinguibili_?
- Il raggruppamento dipende oppure no dall'ordine degli elementi scelti?

Una volta risposto a queste domande, il numero di possibili raggruppamenti
dipende solamente da pochi parametri. Nei casi che vedremo ne bastano quasi
sempre due: la quantità $n$ di elementi a disposizione e la lunghezza $k$ del
raggruppamento (il numero di elementi che contiene). Normalmente si utilizza
la seguente metafora: $n$ _oggetti_ (indipendentemente dalla loro effettiva
tangibilità) vanno assegnati a $k$ _posti_. Nei paragrafi seguenti vedremo
quali sono le principali modalità di raggruppamento e per ognuna di esse
deriveremo le formule per contare il numero di raggruppamenti possibili.

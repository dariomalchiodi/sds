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

(chap:presentazione)=
# Presentazione

La prima parte del libro introduce alcuni strumenti di base per l’analisi
automatica di dataset di dimensioni contenute[^big-data], mediante l’uso di un
computer. La padronanza di questi strumenti, unita alla capacità di applicarli
in modo efficace ai diversi scenari della _data science_, è oggi fondamentale
per analizzare e interpretare l’ampia varietà di dati disponibili e sfruttarli
come supporto alle decisioni.

Tra gli strumenti indispensabili troviamo:

- un linguaggio di programmazione, che permetta di scrivere istruzioni
  per automatizzare l’elaborazione dei dati;
- una libreria per la gestione strutturata dei _dataset_.

In questo libro utilizzerò rispettivamente Python e Pandas, presentati
rispettivamente nel {ref}`chap:intro-python` e nel {ref}`chap:pandas`. Sebbene
esistano molte alternative valide, queste due tecnologie rappresentano oggi
una parte centrale dell'ecosistema per l'analisi dei dati, sia in ambito
accademico che nel mondo del lavoro.



[^big-data]: Un _dataset_ si considera di dimensioni ridotte quando può essere
elaborato con le risorse disponibili su un singolo elaboratore. Nel caso più
semplice &mdash;quello trattato in questo libro&mdash; l'intero insieme di dati
può essere caricato nella memoria centrale di un computer. In generale, si
parla ancora di dati «gestibili localmente» se il _dataset_ può risiedere nella
memoria di massa e venire elaborato progressivamente in quella centrale, per
esempio trasferendo un _record_ alla volta. Quando invece le dimensioni dei
dati superano di molto la capacità della memoria di massa disponibile (in
linea di massima, oltre un terabyte con l'hardware attualmente disponibil), si
entra nel campoi dei _big data_, che richiedono approcci differenti rispetto a
quelli dell'analisi dei dati in senso classico.
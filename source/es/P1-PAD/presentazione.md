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

# Presentazione

La prima parte del libro introduce alcuni strumenti computazionali fondamentali
per l’analisi automatica di dataset di dimensioni contenute[^big-data],
mediante l’uso di un computer. La padronanza di tali strumenti, unita alla
capacità di applicarli in modo efficace ai diversi scenari della _data science_,
costituisce oggi una competenza essenziale per analizzare e interpretare
l’ampia varietà di fonti di dati disponibili, utilizzandoli come supporto alle
decisioni.

Tra gli strumenti necessari figurano:

- un linguaggio di programmazione, che consenta di scrivere istruzioni
  per automatizzare l’elaborazione dei dati;
- una libreria per la gestione strutturata dei _dataset_.

In questo libro utilizzerò rispettivamente Python e Pandas, presentati
rispettivamente nei Capitoli
{ref}`Elaborare i dati con Python <chap:intro-python>` e
{ref}`Pandas <chap:pandas>`. Queste non sono tuttavia le uniche soluzioni
disponibili: esistono diverse alternative valide, ma Python e Pandas
rappresentano attualmente una parte consistente dell’ecosistema di strumenti
per l’analisi dei dati, sia in ambito accademico che professionale.



[^big-data]: Un dataset si considera di dimensioni ridotte quando può essere
elaborato con le risorse disponibili su un singolo elaboratore. In particolare,
nel caso più semplice &emdash; che è quello trattato in questo libro &emdash;
l'intero insieme di dati può essere caricato nella memoria centrale di un
computer. Più in generale, si parla ancora di dati «gestibili localmente»
se il _dataset_ può risiedere nella memoria di massa e venire elaborato
progressivamente in memoria centrale, per esempio trasferendo un _record_ alla
volta. Quando, invece, le dimensioni del _dataset_ superano significativamente
la capacità della memoria di massa disponibile (ad esempio, oltre un terabyte
con l'hardware attualmente disponibil), si entra nell’ambito dei _big data_,
che richiedono approcci computazionali differenti rispetto a quelli
dell’analisi classica dei dati.
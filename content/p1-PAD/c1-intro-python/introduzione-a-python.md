---
jupytext:
  formats: ipynb,md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.10.3
kernelspec:
  display_name: Python 3
  language: python
  name: python3
numbering:
  heading_1: true
  heading_2: true
  enumerator: 2.%s

title: 2. Elaborare i dati con python
---

(chap-python)=

> The Zen of Python, by Tim Peters<br/>
> 
> Beautiful is better than ugly.<br/>
> Explicit is better than implicit.<br/>
> Simple is better than complex.<br/>
> Complex is better than complicated.<br/>
> Flat is better than nested.<br/>
> Sparse is better than dense.<br/>
> Readability counts.<br/>
> Special cases aren't special enough to break the rules.<br/>
> Although practicality beats purity.<br/>
> Errors should never pass silently.<br/>
> Unless explicitly silenced.<br/>
> In the face of ambiguity, refuse the temptation to guess.<br/>
> There should be one-- and preferably only one --obvious way to do it.<br/>
> Although that way may not be obvious at first unless you're Dutch.<br/>
> Now is better than never.<br/>
> Although never is often better than *right* now.<br/>
> If the implementation is hard to explain, it's a bad idea.<br/>
> If the implementation is easy to explain, it may be a good idea.<br/>
> Namespaces are one honking great idea -- let's do more of those!<br/>


Questo capitolo descrive brevemente i principali strumenti che permettono di
analizzare dati in modo esplorativo usando [Python](https://www.python.org)
come linguaggio di programmazione, i
[notebook](https://en.wikipedia.org/wiki/Notebook_interface) per scrivere ed
eseguire il codice e le principali librerie del cosiddetto
_Python data science stack_, che saranno introdotte via via che queste si
riveleranno necessarie.
```{margin}
I notebook possono essere eseguiti in vari ambienti di elaborazione: al momento
in cui questo libro è stato scritto tra quelli più diffusi ci sono
[Jupyter](https://jupyter.org/) e
[Visual Studio Code](https://code.visualstudio.com/)
```

Tutti gli strumenti a cui faremo riferimento ricadono nella categoria del
[FLOSS](https://it.wikipedia.org/wiki/Free_and_Open_Source_Software), e sono
pertanto distribuiti con licenze che ne permettono, tra le altre cose, il
libero utilizzo.
```{margin}
L'acronimo FLOSS sta per «Free/Libre Open Source Software»
```

La trattazione è pensata per studenti che hanno già familiarità con la
programmazione degli elaboratori e, in particolare, già conoscono almeno
un linguaggio di programmazione che adotta l'approccio imperativo e
procedurale, e che conoscano le basi del paradigma di programmazione orientato
agli oggetti.

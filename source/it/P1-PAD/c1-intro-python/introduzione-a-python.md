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

(chap:intro-python)=
# Elaborare i dati con python

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
>
> --- The Zen of Python, by Tim Peters[^zen]


Questo capitolo descrive brevemente i principali strumenti che permettono di
analizzare dati in modo esplorativo usando [Python](https://www.python.org)
come linguaggio di programmazione, i
[notebook](https://en.wikipedia.org/wiki/Notebook_interface) per scrivere ed
eseguire il codice e le principali librerie del cosiddetto
_Python data science stack_, che saranno introdotte via via che queste si
riveleranno necessarie.
```{margin}
I _notebook_ possono essere eseguiti in vari ambienti di sviluppo: al
momento in cui questo libro è stato scritto tra quelli più diffusi ci sono
[Jupyter](https://jupyter.org/) e
[Visual Studio Code](https://code.visualstudio.com/), che hanno anche il
vantaggio di essere gratuiti, sebbene esistano altre alternative.
```

Tutti gli strumenti a cui farò riferimento ricadono nella categoria del
[FLOSS](https://it.wikipedia.org/wiki/Free_and_Open_Source_Software), e sono
pertanto distribuiti con licenze che ne permettono, tra le altre cose, il
libero utilizzo.
```{margin}
L'acronimo FLOSS sta per «Free/Libre Open Source Software»
```

La trattazione è pensata per studenti che hanno già familiarità con la
programmazione degli elaboratori e, in particolare, sono fluenti con almeno
un linguaggio di programmazione che adotta l'approccio imperativo e
procedurale. Introdurrò invece alcune conoscenze di base del paradigma di
programmazione orientato agli oggetti, necessarie per utilizzare il
_data science stack_ di Python e che non sempre sono alla portata di chi si
appresta a studiare la materia.


[^zen]: Lo «Zen di Python» è il nome che viene ufficialmente dato a $19$
linee guida per la scrittura di codice Python in modo da sfruttarne l'eleganza
e le strutture sintattiche, piuttosto che tradurre in modo pedissequo la
sintassi di altri linguaggi: quello che in gergo si chiama
«scrivere codice pythonico». Queste linee guida, di pubblico dominio, sono
state scritte nel 1999 da Tim Peters, uno dei principali contributori di
Python. Oltre a essere pubblicate in
un'[apposita sezione](https://peps.python.org/pep-0020/) dei
_Python Enhancement Proposals_, vengono automaticamente visualizzate eseguendo
la linea di codice Python `import this`.
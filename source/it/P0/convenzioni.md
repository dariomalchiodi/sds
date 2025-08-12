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

(sec:convenzioni)=
# Convenzioni

Per quanto detto nel paragrafo precedente, spesso inframmezzerò il testo con
del codice, non tanto al fine di eseguirlo, ma più per uno scopo illustrativo
(per esempio, per indicare i letterali `true` e `false` come unici valori
possibili per il tipo di dati `bool`). In questo caso, utilizzerò un carattere
tipografico non proporzionale con un colore diverso da quello del
testo principale. Quando invece sarà necessario mostrare una o più righe di
codice pensate per essere eseguite da chi legge, mostrerò queste righe 
all'interno di un riquadro che ricorda la tipica _cella di codice_ in un
_notebook_. Anche in questo caso utilizzerò un carattere tipografico non
proporzionale, ma la colorazione del testo sarà fatta in modo da evidenziare
dei particolari elementi nel codice (come variabili, letterali, parole chiave
e così via, analogamente a quanto normalmente fatto dai moderni IDE). Inoltre,
il codice risulterà staccato rispetto al testo principale, come nell'esempio
che segue.
```{margin}
È pratica comune utilizzare un carattere tipografico non proporzionale (nel
quale cioè tutti i glifi utilizzati per rappresentare una lettera hanno la
stessa larghezza) per visualizzare codice, input e output, per una serie di
motivi che ottimizzano la leggibilità del codice stesso, come la maggiore
facilità di indentare le istruzioni, il minor rischio di non distinguere tra
caratteri simili come 1 e l.
```

```python
age = 24
print(age <= 42)
```

Di norma, visualizzerò l'eventuale output dell'esecuzione all'interno di
un'apposita _cella di output_, accodata a quella di codice e mostrata come
di seguito.

```python
print(age <= 42)
```

Infine, utilizzerò uno stile specifico per evidenziare nel testo alcune
componenti particolari, come esemplificato qui sotto.

```{admonition} _
:class: naming
Questo tipo di area contiene delle note relative alla nomenclatura utilizzata
in un particolare ambito, o alla descrizione di diciture alternative rispetto
a quelle introdotte.
```

```{prf:definition}
:label: segnaposto-definizione
:class: no-number
In questa area vengono definiti in modo formale uno o più concetti.
```
```{margin}
Definizioni, esempi e così via saranno normalmente numerati, e spesso
accompagnati da un nome specifico racchiuso tra parentesi.
```

```{prf:example}
:label: segnaposto-esempio
:class: no-number
Questa area racchiude un esempio.
```

````{prf:theorem}
:label: segnaposto-teorema
:class: no-number
Questa area contiene la tesi di un teorema.
````

```{prf:corollary}
:label: segnaposto-corollario
:class: no-number
Questa area contiene la definizione di un corollario.
```

```{prf:lemma}
:class: no-number
:label: segnaposto-lemma
Questa area contiene la definizione di un lemma.
```

```{admonition} _
:class: myproof
In questa area viene inserita la dimostrazione di un teorema, di un corollario
o di un lemma. Per alcuni dei teoremi ometterò la relativa dimostrazione. Ciò
capiterà quando sarà importante introdurre un risultato teorico rilevante,
sebbene la sua dimostrazione richieda conoscenze matematiche avanzate.
```

```{note}
Questo tipo di area racchiude alcuni aspetti secondari che preferisco mettere
in evidenza nel testo, piuttosto che descriverli nelle note a pie' di pagina.
```



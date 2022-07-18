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
---

# Convenzioni e notazione

Spesso risulta necessario inframmezzare il testo principale con del codice,
non al fine di eseguirlo ma per scopo illustrativo (per esempio per indicare
i letterali `true` e `false` per il tipo di dati `bool`). In questo caso il
codice viene indicato utilizzando un carattere tipografico non proporzionale
(Fira Code) che sfrutta le cosiddette _legature_ per abbellire il modo in cui
vengono visualizzati alcuni elementi del linguaggio di programmazione.

```{margin}
Il software normalmente impiegato per scrivere codice (editor, IDE, e così
via) utilizza normalmente un tipo di carattere predefinito che non è in grado
di gestire le legature, dunque le sequenze di questo tipo rimarranno invariate
quando vengono inserite. È però abbastanza facile cambiare il tipo di
carattere.
```
Per esempio, l'operatore logico di «maggiore o uguale» è descritto dalla
sequenza dei due simboli
<code style="font-family: monospace !important;">>=</code>,
che una volta digitata viene automaticamente convertita nel simbolo `>=`, più
simile a quello utilizzato in ambito matematico.


Quando invece è necessario mostrare una o più righe di codice intese per
essere eseguite, queste verranno organizzate in una _cella di codice_
all'interno di un notebook, visualizzata nel modo che segue.

```{code-cell} ipython3
:tags: [remove-input]
age = 24
```

```{code-cell} ipython3
:tags: [remove-output]
print(age <= 42)
```

Di norma, l'esito dell'esecuzione di codice sarà visualizzato all'interno di
un'apposita _cella di output_, accodata a quella di codice e mostrata come
di seguito.

```{code-cell} ipython3
:tags: [remove-input]
print(age <= 42)
```

Va notato come le celle di output siano leggermente diverse da quelle di
codice, in quanto queste ultime hanno il bordo sinistro evidenziato con un
colore diverso. Questa convenzione è leggermente diversa da quella utilizzata
normalmente nei notebook, in cui il colore delle celle di input cambia quando
queste vengono selezionate per eseguirle o per modificarne i contenuti.

```{admonition} Nomenclatura
:class: naming
Questo tipo di area contiene delle note relative alla nomenclatura utilizzata
in un particolare ambito, o alla descrizione di diciture alternative rispetto
a quelle introdotte.
```

```{prf:definition} Definizione
:label: segnaposto-definizione
In questa area vengono definiti in modo formale uno o più concetti.
```

```{prf:example} Esempio
:label: segnaposto-esempio
Questa area racchiude un esempio.
```

```{prf:theorem}
:label: segnaposto-teorema
Questa area contiene la tesi di un teorema.
```

```{prf:proof}
In questa area viene inserita la dimostrazione di un teorema.
```

```{prf:corollary} Corollario
:label: segnaposto-corollario
Questa area contiene la definizione di un corollario e la sua dimostrazione.
```
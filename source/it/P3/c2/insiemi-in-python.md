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

(sec_insiemi-in-python)=
# Gli insiemi in Python

Python mette a disposizione il tipo `set` per rappresentare insiemi finiti.
Questi possono essere descritti

```{margin}
In Python si usano quindi le parentesi graffe per delimitare sia i letterali di
tipo insieme che quelli di tipo dizionario. Ciò non comporta ambiguità nel
linguaggio perché in un letterale di tipo insieme queste parentesi contengono
una sequenza di valori, mentre nei letterali di tipo dizionario ciò che è
contenuto è una sequenza di coppie `<chiave>: <valore>`. L'unica eccezione si
ha per l'espressione `{}` che potrebbe indicare sia un dizionario vuoto, sia un
insieme vuoto. L'ambiguità è risolta nel modo seguente: `{}` indica il
dizionario vuoto, mentre per riferirsi a un insieme vuoto è necessario
invocare il costruttore `set` senza specificare argomenti.
```
- tramite dei letterali di tipo insieme, delimitando tramite parentesi graffe
  una sequenza degli elementi dell'insieme da descrivere separati tramite
  virgole, oppure
- invocando il costruttore della classe `set` specificando come argomento un
  iterabile contenente gli elementi dell'insieme.

Pertanto le espressioni `{1, 3, 5}`, `set([1, 3, 5])` e `set((1, 3, 5))`
corrispondono allo stesso oggetto di tipo insieme. Chiaramente tutte le tre
espressioni precedenti individuano lo stesso insieme:

```{code-cell} python
{1, 3, 5} == set([3, 1, 5])
```

L'espressione nella cella precedente e il relativo valore permettono di
sottolineare due cose: la prima è che, coerentemente con la definizione di
insieme, l'ordine con cui si specificano gli elementi è indifferente, e la
seconda è che l'operatore di uguaglianza si può utilizzare mantenendone
invariata la semantica quando i suoi argomenti sono oggetti di tipo insieme.
La {numref}`table-set-operators` elenca la sintassi dei principali operatori
che Python mette a disposizione per gli insiemi, e come si può vedere alcuni
degli operatori introdotti per i tipi di dati semplici si estendon
naturalmente agli insiemi, mantenendo dunque la loro semantica e la sintassi
infissa [^alternate-set-operations]: è questo il caso delle relazioni di
uguaglianza, differenza e appartenenza, così come dell'operazione di
differenza. In altri casi viene modificata la semantica: per esempio `<=`
rappresenta la relazione di sottoinsieme. Vi sono poi degli operatori specifici
legati a intersezione, unione e differenza simmetrica [^bitwise].


```{table} Sintassi delle principali relazioni tra insiemi utilizzabili in Python, indicando con $S$ e $T$ due insiemi e con <code>s</code> e <code>t</code> i corrispondenti oggetti.
:name: table-set-operators
:align: center

| Relazione/operazione | Sintassi |
|----------------------|----------|
| $S = T$              | `s == t` |
| $S \neq T$           | `s != t` |
| $S \subseteq T$      | `s <= t` |
| $S \subset T$        | `s < t`  |
| $S \supseteq T$      | `s >= t` |
| $S \supset T$        | `s > t`  |
| $S \cup T$           | `s \| t` |
| $S \cap T$           | `s & t`  |
| $S \backslash T$     | `s - t`  |
| $S \ominus T$        | `s ^ t`  |
| $e \in S$            | `e in s` |

```

Oltre agli operatori, anche la funzione `len` mantiene inalterato il suo
signifcato, restituendo la cardinalità dell'insieme, intesa come il numero di
elementi in esso contenuti. Ovviamente l'accesso posizionale perde di
significato per questo tipo di dato: le operazioni fondamentali per accedere a
un insieme sono infatti:
- la verifica dell'appartenenza o meno di un elemento a un insieme, utilizzando
  l'operatore `in`,
- l'inserimento di un elemento in un insieme, invocando il metodo `add`
  [^add-existing],
- l'eliminazione di un elemento in un insieme, invocando il metodo `discard`
  [^remove-existing].

Come gli altri tipi visti nel Paragrafo @dati-semplici, anche per
gli insiemi il linguaggio prevede un supporto molto più completo di quanto
descritto in questo paragrafo. La
[documentazione ufficiale](https://docs.python.org/3/library/stdtypes.html#set)
descrive in modo estensivo operatori, funzioni e metodi a disposizione.

[^alternate-set-operations]: Gli operatori fanno in realtà a loro volta
riferimento all'invocazione di particolari metodi della classe `set`: per
esempio l'espressione `s <= t` viene automaticamente tradotta in
`s.issubset(t)`.

[^bitwise]: Gli operatori `&`, `|` e `^` sono utilizzabili anche con altri tipi
di dati (in particolar modo con i valori interi) e fanno riferimento alle
operazioni booleane eseguite bit per bit.

[^add-existing]: Questa operazione non modifica l'insieme nel caso in cui
quest'ultimo includa già l'elemento che si sta tentando di aggiungere.

[^remove-existing]: Anche in questo caso il metodo non ha effetto se l'insieme
non contiene l'elemento da rimuovere; è anche possibile utilizzare il metodo
alternativo `remove` che elimina un elemento da un insieme se quest'ultimo lo
contiene, ed emette un'eccezione nei casi rimanenti.

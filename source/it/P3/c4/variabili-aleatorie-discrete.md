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

(sec_va-discrete)=
# Variabili aleatorie discrete

````{prf:example}
:label: ex-dist-due-dadi
Consideriamo il lancio di due dadi bilanciati e calcoliamo la probabilità che
la somma dei risultati superi una certa soglia.

Lo spazio degli esiti è costituito da tutte le coppie $(d_1, d_2)$ dove
$d_1$ e $d_2$ rappresentano i risultati dei due dadi. Poiché ognuno può
assumere 6 valori distinti, il numero totale di esiti possibili è
$6 \times 6 = 36$. L'ipotesi di bilanciamento dei dadi ci permette di
lavorare in uno spazio equiprobabile, e quindi di applicare la definizione
classica di probabilità.

Visualizziamo lo spazio degli esiti nel grafico seguente, dove ogni pallino
rappresenta una possibile combinazione di risultati.

```{code-cell} python
import matplotlib.pyplot as plt

# Coordinate per tutti i 36 esiti
x = []
y = []
for d1 in range(1, 7):
    for d2 in range(1, 7):
        x.append(d1)
        y.append(d2)

fig, ax = plt.subplots(figsize=(6, 6))
ax.scatter(x, y, s=100, c='steelblue', edgecolors='black', linewidths=0.5)
ax.set_xlabel('Risultato del primo dado')
ax.set_ylabel('Risultato del secondo dado')
ax.set_title('Spazio degli esiti: 36 combinazioni')
ax.set_xticks(range(1, 7))
ax.set_yticks(range(1, 7))
ax.set_xlim(0.5, 6.5)
ax.set_ylim(0.5, 6.5)
ax.grid(True, alpha=0.3)
ax.set_aspect('equal')
plt.show()
```

```{margin}
La somma minima è 2 (quando entrambi i dadi mostrano 1) e quella massima è 12
(quando entrambi mostrano 6).
```

La somma $S = d_1 + d_2$ può assumere valori da 2 a 12. Calcoliamo la
probabilità associata a ogni possibile valore della somma.

```{code-cell} python
from collections import Counter

# Calcolo di tutte le somme possibili
somme = [d1 + d2 for d1 in range(1, 7) for d2 in range(1, 7)]
conteggio = Counter(somme)

# Visualizzazione della distribuzione
fig, ax = plt.subplots(figsize=(8, 5))
valori = sorted(conteggio.keys())
frequenze = [conteggio[v] for v in valori]
probabilita = [f / 36 for f in frequenze]

ax.bar(valori, probabilita, color='steelblue', edgecolor='black')
ax.set_xlabel('Somma dei dadi')
ax.set_ylabel('Probabilità')
ax.set_title('Distribuzione di probabilità della somma')
ax.set_xticks(valori)
plt.show()
```

Applicando la definizione classica di probabilità, la probabilità che la somma
sia almeno 9, ovvero che $S \geq 9$, si calcola contando gli esiti favorevoli:

```{code-cell} python
esiti_favorevoli = sum(1 for d1 in range(1, 7) for d2 in range(1, 7) 
                       if d1 + d2 >= 9)
prob = esiti_favorevoli / 36
print(f'Esiti favorevoli: {esiti_favorevoli}')
print(f'Probabilità che S ≥ 9: {esiti_favorevoli}/36 = {prob:.4f}')
```

Possiamo visualizzare questi esiti favorevoli evidenziandoli nel grafico dello
spazio degli esiti.

```{code-cell} python
fig, ax = plt.subplots(figsize=(6, 6))

for d1 in range(1, 7):
    for d2 in range(1, 7):
        if d1 + d2 >= 9:
            ax.scatter(d1, d2, s=100, c='crimson', edgecolors='black', 
                       linewidths=0.5, zorder=3)
        else:
            ax.scatter(d1, d2, s=100, c='lightgray', edgecolors='black', 
                       linewidths=0.5, zorder=2)

ax.set_xlabel('Risultato del primo dado')
ax.set_ylabel('Risultato del secondo dado')
ax.set_title('Esiti favorevoli (rosso): somma ≥ 9')
ax.set_xticks(range(1, 7))
ax.set_yticks(range(1, 7))
ax.set_xlim(0.5, 6.5)
ax.set_ylim(0.5, 6.5)
ax.grid(True, alpha=0.3)
ax.set_aspect('equal')
plt.show()
```
````
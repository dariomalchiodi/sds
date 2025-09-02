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

(sec:insiemi-finiti-e-infiniti)=
# Insiemi finiti e infiniti
È abbastanza facile farsi venire in mente degli insiemi che contengono un
numero finito di elementi, come ad esempio l'insieme dei membri della Justice
League, quello dei giorni della settimana e quello dei numeri primi minori di
$100$. Diciamo che insiemi di questo tipo sono _finiti_. Esistono però anche
insiemi che non contengono un numero finito di elementi, come l'insieme di
tutte le frazioni, o anche l'insieme di tutti gli insiemi. Per questi insiemi
_infiniti_ si distinguono due casi:

- si dice che un insieme è _infinito numerabile_ quando risulta possibile
  costruire una sequenza (infinita) $x_1, x_2, \dots$ che contiene in qualche
  posizione ognuno dei suoi elementi: l'insieme $D$ dei numeri dispari sopra
  introdotto è pertanto un insieme infinito numerabile;
- in tutti gli altri casi si dice che l'insieme è _infinito non numerabile:_
  l'insieme dei punti di una retta e l'insieme dei numeri reali sono entrambi
  infiniti e non numerabili.

La modalità di descrizione estensiva non è, strettamente parlando, adottabile
per gli insiemi infiniti, visto che per definizione non è possibile elencare
tutti i loro elementi. Qaundo però si ha a che fare con un insieme infinito
numerabile e quest'ultimo è associabile a una sequenza che si può
intuitivamente continuare dopo avere visto solo alcuni tra i suoi elementi
iniziali, risulta accettabile estendere la descrizione estensiva elencando solo
questi elementi, aggiungendo dei punti di sospensione per enfatizzare la non
finitezza dell'insieme. Ad esempio l'insieme dei numeri dispari si può indicare
estensivamente come $D = \{1, 3, 5, 7, 9, ... \}$, sebbene la descrizione
intensiva

```{math}
D = \{ x \in \mathbb N \text{ tale che }
         x = 2n+1 \text{ per qualche } n \in \mathbb N \}
```

sia decisamente più precisa. Ciò non vale invece per gli insiemi infiniti non
numerabili, per i quali sono generalmente utilizzabili sono descrizioni di tipo
intensivo.

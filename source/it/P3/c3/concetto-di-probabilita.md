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

(sec:concetto-probabilita)=
# Il concetto di probabilità

Spostare qui la definizione di esperimento aleatorio e di evento

- accezione classica: la probabilità di un evento è uguale al rapporto tra
  il numero di casi favorevoli e il numero di casi possibili (funziona solo
  per gli spazi equiprobabili)
- accezione soggettiva: la probabilità di un evento riflette la _fiducia_
  che un particolare soggetto ha relativamente al verificarsi dell'evento
  stesso (tipicamente, è il prezzo che questo soggetto ritiene giusto dover
  pagare per partecipare a una scommessa in cui a fronte di un'esecuzione
  dell'evento aleatorio si vince 1 € se l'evento si
  verifica e si perde tutto altrienti, senza sapere se in questa scommessa
  si svolgerà il ruolo dello scommettitore o del banco, per evitare che il
  soggetto bari)
```{margin}
In modo meno formale, si può semplicemente indicare la probabilità come il
rapporto tra il numero di ripetizioni in cui l'evento si verifica ed $n$,
per un valore «molto grande» di $n$.
```  
- accezione frequentista: considerate $n$ ripetizioni dell'evento aleatorio,
  la probabilità di un evento è uguale al limite del rapporto tra il numero
  di volte che l'evento si è verificato ed $n$, per $n \rightarrow +\infty$
  

Formalizzazione assiomatica che è indipendente dal _significato_ che viene
dato al concetto di probabilità
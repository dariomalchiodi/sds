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

(chap:teoria-insiemi)=
# Teoria degli insiemi

Nel 1895 Georg Cantor ha proposto una definizione che coglie particolarmente
bene il concetto intuitivo di insieme {cite}`cantor-1883`: "per molteplicità o
insieme intendo ogni molti che si può pensare come uno" [^citazione-cantor].
Secondo questa definizione, un insieme è essenzialmente un raggruppamento di
oggetti che, sebbene tra loro distinti, sono accomunati da una qualche
proprietà. Nel 1895 lo stesso Cantor riformulò la sua definizione come segue:
"per 'insieme' intendiamo qualsiasi combinazione $M$ di certi oggetti $m$ ben
differenziati nella nostra visione o del nostro pensiero (che sono detti
'elementi' di $M$)" {cite}`cantor-1895`. Pochi anni dopo i matematici hanno
scoperto che fornire una definizione formalmente corretta di insieme richede
molta più attenzione, tipicamente appoggiandosi a un approccio assiomatico
{cite}`suppes`. Nonostante ciò, nel seguito faremo riferimento alle definizioni
sopra indicate, e in particolare alla seconda, al fine di rendere la
trattazione più semplice e più focalizzata rispetto allo scopo di questo libro.
D'altronde, come ricorda Rudy Rucker, è significativo che la parola _set_ abbia
la definizione più lunga tra tutte le parole che compaiono nello Oxford English
Dictionary {cite}`rucker`.

[^citazione-cantor]: Traduzione dal testo originale "Unter einer
'Mannigfaltigkeit' oder 'Menge' verstee ich nämlich allgemein jedes Viele,
welches sich als Eines denken lässt".

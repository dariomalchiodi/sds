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

(chap_teoria-insiemi)=
# Teoria degli insiemi

Nel 1895, Georg Cantor propose una definizione capace di catturare con estrema
efficacia l'idea intuitiva di insieme: «per molteplicità o insieme intendo ogni
_molti_ che si può pensare come _uno_» [^citazione-cantor]. In quest'ottica, un 
insieme è un raggruppamento di oggetti distinti accomunati da una qualche 
proprietà. Poco dopo, lo stesso Cantor affinò la sua definizione: «per 
"insieme" intendiamo qualsiasi collezione $M$ di oggetti $m$ della nostra 
intuizione o del nostro pensiero &mdash; detti "elementi" di $M$ &mdash; che
siano tra loro  ben distinti» {cite}`cantor-1895`.

Pochi anni dopo, la comunità matematica scoprì che questo approccio, oggi noto
come _teoria ingenua degli insiemi_, nascondeva insidie logiche e paradossi;
per evitarli, si rese necessario rifondare la materia su un sistema
assiomatico molto più rigoroso {cite}`suppes`. Nonostante ciò, in questo libro 
ho scelto di adottare la prospettiva ingenua: sebbene meno formale, essa mi 
permette di mantenere la trattazione semplice e focalizzata sugli obiettivi 
didattici di questo libro, senza appesantire troppo il discorso. D'altronde,
come osserva Rudy Rucker, è significativo che la parola  _set_ (insieme) vanti
la definizione più lunga tra tutti i termini dell'_Oxford English  Dictionary_
{cite}`rucker`.

[^citazione-cantor]: Traduzione dall'originale: "Unter einer 
'Mannigfaltigkeit' oder 'Menge' verstehe ich nämlich allgemein jedes Viele, 
welches sich als Eines denken lässt" {cite}`cantor-1883`. L'enfasi in corsivo 
nella traduzione italiana è stata aggiunta da me per sottolineare il 
contrasto concettuale tra pluralità e unità.
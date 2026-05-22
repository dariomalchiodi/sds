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

(chap_calcolo-probabilita)=
# Calcolo delle probabilità

Come ho ricordato all'inizio del libro, citando la [legge di
Franklin](par_franklin-law), quasi nulla è certo. Proprio per questo, quando
ci troviamo di fronte a fenomeni il cui esito non è noto in anticipo, diventa
importante capire come valutare l'incertezza in modo razionale. Se si lancia un
dado, si estrae una figurina da un mazzo ben mescolato, si osserva un
supereroe scelto a caso da un dataset o si interpreta l'esito di un test
diagnostico, non sappiamo quale risultato si presenterà, ma questo non
significa che ogni conclusione sia arbitraria. Il calcolo delle probabilità
nasce proprio per dare una forma matematica a questa valutazione
dell'incertezza, distinguendo ciò che è impossibile, ciò che è certo e ciò che
è soltanto più o meno plausibile.

Nel corso di questo capitolo introdurrò anzitutto il concetto di probabilità e
gli oggetti fondamentali con cui esso viene formalizzato: esperimenti casuali,
esiti ed eventi. Su questa base presenterò poi gli assiomi di
Kolmogorov, che permettono di trattare la probabilità come una funzione
matematica coerente, e mostrerò come tali principi si traducano in regole di
calcolo concrete quando lo spazio degli esiti è finito, sia nel caso
equiprobabile sia quando gli esiti hanno pesi diversi.

Una volta costruito questo linguaggio, passerò a due idee centrali per tutta la
disciplina: l'aggiornamento dell'informazione e l'assenza di influenza tra
eventi. La probabilità condizionata permetterà di capire come cambia una
valutazione quando si sa che un certo evento si è verificato, conducendo alla
regola di fattorizzazione, al teorema delle probabilità totali e al teorema di
Bayes; l'indipendenza servirà invece a formalizzare i casi in cui questa
informazione aggiuntiva non modifica la probabilità risultante. Come negli
altri capitoli, userò esempi concreti per mostrare che, dietro fenomeni solo in
apparenza caotici, si nasconde una struttura logica precisa, utile tanto per
interpretare i dati quanto per costruire strumenti predittivi.

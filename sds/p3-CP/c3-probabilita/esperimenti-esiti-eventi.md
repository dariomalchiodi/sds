# Esperimenti, esiti ed eventi

## Algebra degli eventi

````{prf:definition}
:label: algebra-degli-eventi
Fissato uno spazio degli esiti $\Omega$, si definisce _algebra degli eventi_
una qualsiasi collezione di eventi $\mathbb A \subseteq 2^\Omega$ che
soddisfa le seguenti proprietà:

$$ \Omega \in \mathbb A; $$

$$ \forall E \in \mathbb A \quad \overline E \in \mathbb A; $$

$$ \forall E, F \in \mathbb A \quad E \cup F \in \mathbb A. $$

````


````{prf:definition}
:label: sigma-algebra-degli-eventi
Ogni algebra degli eventi $\mathbb A$ su uno spazio degli esiti $\Omega$
è una _sigma-algebra_ se, rispetta la seguente proprietà oltre a quelle della
{numref}`algebra-degli-eventi`:

$$ \forall E_1, E_2, \dots \in \mathbb A \quad \union_i E_i \in \mathbb A. $$

````

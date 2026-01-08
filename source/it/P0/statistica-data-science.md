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

(sec_statistica-data-science)=
# Statistica, data science e altre etichette

In passato, molti dati venivano considerati un sottoprodotto di procedure
operative &mdash; talvolta informatizzate &mdash; destinati principalmente
all’archiviazione e raramente riutilizzati. L’idea che i dati siano una risorsa
strategica in quasi ogni ambito della conoscenza umana si è affermata solo
negli ultimi vent'anni. Oggi è pienamente riconosciuto il fatto che, se
raccolti, archiviati ed elaborati in modo sistematico, i dati diventano
strumenti essenziali per analizzare processi complessi, aiutare a comprenderli
e supportare decisioni in contesti critici, come quelli medico, politico o
finanziario.

```{margin}
Dopo l'intervento di John Snow, si registrò effettivamente una diminuzione dei
contagi. Tuttavia, questo calo va interpretato in un contesto più ampio: molte
persone avevano già lasciato il quartiere per mettersi al sicuro. In ogni
caso, le scoperte mediche successive confermarono la correttezza
dell'intuizione di Snow sulle modalità di trasmissione della malattia.
```
Eppure, alcuni esempi notevoli mostrano che un approccio _data-driven_ esisteva
già versp la fine del XIX secolo, ben prima che questo termine venisse coniato.
Uno dei più noti risale al 1854, durante un'epidemia di colera a Londra. Il
medico John Snow, convinto che la malattia non si trasmettesse per via
aerea &mdash; mentre i medici dell'epoca la facevano risalire a _miasmi_, o ad
_aria cattiva_ &mdash; decise di raccogliere prove a sostegno di un'ipotesi
diversa: la contaminazione dell'acqua. Per farlo, sovrappose alla mappa del
quartiere di Soho il numero di contagi registrati in ciascuna
casa[^cartografia]. Il risultato, visibile in {numref}`john-snow`, evidenziava
che i casi erano concentrati nelle vicinanze di una pompa d'acqua situata in
Broad Street. Per rafforzare la sua tesi, Snow osservò che i ù birrai, che
bevevano più birra che acqua &mdash; e quindi consumavano un prodotto
pastorizzato &mdash; risultavano meno colpiti dalla malattia. Grazie a queste
evidenze, convinse le autorità a disattivare la pompa, contribuendo così a
contenere l'epidemia.

```{figure} https://upload.wikimedia.org/wikipedia/commons/archive/2/27/20201116211939%21Snow-cholera-map-1.jpg
:width: 60%
:name: john-snow

La mappa del quartiere di Soho disegnata da John Snow durante l'epidemia di
colera del 1854: ogni tratto orizzontale nero indica un contagio registrato
nell'abitazione adiacente. Immagine di pubblico dominio. Realizzata da John
Snow (1854). Fonte: {extlink}`Wikimedia Commons </sds/short/cholera-map>`.
```

Curiosamente, anche il secondo esempio si colloca nel 1854. In quell'anno
Florence Nightingale parte per la Crimea, dove è in corso una guerra tra la
Russia e l' Impero Ottomano, con il coinvolgimento di diverse potenze europee,
incluso il Regno Unito. È da lì che proviene Nightingale, in veste di
sovrintendente dell'Institute for Sick Gentlewoman, insieme ad altre infermiere
volontarie. Per testimoniare le carenze nella gestione delle cure mediche,
decide di raccogliere dati sulle condizioni sanitarie dei soldati. Nel 1858
presenta i risultati in un rapporto intitolato _Notes on Matters Affecting the
Health, Efficiency and Hospital Administration of the British Army_. Questo
documento include un _diagramma polare_[^polari], riprodotto in
{numref}`florence-nightingale` e oggi considerato un classico esempio di
visualizzazione efficace dei dati. Il grafico è composto da due aree circolari,
suddivise in dodici settori che indicano i mesi da aprile 1854 a marzo 1855 (a
sinistra) e da aprile 1855 a marzo 1856 (a destra). L'area di ogni settore
rappresenta il numero di decessi, suddivisi in tre categorie:

- ferite riportate in battaglia (rosso),
- malattie curabili o prevenibili (blu),
- altre cause (nero).

L'effetto visivo è immediato: la maggior parte delle morti non dipendeva dai
combattimenti, fatto che Nightingale usò per denunciare l'inefficienza degli
ospedali da campo, il cui ambiente insalubre portava alla diffusione tra i
soldati di malattie come colera, tifo o dissenteria. È anche grazie a questo
intervento che il sistema sanitario militare venne successivamente riformato.

```{figure} https://upload.wikimedia.org/wikipedia/commons/archive/1/17/20201105141904%21Nightingale-mortality.jpg
:width: 100%
:name: florence-nightingale

Diagrammi polari che mostrano i decessi dei soldati britannici da aprile 1854
a marzo 1856, nell'ospedale militare in cui prestava servizio Florence
Nightingale. Ogni settore rappresenta un mese, con l'area proporzionale al
numero di morti, mentre i colori indicano la causa del decesso: rosso per le
ferite riportate in battaglia, blu per le malattie curabili e nero per altre
cause. Immagine di pubblico dominio. Realizzata da Florence Nightingale (1858).
Fonte: {extlink}`Wikimedia Commons
<https://malchiodi.com/sds/short/nightingale-source>`.
```

I casi di Snow e Nightingale mostrano bene un approccio descrittivo all'analisi
dei dati: raccogliere presentare le informazioni in modo accurato permette di
mettere in luce aspetti rilevanti di un fenomeno &mdash; in questi esempi, le
cause dei contagi di colera e delle morti tra i soldati &mdash; e fornire basi
solide per decisioni informate. A partire dalla fine del XIX secolo, però, la
statistica comincia anche a svilupparsi sul piano teorico e quantitativo. Senza
alcuna pretesa di esaustione, cito due figure fondamentali: Ronald A. Fisher,
che ha avuto un ruolo centrale nel delineare i metodi della statistica moderna
e delle sue applicazioni nei campi della genetica e della produzione agricola,
e William Gossett, che sviluppò tecniche per controllare la qualità della birra
Guinness senza compromettere l’intera produzione. Per motivi di riservatezza,
Gossett pubblicò i suoi risultati con lo pseudonimo «Student», per evitare che
i concorrenti del suo datore di lavoro scoprissero i metodi innovativi usati in
fabbrica.

Con l’avvento dei computer, a partire dagli anni ’40, ci si è presto accorti
che non solo era possibile usarli per meccanizzare delle operazioni, ma anche
per generare e conservare grandi quantità di dati. Col passare del tempo e lo
sviluppo delle tecnologie collegate, la potenza di calcolo è aumentata, i costi
di memorizzazione si sono abbassati e la diffusione di internet ha reso i dati
più accessibili. Questi fattori hanno portato a un drastico aumento del loro
volume, amplificandone il valore.

A cavallo tra il XX e il XXI secolo è emerso il ruolo del _data scientist_, una
persona capace di integrare competenze informatiche e matematico/statistiche
con la conoscenza di un dominio specifico, cosa che consente di trasformare
dati grezzi in informazioni utili, spesso orientate al _business_. Ma che cosa
distingue davvero chi lavora come data scientist da chi si dedica alla
statistica, all'informatica o alla matematica? La risposta non è immediata.
Tutte e tutti devono oggi avere una familiarità più che buona con strumenti e
concetti propri dell'informatica, oltre a conoscere almeno le basi della
statistica e della matematica. Tuttavia, queste figure restano distinte: chi
opera in informatica non coincide quasi mai con chi invece si occupa di
statistica o matematica, e viceversa. Per esempio, esistono aree
dell’informatica &mdash; come lo sviluppo di sistemi operativi o di applicazioni
per _smartphone_ e dispositivi mobili &mdash; che possono essere tranquillamente
ignorate in ambiti tipici della matematica, della statistica o della data
science. Allo stesso modo, nel contesto informatico difficilmente ci si spinge
in campi come la topologia o la verifica d'ipotesi.

Sottolineo di non avere volutamente messo in campo, finora, l’intelligenza
artificiale, disciplina relativamente recente ma che sta avendo un grande
impatto nella vita quotidiana. Sebbene spesso si intrecci con l’analisi dei
dati, il suo obiettivo principale è lo studio e la replicazione automatica di
processi che, quando svolti dagli esseri umani, richiedono l'impiego di una
qualche forma di intelligenza. In alcuni casi, questi processi si basano su
ragionamenti guidati dai dati; in altri, invece, sono necessari degli approcci
completamente diversi. È proprio questa varietà di obiettivi e metodi che rende
l'intelligenza artificiale una branca dell'informatica meritevole di un
trattamento separato rispetto ai temi affrontati nel testo.

Questo libro si propone di trattare argomenti che spaziano dalla programmazione
all’analisi dei dati, passando per la probabilità e la statistica. Una
combinazione impegnativa, ma coerente con il percorso formativo &mdash; spesso
frammentato &mdash; di chi studia informatica. Leggerlo (e, _ça va sans dire_,
comprenderne i contenuti) non vi trasformerà in _data scientist_, né in persone
esperte di statistica o matematica. E, a voler essere precisi, nemmeno di
informatica o di intelligenza artificiale. Ma vi fornirà una base solida, uno
dei mattoni fondamentali per acquisire una conoscenza il più possibile completa
dell'informatica, con la conseguente autonomia professionale &mdash; insomma,
sviluppare competenze che faranno di voi persone da prendere sul serio. In ogni
caso, mi preme sottolineare che, alla fine, ciò che conta non è l’etichetta
professionale che ci viene attribuita, ma ciò che sappiamo fare bene.


[^cartografia]: Sebbene l'approccio di Snow sia il più noto, i veri precursori
della _cartografia statistica_ furono i francesi André-Michel Guerry e Charles
Dupin, che già nella prima metà dell'Ottocento usavano grafici per evidenziare
differenze tra le provincie della Repubblica in termini di alfabetizzazione o
criminalità. Dupin fu il primo a introdurre quelle che oggi chiamiamo
{extlink}`mappe coropletiche
<https://it.wikipedia.org/wiki/Mappa_coropletica>`, in cui le regioni di una
mappa geografica vengono colorate in funzione del valore di un indicatore
specifico.

[^polari]: Va notato che i diagrammi polari resi celebri da Florence
Nightingale erano già stati introdotti nel 1829 da André-Michel Guerry, lo
stesso citato nella nota precedente.
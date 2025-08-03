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

(sec:statistica-data-science)=
# Statistica, data science e altre etichette

In passato, i dati venivano nella maggior parte dei casi considerati un
sottoprodotto di procedure operative&mdash;talvolta
informatizzate&mdash;destinati principalmente all’archiviazione e raramente
riutilizzati nei processi produttivi. L’idea che essi rappresentino una risorsa
cruciale in pressoché ogni ambito della conoscenza umana si è consolidata solo
negli ultimi vent'anni, riconoscendo pienamente il fatto che, quando vengono
sistematicamente raccolti, archiviati ed elaborati, i dati diventano strumenti
fondamentali per analizzare processi complessi e supportare decisioni in
contesti critici, come quelli della medicina, della politica o della finanza.

```{margin}
È importante sottolineare che, dopo l'intervento di John Snow, si registrò
effettivamente una diminuzione dei contagi. Tuttavia, questo calo va
interpretato in un contesto più ampio, dovuto anche al fatto che una parte
significativa della popolazione aveva abbandonato il quartiere per mettersi al
sicuro. In ogni caso, le successive scoperte della ricerca medica confermeranno
la validità dell'ipotesi di Snow riguardo alle modalità di trasmissione della
malattia.
```
Esistono però alcuni casi storici che mostrano come l’approccio _data-driven_
fosse già presente alla fine del XIX secolo. Nel 1854, a fronte di un'epidemia
di colera a Londra, il medico John Snow sovrappose alla mappa del quartiere di
Soho le informazioni relative al numero di contagi nelle singole
case[^cartografia]. Il grafico ottenuto, visibile in {numref}`john-snow`,
evidenzia come i casi si concentrassero nelle vicinanze di una pompa d'acqua
situata in Broad Street. Lo scopo di Snow era quello di refutare la convinzione
dei medici dell'epoca che il contagio avvenisse per via aerea (si parlava
di _miasmi_, o di _aria cattiva_), avvalorando nel contempo l'ipotesi che la
vera causa fosse la contaminazione dell'acqua. A sostegno di questa ipotesi,
Snow osservò anche che i birrai, che bevevano più birra&mdash;sottoposta a
pastorizzazione&mdash;che acqua, risultavano meno colpiti dalla malattia.
Grazie a queste evidennze, convinse le autorità a disattivare la pompa,
contribuendo così a contenere l'epidemia.

```{figure} https://upload.wikimedia.org/wikipedia/commons/archive/2/27/20201116211939%21Snow-cholera-map-1.jpg
:width: 60%
:name: john-snow

Mappa del quartiere di Soho, Londra, con indicazione del numero di contagi
nelle singole case (i tratti orizzontali neri) durante l'epidemia di colera del
1854.   Immagine di pubblico dominio. Realizzata da John Snow (1854).
Fonte: [Wikimedia Commons](https://en.wikipedia.org/wiki/File:Snow-cholera-map-1.jpg).
```

Curiosamente, anche il secondo esempio si colloca nello stesso anno. Nel 1854,
Florence Nightingale arriva in missione in Crimea, dove è in corso una guerra
iniziata tra la Russia e l' Impero Ottomano, con il coinvolgimento di diverse
potenze europee, incluso il Regno Unito. È da lì che proviene Nightingale, in
veste di sovrintendente dell'Institute for Sick Gentlewoman, insieme ad altre
infermiere volontarie. Rendendosi conto della disorganizzazione delle cure
mediche fornite ai soldati, raccoglie dati che presenterà nel 1858 in un
rapporto intitolato _Notes on Matters Affecting the Health, Efficiency and
Hospital Administration of the British Army_. In questo documento è incluse un
celebre _diagramma polare_[^polari], riprodotto in
{numref}`florence-nightingale` e spesso citato come esempio di visualizzazione
efficace dei dati. Il diagramma è composto da due aree circolari, ciascuna
suddivisa in dodici settori, uno per ogni mese dei periodi aprile
1854&ndash;marzo 1855 e aprile 1855&ndash;marzo 1856. L'area di ogni settore
rappresenta il numero di decessi mensili tra i soldati, suddivisi in tre
categorie:

- ferite riportate in battaglia (rosso),
- malattie curabili o prevenibili (blu),
- altre cause (nero).

Senza entrare nei dettagli tecnici, è evidente che la maggior parte dei decessi
non era dovuta ai combattimenti, fatto che Nightingale uso per denunciare la
disorganizzazione degli ospedali da campo, il cui ambiente insalubre portava
alla diffusione tra i soldati di malattie come colera, tifo o dissenteria. È
anche grazie a questo intervento che il sistema sanitario militare venne
successivamente riformato. 

```{figure} https://upload.wikimedia.org/wikipedia/commons/archive/1/17/20201105141904%21Nightingale-mortality.jpg
:width: 100%
:name: florence-nightingale

Diagrammi polari che mostrano la serie dei decessi dei soldati britannici,
registrati tra aprile 1854 e marzo 1856, nell'ospedale militare in cui prestava
servizio Florence Nightingale. L'area di ogni settore rappresenta il numero di
morti, mentre i colori indicano la causa del decesso: rosso per le ferite
riportate in battaglia, blu per le malattie curabili e nero per altre cause.
Immagine di pubblico dominio. Realizzata da Florence Nightingale (1858).
Fonte: [Wikimedia Commons](https://en.wikipedia.org/wiki/File:Nightingale-mortality.jpg).
```

I casi di Snow e Nightingale illustrano un approccio descrittivo all'analisi
dati: una buona raccolta e presentazione delle informazioni permette di mettere
in luce aspetti rilevanti di un fenomeno (la cause, nella fattispecie, dei
contagi di colera e della maggior parte delle morti tra i soldati), supportando
decisioni informate. In parallelo, a partire dalla fine del XIX secolo, si
sviluppa anche la statistica in senso più quantitativo e teorico. Senza alcuna
pretesa di esaustione, vale la pena menzionare i contributi di Ronald A. Fisher,
che ha avuto un ruolo centrale nel delineare i metodi della statistica
moderna, nonché nelle sue applicazioni nei campi della genetica e della
produzione agricola, e di William Gossett, che sviluppò tecniche statistiche
per controllare la qualità della birra Guinness senza compromettere l’intera
produzione, pubblicando i suoi risultati sotto lo pseudonimo «Student» per
evitare che i concorrenti del suo datore di lavoro scoprissero i metodi
innovativi che venivano usati in fabbrica.

Con l’avvento dei computer, impiegati a partire dagli anni '40 per
automatizzare compiti ripetitivi, ci si è presto accorti che non solo era
possibile meccanizzare delle operazioni, ma anche generare e conservare una
notevole mole di dati. La crescente potenza di calcolo, la riduzione dei costi
di memorizzazione e la diffusione di internet hanno reso questi dati più
accessibili e ne hanno drasticamente aumentato il volume, amplificandone il
valore.

A cavallo tra il XX e il XXI secolo è emersa la figura del _data scientist_,
professionista capace di integrare competenze informatiche e statistiche con
la conoscenza di uno specifico dominio applicativo, per trasformare dati grezzi
in informazioni utili, spesso orientate al _business_. Ma cosa distingue un
data scientist da uno statistico o da un informatico?

La risposta non è semplice. Oggi, uno statistico deve avere una solida
familiarità con strumenti e concetti propri dell'informatica, così come
un informatico dovrebbe padroneggiare alcuni aspetti fondamentali della
statistica e della matematica. Tuttavia, le tre figure non coincidono: un
informatico non è quasi mai anche uno statistico, né un matematico, e viceversa.
Esistono ambiti dell’informatica, come lo sviluppo di sistemi operativi o di
applicazioni per dispositivi mobili, che un matematico può ignorare del tutto;
allo stesso modo, molti informatici conservano solo vaghi ricordi di concetti
probabilistici o statistici, e difficilmente si avventurerebbero in territori
come la topologia o la verifica d'ipotesi.

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

Questo libro si propone di trattare argomenti che spaziano dalla
programmazione all’analisi dei dati, passando per la probabilità e la
statistica. Una combinazione impegnativa, ma coerente con il percorso formativo
&mdash;spesso frammentato&mdash;di chi studia informatica. Leggerlo (e, _ça va
sans dire_, comprenderne i contenuti) non vi trasformerà in _data scientist_,
né in statistici o matematici. E, a voler essere precisi, nemmeno in
informatici o in esperti di intelligenza artificiale. Ma vi fornirà una base
solida, uno dei mattoni fondamentali per diventare un informatico competente e
preparato&mdash; insomma, uno da prendere sul serio. In ogni caso, mi preme
sottolineare che, alla fine, ciò che conta non è l’etichetta professionale che
ci viene attribuita, ma ciò che sappiamo fare bene.


[^cartografia]: Sebbene l'approccio di Snow sia quello più noto, i veri
precursori della _cartografia statistica_ furono i francesi André-Michel Guerry
e Charles Dupin, che già nella prima metà dell'Ottocento usavano grafici per
evidenziare differenze tra le provincie della Repubblica in aspetti come
l'alfabetizzazione o il tasso di criminalità. Dupin fu il primo a introdurre
quelle che oggi chiamiamo
[mappe coropletiche](https://it.wikipedia.org/wiki/Mappa_coropletica), in cui
le regioni di una mappa geografica vengono colorate in funzione del valore di
un indicatore specifico.

[^polari]: Va notato che i diagrammi polari resi celebri da Florence
Nightingale erano già stati introdotti nel 1829 da André-Michel Guerry (lo
stesso citato nella nota precedente).
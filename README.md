# Superhero Data Science

[![License: CC BY-NC-SA 4.0][cc-by-nc-sa-shield]][cc-by-nc-sa]
[![License: MIT][mit-image]][mit]

## Accesso online

Il libro è disponibile online all'indirizzo
[https://malchiodi.com/sds](https://malchiodi.com/sds).

## Installazione locale

Nota: le seguenti istruzioni fanno riferimento a un ambiente Linux.
L'installazione in altri sistemi operativi può richiedere alcune minime
variazioni.

È possibile installare localmente il libro clonando questo repository e
installando le librerie da cui il progetto dipende. Per fare ciò, è altamente
consigliato creare e attivare un environment virtuale nel quale installare
`pip` e `pip-compile`. Successivamente è sufficiente posizionarsi nella
directory radice del repository clonato ed eseguire i seguenti comandi:

    $ pip-compile --strip-extras
    $ pip install -r requirements.txt

Una volta installate le librerie, per consultare il libro basta eseguire il
seguente comando nell'environment creato appositamente

    $ myst start --execute

che eseguirà un server web locale (per default sulla porta `3000`), al quale
collegarsi usando un browser.

## Licenza

I contenuti testuali di questo libro sono soggetti alla licenza
[Creative Commons BY-NC-SA 4.0 International License][cc-by-nc-sa].
Il codice è rilasciato sotto licenza
All the code is licensed under an [MIT](CODE_LICENSE).
Per eventuali contributi si prega di consultare le relative
[Linee guida](CONTRIBUTING.md).

Copyright © 2021–present [Dario Malchiodi](https://malchiodi.di.unimi.it).

[cc-by-nc-sa]: http://creativecommons.org/licenses/by-nc-sa/4.0/
[cc-by-nc-sa-shield]: https://img.shields.io/badge/License-CC_BY--NC--SA_4.0-lightgrey.svg
[mit]: https://opensource.org/licenses/MIT
[mit-image]: https://img.shields.io/badge/License-MIT-yellow.svg


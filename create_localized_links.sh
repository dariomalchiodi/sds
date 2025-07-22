#!/bin/bash

# Script to create symbolic links for localized URLs

BASE_DIR="/home/malchiodi/repo/editoria/sds/source"

echo "Creating symbolic links for English version..."

cd "$BASE_DIR/en"

# Root level
ln -sf landing.md home.md

# P0 directory
cd P0
ln -sf presentazione.md introduction.md
ln -sf approccio.md approach.md  
ln -sf ringraziamenti.md acknowledgments.md
ln -sf imparare-e-programmare.md learning-and-programming.md
ln -sf convenzioni.md conventions.md
ln -sf notazione.md notation.md
ln -sf utilizzo-in-insegnamento.md use-in-teaching.md
ln -sf uno-sguardo-di-insieme.md overview-at-a-glance.md

cd ..

# P1-PAD directory
cd P1-PAD
ln -sf presentazione.md introduction.md

cd c1-intro-python
ln -sf introduzione-a-python.md introduction-to-python.md
ln -sf installare-python.md installing-python.md
ln -sf tipi-di-dati.md data-types.md
ln -sf dati-semplici.md simple-data.md
ln -sf dati-strutturati.md structured-data.md
ln -sf strutture-di-controllo.md control-structures.md
ln -sf funzioni.md functions.md
ln -sf importare-moduli.md importing-modules.md
ln -sf disegnare-grafici.md drawing-charts.md
ln -sf leggere-file.md reading-files.md

cd ../..

echo "English symbolic links created successfully!"

echo "Creating symbolic links for French version..."

cd "$BASE_DIR/fr"

# Root level
ln -sf landing.md accueil.md

# P0 directory  
cd P0
ln -sf presentazione.md presentation.md
ln -sf approccio.md approche.md
ln -sf ringraziamenti.md remerciements.md
ln -sf imparare-e-programmare.md apprendre-et-programmer.md
ln -sf convenzioni.md conventions.md
ln -sf notazione.md notation.md
ln -sf utilizzo-in-insegnamento.md utilisation-enseignement.md
ln -sf uno-sguardo-di-insieme.md apercu-general.md

cd ..

# P1-PAD directory
cd P1-PAD
ln -sf presentazione.md presentation.md

cd c1-intro-python
ln -sf introduzione-a-python.md introduction-a-python.md
ln -sf installare-python.md installer-python.md
ln -sf tipi-di-dati.md types-de-donnees.md
ln -sf dati-semplici.md donnees-simples.md
ln -sf dati-strutturati.md donnees-structurees.md
ln -sf strutture-di-controllo.md structures-de-controle.md
ln -sf funzioni.md fonctions.md
ln -sf importare-moduli.md importer-modules.md
ln -sf disegnare-grafici.md dessiner-graphiques.md
ln -sf leggere-file.md lire-fichiers.md

cd ../..

echo "French symbolic links created successfully!"

echo "All symbolic links have been created!"

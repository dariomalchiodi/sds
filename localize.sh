#!/usr/bin/env bash

original=("Figure" "Table" "Footnotes" "References")
translation=("Figura" "Tabella" "Note" "Bibliografia")

cd _build
echo "Now in $(pwd)"

for i in ${!original[@]};
do
    EN=${original[$i]}
    IT=${translation[$i]}
    echo "substitution $EN -> $IT"
    for FILE in $(grep -R -l --include="*.js*" $EN .)
    do
        sed -i -e "s/$EN/$IT/g" $FILE
    done
done

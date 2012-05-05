#!/bin/bash
if [ "$(echo $0 | sed 's|[^/]*$||')" != "./" ] ; then cd $(echo $0 | sed 's|[^/]*$||') ; fi

echo "Génération de la liste de base via circos-data-gouv.csv"
python genListCodes.py > listCodes.csv
wc -l listCodes.csv

echo "Normalisation"
python normaliseListCodes.py > normalisedListCodes.csv
wc -l normalisedListCodes.csv

echo "Génération des correspondances"
python listAllByCirco.py > listAllByCirco.csv
wc -l listAllByCirco.csv

echo "Génération de la liste des doubles"
python genDoubles.py > doubles.txt
wc -l doubles.txt

echo "Génération de la liste des circos sans doubles par villes"
python listGdBy.py > gdByTown.csv
wc -l gdByTown.csv

echo "Génération de la liste des circos par circos sans doubles"
python listGdBy.py 1 > gdByCirco.csv
wc -l gdByCirco.csv

echo "Génération de la liste des circos problématiques par villes sans les doubles"
python listBadBy.py > badByTown.csv
wc -l badByTown.csv

echo "Génération de la liste des circos problématiques par circos sans les doubles"
python listBadBy.py 1 > badByCirco.csv
wc -l badByCirco.csv

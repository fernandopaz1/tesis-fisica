#!/bin/bash
rm main.e
reset

dim=$1
iteraciones=$2
Z=$3

if (("$1" < "10")); then
  echo "No se aceptan redes menores a 10 de dimension";
   exit 1
fi

if (("$2" < "100")); then
  echo "No se aceptan menos de 100 iteraciones";
   exit 1
fi

Z_sin_punto=$(echo $Z | sed 's/\.//g')

echo "#define DIM $dim" > ./include/parametros.h
echo "#define ITERACIONES $iteraciones" >> ./include/parametros.h
echo "#define Z_c $Z" >> ./include/parametros.h

name_avalanchas_csv="avalanchas${dim}_Zc${Z_sin_punto}.csv"

file=main

g++ -o $file.e $file.cpp -Ofast -lboost_iostreams -lboost_system -lboost_filesystem
./$file.e


rm $file.e

FILE=caracterizacion.csv
if test -f "$FILE"; then
    echo "$FILE exists."
    mv ./caracterizacion.csv ./data/$name_avalanchas_csv
    python graficar.py $1 $2 $3
    # python graficoEnergias.py $1
fi

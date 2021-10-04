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


echo "#define DIM $dim" > ./include/parametros.h
echo "#define ITERACIONES $iteraciones" >> ./include/parametros.h
echo "#define Z_c $Z" >> ./include/parametros.h
file=main

g++ -o $file.e $file.cpp -Ofast -lboost_iostreams -lboost_system -lboost_filesystem
./$file.e
rm $file.e
python graficar.py $1 $2
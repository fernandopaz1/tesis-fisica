#!/bin/bash
reset

echo "First arg: $1"
echo "Second arg: $2"
dim=$1
iteraciones=$2
echo "#define DIM $dim" > ./include/parametros.h
echo "#define ITERACIONES $iteraciones" >> ./include/parametros.h
file=main
# gcc -O3 -W $file.cpp -o $file.e -lm

g++ -o $file.e $file.cpp -Ofast -lboost_iostreams -lboost_system -lboost_filesystem
./$file.e
rm $file.e

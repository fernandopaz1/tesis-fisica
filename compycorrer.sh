#!/bin/bash
reset

dim=$1
iteraciones=$2
Z=$3
overwrite=$4
perturbado=$5

if (("$1" < "10")); then
  echo "No se aceptan redes menores a 10 de dimension";
   exit 1
fi

dim_str="$dim"

if (("$dim" < "100")); then
  dim_str="0$dim"
fi

if (("$2" < "100")); then
  echo "No se aceptan menos de 100 iteraciones";
   exit 1
fi

Z_sin_punto=$(echo $Z | sed 's/\.//g')

echo "#define DIM $dim" > ./include/parametros.h
echo "#define ITERACIONES $iteraciones" >> ./include/parametros.h
echo "#define Z_c $Z" >> ./include/parametros.h
echo "#define OVERWRITE $overwrite" >> ./include/parametros.h

#echo "const char *filename= \"./chaosData/red_equilibrio${dim_str}_Zc${Z_sin_punto}.csv\";" >> ./include/parametros.h
echo "const char *filename= \"./chaosData/red_equilibrio${dim}.csv\";" >> ./include/parametros.h
echo "const char *perfil_file= \"./chaosData/perfil${dim}_Zc${Z_sin_punto}.csv\";" >> ./include/parametros.h


echo "#define PERTURBADO $perturbado" >> ./include/parametros.h
echo "#define PERTURBCION 0.1" >> ./include/parametros.h

nombre=""
if(("$perturbado"=="true")); then
  nombre="_1"
fi


name_avalanchas_csv="avalanchas${dim}_Zc${Z_sin_punto}${nombre}.csv"
name_serie_csv="serie${dim}_Zc${Z_sin_punto}${nombre}"


file="main${dim}_Zc${Z_sin_punto}$nombre"

g++ -o $file.e main.cpp -Ofast -lboost_iostreams -lboost_system -lboost_filesystem
time ./$file.e

notify-send Simulacion "Se termino de ejecutar la simulación" 

rm $file.e


FILE2=datos.csv
if test -f "$FILE2"; then
  number=0
  if test -f "./chaosData/${name_serie_csv}.csv"; then
   number=$((number + 1)); else
    echo "$FILE2 exists."
    echo "entro como si no existiera"
    echo "./chaosData/${name_serie_csv}.csv"
    mv ./datos.csv ./chaosData/$name_serie_csv.csv
  fi
  echo "./chaosData/${name_serie_csv}_number${number}.csv"
  while test -f "./chaosData/${name_serie_csv}_number$number.csv";
  do
    number=$((number + 1))
  done
    echo "$FILE2 exists."
    mv ./datos.csv ./chaosData/${name_serie_csv}_number$number.csv
fi

FILE=caracterizacion.csv
if test -f "$FILE"; then
    echo "$FILE exists."
    mv ./caracterizacion.csv ./chaosData/$name_avalanchas_csv
fi
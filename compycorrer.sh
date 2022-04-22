#!/bin/bash
rm main.e
reset

#Parametros pasados al script
dim=$1
iteraciones=$2
Z=$3
overwrite=$4 # si es true sobreescribe la red al finalizar la simulacion

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


# pasando parametros a la simulación

echo "#define DIM $dim" > ./include/parametros.h
echo "#define ITERACIONES $iteraciones" >> ./include/parametros.h
echo "#define Z_c $Z" >> ./include/parametros.h
echo "#define OVERWRITE $overwrite" >> ./include/parametros.h

echo "const char *filename= \"./data/red_equilibrio${dim}.csv\";" >> ./include/parametros.h
echo "const char *perfil_file= \"./data/perfil${dim}_Zc${Z_sin_punto}.csv\";" >> ./include/parametros.h



name_avalanchas_csv="avalanchas${dim}_Zc${Z_sin_punto}.csv"
name_serie_csv="serie${dim}_Zc${Z_sin_punto}"


file="main${dim}_Zc${Z_sin_punto}"


# Compila y corremos la simulación
g++ -o $file.e main.cpp -Ofast -lboost_iostreams -lboost_system -lboost_filesystem
time ./$file.e

notify-send Simulacion "Se termino de ejecutar la simulación" 

rm $file.e

# Si no existe el archivo con los mismos parametros de la simulación lo guardo con un nombre
# si existe lo guardo con el mismop nombre mas un numero que se va incrementando
FILE2=datos.csv
if test -f "$FILE2"; then
  number=0
  if test -f "./data/${name_serie_csv}.csv"; then
   number=$((number + 1)); else
    echo "$FILE2 exists."
    echo "entro como si no existiera"
    echo "./data/${name_serie_csv}.csv"
    mv ./datos.csv ./data/$name_serie_csv.csv
  fi
  echo "./data/${name_serie_csv}_number${number}.csv"
  while test -f "./data/${name_serie_csv}_number$number.csv";
  do
    number=$((number + 1))
  done
    echo "$FILE2 exists."
    mv ./datos.csv ./data/${name_serie_csv}_number$number.csv
fi

# Este archivo siempre se guarda, un  corte transversal de la red
# sirve para ver si esta en equilibrio
FILE=caracterizacion.csv
if test -f "$FILE"; then
    echo "$FILE exists."
    mv ./caracterizacion.csv ./data/$name_avalanchas_csv
fi

# Analisis en python
read -p "Queres analizar los datos con python? [ y | n ]:  " yn
  case $yn in
      [Yy]* ) python graficar.py $dim $iteraciones $Z $number
              python graficoEnergias.py $dim;;
      [Nn]* ) exit;;
  esac



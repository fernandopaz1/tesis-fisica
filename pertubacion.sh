#!/bin/bash
reset

dim=$1
iteraciones=$2
Z=$3
overwrite=$4

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

./compycorrer.sh $dim $iteraciones $Z $overwrite "false"
# sleep 10
# echo "Segunda simulacion"
# ./compycorrer.sh $dim $iteraciones $Z $overwrite "true"


read -p "Queres analizar los datos con python? [ y | n ]:  " yn
  case $yn in
      [Yy]* ) python graficar.py $1 $2 $3 0;
              python graficoEnergias.py $1;;
      [Nn]* ) exit;;
  esac



#!/bin/bash

#########################
#
# Script para correr simulaciones de un sistema sin perturbar y otro perturbado
# Una vez finalizadad la simulacion pregunta si se quiere analizar los datos obtenidos
#
# Ejemplo: ./pertubacion.sh <dim> <iteraciones> <Z> <overwrite> <perturbacion>
#
#########################


reset

dim=$1                    # Dimension de la red
iteraciones=$2            # Cantidad de iteraciones
Z=$3                      # Threshold de la red
overwrite=$4              # Indica si se sobreescribe el campo en equilibrio guardado
perturbacion=$5           # Aplitud con la cual se hara la simulacion perturbada (es un porcentaje del B_max de la red cargada)

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

./compycorrer.sh $dim $iteraciones $Z $overwrite false "0"
sleep 10
echo "Segunda simulacion"
./compycorrer.sh $dim $iteraciones $Z $overwrite true "$perturbacion"


python graficar.py $1 $2 $3 $5
python graficoEnergias.py $1
# read -p "Queres analizar los datos con python? [ y | n ]:  " yn
#   case $yn in
#       [Yy]* ) python graficar.py $1 $2 $3 $5;
#               python graficoEnergias.py $1;;
#       [Nn]* ) exit;;
#   esac



########################################
#
# Este script se encarga de compilar y ejecutar la simulacion principal para luego analizar
# los datos con otro script de python.
#
################
#!/bin/bash
reset

dim=$1                #Dimension de la red
iteraciones=$2        # Cantidad de iteraciones
Z=$3                  # Threshold del sistema
overwrite=$4          # Indica si al correr las simulaciones se sobreescribe la red en equilibrio
perturbado=$5         # Indica si al cargar la red se debe perturbar
perturbacion=$6       # Aplitud de la perturbacion (es un porcentaje de B_max de la red)

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
pert_sin_punto=$(echo $perturbacion | sed 's/\.//g')


nombre="_pert$pert_sin_punto"


echo "#define DIM $dim" > ./include/parametros.h
echo "#define ITERACIONES $iteraciones" >> ./include/parametros.h
echo "#define Z_c $Z" >> ./include/parametros.h
echo "#define OVERWRITE $overwrite" >> ./include/parametros.h

#echo "const char *filename= \"./chaosData/red_equilibrio${dim_str}_Zc${Z_sin_punto}.csv\";" >> ./include/parametros.h
echo "const char *filename= \"./chaosData/red_equilibrio${dim}.csv\";" >> ./include/parametros.h
echo "const char *perfil_file= \"./chaosData/perfil${dim}_Zc${Z_sin_punto}${nombre}.csv\";" >> ./include/parametros.h
echo "const char *series_file= \"./chaosData/serie${dim}_Zc${Z_sin_punto}${nombre}.csv\";" >> ./include/parametros.h
echo "const char *avalanchas_file= \"./chaosData/avalanchas${dim}_Zc${Z_sin_punto}${nombre}.csv\";" >> ./include/parametros.h


echo "#define PERTURBADO $perturbado" >> ./include/parametros.h
echo "#define PERTURBACION $perturbacion" >> ./include/parametros.h




file="main${dim}_Zc${Z_sin_punto}$nombre"

g++ -o $file.e main.cpp -Ofast -lboost_iostreams -lboost_system -lboost_filesystem
time ./$file.e

notify-send Simulacion "Se termino de ejecutar la simulación" 

rm $file.e

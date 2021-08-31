# Tesis de Licenciatura en Ciencias Física

Este repositorio contiene simulaciones que forman parte de mi trabajo de tesis de licenciatura.

<figure class="image">
  <img src="https://user-images.githubusercontent.com/26823588/131282034-7a24f05a-b8c4-494f-8c8d-97ecefd94f5d.png" alt="{{ include.description }}">
  <figcaption>Fig: Simulación de un sistema SOC utilizando una red de 60X60.</figcaption>
</figure>

## Ejecutar este proyecto

Para correr este proyecto es necesario instalar instalar librerias con los siguientes comandos.

`sudo apt-get install g++`

`sudo apt-get install gnuplot`

`sudo apt-get install libgnuplot-iostream-dev`

Descargar este repositorio via

`git clone https://github.com/fernandopaz1/tesis-fisica.git`

moverse dentro de la carpeta contenedora con

`cd tesis-fisica`

cambiar los permisos del archivo compycorrer.sh con

`chmod 744 compycorrer.sh`

y ejecutar el archivo compycorrer.sh con

`./compycorrer.sh`

## Ejecutar tests unitarios

Si se desea testear la aplicacion se debe correr el siguiente comando en la carpeta `tesis-fisica`

`mkdir ext && cd ext && git clone https://github.com/google/googletest.git`

Nuevamente en la carpeta `tesis-fisica` es necesario dar permisos de ejecucion al archivo `testear.sh` con el comando:

`chmod 744 testear.sh`

y correr los tests con el comando

`./testear.sh`

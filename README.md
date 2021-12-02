# Tesis de Licenciatura en Ciencias Física

Este repositorio contiene simulaciones que forman parte de mi trabajo de tesis de licenciatura.

<figure class="image">
  <img src="https://user-images.githubusercontent.com/26823588/131282034-7a24f05a-b8c4-494f-8c8d-97ecefd94f5d.png" alt="{{ include.description }}">
  <figcaption>Fig: Simulación de un sistema SOC utilizando una red de 60X60.</figcaption>
</figure>

## Ejecutar este proyecto

Para correr este proyecto es necesario instalar instalar librerias con los siguientes comandos.

`sudo apt-get install g++`



Descargar este repositorio via

`git clone https://github.com/fernandopaz1/tesis-fisica.git`

moverse dentro de la carpeta contenedora con

`cd tesis-fisica`

cambiar los permisos del archivo compycorrer.sh con

`chmod 744 compycorrer.sh`

y ejecutar el archivo compycorrer.sh con los parametros correspondientes al tamaño de la red, la cantidad de iteraciones y el valor de umbral, por ejemplo

`./compycorrer.sh 64 100000 "0.2"`

<details>
<summary>Si hay problemas con libboost</summary>
<br>
  <details>
<summary>En Ubuntu/Debian</summary>
  <br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sudo apt install libboost-all-dev
  </details>
<br>
  <details>
 <summary>En Fedora</summary>
  <br>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  sudo dnf install boost-devel
  </details>
</details>
<br>


El programa para graficar se ejecuta automáticamente luego de terminar la simulación, pero en caso de querer correrlo nuevamente se lanza desde la terminal con el comando

`python graficar.py 64 100000 02`

## Dependencias de Python

Para graficar el output de la simulacion se deben instalar las librerias en `requeriments.txt` con el comando

`pip install -r requeriments.txt`

o hacerlo dentro de un entorno virtual mediante los comandos

`pip install virtualenv`

`python -m venv env`

`source env/bin/activate`

`python -m pip install --upgrade pip `

`pip install -r requeriments.txt`

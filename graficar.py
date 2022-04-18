####################################
#
# Gráficos de avalanchas y energias
#  
# Ejemplo de invocacion: python graficar.py <dim> <iteraciones> <Z>
# El threshold debe ser pasado como un string . Por ejemplo "0.05"
#
####################################

from entropia_permutaciones.Entropy import Entropy
from entropia_permutaciones.Clasificador import Clasificador
import numpy as np
import matplotlib.pyplot as plt
import graficoAvalanchas as gA
import graficoEnergias as gE
import pandas as pd
import powerlaw as pl
import sys
import os
from csv import writer
import re

dim=int(sys.argv[1])                    # Dimension de la red
iteraciones=int(sys.argv[2])            # Cantidad de iteracines
Z_c_original=sys.argv[3]                # Threshold de la red en formato string sin punto
Z_c=Z_c_original.replace(".","")


def get_label(path, filename):
    lab="Original"
    if re.findall("pert\d\d", filename):
        aux=path[-6:-4].replace(".","")
        par=aux if int(aux)>=10 else aux[0]+"."+aux[1]
        lab=r'$\eta$ {param}'.format(param=par)
    return lab

# Funcion que hace Graficos de P, E y T en funcion del numero de avalancha
def plot_avalanchas(path):
    lab="Original"
    if re.findall("pert\d\d", filename):
        aux=path[-6:-4].replace(".","")
        par=aux if int(aux)>=10 else aux[0]+"."+aux[1]
        lab=r'$\eta$ {param}'.format(param=par)
    data = pd.read_csv(path)
    plt.figure(3)
    plt.plot(data['nro'],data['P'],label=lab )
    plt.xlabel("Número de avalancha")
    plt.ylabel("P")
    plt.legend(loc='upper right', ncol=3)

    plt.figure(1)
    plt.plot(data['nro'],data['E'],label=lab )
    plt.xlabel("Número de avalancha")
    plt.ylabel("E")
    plt.legend(loc='upper right', ncol=3)

    plt.figure(2)
    plt.plot(data['nro'],data['T'],label=lab )
    plt.xlabel("Número de avalancha")
    plt.ylabel("Duración")
    plt.legend(loc='upper right', ncol=3)
    data = data.iloc[0:0]

# Graficos de energia liberada, energia total y diference de energia entre
# perturbacion y original.
def plot_energias(path, original):
    lab="Original"
    if re.findall("pert\d\d", filename):
        aux=path[-6:-4].replace(".","")
        par=aux if int(aux)>=10 else aux[0]+"."+aux[1]
        lab=r'$\eta$ {param}'.format(param=par)
    data = pd.read_csv(path)
    
    plt.figure(5)
    plt.plot(data['Iteraciones'],data['Energia_total'],label=lab)
    plt.xlabel("Iteracion")
    plt.ylabel("Energia Total")
    plt.legend(loc='upper right', ncol=3)

    plt.figure(6)
    plt.plot(data['Iteraciones'],data['Energia_liberada'],label=lab)
    plt.xlabel("Iteracion")
    plt.ylabel("Energia Liberada")
    plt.legend(loc='upper right', ncol=3)

    plt.figure(7)
    plt.plot(data['Iteraciones'],data['Energia_total']-original['Energia_total'],label=lab)
    plt.xlabel("Iteracion")
    plt.ylabel("Diferencia de Energía")
    plt.legend(loc='upper right', ncol=3)
    data = data.iloc[0:0]

def plot_entropy(path, filename):
    lab = get_label(path, filename)
    data = pd.read_csv(path)
    entropies=[]
    for i in range(2,15):
        e = Entropy(i)
        value = e.entropy_calculation(*data['Energia_total'])/(i-1)
        entropies.append(value)
    
    plt.figure(8)
    plt.scatter(range(2,15),entropies,label=lab)
    plt.xlabel("Orden")
    plt.ylabel("<h(n)>")
    plt.legend(loc='upper right', ncol=3)
    data = data.iloc[0:0]

def plot_lyapunov(path, filename):
    lab = get_label(path, filename)
    data = pd.read_csv(path)
    valor_inicial = data['Energia_total'][0]
    # for i in range(0,20):
    #     print(data['Energia_total'][i+1]-data['Energia_total'][i])
    # return
    prom = 1000
    lyapunov = []
    points = len(data['Energia_total'])//prom-1
    for i in range(0,points):
        actual_point = 0
        for j in range(0,prom-1):
            value = np.abs(data['Energia_total'][i*prom +j+1]-data['Energia_total'][i*prom+j])
            if(value!=0):
                actual_point += np.log(value)
            # else:
            #     print(data['Energia_total'][i*1000 +j+1],data['Energia_total'][i*1000 +j])
        actual_point /= prom
        lyapunov.append(actual_point)
    
    plt.figure(9)
    plt.plot(range(0,points),lyapunov,label=lab)
    plt.xlabel("Orden")
    plt.ylabel("<h(n)>")
    plt.legend(loc='upper right', ncol=3)
    data = data.iloc[0:0]

# iteracion sobre toda la carpeta chaos data graficando
original=pd.read_csv("chaosData/serie64_Zc02_pert0.csv")
for filename in os.listdir("chaosData/"):
    if "avalanchas" in filename: 
        path=os.path.join("chaosData/", filename)
        # plot_avalanchas(path)
        continue
    elif "serie" in filename: 
        path=os.path.join("chaosData/", filename)
        # plot_energias(path, original)
        # plot_entropy(path, filename)
        plot_lyapunov(path, filename)
        continue
    else:
        continue
    
plt.show()
exit()
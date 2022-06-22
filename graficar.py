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
from utils.DatosAvalacha import DatosAvalacha
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
perturbacion = sys.argv[4] # Parametro de perturbacion de la red


def get_label(path, filename):
    lab="Original"
    if re.findall("pert\d\d", filename):
        aux=path[-6:-4].replace(".","")
        par=aux if int(aux)>=10 else aux[0]+"."+aux[1]
        lab=r'$\eta$ {param}'.format(param=par)
    return lab

def print_to_csv(List,nombre_csv):
    # Open our existing CSV file in append mode
    # Create a file object for this file
    with open(nombre_csv, 'a') as f_object:

        # Pass this file object to csv.writer()
        # and get a writer object
        writer_object = writer(f_object)

        # Pass the list as an argument into
        # the writerow()
        writer_object.writerow(List)

        #Close the file object
        f_object.close()


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

def lyapunov(path, filename, original):
    lab = get_label(path, filename)
    data = pd.read_csv(path)
    valor_inicial = data['Energia_total'][0]

    points = 1000000
    for i in range(1000,points):
        actual_point = 0
        value = np.abs(data['Energia_total'][i]-original['Energia_total'][i])
        if(value!=0):
            actual_point += np.log(value/valor_inicial)
        # else:
        #     print(data['Energia_total'][i*1000 +j+1],data['Energia_total'][i*1000 +j])
    actual_point /= points
    lyapunov = actual_point
    print("Lyapunov", lyapunov)
    return lyapunov
 
def analisis_avalanchas(path):
    lab="Original"
    if re.findall("pert\d\d", filename):
        aux=path[-6:-4].replace(".","")
        par=aux if int(aux)>=10 else aux[0]+"."+aux[1]
        lab=r'$\eta$ {param}'.format(param=par)
    data = pd.read_csv(path)
    datos = DatosAvalacha(len(data["nro"]),min(data["E"]),max(data["E"]),min(data["P"]),max(data["P"]),min(data["T"]),max(data["T"]))
    cant_avalanchas = len(data["nro"])

    print(path)
    print("#Avalanchas", datos.numero_avalanchas)
    print("max_T", datos.max_T)
    print("min_T", datos.min_T)
    print("max_E", datos.max_E)
    print("min_E", datos.min_E)
    print("max_P", datos.max_P)
    print("min_P", datos.min_P)
    return datos
    




# iteracion sobre toda la carpeta chaos data graficando
original_filename = "chaosData/serie64_Zc02_pert0.csv"
avalancha_original = "avalanchas64_Zc02_pert0.csv"
original=pd.read_csv("chaosData/serie64_Zc02_pert0.csv")
for filename in os.listdir("chaosData/"):
    if "avalanchas" in filename: 
        path=os.path.join("chaosData/", filename)
        if(avalancha_original.__ne__(filename)):
            data_pert = analisis_avalanchas(path)
        else:
            data_original = analisis_avalanchas(path)
        # plot_avalanchas(path)
        continue
    elif "serie" in filename: 
        path=os.path.join("chaosData/", filename)
        # plot_energias(path, original)
        # plot_entropy(path, filename)
        if(original_filename.__ne__(path)):
            lyapunov_coef = lyapunov(path, filename, original)
        continue
    else:
        continue
    
plt.show()


respuesta = input("¿Desea guardar los datos? (y/n)")
nombre_csv="./chaosData/datosAvalanchas.csv"
if respuesta == "y":
    if(not os.path.isfile(nombre_csv)):
        List=["dim","iteraciones",'threshold',"perturbacion (%)","lyapunov","avalanchas","avalanchas_pert","min_e","min_e_pert","max_e","max_e_pert","min_p","min_p_pert","max_p","max_p_pert","min_t","min_t_pert","max_t","max_t_pert"]
        print_to_csv(List,nombre_csv)
    List=[dim,iteraciones,Z_c_original,perturbacion, lyapunov_coef, data_original.numero_avalanchas, data_pert.numero_avalanchas, data_original.min_E, data_pert.min_E, data_original.max_E, data_pert.max_E, data_original.min_P, data_pert.min_P, data_original.max_P, data_pert.max_P, data_original.min_T, data_pert.min_T, data_original.max_T, data_pert.max_T]
    print_to_csv(List,nombre_csv)




exit()
import numpy as np
import matplotlib.pyplot as plt
import graficoAvalanchas as gA
import graficoEnergias as gE
import pandas as pd
import powerlaw as pl
import sys
import os
from csv import writer

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




# exit()

dim=int(sys.argv[1])
iteraciones=int(sys.argv[2])
Z_c_original=sys.argv[3]
Z_c=Z_c_original.replace(".","")
try:
    number=str("_number"+sys.argv[4]) 
except IndexError:
    number=str()
# number=str("_number"+sys.argv[4]) if int(sys.argv[4])>0 else str()



# data = pd.read_csv("data/serie{dim}_Zc{Z_c}{n}.csv".format(dim=dim,Z_c=Z_c,n=number))

# data = data[:-1]
# gE.graficar_energias(data)
# gE.graficar_perfil(dim, True)

# data = data.iloc[0:0]

# exit()

perfil = pd.read_csv("data/perfil{dim}_Zc{Z_c}.csv".format(dim=dim,Z_c=Z_c))
gE.ultimo_perfil(perfil, dim)

perfil = perfil.iloc[0:0]

avalanchas = pd.read_csv("data/avalanchas{dim}_Zc{Z_c}.csv".format(dim=dim,Z_c=Z_c))
avalanchas = avalanchas[:-1]
avalanchas =avalanchas[avalanchas !=0]

print(len(avalanchas["nro"]))

#################
# Las funciones plot hacen el grafico en escala
# logaritmica, y devuelven las pendientes calculadas con el ajuste lineal
# Los parametros numericos son el minimo y maximo a considerar para hacer el ajuste
#################

# pendiente_P_vs_E=gA.plot_loglog_fit(avalanchas,"P","E",10,1000)
# pendiente_P_vs_T=gA.plot_loglog_fit(avalanchas,"T","P",100,100000)

# print("Pendiente P vs E",pendiente_P_vs_E)
# print("Pendiente P vs T",pendiente_P_vs_T)

pendiente_E, pendiente_E_error=gA.plot_histograma_fit(avalanchas,"E",37,100000)
pendiente_P, pendiente_P_error=gA.plot_histograma_fit(avalanchas,"P",12,300)
pendiente_T, pendiente_T_error=gA.plot_histograma_fit(avalanchas,"T",10,900)

print("Pendiente E",pendiente_E)
print("Pendiente P",pendiente_P)
print("Pendiente T",pendiente_T)

#################
#  Pregunta si queremos guardar todas las pendientes de los gráficos
#  en un csv
#################

respuesta = input("¿Desea guardar los datos? (y/n)")
nombre_csv="./data/pendientes_avalanchas.csv"
if respuesta == "y":
    if(not os.path.isfile(nombre_csv)):
        List=["dim","iteraciones","avalanchas",'threshold',"alpha_e","alpha_e_err","alpha_p","alpha_p_err",'alpha_t',"alpha_t_err"]
        print_to_csv(List,nombre_csv)
    List=[dim,iteraciones,len(avalanchas["nro"]),Z_c_original,pendiente_E,pendiente_E_error,pendiente_P,pendiente_P_error,pendiente_T,pendiente_T_error]
    print_to_csv(List,nombre_csv)


avalanchas = avalanchas.iloc[0:0]

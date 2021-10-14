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


avalanchas = pd.read_csv("data/avalanchas{dim}_Zc{Z_c}.csv".format(dim=dim,Z_c=Z_c))
avalanchas = avalanchas[:-1]
avalanchas =avalanchas[avalanchas !=0]



# data = pd.read_csv("datos.csv") 
# data = data[:-1]
# gE.graficar_energias(data)
# gE.graficar_perfil(dim)



pendiente_P_vs_E=gA.plot_loglog_fit(avalanchas,"P","E",10,1000)
# gA.plot_loglog_fit(avalanchas,"R","A",10,32)
pendiente_P_vs_T=gA.plot_loglog_fit(avalanchas,"T","P",100,100000)

print("Pendiente P vs E",pendiente_P_vs_E)
print("Pendiente P vs T",pendiente_P_vs_T)

pendiente_E=gA.plot_histograma_fit(avalanchas,"E",37,100000)
pendiente_P=gA.plot_histograma_fit(avalanchas,"P",12,300)
pendiente_T=gA.plot_histograma_fit(avalanchas,"T",10,900, True)

print("Pendiente E",pendiente_E)
print("Pendiente P",pendiente_P)
print("Pendiente P",pendiente_T)

respuesta = input("¿Desea guardar los datos? (y/n)")
nombre_csv="./data/pendientes_avalanchas.csv"
if respuesta == "y":
    if(not os.path.isfile(nombre_csv)):
        List=["dim","iteraciones","avalanchas",'threshold',"alpha_e","alpha_p",'alpha_t']
        print_to_csv(List,nombre_csv)
    List=[dim,iteraciones,len(avalanchas["nro"]),Z_c_original,pendiente_E,pendiente_P,pendiente_T]
    print_to_csv(List,nombre_csv)



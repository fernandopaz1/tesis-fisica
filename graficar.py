import numpy as np
import matplotlib.pyplot as plt
import graficoAvalanchas as gA
import graficoEnergias as gE
import pandas as pd
import powerlaw as pl
import sys
import os
from csv import writer

# def print_to_csv(List,nombre_csv):
#     # Open our existing CSV file in append mode
#     # Create a file object for this file
#     with open(nombre_csv, 'a') as f_object:

#         # Pass this file object to csv.writer()
#         # and get a writer object
#         writer_object = writer(f_object)

#         # Pass the list as an argument into
#         # the writerow()
#         writer_object.writerow(List)

#         #Close the file object
#         f_object.close()




# exit()

dim=int(sys.argv[1])
iteraciones=int(sys.argv[2])
Z_c_original=sys.argv[3]
Z_c=Z_c_original.replace(".","")



data = pd.read_csv("chaosData/avalanchas{dim}_Zc{Z_c}.csv".format(dim=dim,Z_c=Z_c))

data2 = pd.read_csv("chaosData/avalanchas{dim}_Zc{Z_c}_1.csv".format(dim=dim,Z_c=Z_c))


plt.figure(1)
plt.plot(data['nro'],data['T'])
plt.plot(data2['nro'],data2['T'])
plt.show()

# data = data[:-1]
# gE.graficar_energias(data)
# gE.graficar_perfil(dim, True)

# data = data.iloc[0:0]

# exit()
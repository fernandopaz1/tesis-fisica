import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sys


dim=int(sys.argv[1])

# plt.ion()

data = pd.read_csv("datos.csv") 
data = data[:-1]

try:
    perfil = pd.read_csv("perfil.csv",error_bad_lines=False)
    perfil = perfil[:-1]
    for i in range(0,len(perfil),10):
        plt.figure(3)
        it=i*20000
        actual=perfil.loc[i]
        plt.plot(perfil.loc[i], label="Iter nro {iteracion}".format(iteracion=it))
        plt.xlabel("x")
        plt.ylabel("y")
        plt.xticks(np.arange(0, dim+1, 2.0))
        plt.legend(loc='upper right')
        plt.show(block=False)
except:
    print("No se pudo levantar el perfil")


plt.figure(1)
plt.plot(data["Iteraciones"],data["Energia_liberada"],  label="Energia liberada", linewidth=0.05,)
plt.xlabel("Iteraciones")
plt.ylabel("e_r")
# plt.xscale("log")
plt.legend()
plt.show(block=False)


plt.figure(2)
plt.plot(data["Iteraciones"],data["Energia_total"], label="Energia total")
plt.xlabel("Iteraciones")
plt.ylabel("e_t")
# plt.yscale("log")
# plt.xscale("log")
plt.legend()
plt.show()


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sys



# plt.ion()

def graficar_perfil(dim, block=False):
    try:
        perfil = pd.read_csv("perfil.csv",error_bad_lines=False)
        perfil = perfil[:-1]
        step=int(len(perfil)/10)
        for i in range(0,len(perfil),step):
            plt.figure(3)
            it=i*20000
            actual=perfil.loc[i]
            plt.plot(perfil.loc[i], label="t={iteracion}".format(iteracion=it))
            plt.xlabel(r"$k$")
            plt.ylabel(r"$B(x_{},y_k)$".format(int(dim/2)))
            plt.xticks(np.arange(0, dim+1, int(dim/10)))
            plt.legend(loc='upper right')
            plt.show(block=block)
    except:
        print("No se pudo levantar el perfil")

def graficar_energias(data, block=False):
    plt.figure(1)
    plt.plot(data["Iteraciones"],data["Energia_liberada"],  label="Energia liberada", linewidth=0.05,)
    plt.xlabel("Iteraciones")
    plt.ylabel(r"$E_r/\epsilon_0$")
    plt.legend()
    plt.show(block=block)

    plt.figure(2)
    plt.plot(data["Iteraciones"],data["Energia_total"], label="Energia total")
    plt.xlabel("Iteraciones")
    plt.ylabel(r"$E_t/\epsilon_0$")
    plt.legend()
    plt.show(block=block)

if __name__=="__main__":    
    dim=int(sys.argv[1])
    graficar_energias(pd.read_csv("datos.csv"))
    graficar_perfil(dim,True)

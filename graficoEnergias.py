import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sys


# plt.ion()

def graficar_perfil(dim, block=False):
    
    try:
        perfil = pd.read_csv("perfil.csv")
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
        plt.show()
    except:
        print("No se pudo levantar el perfil")

def ultimo_perfil(perfil, dim):
    plt.figure(3)
    plt.plot(perfil.iloc[0], label="Perfil")
    plt.xlabel(r"$k$")
    plt.ylabel(r"$B(x_{},y_k)$".format(int(dim/2)))
    # plt.xticks(np.arange(0, dim+1, int(dim/10)))
    plt.legend(loc='upper right')
    plt.show()
   
def graficar_energias(data, block=False):
    # plt.figure(1)
    # plt.plot(data["Iteraciones"],data["Energia_liberada"],  label="Energia liberada", linewidth=0.05,)
    # plt.xlabel("Iteraciones")
    # plt.ylabel(r"$E_r/\epsilon_0$")
    # plt.legend()
    # plt.show(block=False)

    plt.figure(2)
    plt.plot(data["Iteraciones"],data["Energia_total"], label="Energia total")
    plt.xlabel("Iteraciones")
    plt.ylabel(r"$E_t/\epsilon_0$")
    plt.legend()
    plt.show()

if __name__=="__main__":    
    pass

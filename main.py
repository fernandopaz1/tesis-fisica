from typing import NewType
import numpy as np
import matplotlib.pyplot as plt
import time
from numpy.core.shape_base import block
import seaborn as sns
import random as rnd

plt.ion()

plt.figure()

# n = int(input("Ingrese el tamaño de la red:   "))
n=20
n_cuad=n*n

B = np.zeros((n, n))
C = np.zeros((n, n))


def plot_matrix(B):
    plt.imshow(B)
    plt.draw()
    plt.pause(1)
    plt.clf()


def energia_total(B):
    E_total=0
    for i in range(n):
        for j in range(n):
            E_total= E_total+B[i][j]*B[i,j]
    return E_total/n_cuad

def suma_vecinos(B, i, j):
    suma=0.0
    if(i != 0):
        suma = B[i-1][j]
    if(i != n-1):
        suma = suma + B[i+1][j]
    if(j != 0):
        suma=suma + B[i][j-1]
    if j != n-1:
        suma= suma+ B[i][j+1]
    return suma

def aumentar_vecinos(B, i, j,cantindad):
    if(i != 0):
        B[i-1][j]= B[i-1][j]+cantindad
    if(i != (n-1)):
        B[i+1][j]=B[i+1][j]+cantindad
    if(j != 0):
        B[i][j-1]=B[i][j-1]+cantindad
    if(j != (n-1)):
        B[i][j+1]=B[i][j+1]+cantindad

def actualizar_red(B,C):
    B=C
    C[:] = 0

def perturbar_nodo_aleatorio(B, sigma1, sigma2):
    i= rnd.randint(0,n-1)
    j= rnd.randint(0,n-1)
    B[i][j]=rnd.uniform(sigma1, sigma2)

def soc(B,C):
    sigma1=-0.2
    sigma2=0.8
    Z_c=0.2
    D=2
    s=2*D+1
    e0= (2*D/s)*Z_c*Z_c


    for t in range(1000):
        e=0
        for i in range(n):
            for j in range(n):
                Z_k=B[i][j]-(1/(2*D))*suma_vecinos(B,i,j)
                if(abs(Z_k)>Z_c):
                    C[i][j]=C[i][j]-(2*D/2)*Z_c 
                    aumentar_vecinos(C, i, j, Z_c/s)
                    e= e+((2.0*Z_k/Z_c)-1.0)
        if(e>0):
            actualizar_red(B,C)
        else:
            perturbar_nodo_aleatorio(B, sigma1,sigma2)
        plot_matrix(B)

soc(B,C)

# for i in range(100):

#     B = np.random.random((n, n))
#     plot_matrix(B)


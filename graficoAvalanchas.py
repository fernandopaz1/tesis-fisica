import numpy as np
import matplotlib.pyplot as plt
from numpy.core.shape_base import block
import pandas as pd
import sys


bin=1000
bin_e=100
histType="stepfilled" #bar step stepfilled
avalanchas = pd.read_csv("caracterizacion.csv") 
avalanchas = avalanchas[:-1]
avalanchas =avalanchas[avalanchas !=0]

def fitLogaritmico(x,y):
    if isinstance(x,(list,np.ndarray)):
        cuttof=np.argwhere(y==0)
        if(cuttof.size!=0):
            x=x[0:cuttof[0][0]]
            y=y[0:cuttof[0][0]]
    logx = np.log(x)
    logy = np.log(y)
    coeffs = np.polyfit(logx,logy,deg=1)
    poly = np.poly1d(coeffs)
    return poly, coeffs

def filtrar(A ,min, max):
    return [a for a in A if a>min and a<max]

def filtrar_dataframe(A, columna1, columna2,min,max):
    A=A.filter(items=[columna1,columna2])
    return A.loc[(A[columna1] > min) & (A[columna1] < max)]

plt.figure(1)
# plt.title("Avalanchas")
plt.xlabel(r'${P}/{\epsilon_{0}}$')
plt.ylabel(r'${E}/{\epsilon_{0}}$')
subset=filtrar_dataframe(avalanchas,"P","E",10,1000)
fit, coeffs=fitLogaritmico(subset["P"],subset["E"])
yfit= lambda x: np.exp(fit(np.log(x)))
plt.plot(subset["P"],yfit(subset["P"]), color="red", label="Pendiente {pendiente:.2f}".format(pendiente=coeffs[0]))
plt.scatter(avalanchas["P"],avalanchas["E"],label=r'$E/{\epsilon_{0}}$ vs $P/{\epsilon_{0}}$',marker='o', s=0.1)
plt.xscale('log')
plt.yscale('log')
plt.legend(loc='upper right')
# plt.savefig("avalanchas.png")
plt.show(block=False)


plt.figure(2)
plt.xlabel('T')
plt.ylabel(r'${P}/{\epsilon_{0}}$')
plt.scatter(avalanchas["T"],avalanchas["P"],label=r'${P}/{\epsilon_{0}}$ vs T',marker='o',s=0.1)
subset=filtrar_dataframe(avalanchas,"T","P",100,100000)
fit, coeffs=fitLogaritmico(subset["T"],subset["P"])
yfit= lambda x: np.exp(fit(np.log(x)))
plt.plot(subset["T"],yfit(subset["T"]), color="red", label="Pendiente {pendiente:.2f}".format(pendiente=coeffs[0]))
plt.xscale('log')
plt.yscale('log')
plt.legend(loc='upper right')
plt.show(block=False)


def filtrar_bins(bin,count, min,max):
    return [a for a in bin if a>min and a<max]

plt.figure(3)
counts,bin_edges=np.histogram(avalanchas["P"],bins=bin)
bins = (bin_edges[:-1] + bin_edges[1:])/2
df_bins = pd.DataFrame(data=[bins, counts]).T
df_bins=df_bins[df_bins[1]!=0]
subset=filtrar_dataframe(df_bins,0,1,10,100)
fit, coeffs=fitLogaritmico(df_bins[0],df_bins[1])
yfit= lambda x: np.exp(fit(np.log(x)))
plt.plot(df_bins[0],yfit(df_bins[0]), color="red", label="Pendiente {pendiente:.2f}".format(pendiente=coeffs[0]))
plt.xscale('log')
plt.hist(avalanchas["P"],bins=bin,label=r'$f({P}/{\epsilon_{0}})$',alpha=0.5,
         log=True,histtype=histType)
plt.yscale('log')
plt.xlabel(r'${P}/{\epsilon_{0}}$')
plt.scatter(bins,counts,label=r'$f({P}/{\epsilon_{0}})$',marker='o',s=10)


plt.ylabel(r'$f({P}/{\epsilon_{0}})$')
plt.legend(loc='upper right')
plt.show(block=False)



plt.figure(4)
counts,bin_edges=np.histogram(avalanchas["E"],bins=bin_e)
bins = (bin_edges[:-1] + bin_edges[1:])/2
df_bins = pd.DataFrame(data=[bins, counts]).T
df_bins=df_bins[df_bins[1]!=0]
subset=filtrar_dataframe(df_bins,0,1,10,100)
fit, coeffs=fitLogaritmico(df_bins[0],df_bins[1])
yfit= lambda x: np.exp(fit(np.log(x)))
plt.plot(df_bins[0],yfit(df_bins[0]), color="red", label="Pendiente {pendiente:.2f}".format(pendiente=coeffs[0]))

plt.xscale('log')
plt.hist(avalanchas["E"],bins=bin_e,label=r'$f({E}/{\epsilon_{0}})$',alpha=0.5,
         log=True,histtype=histType)
plt.yscale('log')
plt.xlabel(r'${E}/{\epsilon_{0}}$')
plt.scatter(bins,counts,label=r'$f({E}/{\epsilon_{0}})$',marker='o',s=10)
plt.ylabel(r'$f({E}/{\epsilon_{0}})$')
plt.legend(loc='upper right')
plt.show(block=False)

plt.figure(5)
counts,bin_edges=np.histogram(avalanchas["T"],bins=bin)
bins = (bin_edges[:-1] + bin_edges[1:])/2
df_bins = pd.DataFrame(data=[bins, counts]).T
df_bins=df_bins[df_bins[1]!=0]
subset=filtrar_dataframe(df_bins,0,1,10,100)
fit, coeffs=fitLogaritmico(df_bins[0],df_bins[1])
yfit= lambda x: np.exp(fit(np.log(x)))
plt.plot(df_bins[0],yfit(df_bins[0]), color="red", label="Pendiente {pendiente:.2f}".format(pendiente=coeffs[0]))
plt.xscale('log')
plt.hist(avalanchas["T"],bins=bin,label=r'$f(T)$',alpha=0.5,log=True,histtype=histType)
plt.yscale('log')
plt.xlabel('T')
plt.scatter(bins,counts,label=r'$f(T)$',marker='o',s=10)
plt.ylabel(r'$f(T)$')
plt.legend(loc='upper right')
plt.show()


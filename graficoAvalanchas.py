import numpy as np
import powerlaw as pl

import matplotlib.pyplot as plt
from numpy.core.shape_base import block
import pandas as pd
import sys


bin=1000
bin_e=100
histType="stepfilled" #bar step stepfilled
avalanchas=[]

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


def filtrar_dataframe(A, columna1, columna2,min,max):
    A=A.filter(items=[columna1,columna2])
    B=A.loc[(A[columna1] > min) & (A[columna1] < max)]
    return B

def plot_fit(A,campo1,campo2,min,max):
    subset=filtrar_dataframe(A,campo1,campo2,min,max)
    fit, coeffs=fitLogaritmico(subset[campo1],subset[campo2])
    yfit= lambda x: np.exp(fit(np.log(x)))
    plt.plot(subset[campo1],yfit(subset[campo1]), color="red", label="Pendiente {pendiente:.2f}".format(pendiente=coeffs[0]))

def plot_loglog_fit(A,campo1,campo2,min,max, block=False):
    plt.figure()
    # plt.title("Avalanchas")
    plt.xlabel(r'${}/\epsilon_0$'.format(campo1))
    plt.ylabel(r'${}/\epsilon_0$'.format(campo2))
    plot_fit(A,campo1,campo2,min,max)
    plt.scatter(A[campo1],A[campo2],label=r'${E}/\epsilon_0$ vs ${P}/\epsilon_0$'.format(E=campo1,P=campo2),marker='o', s=0.1)
    plt.xscale('log')
    plt.yscale('log')
    plt.legend(loc='upper right')
    # plt.savefig("avalanchas.png")
    plt.show(block=block)


def fit_histograma(bins,counts, min,max):
    df_bins = pd.DataFrame(data=[bins, counts]).T
    df_bins=df_bins[df_bins[1]!=0]
    subset=filtrar_dataframe(df_bins,0,1,min,max)
    fit, coeffs=fitLogaritmico(subset[0],subset[1])
    yfit= lambda x: np.exp(fit(np.log(x)))
    plt.plot(subset[0],yfit(subset[0]), color="red", label="Pendiente {pendiente:.2f}".format(pendiente=coeffs[0]))    


def plot_histograma_fit(A,campo, min,max, block=False):
    plt.figure()
    P=A[campo]
    if(campo=="T"):
        bins=50
    else:
        bins=500
    logbins= np.logspace(np.log10(P.min()), np.log10(P.max()), bins)
    counts,bin_edges=np.histogram(P,bins=logbins,density=True)
    bins = (bin_edges[:-1] + bin_edges[1:])/2
    fit_histograma(bins,counts,min,max)
    plt.hist(P,bins=logbins,label=r'$f({}/\epsilon_0)$'.format(campo),alpha=0.5,histtype=histType,density=True)
    
    fit = pl.Fit(P, xmin=min, xmax=max, fit_method="KS")
    alpha=fit.power_law.alpha
    sigma=fit.power_law.sigma
    fit.power_law.plot_pdf(color = "b", label = r'Powerlaw $\alpha={pendiente:.2f}\pm{error:.2f}$'.format(pendiente=alpha,error=sigma))
    pl.plot_pdf(P,color = "b", label = r'Dist con bins de powerlaw')

    
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel(r'${campo}/\epsilon_0$'.format(campo=campo))
    plt.ylabel(r'$f({campo}/\epsilon_0)$'.format(campo=campo))
    plt.legend(loc='upper right')
    plt.show(block=block) 

if __name__ == "__main__":
    avalanchas = pd.read_csv("caracterizacion.csv") 
    avalanchas = avalanchas[:-1]
    avalanchas =avalanchas[avalanchas !=0]
    plot_loglog_fit(avalanchas,"P","E",10,1000)
    plot_loglog_fit(avalanchas,"T","P",1000,100000)

    plot_histograma_fit(avalanchas,"P",3,300)
    plot_histograma_fit(avalanchas,"E",100,3000)
    plot_histograma_fit(avalanchas,"T",3000,230000, True)

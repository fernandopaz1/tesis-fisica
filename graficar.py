import graficoAvalanchas as gA
import graficoEnergias as gE
import pandas as pd
import sys


dim=int(sys.argv[1])
iteraciones=int(sys.argv[2])

if(iteraciones<10000000):
    data = pd.read_csv("datos.csv") 
    data = data[:-1]
    gE.graficar_energias(data)
    gE.graficar_perfil(dim)

avalanchas = pd.read_csv("caracterizacion.csv") 
avalanchas = avalanchas[:-1]
avalanchas =avalanchas[avalanchas !=0]



gA.plot_loglog_fit(avalanchas,"P","E",10,1000)
gA.plot_loglog_fit(avalanchas,"T","P",1000,100000)
gA.plot_histograma_fit(avalanchas,"P",3,300)
gA.plot_histograma_fit(avalanchas,"E",100,3000)
gA.plot_histograma_fit(avalanchas,"T",3000,230000, True)



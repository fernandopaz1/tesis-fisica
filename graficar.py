import graficoAvalanchas as gA
import graficoEnergias as gE
import pandas as pd
import sys


dim=int(sys.argv[1])
iteraciones=int(sys.argv[2])

data = pd.read_csv("datos.csv") 
data = data[:-1]
gE.graficar_energias(data)
gE.graficar_perfil(dim)

avalanchas = pd.read_csv("caracterizacion.csv") 
avalanchas = avalanchas[:-1]
avalanchas =avalanchas[avalanchas !=0]



gA.plot_loglog_fit(avalanchas,"P","E",10,1000)
gA.plot_loglog_fit(avalanchas,"R","A",10,32)
gA.plot_loglog_fit(avalanchas,"T","P",10,10000)
gA.plot_histograma_fit(avalanchas,"P",10,100)
gA.plot_histograma_fit(avalanchas,"E",145,10000)
gA.plot_histograma_fit(avalanchas,"T",10,200, True)



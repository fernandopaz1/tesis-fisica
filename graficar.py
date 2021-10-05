import numpy as np
import matplotlib.pyplot as plt
import graficoAvalanchas as gA
import graficoEnergias as gE
import pandas as pd
import powerlaw as pl
import sys


dim=int(sys.argv[1])
iteraciones=int(sys.argv[2])


avalanchas = pd.read_csv("caracterizacion.csv") 
avalanchas = avalanchas[:-1]
avalanchas =avalanchas[avalanchas !=0]


fit = pl.Fit(avalanchas["P"])
print(fit.power_law.alpha)
print(fit.power_law.sigma)
fit.distribution_compare("power_law", "exponential")
pl.plot_pdf(avalanchas["P"], linear_bins=False, color = "b", label = "Power Law")
print(avalanchas["P"].min())
print(avalanchas["P"].max())

logbins= np.logspace(np.log10(avalanchas["P"].min()), np.log10(avalanchas["P"].max()), 100)
plt.hist(avalanchas["P"], bins = logbins, alpha=0.5,histtype="stepfilled",density=True)
plt.xscale("log")
plt.show()

exit()

data = pd.read_csv("datos.csv") 
data = data[:-1]
gE.graficar_energias(data)
gE.graficar_perfil(dim)



gA.plot_loglog_fit(avalanchas,"P","E",10,1000)
gA.plot_loglog_fit(avalanchas,"R","A",10,32)
gA.plot_loglog_fit(avalanchas,"T","P",10,10000)


gA.plot_histograma_fit(avalanchas,"E",145,10000)
gA.plot_histograma_fit(avalanchas,"T",10,200, True)



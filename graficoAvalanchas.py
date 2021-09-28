import numpy as np
import matplotlib.pyplot as plt
from numpy.core.shape_base import block
import pandas as pd
import sys


bin=5
avalanchas = pd.read_csv("caracterizacion.csv") 
avalanchas = avalanchas[:-1]

plt.figure(1)
# plt.title("Avalanchas")
plt.xlabel(r'${P}/{\epsilon_{0}}$')
plt.ylabel(r'${E}/{\epsilon_{0}}$')
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
plt.xscale('log')
plt.yscale('log')
plt.legend(loc='upper right')
plt.show(block=False)


plt.figure(3)
counts,bin_edges=np.histogram(avalanchas["P"],bins=bin)
bins = (bin_edges[:-1] + bin_edges[1:])/2
plt.xscale('log')
# plt.hist(avalanchas["P"],bins=bin,label=r'$f({P}/{\epsilon_{0}})$',alpha=0.5, log=True,histtype='step')
plt.yscale('log')
plt.xlabel(r'$f({P}/{\epsilon_{0}})$')
plt.scatter(bins,counts,label=r'$f({P}/{\epsilon_{0}})$',marker='o',s=10)
plt.ylabel(r'$f({P}/{\epsilon_{0}})$')
plt.legend(loc='upper right')
plt.show(block=False)


plt.figure(4)
counts,bin_edges=np.histogram(avalanchas["E"],bins=bin)
bins = (bin_edges[:-1] + bin_edges[1:])/2
plt.xscale('log')
# plt.hist(avalanchas["E"],bins=bin,label=r'$f({E}/{\epsilon_{0}})$',alpha=0.5, log=True,histtype='step')
plt.yscale('log')
plt.xlabel(r'$f({P}/{\epsilon_{0}})$')
plt.scatter(bins,counts,label=r'$f({E}/{\epsilon_{0}})$',marker='o',s=10)
plt.ylabel(r'$f({E}/{\epsilon_{0}})$')
plt.legend(loc='upper right')
plt.show(block=False)

plt.figure(5)
counts,bin_edges=np.histogram(avalanchas["T"],bins=bin)
bins = (bin_edges[:-1] + bin_edges[1:])/2
plt.xscale('log')
# plt.hist(avalanchas["T"],bins=bin,label=r'$f(T)$',alpha=0.5, log=True,histtype='step')
plt.yscale('log')
plt.xlabel(r'$f(T)$')
plt.scatter(bins,counts,label=r'$f(T)$',marker='o',s=10)
plt.ylabel(r'$f(T)$')
plt.legend(loc='upper right')
plt.show()


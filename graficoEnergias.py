import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# plt.ion()

data = pd.read_csv("datos.csv") 


plt.figure()
plt.plot(data["Iteraciones"],data["Energia_liberada"],  label="Energia liberada")
plt.xlabel("Iteraciones")
plt.ylabel("e_r")
plt.xscale("log")
plt.legend()
plt.show(block=False)


plt.figure(2)
plt.plot(data["Iteraciones"],data["Energia_total"], label="Energia total")
plt.xlabel("Iteraciones")
plt.ylabel("e_t")
plt.yscale("log")
plt.xscale("log")
plt.legend()
plt.show()
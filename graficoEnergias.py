import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("datos.csv") 

print(data.head)

plt.figure()
plt.plot(data["Iteraciones"],data["Energia_liberada"])
plt.show()


plt.figure(2)
plt.plot(data["Iteraciones"],data["Energia_total"])
plt.show()
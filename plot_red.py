
import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

plt.style.use('fivethirtyeight')

x_vals = []
y_vals = []

index = count()


def animate(i):
    data = np.loadtxt(open("matriz.csv", "rb"), delimiter=",", skiprows=1)

    plt.cla()

    plt.imshow(data, label='Channel 1')

    plt.legend(loc='upper left')
    plt.tight_layout()


ani = FuncAnimation(plt.gcf(), animate, interval=100)

plt.tight_layout()
plt.show()
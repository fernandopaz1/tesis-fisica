from .Clasificador import Clasificador
import numpy as np

class Entropy:
    def __init__(self, order):
        self._classifier = Clasificador(order)

    def entropy_calculation(self, *args):
        self._classifier.classify_all(*args)
        entropy = 0
        for i in self._classifier.series_types():
            probability = self._classifier.probability(i)
            entropy -= probability*np.log2(probability)
        return entropy

if __name__ == '__main__':
    print("Se esta ejecuntando el script Entropy como main")
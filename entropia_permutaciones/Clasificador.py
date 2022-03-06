class Clasificador:
    def __init__(self, n):
        if(n<2):
            raise ValueError('No se puede calcular la entropia de permutacion para n<2') 
        self.order = n
        self._classifier = {}
        self._total = 0
    
    @staticmethod
    def get_type(*args: float):
        """Toma una lista de numeros y los codifica un binario
        con 1 si la sucesión crece y 0 si decrece.

        Keyword arguments:
        *args -- lista de numeros
        """
        a=0
        numberList =[item for item in args]
        for i in range(0, len(numberList)-1):
            a = a << 1
            if(numberList[i] < numberList[i+1]):
                a = a | 1
        return a
    
    def clasify_segment(self, *args: float):
        """Clasifica una lista de numeros en un diccionario.

        Keyword arguments:
        *args -- lista de numeros
        """
        key = Clasificador.get_type(*args)
        self.total = self.total+1
        self._classifier[key]= self._classifier.get(key, 0) + 1
    
    @property
    def total(self):
        return self._total
    
    @total.setter
    def total(self, total):
        self._total = total

    def get_aperances(self, key: int):
        """Dada una key nos dice cuantas veces ocurre esa combinacion.

        Keyword arguments:
        key -- entero positivo
        """
        return self._classifier.get(key,0)

    def probability(self, key):
        return self.get_aperances(key)/self.total

    def classify_all(self, *args):
        series = list(args)
        for i in range(0, len(series)-self.order+1):
            self.clasify_segment(*series[i:i+self.order])
    
    def series_types(self):
        return self._classifier.keys()

if __name__ == "__main__":
    print("Clasificador")
    
    


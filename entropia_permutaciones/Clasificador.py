import pytest
class Clasificador:
    def __init__(self, n):
        self.order = n
        self.classifier = {}
    
    # Clasifica una lista de numeros dependiendo si la sucecion crece o decrece asignando 1 y 0
    # Cualquier lista de n elementos se codifica en un numero binario de n-1 digitos.
    @staticmethod
    def get_type(*args):
        a=0
        numberList =[item for item in args]
        for i in range(0, len(numberList)-1):
            a = a << 1
            if(numberList[i] < numberList[i+1]):
                print("entro")
                a = a | 1
            print(a)
        return a
    

# codificaccion en binario 00
def test_classification_all_minor():
    assert Clasificador.get_type(3,2,1) == 0

# codificaccion en binario 11
def test_classification_all_mayor():
    assert Clasificador.get_type(10,11,12) == 3

# codificaccion en binario 10
def test_classification_all_mayor_menor():
    assert Clasificador.get_type(10,11,9) == 2

# codificaccion en binario 01
def test_classification_all_menor_mayor():
    assert Clasificador.get_type(10,9,100) == 1

# codificaccion en binario 00
def test_classification_constante():
    assert Clasificador.get_type(1,1,1) == 0

if __name__ == "__main__":
    print("Clasificador")
    
    


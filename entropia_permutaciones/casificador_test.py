import pytest
from Clasificador import Clasificador 

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


def test_classification_dict():
    c = Clasificador(3)
    c.clasify_segment(1,2,3)
    c.clasify_segment(10,11,12)
    c.clasify_segment(10,9,100)
    assert c.get_aperances(3) == 2
    assert c.get_aperances(0) == 0
    assert c.get_aperances(1) == 1
    assert c.total == 3
    assert c.probability(3) == 2/3
    assert c.probability(0) == 0
    assert c.probability(1) == 1/3

def test_classification_probability():
    c = Clasificador(3)
    c.classify_all(1,2,3,10,1)
    assert c.get_aperances(3) == 2
    assert c.get_aperances(0) == 0
    assert c.get_aperances(2) == 1
    assert c.total == 3
    assert c.probability(3) == 2/3
    assert c.probability(0) == 0
    assert c.probability(2) == 1/3

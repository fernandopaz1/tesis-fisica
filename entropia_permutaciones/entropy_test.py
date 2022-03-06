import pytest
import numpy as np
from Entropy import Entropy 


def test_entropy_H2():
    e = Entropy(2)
    result = -(4/6)*np.log2(4/6)-(2/6)*np.log2(2/6)
    assert e.entropy_calculation(4,7,9,10,6,11,3) == result
    
def test_entropy_H3():
    e = Entropy(3)
    result = -(4/5)*np.log2(2/5)-(1/5)*np.log2(1/5)
    assert e.entropy_calculation(4,7,9,10,6,11,3) == result

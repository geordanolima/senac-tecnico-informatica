import pytest
from calculadora import somar, subtrair


def test_soma():
    assert somar(valor_1=2.0, valor_2=8.0) == 10.0

def test_error_soma():
    with pytest.raises(Exception):
        somar(valor_1=1, valor_2=2)

def test_subteacao():
    assert subtrair(valor_1=1.0, valor_2=1.0) == 0.0
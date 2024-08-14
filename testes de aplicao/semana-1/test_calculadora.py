import pytest
from calculadora import somar


def test_soma():
    assert somar(valor_1=2.0, valor_2=8.0) == 10.0

def test_error_soma():
    with pytest.raises(Exception):
        somar(valor_1=1, valor_2=2)
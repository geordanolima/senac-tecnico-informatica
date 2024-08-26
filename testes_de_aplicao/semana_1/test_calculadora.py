import pytest
from .calculadora import somar, subtrair, multiplicar, dividir, e_float, calcular, identificar_operacao


@pytest.mark.parametrize(
    "valor_1,valor_2,resultado_esperado",
    [
        (1.0, 1.0, 2),
        (8.0, -2.0, 6.0),
        (-3.0, 4.0, 1.0),
        (2.1, 2.5, 4.6),
    ],
)
def test_soma(valor_1, valor_2, resultado_esperado):
    assert somar(valor_1=valor_1, valor_2=valor_2) == resultado_esperado


@pytest.mark.parametrize(
    "valor_1,valor_2,resultado_esperado",
    [
        (1, 1, 2.0),
        (8.0, -2, 6.0),
        (-3, 4.0, 1.0),
    ],
)
def test_error_soma(valor_1, valor_2, resultado_esperado):
    with pytest.raises(Exception):
        somar(valor_1=valor_1, valor_2=valor_2) == resultado_esperado


@pytest.mark.parametrize(
    "valor_1,valor_2,resultado_esperado",
    [
        (1.0, 1.0, 0.0),
        (8.0, 2.0, 6.0),
        (3.0, 4.0, -1.0),
        (2.5, 2.0, 0.5),
    ],
)
def test_subteacao(valor_1, valor_2, resultado_esperado):
    assert subtrair(valor_1=valor_1, valor_2=valor_2) == resultado_esperado


@pytest.mark.parametrize(
    "valor_1,valor_2,resultado_esperado",
    [
        (1, 1, 0.0),
        (8.0, 2, 6.0),
        (3, 4.0, 1.0),
    ],
)
def test_error_subtracao(valor_1, valor_2, resultado_esperado):
    with pytest.raises(Exception):
        subtrair(valor_1=valor_1, valor_2=valor_2) == resultado_esperado


@pytest.mark.parametrize(
    "valor_1,valor_2,resultado_esperado",
    [
        (1.0, 1.0, 1),
        (8.0, 2.0, 16.0),
        (3.0, 4.0, 12.0),
        (2.5, 2.0, 5.0),
    ],
)
def test_multiplicacao(valor_1, valor_2, resultado_esperado):
    assert multiplicar(valor_1=valor_1, valor_2=valor_2) == resultado_esperado


@pytest.mark.parametrize(
    "valor_1,valor_2,resultado_esperado",
    [
        (1, 1, 1),
        (8, 2.0, 16.0),
        (3.0, 4, 12.0),
    ],
)
def test_error_multiplicacao(valor_1, valor_2, resultado_esperado):
    with pytest.raises(Exception):
        multiplicar(valor_1=valor_1, valor_2=valor_2) == resultado_esperado


@pytest.mark.parametrize(
    "valor_1,valor_2,resultado_esperado",
    [
        (1.0, 1.0, 1),
        (8.0, 2.0, 4.0),
        (3.0, 4.0, 0.75),
        (2.5, 2.0, 1.25),
    ],
)
def test_divisao(valor_1, valor_2, resultado_esperado):
    assert dividir(valor_1=valor_1, valor_2=valor_2) == resultado_esperado


@pytest.mark.parametrize(
    "valor_1,valor_2,resultado_esperado",
    [
        (1, 1.0, 1),
        (8, 2.0, 4.0),
        (3.0, 4, 0.75),
        (1.0, 0.0, 0.0)
    ],
)
def test_error_divisao(valor_1, valor_2, resultado_esperado):
    with pytest.raises(Exception):
        dividir(valor_1=valor_1, valor_2=valor_2) == resultado_esperado


@pytest.mark.parametrize(
    "valor",
    [1.0, 2.5, 1.111, 3.0902],
)
def test_e_float(valor):
    assert e_float(valor)


@pytest.mark.parametrize(
    "valor",
    [1, 'a', (), [], {}, None, False],
)
def test_error_e_float(valor):
    with pytest.raises(Exception):
        assert e_float(valor)


@pytest.mark.parametrize(
    "text,expressao,resultado_esperado",
    [
        ('C', '', False),
        ('1', 'Erro', '1'),
        ('1', '0', '1'),
        ('+', '1', '1+'),
        ('1', '1+', '1+1'),
        ('=', '1+1', 2),
        ('=', '1.1+1', 2.1),
    ],
)
def test_calcular(text, expressao, resultado_esperado):
    assert calcular(text, expressao) == resultado_esperado


@pytest.mark.parametrize(
    "text,expressao",
    [
        ('X', None),
        (1, ''),
        ('', ''),
    ],
)
def test_erro_calcular(text, expressao):
    with pytest.raises(Exception):
        assert calcular(text, expressao)


@pytest.mark.parametrize(
    "valor_1,operacao,valor_2,resultado_esperado",
    [
        ('1', '*', '2', 2),
        ('4', '/', '2', 2),
        ('1', '+', '1', 2),
        ('3', '-', '1', 2),
    ],
)
def test_identificar_operacao(valor_1, operacao, valor_2, resultado_esperado):
    assert identificar_operacao(valor_1, operacao, valor_2) == resultado_esperado


@pytest.mark.parametrize(
    "valor_1,operacao,valor_2",
    [
        ('1', '#', '2'),
        ('4', 1, '2'),
        ('1', None, '1'),
        ('3', False, '1'),
    ],
)
def test_erro_identificar_operacao(valor_1, operacao, valor_2):
    with pytest.raises(Exception):
        assert identificar_operacao(valor_1, operacao, valor_2)

from .estruturas_python import Testes

def test_aprovacao():
    assert Testes().verifica_aprovacao_aluno(nota=10) == "Reprovado!"
    assert Testes().verifica_aprovacao_aluno(nota=65) == "Recuperação!"
    assert Testes().verifica_aprovacao_aluno(nota=90) == "Aprovado!"


def test_saudacao():
    assert Testes().saudacao(nome="Teste") == "Olá, Teste!"
    
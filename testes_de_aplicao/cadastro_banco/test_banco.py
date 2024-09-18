import pytest
from sqlite_banco import Banco


@pytest.fixture
def banco():
    import os

    DB_NAME_TEST = 'teste.db'
    banco = Banco(nome_banco=DB_NAME_TEST)
    yield banco
    os.remove(DB_NAME_TEST)
    return banco

@pytest.fixture
def limpar_banco(banco):
    banco._executa_database(sql=f'DELETE FROM {banco.tabela}')


def test_verifica_tabela_criada(banco):
    resultado = banco._busca_database(sql=f"""
            SELECT name FROM sqlite_master 
            WHERE type='table' AND name='{banco.tabela}'
        """,
        one=True
    )
    assert resultado[0] == banco.tabela

def test_insere_registro(banco, limpar_banco):
    nome = "teste"
    cpf = "cpf"
    erro = banco.inserir_registro(
        nome=nome, email="teste", cpf=cpf, senha="teste"
    )
    assert not erro

def test_busca_registro_inserido(banco, limpar_banco):
    nome = "joao da silva"
    email = "email@email.com"
    cpf = "12312312345"
    senha = "senha"
    erro = banco.inserir_registro(
        nome=nome, email=email, cpf=cpf, senha=senha
    )
    assert not erro
    cadastro = banco.buscar_cadastro_cpf(cpf=cpf)
    assert cadastro[1] == nome
    assert cadastro[2] == email
    assert cadastro[3] == cpf
    assert cadastro[4] == senha

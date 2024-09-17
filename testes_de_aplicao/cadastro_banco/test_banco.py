import pytest
from sqlite_banco import Banco


@pytest.fixture
def banco():
    return Banco(nome_banco='teste.db')

@pytest.fixture
def limpar_banco(banco):
    banco._conectar()
    banco.cursor.execute(f'DELETE FROM {banco.tabela}')
    banco.conn.commit()
    banco.conn.close()


def test_verifica_tabela_criada(banco):
    banco._conectar()
    banco.cursor.execute(
        f"""
            SELECT name FROM sqlite_master 
            WHERE type='table' AND name='{banco.tabela}'
        """
    )
    assert banco.cursor.fetchone()[0] == banco.tabela
    banco.conn.close()

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

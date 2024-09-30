import pytest
from sqlite_banco import Banco


@pytest.fixture
def banco():
    import os

    DB_NAME_TEST = 'teste.db'
    banco = Banco(nome_banco=DB_NAME_TEST)
    # comando yeld vai ter o papel do return, mas vai esperar terminar o processo que utiliza a variavel banco
    yield banco
    # assim que terminar de usar o banco, vai executar a proxima linha para remover arquivo do banco sqlite
    os.remove(DB_NAME_TEST)


@pytest.fixture
def limpar_banco(banco):
    banco._executa_database(sql=f'DELETE FROM {banco.tabela}')


# testes de unidade de banco 
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
    email = "email@email.com"
    cpf = "cpf"
    senha = "senha"
    erro = banco.inserir_registro(nome=nome, email=email, cpf=cpf, senha=senha)
    assert not erro


# testes de componente
def test_busca_registro_inserido(banco, limpar_banco):
    nome = "nome"
    email = "email"
    cpf = "cpf"
    senha = "senha"
    erro = banco.inserir_registro(
        nome=nome, email=email, cpf=cpf, senha=senha
    )
    assert not erro
    # busca por cpf
    cadastro = banco.buscar_cadastro_cpf(cpf=cpf)
    # busca por identificador
    cadastro_id = banco.buscar_cadastro(id=cadastro[0])
    # busca por email
    cadastro_email = banco.buscar_cadastro_email(email=email)
    assert cadastro_id[1] == cadastro_email[1] == cadastro[1] == nome
    assert cadastro_id[2] == cadastro_email[2] == cadastro[2] == email
    assert cadastro_id[3] == cadastro_email[3] == cadastro[3] == cpf
    assert cadastro_id[4] == cadastro_email[4] == cadastro[4] == senha

def test_busca_login(banco, limpar_banco):
    nome = "joao da silva"
    email = "email@email.com"
    cpf = "12312312345"
    senha = "senha"
    erro = banco.inserir_registro(
        nome=nome, email=email, cpf=cpf, senha=senha
    )
    assert not erro
    # busca por email e senha
    cadastro = banco.buscar_login(email=email, senha=senha)
    assert cadastro[1] == nome
    assert cadastro[2] == email
    assert cadastro[3] == cpf
    assert cadastro[4] == senha


def test_busca_todos_dados(banco, limpar_banco):
    cadastros = []
    for indice in range(0, 10):
        nome = f"nome cadastro {indice}"
        email = f"email{indice}@email.com"
        cpf = f"0000000000{indice}"
        senha = f"senha{indice}"
        erro = banco.inserir_registro(nome=nome, email=email, cpf=cpf, senha=senha)
        cadastros.append([indice+1, nome, email, cpf, senha])
        assert not erro
    cadastros_banco = banco.buscar_todos_os_cadastros()
    assert len(cadastros_banco) == len(cadastros)
    assert list(cadastros[0]) == list(cadastros_banco[0])


def test_banco_atualiza_cadastro(banco, limpar_banco):
    nome = "joao da silva"
    email = "email@email.com"
    cpf = "12312312345"
    senha = "senha"
    nome_alterado = "josé teste"
    senha_alterada = "alterada"
    erro = banco.inserir_registro(nome=nome, email=email, cpf=cpf, senha=senha)
    assert not erro
    cadastro = banco.buscar_cadastro_cpf(cpf=cpf)
    assert cadastro[1] == nome
    assert cadastro[4] == senha
    erro = banco.atualizar_registro(
        id=cadastro[0], nome=nome_alterado, senha=senha_alterada)
    cadastro_alterado = banco.buscar_cadastro_cpf(cpf=cpf)
    assert cadastro_alterado[1] == nome_alterado
    assert cadastro_alterado[4] == senha_alterada

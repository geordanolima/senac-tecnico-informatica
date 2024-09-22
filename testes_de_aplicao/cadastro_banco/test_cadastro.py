import pytest

from cadastro import Pessoa, Cadastro
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
def cadastro(banco) -> Cadastro:
    return Cadastro(banco=banco)


@pytest.fixture
def insere_cadastro(cadastro):
    pessoa = Pessoa(nome="nome teste", email="email@teste.com", cpf="123454678901", senha="Teste!23")
    cadastro.cadastrar(pessoa=pessoa, confirma_senha="Teste!23")


# testes de unidade
@pytest.mark.parametrize(
    "nome,resultado_esperado", [
        ("joão da silva", None),
        ("Maria de Lurdes e Pereira", None),
        ("  nome com espaço antes e depois  ", None),
        (
            "nome com mais de 100 caracteres nome com mais de 100 caracteres nome com mais de 100 caracteres nome com",
            "o nome precisa ter até 100 caracters"
        ),
        ("nomesemespaco", "preencha o sobrenome também"),
        ("joao a silva", "o nome precisa ter ao menos 2 caracteres"),
        ("joão da aaaaaaaaa", "não é permitido nomes com todos os caracteres iguais")
    ]
)
def test_nome(cadastro, nome, resultado_esperado):
    assert cadastro._valida_nome(nome=nome) == resultado_esperado


@pytest.mark.parametrize(
    "email,resultado_esperado", 
    [
        ("email@email.com", None),
        ("email@teste.edu.br", None),
        ("emailcommaisde50caracteresemailcommaisde50caracteres", "o email pode ter somente 50 caracteres"),
        ("emailsemarroba.com.br", "email precisa ter @"),
        ("emailcom@massemponto", "email precisa ter . após o @"),
        ("emailcom@ecom.terminadoem.", "email não pode terminar em ."),
        ("email@.com", "não pode ter . logo após o @")
    ]
)
def test_email(cadastro, email, resultado_esperado):
    assert cadastro._valida_email(email=email) == resultado_esperado


def test_email_2(cadastro):
    assert cadastro._valida_email(email="email@email.com") == None
    assert cadastro._valida_email(email="email@teste.edu.br") == None
    assert cadastro._valida_email(
        email="emailcommaisde50caracteresemailcommaisde50caracteres") == "o email pode ter somente 50 caracteres"
    assert cadastro._valida_email(email="emailsemarroba.com.br") == "email precisa ter @"
    assert cadastro._valida_email(email="emailcom@massemponto") == "email precisa ter . após o @"
    assert cadastro._valida_email(email="emailcom@ecom.terminadoem.") == "email não pode terminar em ."
    assert cadastro._valida_email(email="email@.com") == "não pode ter . logo após o @"



@pytest.mark.parametrize(
    "cpf,resultado_esperado", 
    [
        ("997.251.290-83", None),
        ("76739421005", None),
        ("111111111111111", "CPF inválido"),
        ("000111", "CPF inválido"),
        ("teste", "CPF inválido"),
        ("0001++11", "CPF inválido"),
        ("00011__221", "CPF inválido"),
    ]
)
def test_cpf(cadastro, cpf, resultado_esperado):
    assert cadastro._valida_cpf(cpf=cpf) == resultado_esperado


@pytest.mark.parametrize(
    "senha,resultado_esperado",
    [
        ("Teste@123456", None),
        ("1testedeerro", "é necessário possuir caracter especial"),
        ("@@@@@@@@@@@@", "é necessário possuir valores numericos"),
        ("c1rt@", "a senha deve ter entre 8 e 16 caracteres"),
        ("esta_senh@_é_bem_long4", "a senha deve ter entre 8 e 16 caracteres")
    ]
)
def test_senha(cadastro, senha, resultado_esperado):
    assert cadastro._valida_senha(senha=senha) == resultado_esperado


# testes de componente
@pytest.mark.parametrize(
    "pessoa,conf_senha,resultado_esperado",
    [
        (Pessoa(nome="nome teste", email="email@email.com", cpf="76739421005", senha="Teste@1234"), "Teste@1234", None),
        (Pessoa(nome="", email="email", cpf="123", senha="senha"), "", "Preencha todos os campos"),
        (Pessoa(nome="nome", email="email", cpf="123", senha="senha"), "", "preencha o sobrenome também"),
        (Pessoa(nome="nome teste", email="email", cpf="123", senha="senha"), "", "email precisa ter @"),
        (Pessoa(nome="nome teste", email="email@email.com", cpf="123", senha="senha"), "", "CPF inválido"),
        (
            Pessoa(nome="nome teste", email="email@email.com", cpf="76739421005", senha="Teste"),
            "",
            "é necessário possuir caracter especial"
        ),
        (
            Pessoa(nome="nome teste", email="email@email.com", cpf="76739421005", senha="Teste@1234"),
            "",
            "As senhas não coincidem!"
        ),
        
    ]
)
def test_validacao(cadastro, pessoa, conf_senha, resultado_esperado):
    assert cadastro.validacao(pessoa=pessoa, confirma_senha=conf_senha) == resultado_esperado


# testes de integração
@pytest.mark.parametrize(
    "pessoa,conf_senha,resultado_esperado",
    [
        (
            Pessoa(nome="nome teste", email="email@email.com", cpf="76739421005", senha="Teste@1234"),
            "Teste@1234",
            (True, 'cadastrado no id: 1')
        ),
        (Pessoa(nome="", email="email", cpf="123", senha="senha"), "", (False, "Preencha todos os campos")),
        (Pessoa(nome="nome", email="email", cpf="123", senha="senha"), "", (False, "preencha o sobrenome também")),
        (Pessoa(nome="nome teste", email="email", cpf="123", senha="senha"), "", (False, "email precisa ter @")),
        (Pessoa(nome="nome teste", email="email@email.com", cpf="123", senha="senha"), "", (False, "CPF inválido")),
        (
            Pessoa(nome="nome teste", email="email@email.com", cpf="76739421005", senha="Teste"),
            "",
            (False, "é necessário possuir caracter especial")
        ),
        (
            Pessoa(nome="nome teste", email="email@email.com", cpf="76739421005", senha="Teste@1234"),
            "",
            (False, "As senhas não coincidem!")
        ),
    ]
)
def test_cadastrar(cadastro, pessoa, conf_senha, resultado_esperado):
    assert cadastro.cadastrar(pessoa=pessoa, confirma_senha=conf_senha) == resultado_esperado
    if resultado_esperado[0]:
        usuario_cadastrado = cadastro.buscar_cpf(cpf=pessoa.cpf)
        assert usuario_cadastrado.nome == pessoa.nome
        assert usuario_cadastrado.email == pessoa.email
        assert usuario_cadastrado.cpf == pessoa.cpf
        assert usuario_cadastrado.senha == pessoa.senha


@pytest.mark.parametrize(
    "pessoa_alt,resultado_esperado",
    [
        (
            Pessoa(id=1, nome="novo nome", email="", cpf="", senha="Teste!23"),
            (True, "Atualizado com sucesso!"),
        ),
        (
            Pessoa(id=1, nome="novo nome", email="", cpf="", senha="NovaSenha!23"),
            (True, "Atualizado com sucesso!"),
        ),
        (
            Pessoa(id=1, nome="nome_errado", email="", cpf="", senha="Teste!23"),
            (False, "preencha o sobrenome também"),
        ),
        (
            Pessoa(id=1, nome="novo nome", email="", cpf="", senha="senhasemnumeros"),
            (False, "é necessário possuir caracter especial"),
        ),
    ]
)
def test_alterar_cadastro(cadastro, insere_cadastro, pessoa_alt, resultado_esperado):
    resultado = cadastro.atualizar_cadastro(id=pessoa_alt.id, nome=pessoa_alt.nome, senha=pessoa_alt.senha)
    assert resultado == resultado_esperado
    
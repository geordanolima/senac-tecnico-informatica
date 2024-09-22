import os
from datetime import datetime
from cadastro import Cadastro, Pessoa
from sqlite_banco import Banco


os.remove('teste_desenpenho.db')
cadastro = Cadastro(banco=Banco(nome_banco='teste_desenpenho.db'))

quantidade = 10000

inicio = datetime.now()
senha = "Senha@123"
pessoa = Pessoa(nome="nome teste", email="", cpf="", senha=senha)

for indice in range(0, quantidade):
    pessoa.email = f"email{indice}@teste.com"
    pessoa.cpf = str(indice + 1).zfill(11)
    sucesso, mensagem = cadastro.cadastrar(pessoa=pessoa, confirma_senha=senha)
    assert sucesso
final = datetime.now()
print(f"[INSERSÃO] Tempo para inserir {quantidade} registros = {final - inicio}")
inicio = datetime.now()
todos_cadastros = cadastro.banco.buscar_todos_os_cadastros()
assert len(todos_cadastros) == quantidade
final = datetime.now()
print(f"[CONSULTA] Tempo para consultart {quantidade} registros = {final - inicio}")
os.remove('teste_desenpenho.db')

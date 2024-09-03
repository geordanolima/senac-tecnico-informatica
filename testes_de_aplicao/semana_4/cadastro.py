import json

class Pessoa():
    nome: str
    email:str
    cpf: str
    senha: str

    def __init__(self, nome, email, cpf, senha) -> None:
        self.nome = nome
        self.email = email
        self.cpf = cpf
        self.senha = senha


class Cadastro:
    def cadastrar(self, pessoa: Pessoa, confirma_senha: str) -> list[bool, str]:
        dados_invalidados = self.validacao(pessoa, confirma_senha)
        if dados_invalidados:
            return False, dados_invalidados
        self._salvar(obj=pessoa.__dict__)
        return True, pessoa.__dict__
    
    def validacao(self, pessoa: Pessoa, confirma_senha: str):
        if not (pessoa.nome and pessoa.email and pessoa.cpf and pessoa.senha):
            return "Preencha todos os campos"
        _nome = self._valida_nome(pessoa.nome)
        if _nome:
            return _nome
        _email = self._valida_email(pessoa.email)
        if _email:
            return _email
        _cpf = self._valida_cpf(pessoa.cpf)
        if _cpf:
            return _cpf
        if pessoa.senha != confirma_senha:
            return "As senhas não coincidem!"
    
    def _valida_nome(self, nome: str):
        sobrenomes_um_caracter = ['e']
        nomes = nome.strip().split(' ')
        if len(nomes) <= 1:
            return "preencha o sobrenome também"
        for nome in nomes:
            if len(nome) < 2 and nome not in sobrenomes_um_caracter:
                return "verifique o nome digitado"
            if nome.count(nome[0]) == len(nome) and nome not in sobrenomes_um_caracter:
                return "não é permitido nomes com todos os caracteres iguais"
        return None

    def _valida_email(self, email: str):
        if email.find('@') < 3:
            return "email precisa ter @"
        if email.find('.') < email.find('@'):
            return "email precisa ter . após o @"
        return None
    
    def _valida_cpf(self, cpf: str):
        _cpf = cpf.replace('.', '').replace('-', '')
        try:
            int(_cpf)
            if len(_cpf) != 11:
                raise
            return None
        except Exception:
            return "CPF inválido"
    
    def _salvar(self, obj: dict):
        arquivo = open("dados.json", "a")
        json.dump(obj, arquivo)
        arquivo.write("\n")
        arquivo.close()

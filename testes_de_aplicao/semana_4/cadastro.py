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
        _senha = self._valida_senha(senha=pessoa.senha)
        if _senha:
            return _senha
        if pessoa.senha != confirma_senha:
            return "As senhas não coincidem!"
    
    def _valida_nome(self, nome: str):
        sobrenomes_um_caracter = ['e']
        nomes = nome.strip().split(' ')
        if len(nome) >= 100:
            return "o nome precisa ter até 100 caracters"
        if len(nomes) <= 1:
            return "preencha o sobrenome também"
        for nome in nomes:
            if len(nome) < 2 and nome not in sobrenomes_um_caracter:
                return "o nome precisa ter ao menos 2 caracteres"
            if nome.count(nome[0]) == len(nome) and nome not in sobrenomes_um_caracter:
                return "não é permitido nomes com todos os caracteres iguais"
        return None

    def _valida_email(self, email: str):
        if len(email) >= 50:
            return "o email pode ter somente 50 caracteres"
        if email.find('@') < 3:
            return "email precisa ter @"
        if email.find('.') < email.find('@'):
            return "email precisa ter . após o @"
        if email[-1] == '.':
            return "email não pode terminar em ."
        if email[email.find("@")+1] == ".":
            return "não pode ter . logo após o @"
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

    def _valida_senha(self, senha: str):
        especiais = ["!","@","#","$","%","&","*","(",")","-","_","+","=",".",",","\\","|","'",'"']
        count = 0
        for char in especiais:
            if senha.find(char) >= 0:
                count = 1
        if not count:
            return "é necessário possuir caracter especial"
        count = 0
        for num in range(0, 10):
            if senha.find(str(num)) >= 0:
                count = 1
        if not count:
            return "é necessário possuir valores numericos"
        if len(senha) < 8 or len(senha) > 16:
            return "a senha deve ter entre 8 e 16 caracteres"
        return None
        
    def _salvar(self, obj: dict):
        arquivo = open("dados.json", "a")
        json.dump(obj, arquivo)
        arquivo.write("\n")
        arquivo.close()

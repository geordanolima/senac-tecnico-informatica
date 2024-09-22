import json
from sqlite_banco import Banco


class Pessoa():
    id: int
    nome: str
    email:str
    cpf: str
    senha: str

    def __init__(self, nome, email, cpf, senha, id: int =0) -> None:
        self.id = id
        self.nome = nome
        self.email = email
        self.cpf = cpf
        self.senha = senha

    def dict(self):
        return self.__dict__


class Cadastro:
    def __init__(self, banco: Banco):
        self.banco = banco
    
    def cadastrar(self, pessoa: Pessoa, confirma_senha: str) -> list[bool, str]:
        dados_invalidados = self.validacao(pessoa, confirma_senha)
        if dados_invalidados:
            return False, dados_invalidados
        try:
            resultado = self._salvar(pessoa=pessoa)
            return True, resultado
        except Exception as erro:
            return False, erro

    def atualizar_cadastro(self, id, nome, senha):
        _nome = self._valida_nome(nome=nome)
        if _nome:
            return False, _nome
        _senha = self._valida_senha(senha=senha)
        if _senha:
            return False, _senha
        mensagem = self.banco.atualizar_registro(id=id, nome=nome, senha=senha)
        if mensagem:
            return False, mensagem
        return True, "Atualizado com sucesso!"

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
        _senha = self._valida_senha(pessoa.senha)
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
        if email.rfind('.') < email.find('@'):
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
        
    def _salvar(self, pessoa: Pessoa):
        if self.banco:
            erro = self.banco.inserir_registro(
                nome=pessoa.nome,
                email=pessoa.email,
                cpf=pessoa.cpf,
                senha=pessoa.senha,
            )
            if erro:
                raise erro
            return f"cadastrado no id: {self.buscar_cpf(cpf=pessoa.cpf).id}"
        else:
            return "Erro ao salvar"
    
    def buscar(self, id: str):
        if id:
            dado = self.banco.buscar_cadastro(id=id)
            if dado:
                return Pessoa(id=dado[0], nome=dado[1], email=dado[2], cpf=dado[3], senha=dado[4])
            return f'Não há cadastro com id {id}'
        return 'Id não informado para busca'
    
    def buscar_cpf(self, cpf: str):
        if cpf:
            dado = self.banco.buscar_cadastro_cpf(cpf=cpf)
            if dado:
                return Pessoa(id=dado[0], nome=dado[1], email=dado[2], cpf=dado[3], senha=dado[4])
            return f'Não há cadastro com cpf {cpf}'
        return 'cpf não informado para busca'

    def backup(self):
        dados_backup = []
        lista = self.banco.buscar_todos_os_cadastros()
        for item in lista:
            dados_backup.append(Pessoa(id=item[0], nome=item[1], email=item[2], cpf=item[3], senha=item[4]).dict())
        with open('backup.json', 'a') as arquivo:
            json.dump(dados_backup, arquivo, indent=4)
        return 'backup realizado com sucesso'

    def login(self, email, senha):
        usuario = self.banco.buscar_login(email=email, senha=senha)
        if usuario:
            return "login realizado com sucesso"
        return "erro ao realizar login"
        
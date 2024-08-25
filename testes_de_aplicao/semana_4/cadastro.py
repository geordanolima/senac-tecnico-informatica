import json


class Cadastro:
    def cadastrar(self, nome: str, email: str, cpf: str, senha: str, confirma_senha: str) -> list[bool, str]:
        if not (nome and email and cpf and senha):
            return False, "Preencha todos os campos"
        if senha != confirma_senha:
            return False, "As senhas não coincidem!"
        dados = {
            "nome": nome,
            "email": email,
            "cpf": cpf,
            "senha": senha
        }
        self._salvar(obj=dados)
        return True, dados
    
    def _salvar(self, obj: dict):
        arquivo = open("dados.json", "a")
        json.dump(obj, arquivo)
        arquivo.write("\n")
        arquivo.close()
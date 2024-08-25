from pydantic import BaseModel


class CadastroRequest(BaseModel):
    nome: str
    email: str
    cpf: str
    senha: str
    confirma_senha: str
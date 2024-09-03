import json
from fastapi import FastAPI, Response, status

from .cadastro_request import CadastroRequest
from .cadastro import Cadastro
from .calculadora import calcular

app = FastAPI()


@app.get('/calcular/{expressao}')
def get_calcular(expressao):
    resultado = calcular(expression=expressao)
    if resultado == "Erro":
        return Response(
            json.dumps({'Erro': f'Não foi possível calcular a expressão: {expressao}'}),
            status_code=status.HTTP_400_BAD_REQUEST,
            headers={'content-type': 'application/json'},
        )
    return Response(json.dumps({'resultado': resultado}), headers={'content-type': 'application/json'})


@app.post('/cadastro')
def post_cadastro(body: CadastroRequest):
    sucesso, resultado = Cadastro().cadastrar(
        nome=body.nome, email=body.email, cpf=body.cpf, senha=body.senha, confirma_senha=body.confirma_senha
    )
    if not sucesso:
        return Response(
            json.dumps({'Erro': resultado}),
            status_code=status.HTTP_400_BAD_REQUEST,
            headers={'content-type': 'application/json'},
        )
    return Response(json.dumps(resultado), headers={'content-type': 'application/json'})

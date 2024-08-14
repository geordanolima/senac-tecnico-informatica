# senac-tecnico-informatica

### Criação de executáveis com python
> para gerar executável do código python
---
1. rode o comando ``pip install -r requirements.txt``
2. rode o comando: ``pyinstaller --onefile --path {.env/Lib/site-packages/} --noconsole --name "{nome_exe}" {arquivo.py}``
> Obs.: ``--path {.env/Lib/site-packages/}`` não é obrigatório, somente se houver bibliotecas externas

---

## Aula3: Testes de caixa preta
Solicitado que fossem identificados em um executável de uma calculadora erros.
> foram adicionados intencionalmente 2 erros ao executável:
> - ao somar um numero par com numero impar retorna uma subtração
> - ao multiplicar um numero impar com numero par retorna a divisao do numero par por 2

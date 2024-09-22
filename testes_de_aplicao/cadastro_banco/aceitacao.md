# Aceitação

## Requisitos

- A aplicação deve permitir o cadastro de um usuário que tenha as seguintes informações
    - nome
    - email
    - cpf
    - senha
- Deve permitir cadastrar apenas um usuário por email e senha
- Cada campo deve ter sua própria validação
    - o nome não deve aceitar cadastros com numeros, sem sobrenome e outras validações pertinentes
    - o email deve obrigatóriamente ter @ após .
    - o cpf deve ser composto apenas por numeros, e deve possuir exatamente 11 digitos
        - pode ser adicionado com mascara, mas esta deve ser removida antes de salvar
- Após salvar, deve retornar o identificador do cadastro
- Deve permitir a consulta do cadastro por identificador
- Deve permitir realizar um backup dos dados cadastrados
    - Esta ação deve gerar um arquivo ``backup.json`` com as informações dos registos armazenados no banco
- Deve permitir realizar o login
    - Para esta ação, deve ser informado o email e a senha
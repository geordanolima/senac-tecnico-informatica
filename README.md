# senac-tecnico-informatica

> para gerar executável do código python
---
1. rode o comando ``pip install -r requirements.txt``
2. rode o comando: ``pyinstaller --onefile --path {.env/Lib/site-packages/} --noconsole --name "{nome_exe}" {arquivo.py}``
> Obs.: ``--path {.env/Lib/site-packages/}`` não é obrigatório, somente se houver bibliotecas externas

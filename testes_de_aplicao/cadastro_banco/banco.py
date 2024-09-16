import sqlite3


conexao = sqlite3.connect('banco_teste.db')
cursor = conexao.cursor()

# cursor.execute(
#     """ 
#         CREATE TABLE tabela_teste (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             nome TEXT NOT NULL,
#             cpf TEXT UNIQUE NOT NULL,
#             campo TEXT NULL
#         )
#     """
# )

# conexao.commit()
# conexao.close()
cursor.execute(""" INSERT INTO tabela_teste (nome, cpf) VALUES ('teste', 'teste5')""")
# cursor.execute(""" UPDATE tabela_teste SET campo='campo preenchido' WHERE id = 2 """)
# cursor.execute(""" UPDATE tabela_teste SET campo='campo tambem' WHERE cpf = 'teste' """)
# cursor.execute(""" DELETE FROM tabela_teste WHERE id=1 """)
conexao.rollback()
cursor.execute(" SELECT * FROM tabela_teste where cpf = 'teste5'")
print(cursor.fetchone())
# conexao.commit()


conexao.close()
import sqlite3


class Banco:
    def __init__(self, nome_banco: str = 'cadastro.db') -> None:
        self.nome_banco = nome_banco
        self.tabela = 'usuario'
        self.cria_banco()

    def _executa_database(self, sql):
        # print(sql)
        try:
            self.conn = sqlite3.connect(self.nome_banco)
            self.cursor = self.conn.cursor()
            self.cursor.execute(sql)
            self.conn.commit()
            self.conn.close()
        except Exception as erro:
            self.conn.close()
            return erro.args

    def _busca_database(self, sql, one: bool = False):
        # print(sql)
        try:
            self.conn = sqlite3.connect(self.nome_banco)
            self.cursor = self.conn.cursor()
            self.cursor.execute(sql)
            if one:
                resultado = self.cursor.fetchone()
            else:
                resultado = self.cursor.fetchall()
            self.conn.close()
            return resultado
        except Exception as erro:
            self.conn.close()
            return erro.args

    def cria_banco(self):
        tabela_existente = self._busca_database(sql=f"SELECT name FROM sqlite_master WHERE type='table' AND name='{self.tabela}'")
        if not tabela_existente:
            # Criando a tabela 'usuarios'
            self._executa_database(sql=f'''
                CREATE TABLE {self.tabela} (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    email TEXT UNIQUE NOT NULL,
                    cpf TEXT UNIQUE NOT NULL,
                    senha TEXT NOT NULL
                )
            ''')

    def inserir_registro(self, nome, email, cpf, senha):
        return self._executa_database(
            sql=f'''
            INSERT INTO {self.tabela} (nome, email, cpf, senha) VALUES ('{nome}', '{email}', '{cpf}', '{senha}')
            '''.format(nome=nome, email=email, cpf=cpf, senha=senha)
        )

    def atualizar_registro(self, id, nome, senha):
        return self._executa_database(
            sql=f"UPDATE {self.tabela} SET nome='{nome}', senha='{senha}' WHERE id={id}"
        )

    def buscar_cadastro(self, id):
        return self._busca_database(
            sql='SELECT * FROM {tabela} where id = {id}'.format(tabela=self.tabela, id=id),
            one=True
        )

    def buscar_cadastro_cpf(self, cpf):
        return self._busca_database(
            sql="SELECT * FROM {tabela} where cpf = '{cpf}'".format(tabela=self.tabela, cpf=cpf),
            one=True
        )

    def buscar_todos_os_cadastros(self):
        return self._busca_database(
            sql=f'SELECT * FROM {self.tabela}'
        )

    def buscar_cadastro_email(self, email):
        return self._busca_database(
            sql=f"SELECT * FROM {self.tabela} WHERE email='{email}'",
            one=True
        )

    def buscar_login(self, email, senha):
        return self._busca_database(
            sql=f"SELECT * FROM {self.tabela} WHERE email='{email}' and senha = '{senha}'",
            one=True
        )

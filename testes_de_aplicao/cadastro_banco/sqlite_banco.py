import sqlite3


class Banco:
    def __init__(self, nome_banco: str = 'cadastro.db') -> None:
        self.nome_banco = nome_banco
        self.cria_banco()

    def _conectar(self):
        self.conn = sqlite3.connect(self.nome_banco)
        self.cursor = self.conn.cursor()

    def cria_banco(self):
        self._conectar()
        self.cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='usuarios'")
        if self.cursor.fetchone() is None:
            # Criando a tabela 'usuarios'
            self.cursor.execute('''
                CREATE TABLE usuarios (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    email TEXT UNIQUE NOT NULL,
                    cpf TEXT UNIQUE NOT NULL,
                    senha TEXT NOT NULL
                )
            ''')
            self.conn.commit()
        self.conn.close()

    def inserir_registro(self, nome, email, cpf, senha):
        try:
            self._conectar()
            # Inserindo um novo usuário
            sql = '''INSERT INTO usuarios (nome, email, cpf, senha) VALUES  ('{nome}', '{email}', '{cpf}', '{senha}')'''
            sql = sql.format(nome=nome, email=email, cpf=cpf, senha=senha)
            print(sql)
            self.cursor.execute(sql)
            self.conn.commit()
            self.conn.close()
        except Exception as erro:
            self.conn.close()
            return erro.args

    def buscar_cadastro(self, id):
        self._conectar()
        self.cursor.execute('SELECT * FROM usuarios where id = {id}'.format(id=id))
        results = self.cursor.fetchone()
        self.conn.close()
        return results

    def buscar_cadastro_cpf(self, cpf):
        self._conectar()
        self.cursor.execute('SELECT * FROM usuarios where cpf = {cpf}'.format(cpf=cpf))
        results = self.cursor.fetchone()
        self.conn.close()
        return results

    def buscar_todos_os_cadastros(self):
        self._conectar()
        self.cursor.execute('SELECT * FROM usuarios')
        results = self.cursor.fetchall()
        self.conn.close()
        return results

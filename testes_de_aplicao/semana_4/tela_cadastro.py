from cadastro import Pessoa
import tkinter as tk
from cadastro import Cadastro

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.cadastro = Cadastro()
        self.title("Cadastro")
        self.geometry("300x350")

        # Variáveis para armazenar os valores dos campos
        self.nome = tk.StringVar()
        self.email = tk.StringVar()
        self.cpf = tk.StringVar()
        self.senha = tk.StringVar()
        self.confirma_senha = tk.StringVar()

        # Labels e entradas
        tk.Label(self, text="Nome Completo:", width="200", anchor="w").pack(padx=10, pady=10)
        tk.Entry(self, textvariable=self.nome).pack(fill=tk.X, expand=True, padx=10)
        tk.Label(self, text="Email:", width="200", anchor="w").pack(padx=10)
        tk.Entry(self, textvariable=self.email).pack(fill=tk.X, expand=True, padx=10)
        tk.Label(self, text="CPF:", width="200", anchor="w").pack(padx=10)
        tk.Entry(self, textvariable=self.cpf).pack(fill=tk.X, expand=True, padx=10)
        tk.Label(self, text="Senha:", width="200", anchor="w").pack(padx=10)
        tk.Entry(self, textvariable=self.senha, show="*").pack(fill=tk.X, expand=True, padx=10)
        tk.Label(self, text="Confirmar Senha:", width="200", anchor="w").pack(padx=10)
        tk.Entry(self, textvariable=self.confirma_senha, show="*").pack(fill=tk.X, expand=True, padx=10)

        self.mensagem = tk.Label(self, text='')
        self.mensagem.pack()

        tk.Button(self, text="Limpar", command=self.limpar_campos).pack(side=tk.LEFT, padx=10, pady=10)
        tk.Button(self, text="Confirmar", command=self.confirmar).pack(side=tk.RIGHT, padx=10, pady=10)

    def limpar_campos(self):
        # Limpa os campos de entrada
        self.nome.set("")
        self.email.set("")
        self.cpf.set("")
        self.senha.set("")
        self.confirma_senha.set("")
        
    def confirmar(self):
        pessoa = Pessoa(
            nome=self.nome.get(),
            email=self.email.get(),
            cpf=self.cpf.get(),
            senha=self.senha.get(),
        )
        sucesso, mensagem = self.cadastro.cadastrar(
            pessoa=pessoa,            
            confirma_senha=self.confirma_senha.get(),
        )
        self.mensagem.config(text=mensagem)
        if sucesso:
            self.limpar_campos()


if __name__ == "__main__":
    app = Application()
    app.mainloop()
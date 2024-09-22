import tkinter as tk
from .cadastro import Cadastro, Pessoa
from .sqlite_banco import Banco


class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.cadastro = Cadastro(banco=Banco())
        self.title("Cadastro")
        self.geometry("300x400")

        # Variáveis para armazenar os valores dos campos
        self.id = tk.StringVar()
        self.nome = tk.StringVar()
        self.email = tk.StringVar()
        self.cpf = tk.StringVar()
        self.senha = tk.StringVar()
        self.confirma_senha = tk.StringVar()
        self.busca = False

        # Labels e entradas
        tk.Label(self, text="Id:", width="200", anchor="w").pack(padx=10, pady=10)
        self.eid = tk.Entry(self, textvariable=self.id)
        self.eid.pack(fill=tk.X, expand=True, padx=10)
        tk.Button(self, text="Buscar", command=self.buscar).pack(fill=tk.X, expand=True, padx=10, pady=10)

        tk.Label(self, text="Nome Completo:", width="200", anchor="w").pack(padx=10, pady=10)
        self.enome = tk.Entry(self, textvariable=self.nome)
        self.enome.pack(fill=tk.X, expand=True, padx=10)
        tk.Label(self, text="Email:", width="200", anchor="w").pack(padx=10)
        self.eemail = tk.Entry(self, textvariable=self.email)
        self.eemail.pack(fill=tk.X, expand=True, padx=10)
        tk.Label(self, text="CPF:", width="200", anchor="w").pack(padx=10)
        self.ecpf =tk.Entry(self, textvariable=self.cpf)
        self.ecpf.pack(fill=tk.X, expand=True, padx=10)
        tk.Label(self, text="Senha:", width="200", anchor="w").pack(padx=10)
        self.esenha = tk.Entry(self, textvariable=self.senha, show="*")
        self.esenha.pack(fill=tk.X, expand=True, padx=10)
        tk.Label(self, text="Confirmar Senha:", width="200", anchor="w").pack(padx=10)
        self.econfirmasenha = tk.Entry(self, textvariable=self.confirma_senha, show="*")
        self.econfirmasenha.pack(fill=tk.X, expand=True, padx=10)

        self.mensagem = tk.Label(self, text='')
        self.mensagem.pack()

        tk.Button(self, text="Limpar", command=self.limpar_campos).pack(side=tk.LEFT, padx=10, pady=10)
        tk.Button(self, text="Salvar", command=self.confirmar).pack(side=tk.RIGHT, padx=10, pady=10)
        tk.Button(self, text="Backup/json", command=self.backup).pack(fill=tk.X, expand=True, padx=10, pady=10)

    def limpar_campos(self):
        # Limpa os campos de entrada
        self.id.set("")
        self.nome.set("")
        self.email.set("")
        self.cpf.set("")
        self.senha.set("")
        self.confirma_senha.set("")
        self.eid.config(state="normal")
        self.enome.config(state="normal")
        self.eemail.config(state="normal")
        self.ecpf.config(state="normal")
        self.esenha.config(state="normal")
        self.econfirmasenha.config(state="normal")
        self.mensagem.config(text="")
    
    def buscar(self):
        resultado = self.cadastro.buscar(id=self.id.get())
        if type(resultado) == str:
            self.mensagem.config(text=resultado)
            return
        self.mensagem.config(text="")
        self.id.set(resultado.id)
        self.nome.set(resultado.nome)
        self.cpf.set(resultado.cpf)
        self.email.set(resultado.email)
        self.senha.set(resultado.senha)
        self.confirma_senha.set(resultado.senha)

        self.eid.config(state="readonly")
        self.enome.config(state="normal")
        self.eemail.config(state="readonly")
        self.ecpf.config(state="readonly")
        self.esenha.config(state="normal")
        self.econfirmasenha.config(state="normal")
    
    def confirmar(self):
        if self.eid["state"] == "normal":
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
        else:
            id = self.id.get()
            nome = self.nome.get()
            senha = self.senha.get()
            sucesso, mensagem = self.cadastro.atualizar_cadastro(id=id, nome=nome, senha=senha)
            self.mensagem.config(text=mensagem)
            if sucesso:
                self.limpar_campos()

    def backup(self):
        retorno = self.cadastro.backup()
        if retorno:
            self.mensagem.config(text=retorno)


if __name__ == "__main__":
    app = Application()
    app.mainloop()
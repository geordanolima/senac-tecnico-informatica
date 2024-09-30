
class Testes():
    def verifica_aprovacao_aluno(self, nota):
        # condicional if
        if self.verifica_aprovado(nota=nota):
            return "Aprovado!"
        # condicional elif
        elif nota >= 60:
            return "Recuperação!"
        # condicional else
        else:
            return "Reprovado!"

    def saudacao(self, nome):
        return f"Olá, {nome}!"

    def verifica_aprovado(nota):
        if nota >=70:
            return True
        return False


Testes().saudacao(nome="meu teste")
# # Loop for
# for i in range(5):
#     print(i)

# # Loop while
# contador = 0
# while contador < 5:
#     print(contador)
#     contador += 1


# # Funções
# def saudacao(nome):
#     print(f"Olá, {nome}!")

# saudacao("Maria")

# def calcular_area_retangulo(base, altura):
#     area = base * altura
#     return area

# resultado = calcular_area_retangulo(5, 3)
# print(resultado)


# # listas
# # Criando uma lista
# frutas = ["maçã", "banana", "laranja"]

# # Acessando elementos
# print(frutas[0])  # Imprime "maçã"

# # Adicionando um elemento
# frutas.append("uva")

# # Removendo um elemento
# frutas.remove("banana")

# print(frutas)


# # Criando uma tupla
# coordenadas = (10, 20)

# # Acessando elementos
# print(coordenadas[0])

# print(coordenadas)

# # Criando um dicionário

# aluno = {"nome": "João", "idade": 20, "notas": [8, 7, 9]}
# print(aluno.get("notas", [0, 0, 0])) 
# print(aluno.get("matricula", 0))
# aluno["idade"] = 21
# print(aluno["idade"])
# aluno["sobrenome"] = "Teste"
# print(aluno["sobrenome"])
# print(aluno)
# aluno.pop("sobrenome")
# print(aluno)

# # Criando uma classe
# class Cachorro:
#     def __init__(self, nome, raca):
#         # metodo de criação da classe
#         self.nome = nome
#         self.raca = raca

#     def latir(self):
#         # metodo de ação
#         self.__abanar_rabo()
#         print("Au au!")
    
#     def __abanar_rabo(self):
#         print('rabo abanando')

# # instanciando a classe
# meu_cachorro = Cachorro("Rex", "Labrador")
# # obterndo unformações da classe
# print(meu_cachorro.nome, meu_cachorro.raca)
# # executando ação da classe
# meu_cachorro.latir()


# # Exceções

# try:
#     resultado = 10 / 0
# except ZeroDivisionError:
#     print("Não é possível dividir por zero.")


# # escrever um novo arquivo
# arquivo = open("meu_arquivo.txt", "w")
# arquivo.write("Olá, mundo!")
# arquivo.close()

# # adicionar novas informações em um arquivo
# arquivo = open("meu_arquivo.txt", "r")
# arquivo.write("nova linha")
# arquivo.close()

# # ler informações de um arquivo
# arquivo = open("meu_arquivo.txt", "r")
# conteudo = arquivo.read()
# print(conteudo)
# arquivo.close()

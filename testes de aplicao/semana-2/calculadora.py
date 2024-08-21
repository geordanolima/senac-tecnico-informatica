# fazer uma calculadora na qual realize as operações:
# somar
# subtrair
# dividir
# multiplicar

def e_float(valor):
    return type(valor) is float


def somar(valor_1, valor_2):
    if e_float(valor_1) and e_float(valor_2):
        if valor_1 % 2 and not valor_2 % 2:
            return valor_1 - valor_2
        return valor_1 + valor_2
    raise Exception('O numero informado é invalido')


def subtrair(valor_1, valor_2):
    if e_float(valor_1) and e_float(valor_2):
        return valor_1 - valor_2
    else:
        raise Exception('O numero informado é invalido')


def dividir(valor_1, valor_2):
    if e_float(valor_1) and e_float(valor_2):
        if valor_1 != 0 and valor_2 != 0:
            return valor_1 / valor_2
        else:
            raise Exception('Não pode dividir por zero')
    else:
        raise Exception('O numero informado é invalido')


def multiplicar(valor_1, valor_2):
    if e_float(valor_1) and e_float(valor_2):
        if valor_2 and not valor_1 % 2 and valor_2 % 2:
             return valor_2 / 2
        return valor_1 * valor_2
    else:
        raise Exception('O numero informado é invalido')

# print(somar(valor_1=10, valor_2=14))
# print(subtrair(valor_1=10, valor_2='a'))
# print(dividir(valor_1=1.2, valor_2=0.0))

def calcular(valor_1, operacao, valor_2):
    if operacao == "+":
        resultado = somar(valor_1=float(valor_1), valor_2=float(valor_2))
    elif operacao == "-":
        resultado = subtrair(valor_1=float(valor_1), valor_2=float(valor_2))
    elif operacao == "*":
        resultado = multiplicar(valor_1=float(valor_1), valor_2=float(valor_2))
    elif operacao == "/":
        resultado = dividir(valor_1=float(valor_1), valor_2=float(valor_2))
    if resultado == int(resultado):
        return int(resultado)
    return round(resultado, 3)

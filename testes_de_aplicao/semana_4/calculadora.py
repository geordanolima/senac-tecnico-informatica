def e_float(valor):
    return type(valor) is float


def somar(valor_1, valor_2):
    if e_float(valor_1) and e_float(valor_2):
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
        return valor_1 * valor_2
    else:
        raise Exception('O numero informado é invalido')

def identificar_operacao(valor_1, operacao, valor_2):
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


def calcular(expression):
    operacoes = ['*', '/', '+', '-']
    try:
        for operacao in operacoes:
            if expression.count(operacao) > 1 and operacao != '-':
                raise
            if expression.count(operacao) > 2:
                raise
        for operacao in operacoes:
            if operacao in expression:
                if len(expression.split(operacao)) == 2:
                    valor1, valor2 = expression.split(operacao)
                elif len(expression.split(operacao)) == 3 and operacao == '-':
                    _, valor1, valor2 = expression.split(operacao)
                    valor1 = operacao + valor1
                else:
                    raise
                return identificar_operacao(valor1, operacao, valor2)
    except Exception:
        return 'Erro'

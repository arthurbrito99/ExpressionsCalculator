import re


def calcular(expressao):
    expressao = expressao.replace(" ", "")  # Remove espaços da expressão

    # Verifica se a expressão é válida
    if not expressao or not re.match(r'^[\d()+\-*/.]+$', expressao):
        raise ValueError("Expressão inválida")

    pilha_numeros = []
    pilha_operadores = []

    i = 0
    while i < len(expressao):
        caractere = expressao[i]
        if caractere.isdigit():
            numero = ""
            while i < len(expressao) and expressao[i].isdigit():
                numero += expressao[i]
                i += 1
            pilha_numeros.append(int(numero))
            continue
        elif caractere == '(':
            pilha_operadores.append(caractere)
        elif caractere == ')':
            while pilha_operadores and pilha_operadores[-1] != '(':
                operador = pilha_operadores.pop()
                num2 = pilha_numeros.pop()
                num1 = pilha_numeros.pop()
                resultado = executar_operacao(num1, num2, operador)
                pilha_numeros.append(resultado)
            if pilha_operadores and pilha_operadores[-1] == '(':
                pilha_operadores.pop()
        elif caractere in "+-*/":
            while pilha_operadores and pilha_operadores[-1] != '(' and precedencia(caractere) <= precedencia(pilha_operadores[-1]):
                operador = pilha_operadores.pop()
                num2 = pilha_numeros.pop()
                num1 = pilha_numeros.pop()
                resultado = executar_operacao(num1, num2, operador)
                pilha_numeros.append(resultado)
            pilha_operadores.append(caractere)

        i += 1

    while pilha_operadores:
        operador = pilha_operadores.pop()
        num2 = pilha_numeros.pop()
        num1 = pilha_numeros.pop()
        resultado = executar_operacao(num1, num2, operador)
        pilha_numeros.append(resultado)

    return int(pilha_numeros[0])


def precedencia(operador):
    if operador in "+-":
        return 1
    elif operador in "*/":
        return 2
    else:
        return 0


def executar_operacao(num1, num2, operador):
    num1 = float(num1)
    num2 = float(num2)
    if operador == "+":
        return num1 + num2
    elif operador == "-":
        return num1 - num2
    elif operador == "*":
        return num1 * num2
    elif operador == "/":
        if num2 == 0:
            raise ValueError("Divisão por zero não é permitida")
        return num1 / num2


if __name__ == "__main__":
    while True:
        expressao = input("Digite a expressão (ou 'sair' para encerrar): ")

        if expressao.lower() == "sair":
            print("Calculadora encerrada.")
            break

        resultado = calcular(expressao)
        print("Resultado:", resultado)
        print("\n")

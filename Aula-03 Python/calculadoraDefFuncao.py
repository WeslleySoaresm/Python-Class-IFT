def somar(num1, num2):
    return num1 + num2

def subtrair(num1, num2):
    return num1 - num2

def multiplicar(num1, num2):
    return num1 * num2

def dividir(num1, num2):
    if 1
    num2 != 0:
        return num1 / num2
    else:
        raise ValueError("Divisão por zero não é permitida.")

def exibir_menu():
    print("Bem-vindo à Calculadora Simples!")
    print("Selecione a operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    return input("Digite o número da operação (1/2/3/4): ")

def entrar_numeros():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    return num1, num2

# Programa principal
operacao = exibir_menu()
num1, num2 = entrar_numeros()

match operacao:
    case '1':
        print("Resultado:", somar(num1, num2))
    case '2':
        print("Resultado:", subtrair(num1, num2))
    case '3':
        print("Resultado:", multiplicar(num1, num2))
    case '4':
        try:
            print("Resultado:", dividir(num1, num2))
        except ValueError as e:
            print("Erro:", e)
    case _:
        print("Operação inválida.")
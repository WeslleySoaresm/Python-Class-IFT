# caculadora versão 2 usando macth
# Esta é uma calculadora simples que realiza operações básicas
# como adição, subtração, multiplicação e divisão.

print("Bem-vindo à Calculadora Simples!")
print("Selecione a operação:")
print("1. Adição")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")
operacao = input("Digite o número da operação (1/2/3/4): ") 
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))    


# Usando match-case para selecionar a operação
# Esta é uma nova abordagem que substitui os if-elif-else por match-case

match operacao:
    case '1':
        resultado = num1 + num2
        print(f"{num1} + {num2} = {resultado}")
    case '2':
        resultado = num1 - num2
        print(f"{num1} - {num2} = {resultado}")
    case '3':
        resultado = num1 * num2
        print(f"{num1} * {num2} = {resultado}")
    case '4':
        if num2 != 0:
            resultado = num1 / num2
            print(f"{num1} / {num2} = {resultado}")
        else:
            print("Erro: Divisão por zero não é permitida.")
    case _:
        print("Operação inválida. Por favor, selecione uma operação válida.")
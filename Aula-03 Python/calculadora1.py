# caculadora versão 1
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
if operacao == '1':
    resultado = num1 + num2
    print(f"{num1} + {num2} = {resultado}")
elif operacao == '2':
    resultado = num1 - num2
    print(f"{num1} - {num2} = {resultado}")
elif operacao == '3':
    resultado = num1 * num2
    print(f"{num1} * {num2} = {resultado}")
elif operacao == '4':
    if num2 != 0:
        resultado = num1 / num2
        print(f"{num1} / {num2} = {resultado}")
    else:
        print("Erro: Divisão por zero não é permitida.")
else:
    print("Operação inválida. Por favor, selecione uma operação válida.")   



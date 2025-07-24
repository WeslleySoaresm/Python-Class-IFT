import math


#calculadora
#<- solicita o primeiro número
#<- converte a entrada do usuário para um número inteiro
#<- int() converte a string de entrada para um inteiro
#<- input() lê a entrada do usuário
#<- int() é usado para converter a entrada do usuário em um número inteiro
op1 = int(input("Digite o primeiro número: "))
op2 = int(input("Digite o segundo número: ")) 


# operador de soma simples
result = op1 + op2
print(f"Resultado da soma: {result}") #operador de soma




operacao = input("Digite a operação (+, -, *, /): ")


if operacao == "+":
   resultado = op1 + op2
elif operacao == "-":
   resultado = op1 - op2
elif operacao == "*":
   resultado = op1 * op2
elif operacao == "/":
   resultado = op1 / op2
else:
   resultado = "Operação inválida"


print(f"Resultado: {resultado}")

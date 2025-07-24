#Comandos de Decisão
# Este exemplo demonstra o uso de comandos de decisão em Python

# Exemplo de uso de comandos de decisão
idade = int(input("Digite sua idade: "))
if idade < 18:
    print("Você é menor de idade.")
elif idade < 65:
    print("Você é adulto.")
else:
    print("Você é idoso.")

# Comando de Decisão em Python
# Solicita ao usuário que insira um número
numero = int(input("Digite um número: "))
# Verifica se o número é positivo, negativo ou zero
if numero > 0:
    print("O número é positivo.")
elif numero < 0:
    print("O número é negativo.")
else:
    print("O número é zero.")
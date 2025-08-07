#programa deve ler um numero inteiro e exibir se o numero é par ou ímpar
numero = int(input("Digite um número inteiro: "))
if numero % 2 == 0: #verifica se o resto da divisão por 2 é igual a zero se for 0 é par, se não é ímpar
    print("O número é par.")
else:
    print("O número é ímpar.")

# Fim do programa
# Exemplo de uso:
# Digite um número inteiro: 4
# O número é par.
# Digite um número inteiro: 5
# O número é ímpar. 

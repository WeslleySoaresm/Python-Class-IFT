# o operador in verifica se um elemento está presente em uma lista
lista = [1, 2, 3, 4, 5]
print(3 in lista)  # Saída: True
print(6 in lista)  # Saída: False

# o operador in verifica se uma substring está presente em uma string
texto = "Python é uma linguagem de programação."
print("Python" in texto)  # Saída: True
print("Java" in texto)  # Saída: False  

# o operador in verifica se uma chave está presente em um dicionário
dicionario = {"nome": "Weslley Sares", "idade": 30}
print("nome" in dicionario)  # Saída: True
print("endereco" in dicionario)  # Saída: False

# o operador in verifica se um elemento está presente em um conjunto
conjunto = {1, 2, 3, 4, 5}
print(3 in conjunto)  # Saída: True
print(6 in conjunto)  # Saída: False


# o operador in verifica se um caractere está presente em uma string
nome = "Weslley Sares"
print("W" in nome)  # Saída: True
print("x" in nome)  # Saída: False

# o operador in verifica se uma substring está presente em uma string
frase = "A vida é bela"
print("vida" in frase)  # Saída: True
print("tristeza" in frase)  # Saída: False

# o operador in verifica se um elemento está presente em uma tupla
tupla = (1, 2, 3, 4, 5)
print(3 in tupla)  # Saída: True
print(6 in tupla)  # Saída: False


#tamanhoh de uma string
nome = "Weslley Soares"
print(len(nome))  # Exibe o tamanho da string (número de caracteres)

# Verifica se uma substring está presente na string
if "Soares" in nome:
    print("A substring 'Soares' está presente no nome.")
else:
    print("A substring 'Soares' não está presente no nome.")

#pegando as letras de uma string
nome = "Weslley Sares"
print(nome[0])  # Exibe a primeira letra da string
print(nome[1])  # Exibe a segunda letra da string
print(nome[-1])  # Exibe a última letra da string
print(nome[0:5])  # Exibe os primeiros 5 caracteres da string
print(nome[6:])  # Exibe os caracteres a partir do índice 6 até

# o final
print(nome[:5])  # Exibe os primeiros 5 caracteres da string
print(nome[::2])  # Exibe os caracteres da string com passo 2 (ou seja, pula um caractere)
print(nome[::-1])  # Exibe a string invertida
print(len(nome))  # Exibe o comprimento da string

# Exibe o tipo da variável nome
print(type(nome))  # Exibe o tipo da variável nome

# Exibe o tipo da variável texto
texto = "Python é uma linguagem de programação."
print(type(texto))  # Exibe o tipo da variável texto

# determina o número de vezes que uma substring aparece na string
print(nome.count("e"))  # Conta quantas vezes a letra 'e' aparece na string
print(nome.count("Sares"))  # Conta quantas vezes a substring "Sares" aparece na string

nome = "weslley Sares"
print(nome)

# Exibe o tipo do nome
print(type(nome))  # Exibe o tipo do nome

# Exemplo de uso de strings em Python
texto = "Python é uma linguagem de programação."
print(texto)

# Exibe o tipo do texto
print(type(texto))  # Exibe o tipo do texto


nome =nome.upper()  # Converte o nome para letras maiúsculas
print(nome)  # Exibe o nome em letras maiúsculas            
nome = nome.lower()  # Converte o nome para letras minúsculas
print(nome)  # Exibe o nome em letras minúsculas
nome ="Weslley Sares"  # Define o nome novamente
nome = nome.swapcase()  # Converte o nome para maiúsculas e minúsculas alternadas
print(nome)  # Exibe o nome com maiúsculas e minúsculas alternadas      
nome = "Janaina"
nome = nome.capitalize()  # Converte a primeira letra do nome para maiúscula
print(nome)  # Exibe o nome com a primeira letra maiúscula
nome = "Weslley Sares"
nome = nome.title()  # Converte a primeira letra de cada palavra do nome para maiúscula
print(nome)  # Exibe o nome com a primeira letra de cada palavra maiúscula

# Exemplo de uso de f-strings
nome = "Weslley Sares"
idade = 30
mensagem = f"Meu nome é {nome} e tenho {idade} anos."
print(mensagem)  # Exibe a mensagem formatada       

# Exemplo de uso de formatação de strings
nome = "Weslley Sares"
idade = 30
mensagem = "Meu nome é {} e tenho {} anos.".format(nome, idade)
print(mensagem)  # Exibe a mensagem formatada       

# Exemplo de uso de formatação de strings com índices
nome = "Weslley Sares"
idade = 30
mensagem = "Meu nome é {0} e tenho {1} anos.".format(nome, idade)
print(mensagem)  # Exibe a mensagem formatada com índices   
# Exemplo de uso de formatação de strings com dicionário
dados = {"nome": "Weslley Sares", "idade": 30}
mensagem = "Meu nome é {nome} e tenho {idade} anos.".format(**dados)
print(mensagem)  # Exibe a mensagem formatada com dicionário        

#tudo sobre strings
nome = "Weslley Sares"
print(nome)  # Exibe o nome
print(nome[0])  # Exibe o primeiro caractere do nome
print(nome[1])  # Exibe o segundo caractere do nome
print(nome[-1])  # Exibe o último caractere do nome
print(nome[0:5])  # Exibe os primeiros 5 caracteres do nome
print(nome[6:])  # Exibe os caracteres a partir do índice 6 até o final
print(nome[:5])  # Exibe os primeiros 5 caracteres do nome
print(nome[::2])  # Exibe os caracteres do nome com passo 2 (ou seja, pula um caractere)
print(nome[::-1])  # Exibe o nome invertido
print(len(nome))  # Exibe o comprimento do nome
print(nome.count("e"))  # Conta quantas vezes a letra 'e' aparece no nome
print(nome.find("Sares"))  # Encontra a posição da substring "Sares" no nome
print(nome.index("Sares"))  # Encontra a posição da substring "Sares" no nome (lança erro se não encontrar)
print(nome.replace("Weslley", "João"))  # Substitui "Weslley" por "João" no nome
print(nome.split(" "))  # Divide o nome em uma lista de palavras
print(nome.split("e"))  # Divide o nome em uma lista de substrings usando 'e' como delimitador
print(nome.strip())  # Remove espaços em branco no início e no final do nome
print(nome.lstrip())  # Remove espaços em branco no início do nome
print(nome.rstrip())  # Remove espaços em branco no final do nome
print(nome.upper())  # Converte o nome para letras maiúsculas
print(nome.lower())  # Converte o nome para letras minúsculas
print(nome.title())  # Converte a primeira letra de cada palavra do nome para maiúscula
print(nome.capitalize())  # Converte a primeira letra do nome para maiúscula
print(nome.swapcase())  # Converte maiúsculas em minúsculas e vice-versa
print(nome.startswith("Weslley"))  # Verifica se o nome começa com "Weslley"
print(nome.endswith("Sares"))  # Verifica se o nome termina com "Sares"
print(nome.isalpha())  # Verifica se o nome contém apenas letras
print(nome.isdigit())  # Verifica se o nome contém apenas dígitos
print(nome.isalnum())  # Verifica se o nome contém apenas letras e números
print(nome.islower())  # Verifica se o nome está em letras minúsculas
print(nome.isupper())  # Verifica se o nome está em letras maiúsculas
print(nome.isspace())  # Verifica se o nome contém apenas espaços em branco
print(nome.isnumeric())  # Verifica se o nome contém apenas números
print(nome.isidentifier())  # Verifica se o nome é um identificador válido em Python
print(nome.join(["Olá", "Mundo"]))  # Junta a lista de strings com o nome como separador
print(nome.splitlines())  # Divide o nome em linhas (útil para strings multilinha)
print(nome.zfill(20))  # Preenche o nome com zeros até atingir o comprimento 20
print(nome.center(20))  # Centraliza o nome em um campo de largura 20
print(nome.ljust(20))  # Alinha o nome à esquerda em um campo de largura 20
print(nome.rjust(20))  # Alinha o nome à direita em um campo de largura 20
print(nome.partition("Sares"))  # Divide o nome em três partes: antes, a substring "Sares" e depois
print(nome.rpartition("Sares"))  # Divide o nome em três partes: antes, a substring "Sares" e depois, começando do final
print(nome.split("e",   1))  # Divide o nome em uma lista de substrings usando 'e' como delimitador, limitando a 1 divisão
print(nome.rsplit("e", 1))  # Divide o nome em uma lista de substrings usando 'e' como delimitador, começando do final e limitando a 1 divisão      

# Aula 00 - Introdução ao Python 
import math #<- importando a biblioteca math para usar funções matemáticas


# Imprimir na tela
print("Olá, mundo!") #-podemos usar aspas simples ou duplas




# Variáveis
MAX_VALOR_DO_ALUNO = 10 #<- variável constante MAIS NÃO EXISTE EM PYTHON<
#PYTHON não possui uma palavra-chave para declarar constantes, mas por convenção usamos letras maiúsculas
#NÃO É UMA CONSTANTE, MAS POR CONVENÇÃO USAMOS LETRAS MAIÚSCULAS
# A variável MAX_VALOR_DO_ALUNO é uma convenção para indicar que é uma constante
# Em Python, não há uma maneira de declarar uma constante como em outras linguagens.
#<- constante, por convenção, usamos letras maiúsculas
# PYTHON é uma linguagem de tipagem dinâmica, então não precisamos declarar o tipo da variável.
# Podemos atribuir valores de diferentes tipos a uma variável.
# Exemplo de variáveis de diferentes tipos
# string, inteiro, float, booleano
# Exemplo de variáveis


nome = "Maria" #string
idade = 25 #inteiro
altura = 1.70 #float
estudante = True #booleano


# operadores aritméticos
soma = 5 + 3 #<- soma
subtracao = 10 - 2 #<- subtração
multiplicacao = 4 * 2 #<- multiplicação
divisao = 8 / 2 #<- divisão
modulo = 10 % 3 #<- módulo (resto da divisão)  
exponenciacao = 2 ** 3 #<- exponenciação (2 elevado a 3)
# Imprimindo os resultados das operações
print(f"Soma: {soma}") #<- f-strings para formatação
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao}")
print(f"Módulo: {modulo}")
print(f"Exponenciação: {exponenciacao}")      


# usando a biblioteca math
raiz_quadrada = math.sqrt(16) #<- raiz quadrada de 16
print(f"Raiz quadrada de 16: {raiz_quadrada}") #<- imprimindo a raiz quadrada    




# Estrutura condicional
if idade >= 18:#<- comparação
   print(f"{nome} é maior de idade.")# f-strings para formatação
else:#<- se não
   print(f"{nome} é menor de idade.")


# Laço de repetição
for i in range(5):#<- loop de 0 a 4
   print(i)#<-- imprime o valor de i


# Função saudacao
# Definindo uma função que recebe um parâmetro e retorna uma saudação


def saudacao(nome): #<- definição da função
   return f"Olá, {nome}!" #volta com uma saudação formatada


print(saudacao("João")) #<- chamando a função com o nome "João"

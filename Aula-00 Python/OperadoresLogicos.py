#Operadores Lógicos
x = True
y = False
print(x and y) # False
print(x or y) # True
print(not x) # False
print(not y) # True

# Operadores Lógicos com Comparações
a = 10
b = 20
c = 30
print(a < b and b < c) # True           
print(a < b or b > c) # True
print(not (a > b)) # True

# Verificando se um número está dentro de um intervalo
numero = 15
print(numero > 10 and numero < 20) # True
print(numero < 10 or numero > 20) # False       

# Verificando se uma variável é do tipo correto
variavel = "Python"
print(isinstance(variavel, str) and variavel.startswith("P")) # True
print(isinstance(variavel, int) or isinstance(variavel, float)) # False     

# Verificando se uma lista contém elementos
lista = [1, 2, 3, 4, 5]
print(len(lista) > 0 and 3 in lista) # True
print(len(lista) == 0 or 6 in lista) # False        

# Verificando se uma string não está vazia
texto = "Hello"
print(texto != "" and "H" in texto) # True
print(texto == "" or "Z" in texto) # False  

# Verificando se uma variável é None
variavel_nula = None
print(variavel_nula is None and isinstance(variavel_nula, type(None))) # True
print(variavel_nula is not None or isinstance(variavel_nula, type(int))) # False

# Verificando se duas condições são verdadeiras
condicao1 = True
condicao2 = False
print(condicao1 and condicao2) # False
print(condicao1 or condicao2) # True

# Verificando se uma variável é do tipo correto e não é vazia                               
variavel = [1, 2, 3]
print(isinstance(variavel, list) and len(variavel) > 0) # True
print(isinstance(variavel, list) or len(variavel) == 0) # False

# Verificando se uma variável é do tipo correto e não é None
variavel = "Python"
print(isinstance(variavel, str) and variavel is not None) # True
print(isinstance(variavel, int) or variavel is None) # False                

# Verificando se uma variável é do tipo correto e não é vazia
variavel = "Hello"
print(isinstance(variavel, str) and variavel != "") # True
print(isinstance(variavel, str) or variavel == "") # False      

# Verificando se uma variável é do tipo correto e não é None
variavel = 42
print(isinstance(variavel, int) and variavel is not None) # True
print(isinstance(variavel, str) or variavel is None) # False        

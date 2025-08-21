# Lista de strings
nomes = ["Ana", "Bruno", "Carla"]

# Lista de números
numeros = [10, 20, 30, 40]

# Lista mista
pessoa = ["Rui", 42, True, 1.78]

# Lista vazia, para preencher depois
compras = []

# Criar uma lista a partir de um `range`
sequencia = list(range(5))  # Resultado: [0, 1, 2, 3, 4]

nomes = ["Ana", "Bruno", "Carla", "Daniel"]
# Índices:   0      1        2        3

print(nomes[0])   # Saída: Ana
print(nomes[2])   # Saída: Carla

# Indexação Negativa (para aceder a partir do fim)
print(nomes[-1])  # Saída: Daniel (o último item)
print(nomes[-2])  # Saída: Carla (o penúltimo item)

numeros = [0, 10, 20, 30, 40, 50, 60]

# Do índice 2 até ao 5 (o índice 5 NÃO é incluído)
print(numeros[2:5])   # Saída: [20, 30, 40]

# Do início até ao índice 3 (o 3 NÃO é incluído)
print(numeros[:3])    # Saída: [0, 10, 20]

# Do índice 4 até ao fim
print(numeros[4:])    # Saída: [40, 50, 60]

# A cada dois elementos (passo 2)
print(numeros[::2])   # Saída: [0, 20, 40, 60]

# Inverter uma lista (truque comum)
print(numeros[::-1])  # Saída: [60, 50, 40, 30, 20, 10, 0]



compras = ["Maçãs", "Pão"]
compras.append("Leite")      # ['Maçãs', 'Pão', 'Leite']
compras.insert(1, "Queijo")  # ['Maçãs', 'Queijo', 'Pão', 'Leite']
compras.extend(["Iogurte", "Cereais"]) # ['Maçãs', ..., 'Leite', 'Iogurte', 'Cereais']


letras = ['a', 'b', 'c', 'd', 'c']
letras.remove('c')         # ['a', 'b', 'd', 'c'] (só remove o primeiro 'c')

letra_removida = letras.pop(1) # Remove 'b' e o guarda na variável
print(letra_removida)      # Saída: b
print(letras)              # Saída: ['a', 'd', 'c']

del letras[0]              # ['d', 'c']

cores = ["vermelho", "verde", "azul"]
cores[1] = "amarelo"   # A lista agora é ['vermelho', 'amarelo', 'azul']


numeros = [3, 1, 4, 1, 5, 9, 2]

# Usando sorted() - preferível se quiser manter a original
nova_lista_ordenada = sorted(numeros)
print(f"Original: {numeros}")               # Saída: [3, 1, 4, 1, 5, 9, 2]
print(f"Nova ordenada: {nova_lista_ordenada}") # Saída: [1, 1, 2, 3, 4, 5, 9]

# Usando .sort() - modifica a lista
numeros.sort(reverse=True) # Ordena em ordem decrescente
print(f"Original modificada: {numeros}")    # Saída: [9, 5, 4, 3, 2, 1, 1]


nomes = ["Ana", "Bruno", "Carla", "Ana"]
print(nomes.count("Ana"))       # Saída: 2
print(nomes.index("Bruno"))     # Saída: 1

# Verificando a existência
if "Daniel" in nomes:
    print("Daniel está na lista.")
else:
    print("Daniel não está na lista.")


    matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Aceder ao elemento na linha 1, coluna 2 (o número 6)
print(matriz[1][2]) # Saída: 6



# Forma tradicional
quadrados_trad = []
for x in range(10):
    quadrados_trad.append(x**2)

# Com List Comprehension
quadrados_comp = [x**2 for x in range(10)]

print(quadrados_comp) # Saída: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


numeros = [1, 2, 3, 4, 5, 6, 7, 8]

# Com List Comprehension e condição
pares = [num for num in numeros if num % 2 == 0]

print(pares) # Saída: [2, 4, 6, 8]

for elem in numeros:
    print(elem)
print()
for elem in numeros:
    print(elem, end=" ")
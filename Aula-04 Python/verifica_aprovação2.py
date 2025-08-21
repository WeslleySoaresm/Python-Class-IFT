# Dados dos alunos (com a correção aplicada)
turma = [
    ["Gustavo", 6, 7], 
    ["Gui", 6, 7], 
    ["LP", 5, 6], 
    ["Bil", 4, 7], 
    ["João", 7, 6]
]

APROVAÇÃO = 6 

print("--- Boletim da Turma ---")

# 1. Percorrer cada 'aluno' na lista 'turma'
for aluno in turma:
    # 2. Extrair os dados de cada aluno para variáveis separadas
    nome = aluno[0]
    nota1 = aluno[1]
    nota2 = aluno[2]
    
    # 3. Calcular a média específica para este aluno
    media_aluno = (nota1 + nota2) / 2
    
    # 4. Verificar a condição (aprovado ou reprovado) e imprimir o resultado
    if media_aluno >= 6:
        print(f"✔️ Aluno: {nome:<10} | Média: {media_aluno:.1f} | Situação: Aprovado")
    else:
        print(f"❌ Aluno: {nome:<10} | Média: {media_aluno:.1f} | Situação: Reprovado")

print("--- Fim do Boletim ---")


#Esta segunda abordagem é muito útil quando você precisa de separar os dados em grupos antes de os apresentar.

# Listas para guardar os resultados
aprovados = []
reprovados = []

for aluno in turma:
    nome, nota1, nota2 = aluno
    media_aluno = (nota1 + nota2) / 2
    
    # Criar uma string de resultado para cada aluno
    resultado = f"Aluno: {nome:<10} | Média: {media_aluno:.1f}"
    
    if media_aluno >= 6:
        aprovados.append(resultado)
    else:
        reprovados.append(resultado)

# Agora, imprimir os resultados de forma organizada
print("--- ✅ Alunos Aprovados ---")
for aluno_aprovado in aprovados:
    print(aluno_aprovado)

print("\n--- ❌ Alunos Reprovados ---")
for aluno_reprovado in reprovados:
    print(aluno_reprovado)


#Fazendo calculadora com função def 

def exibir_aluno(aluno):
    print(aluno[0], aluno[1], aluno[2])


def calcular_media(nota1, nota2):
    media = (nota1 + nota2) / 2
    return media

def exibir_aprovação(media):
    if(media >= APROVAÇÃO):
     print("Aluno aprovado")
    else:
        print("Aluno em prova final")


for aluno in turma:
    exibir_aluno(aluno)
    media = calcular_media(aluno[1], aluno[2])
    print(media)
    exibir_aprovação(media)        




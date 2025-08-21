# 1. Importar a biblioteca
from tabulate import tabulate

# Dados dos alunos (com a correção aplicada)
turma = [
    ["Gustavo", 6, 7], 
    ["Gui", 6, 7], 
    ["LP", 5, 6], 
    ["Bil", 4, 7], 
    ["João", 7, 6]
]

# 2. Preparar as estruturas para a tabela
cabecalho = ["Nome", "Nota 1", "Nota 2", "Média", "Situação"]
dados_para_tabela = []

# 3. Processar os dados e PREENCHER a lista 'dados_para_tabela'
for aluno in turma:
    # Extrair os dados
    nome, nota1, nota2 = aluno
    
    # Calcular a média
    media_aluno = (nota1 + nota2) / 2
    
    # Determinar a situação
    if media_aluno >= 6:
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"
        
    # Adicionar a linha (já processada) à nossa lista de dados
    dados_para_tabela.append([nome, nota1, nota2, f"{media_aluno:.1f}", situacao])

# 4. Usar a função tabulate para criar a tabela e imprimi-la
print("\n--- Boletim da Turma (Formatado com Tabulate) ---")
tabela = tabulate(dados_para_tabela, headers=cabecalho)
print(tabela)




# Estilo "grid"
print("\n--- Estilo Grid ---")
print(tabulate(dados_para_tabela, headers=cabecalho, tablefmt="grid"))

# Estilo "fancy_grid"
print("\n--- Estilo Fancy Grid ---")
print(tabulate(dados_para_tabela, headers=cabecalho, tablefmt="fancy_grid"))

# Estilo "pipe" (ótimo para documentação Markdown)
print("\n--- Estilo Pipe (Markdown) ---")
print(tabulate(dados_para_tabela, headers=cabecalho, tablefmt="pipe"))
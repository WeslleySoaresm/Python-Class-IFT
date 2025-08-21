


APROVACAO = 6

def entrada_alunos():
    turma = []
    nome = input("Entre com o nome do aluno:")
    while (nome != ""):
        nota1 = float(input("Entre com a nota 1: "))
        nota2 = float(input("Entre com a nota 2: "))
        turma.append([nome, nota1, nota2])
    return turma


def exibir_aluno(aluno):
    print(aluno[0], aluno[1], aluno[2])


def calcular_media(nota1, nota2):
    media = (nota1 + nota2) / 2
    return media

def exibir_aprovação(media):
    if(media >= APROVACAO):
     print("Aluno aprovado")
    else:
        print("Aluno em prova final")

turma = entrada_alunos()
for aluno in turma:
    exibir_aluno(aluno)
    media = calcular_media(aluno[1], aluno[2])
    print(media)
    exibir_aprovação(media)        



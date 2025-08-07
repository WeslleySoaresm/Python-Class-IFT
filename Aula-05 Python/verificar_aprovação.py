# faça um programa que lea uma nome e duas notas (reais). as notas devem ser maiores ou iguais a zero 
# calcule a média do aluno e exiba o nome do aluno, as notas e a média.
#exiba se o aluno foi aprovado (média maior ou igual a 6) ou reprovado (média menor que 6).

nome = input("Digite o nome do aluno: ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

print("Nome do aluno:", nome)
print("Notas:", nota1, nota2)
print("Média:", media)

if media >= 6:
    print(f" O Aluno: {nome} foi aprovado.")
else:
    print(f" O Aluno: {nome} foi reprovado.")
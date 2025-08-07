# faça um programa que lea uma nome e duas notas (reais). as notas devem ser maiores ou iguais a zero 
# calcule a média do aluno e exiba o nome do aluno, as notas e a média.
#exiba se o aluno foi aprovado (média maior ou igual a 6) ou reprovado (média menor que 6).

nome = input("Digite o nome do aluno: ")
opcao_permitida = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # lista de notas permitidas


while True:
    nota1 = float(input("Digite a primeira nota: ")) # entrada da primeira nota
    nota2 = float(input("Digite a segunda nota: ")) # entrada da segunda nota
    media = (nota1 + nota2) / 2 # cálculo da média
   
    if nota1 not in opcao_permitida or nota2 not in opcao_permitida: # verifica se as notas estão na lista de opções permitidas
        print("Notas inválidas. As notas devem ser entre 0 e 10.") 
        continue # reinicia o loop se as notas forem inválidas
    else:
        if (nota1 < 0 or nota1 > 10 or nota2 < 0 or nota2 > 10):
         print("Notas inválidas. As notas devem ser entre 0 e 10.")
        elif media > 6:
         print(f" O Aluno: {nome} foi aprovado, suas notas foram: {nota1} e {nota2} com média: {media}.")
        else:
         print(f" O Aluno: {nome} foi reprovado, suas notas foram: {nota1} e {nota2} com média: {media}.")

    break
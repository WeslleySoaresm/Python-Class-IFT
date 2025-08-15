#somar os números digitafos pelo usuário até que o número seja igual 
# e calcule a média dos numeros 
cont = 0
soma = 0 
num = int(input("entre com um número: "))
while(num != 0):
    soma += num
    cont += 1
    num = int(input("entre com um numéro"))
if (cont > 0):
    print("Soma=", soma)
    media = soma / cont
    print("Média = ", media)
else:
    print("Nunhum dados")
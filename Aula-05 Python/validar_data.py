# Validação de data no formato dd/mm/aaaa, entrada pelo usuário

def is_bissexto(ano):
    # Verifica se o ano é bissexto
    if ano % 4 == 0:
        if ano % 100 == 0:
            if ano % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def validar_data(data):
    # Valida a data no formato dd/mm/aaaa
    try:
        dia, mes, ano = map(int, data.split('/'))
        if mes < 1 or mes > 12:
            return False
        if dia < 1:
            return False
        if mes == 2:
            if is_bissexto(ano): # Verifica se o ano é bissexto
                if dia > 29:
                    return False
            else:
                if dia > 28:
                    return False
        elif mes in [4, 6, 9, 11]:
            if dia > 30:
                return False
        else:
            if dia > 31:
                return False
        return True
    except ValueError:
        return False

# Loop até o ano ser bissexto
while True:
    data = input("Digite uma data no formato dd/mm/aaaa: ") # entrada de data
    print(f"Validando a data: {data}...\n")
    if validar_data(data):
        print(f"A data {data} é válida.")
        ano = int(data.split('/')[2]) # extraindo o ano da data
        print(f"Verificando se o ano {ano} é bissexto...\n")
        if is_bissexto(ano):
            print(f"O ano {ano} é bissexto.")
            break  # Sai do loop se for bissexto
        else:
            print(f"O ano {ano} não é bissexto.")
            print("Digite uma nova data com um ano bissexto.\n")
    else:
        print(f"A data {data} é inválida. Tente novamente.\n")
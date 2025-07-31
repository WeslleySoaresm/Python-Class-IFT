hora_minutos = "21:30"
hora = int(hora_minutos.split(":")[0])
print(hora)
minutos = int(hora_minutos.split(":")[1])
print(minutos)

# Exibe o tipo da hora e minutos
print(type(hora))  # Exibe o tipo da hora
print(type(minutos))  # Exibe o tipo dos minutos            


#hora em minutoshora_em_minutos = hora * 60 + minutos
print(f"A hora em minutos é: {hora * 60 + minutos}")
# Exibe o tipo da hora em minutos
print(type(hora * 60 + minutos))  # Exibe o tipo da hora em minutos 

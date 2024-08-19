#Desenvolva um programa em Python que peça ao usuário para inserir dois números decimais e calcule a diferença absoluta entre esses dois números. 
# Utilize a função nativa abs para garantir que o resultado seja sempre positivo e round para arredondar o resultado para duas casas decimais.

x, y = float(input("Digite o primeiro numero decimal: ")), float(input("Digite o segundo numero decimal: "))

dif = abs(x - y)

print(f"A diferença absoluta entre {x} e {y} é {round(dif, 2)}")


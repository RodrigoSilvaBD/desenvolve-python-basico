
def calcTri(a, b, c):
    return lad1tri+lad2tri+lad3tri
def calcCirc(a):
    return 2*3,14*raio
def calcQuad(a):
    return 2*lad1 + 2*lad2

print("1 - Calcular perímetro triângulo")
print("2 - Calcular perímetro círculo")
print("3 - Calcular perímetro retângulo")
print("4 - Sair")
cal = int(input("digite o numero da opção de calculo que voce deseja: "))


if cal == 1:
    lad1tri = int(input("Digite o lado 1 do triangulo: "))
    lad2tri = int(input("Digite o lado 2 do triangulo: "))
    lad3tri = int(input("Digite o lado 3 do triangulo: "))
    area_tri = calcTri(lad1tri, lad2tri, lad3tri) # não está fazendo o calculo
    print
elif cal == 2:
    raio = float(input("Digite o raio do circulo"))
    area_cir = calcCirc (raio)
elif cal == 3:
    lad1 = int(input("Digite o lado 1 do retangulo"))
    lad2 = int(input("Digite o lado 2 do retangulo"))
    area_qua = calcQuad(lad1, lad2)





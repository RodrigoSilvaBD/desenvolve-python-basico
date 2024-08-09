#Escreva um programa que leia os comprimentos dos 3 lados de um triângulo e diga se o triângulo é equilátero, isóceles ou escaleno. Regras:

    #Isóceles: Quaisquer dois lados com o mesmo comprimento
    #Equilátero: Os três lados tem o mesmo comprimento
    #Escaleno: Três lados de comprimento diferente

lado1, lado2, lado3 = float(input("Digite o comprimento do lado 1: ")), float(input("Digite o comprimento do lado 2: ")), float(input("DDigite o comprimento do lado 3: "))

if lado1 == lado2 and lado2 == lado3:
    print("Triângulo: Equilatero")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("Triângulo: Isóceles")
else:
    lado1 != lado2 or lado1 != lado3 or lado2 != lado3
    print("Triângulo: Escaleno")
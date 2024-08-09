#Escreva um programa que lê dois números e informa se a sua soma é par ou ímpar. 
# Critério: se o resto da divisão do número por 2 for 0, o número é par, caso contrário é ímpar. 
# Lembre-se do operador do python % que retorna o resto de uma divisão.

num1, num2 = int(input("Digite o primeiro numero: ")), int(input("Digite o segundo numero: "))
#num2 = int(input("Digite o segundo numero: "))

soma = num1 + num2
if soma % 2 == 0:
    print ("A soma dos numeros é par")
else:
    print("A soma dos numeros é impar")
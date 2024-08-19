#Escreva uma função em Python chamada soma_quadrados que recebe dois números como parâmetros e retorna a soma dos seus quadrados.
#No programa principal solicite ao usuário que insira dois números e utilize a função para exibir a soma dos quadrados.

def somaQuadrados(a, b):
    return a**2 + b**2

num1, num2 = float(input("Digite o primeiro numero: ")), float(input("Digite o segundo numero: "))
resultado = somaQuadrados(num1, num2)
print(resultado)
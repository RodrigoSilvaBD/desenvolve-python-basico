# Escreva um script em Python que solicita do usuário uma quantidade indefinida de números inteiros (pelo menos 4 valores), 
# os armazena em uma lista e, usando fatiamento de listas, imprima:

    #A lista original
    #Os 3 primeiros elementos
    #Os 2 últimos elementos
    #A lista invertida (do fim para o começo)
    #Os elementos de índice par (0, 2, 4 … )
    #Os elementos de índice ímpar (1, 3, 5, … )

numeros = []

while True:
    entrada = input("Digite um numero inteiro ou 'fim' para encerrar: ")
    if entrada == 'fim':
        break
    else: 
        entrada == int
        numeros.append(entrada)
if len(numeros) < 4:
    print ("Insira pelo menos 4 numeros.")

print("Lista original é:", numeros)
print("Os 3 primeiros elementos são:", numeros[:3])
print("Os 2 ultimos elementos são:", numeros[-2:])
print("A lista invertida é: ", numeros[::-1])
print("Os elementos de indice par, são: ", numeros[::2])
print("Os elementos de indice impar, são: ", numeros[1::2])

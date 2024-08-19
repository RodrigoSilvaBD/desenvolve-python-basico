#Faça um programa que gere aleatoriamente 20 valores inteiros entre -100 e 100 e os armazene em uma lista. Em seguida imprima na ordem estabelecida:

    #A lista ordenada, sem modificar a lista original
    #A lista original
    #O índice do maior valor da lista
    #O índice do menor valor da lista

import random
aleatorios = []

for i in range(20):
    valor = random.randint(-100, 100)
    aleatorios.append(valor)

print(sorted(aleatorios))
print(aleatorios)
print(F"O maior valor está no indice: ", aleatorios.index(max(aleatorios)))
print(F"O menor valor está no indice: ", aleatorios.index(min(aleatorios)))
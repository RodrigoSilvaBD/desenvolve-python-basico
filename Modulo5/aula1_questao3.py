#Escreva um programa em Python que utiliza a biblioteca random para gerar um número aleatório entre 1 e 10 e peça ao usuário para adivinhar o número. 
# Forneça feedback se o palpite é muito alto, muito baixo ou correto. Interrompa a execução somente quando o usuário acertar o palpite.

import random
n_aleatorio = random.randint(1, 10)


while True:
    chute = int(input("Adivinha o numero entrer 1 e 10: "))
    if chute < n_aleatorio:
        print("Muito baixo, tente novamente!")
    elif chute > n_aleatorio:
        print ("Muito alto, tente novamente!")
    else: 
        print("Você acertou!")
        break

#Você está desenvolvendo um sistema de avaliação de desempenho para um jogo. Escreva um programa em Python que avalia a pontuação do jogador
#  em uma missão e atribui uma classificação com base nas seguintes condições:

    #Se a pontuação for menor que 70, atribua a classificação "Insatisfatório".
    #Se a pontuação for maior ou igual a 70, atribua a classificação "Regular".
    #Se a pontuação for maior ou igual a 80, atribua a classificação "Bom".
    #Se a pontuação for maior ou igual a 90, atribua a classificação "Excelente".

#Escreva um programa que solicita ao usuário a pontuação e imprime a classificação correspondente.

pontuacao = int(input("Por favor insira sua pontuação: "))

if  pontuacao >= 90:
    print("Excelente.")
elif pontuacao >= 80:
    print ("Bom")
elif pontuacao >= 70:
    print("Regular")
else:
    pontuacao < 70
    print ("Insatisfatório!")

#Um instituto realizou uma pesquisa de público e precisa calcular a média de idade dos respondentes. 
# Escreva um programa que leia um inteiro N com a quantidade de respondentes e em seguida leia as 
# N idades de cada respondente. Ao final, imprima a média das idades.
#    (idade1 + idade2 + idade3 + … + idade_n)/N

n = int(input("Digite a quantidade de idades para o calculo. "))

soma = 0
cont = 0

while cont < n:
    idade = int(input("Digite a idade: "))
    soma += idade 

    cont += 1 


print(f" a soma das idades é: {soma}")
print(f" A média das idadees é: {soma/n}")
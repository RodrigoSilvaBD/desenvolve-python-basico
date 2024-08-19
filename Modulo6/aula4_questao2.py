#Solicite uma frase do usuário e usando compreensão de listas imprima:

    #A lista de vogais da frase, ordenada alfabeticamente
    # lista de consoantes da frase

#Exemplo:
#Digite uma frase: Eu gosto de programar em Python
#Vogais: ['a', 'a', 'e', 'e', 'o', 'o', 'o', 'o', 'u']
#Consoantes: ['E', 'g', 's', 't', 'd', 'p', 'r', 'g', 'r', 'm', 'r', 'm', 'P', 'y', 't', 'h', 'n']

frase = str(input("Digite uma frase: "))

vogais = "aeiouAEIOU"
list_vogais = sorted([letra for letra in frase if letra in vogais])
list_consoantes = [letra for letra in frase if letra.isalpha() and letra not in vogais]

print(list_vogais)
print(list_consoantes)
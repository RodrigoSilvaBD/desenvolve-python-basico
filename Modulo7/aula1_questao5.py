# Implemente um código que leia uma string do usuário e imprima quantas vogais existem na frase e quais os seus índices da string.
# Dica: letra in "aeiou". Exemplo:
#Digite uma frase:O Meu amor mora em Roma e me deu um ramo de flores
#19 vogais
#Índices [1, 2, 4, 6, 10, 12, 14, 18, 20, 22, 25, 28, 29, 31, 35, 37, 40, 44, 46]

frase = "O Meu amor mora em Roma e me deu um ramo de flores"

count_vogais = 0
indices = []
for i in range(len(frase)):
    if frase [i].lower() in "aeiou":
        count_vogais += 1
        indices.append(i)
print(count_vogais)
print(indices)

#Desenvolva um programa que solicite ao usuário inserir uma frase e substitua todas as ocorrências de vogal por "*".
#Ex:
#Digite uma frase: O rato roeu a roupa do rei
#Frase modificada: * r*t* r*** * r**p* d* r**

frase = input("Digite uma frase: ")
frase = frase.lower()
vogais = "aeiou"
for n in vogais:
    frase = frase.replace(n, '*')
print(frase)


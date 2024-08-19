#Escreva um script que leia o arquivo salvo no exercício anterior e salva em um novo arquivo "palavras.txt",
# removendo todos os espaços em branco e caracteres não alfabéticos, e separando cada palavra em uma linha. Ao final,
# imprima o conteúdo do arquivo "palavras.txt".
#Ex:
#Bom
#dia
#meu
#nome
#é
#Davi



import re

with open("frase.txt", 'r') as arquivo:
    palavras = re.findall(r'[a-zA-Z]+', arquivo.read())

with open("palavras.txt", 'w') as arquivo:
    arquivo.write('\n'.join(palavras))

with open("palavras.txt", 'r') as arquivo:
    print(arquivo.read())

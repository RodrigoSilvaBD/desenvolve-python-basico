#Entrada de dados, idade, experiencia e quantidade de vitorias
classe = input("Digite a sua classe (guerreiro, mago ou arqueiro): ")
forca = int(input("Digite os pontos de força (de 1 a 20): "))
magia = int(input("Digite os pontos de magia (de 1 a 20): "))

#processamento, true para os dois maior de idade
if classe == "guerreiro" and forca >15 and magia < 10:
    print("True")
elif classe == "mago" and forca <=10 and magia >=15:
    print("True")
elif classe == "arqueiro" and (5 < forca <= 15)  and (5 < magia <= 15):
    print("True")
else:
    print("Pontos de atributo não são consistentes com a classe escolhida.")
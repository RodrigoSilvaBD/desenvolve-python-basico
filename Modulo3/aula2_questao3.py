#Entrada de dados, idade, experiencia e quantidade de vitorias
idade = int(input("Digite a sua idade: "))
experiencia = bool(input("Voce já jogou pelo menos 3 jogos de tabuleiro? "))
vitoria = int(input("Quantas vezes venceu um jogo de tabuleiro? "))

#processamento, true para os dois maior de idade
a = (16 < idade < 18)
c = (vitoria >= 1)
pode_jogar = a and experiencia == True and c


print(f"Apto para ingressar no clube de jogos de tabuleiro: {pode_jogar}")

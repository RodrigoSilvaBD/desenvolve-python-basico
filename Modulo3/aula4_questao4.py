#Você está implementando um sistema de entrega expressa e precisa calcular o valor do frete 
#com base na distância e no peso do pacote. Escreva um código que solicita a distância da entrega
# em quilômetros e o peso do pacote em quilogramas. O programa deve calcular e imprimir o valor do frete 
# de acordo com as seguintes regras:

    #Distância até 100 km: R$1 por kg.
    #Distância entre 101 e 300 km: R$1.50 por kg.
    #Distância acima de 300 km: R$2 por kg.
    #Acrescente uma taxa de R$10 para pacotes com peso superior a 10 kg

distancia = int(input("Por favor insira a distancia em km: "))
peso = int(input("Por favor insira o peso em kg: "))
if peso > 10:
    custo = 10
if distancia < 100:
    custo = custo + peso * 1
    print (f"O preço é {custo}")
if distancia > 100 and distancia <= 300:
    custo = custo + peso * 1.5
    print (f"O preço é {custo}")
if distancia > 300:
    custo = custo + peso * 2
    print (f"O preço é {custo}")

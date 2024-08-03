#leitura de dados (entrada)
fahrenheit = int(input("Digite a temperatura em F: "))


#processamento de dados
celsius = (fahrenheit - 32) * 5 / 9

#impressão de dados (saída)
print (f"{fahrenheit} graus são {int(celsius)} graus Celsius")
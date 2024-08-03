#leitura de dados (entrada)
produto1 = str(input("Digite o nome do produto 1: "))
valor1 = float(input("Digite o valor do produto 1: "))
qnt1 = int(input("Digite a quantidade do produto 1: "))
produto2 = str(input("Digite o nome do produto 2: "))
valor2 = float(input("Digite o valor do produto 2: "))
qnt2 = int(input("Digite a quantidade do produto 2: "))
produto3 = str(input("Digite o nome do produto 3: "))
valor3 = float(input("Digite o valor do produto 3: "))
qnt3 = int(input("Digite a quantidade do produto 3: "))


#processamento de dados
total = valor1*qnt1 + valor2*qnt2 +valor3*qnt3


#impressão de dados (saída)
print(f" Total: {total:,.2f}")
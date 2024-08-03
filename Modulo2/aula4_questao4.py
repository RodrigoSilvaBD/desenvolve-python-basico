#leitura de dados (entrada)
valor_inteiro = int(input("Digite o valor a ser pago: "))


#processamento de dados
nota_100 =  valor_inteiro // 100
valor_inteiro =  valor_inteiro % 100

nota_50 = valor_inteiro // 50
valor_inteiro =  valor_inteiro % 50

nota_20 = valor_inteiro // 20
valor_inteiro =  valor_inteiro % 20

nota_10 = valor_inteiro // 10
valor_inteiro =  valor_inteiro % 10

nota_5 = valor_inteiro // 5
valor_inteiro =  valor_inteiro % 5

nota_2 = valor_inteiro // 2
valor_inteiro =  valor_inteiro % 2

nota_1 = valor_inteiro


#impressão de dados (saída)
print(valor_inteiro)
print (f"{nota_100} nota(s) de 100")
print (f"{nota_50} nota(s) de 50")
print (f"{nota_20} nota(s) de 20")
print (f"{nota_10} nota(s) de 10")
print (f"{nota_5} nota(s) de 5")
print (f"{nota_2} nota(s) de 2")
print (f"{nota_1} nota(s) de 1")
#Maria precisa de sua ajuda para organizar os experimentos de seu laboratório. 
# Ela quer saber no final do ano, quantas cobaias foram utilizadas no laboratório e o percentual 
# de cada tipo de cobaia utilizada. Este laboratório utiliza três tipos de cobaias: sapos, ratos e coelhos. 

#Entrada: A primeira linha de entrada é um inteiro N com a quantidade de experimentos registrados. 
# As N linhas seguintes contém um inteiro Quantia que representa a quantidade de cobaias utilizadas 
# e um caractere Tipo ('S', 'R' ou 'C') com o tipo de cobaia (S:Sapo, R:Rato ou C:Coelho).

#Saída: Apresente o total de cobaias utilizadas, o total de cada tipo de cobaia e o percentual
#  de cada uma em relação ao total de cobaias utilizadas

n = int(input("Digite a quantidade de experimentos: "))

cont = 0
soma_sapo, soma_rato, soma_coelho = 0, 0, 0

while cont <n:
    quantia = int(input("Informe a quantidade de cobaias: "))
    tipo = input("Informe o tipo de cobaia (S, R ou C): ")

    if tipo == 'S' : soma_sapo += quantia
    elif tipo == 'R' : soma_rato += quantia
    elif tipo == 'C' : soma_coelho += quantia


    cont += 1

print("Total de cobaias: ", soma_sapo+soma_rato+soma_coelho)   
print("Total de sapos: ", soma_sapo)
print("Total de ratos: ", soma_rato)
print("Total de coelhos: ", soma_coelho)
print(f"Percentual de sapos: {(soma_sapo/(soma_sapo+soma_coelho+soma_rato))*100:,.2f}%" )
print(f"Percentual de ratos: {(soma_rato/(soma_sapo+soma_coelho+soma_rato))*100:,.2f}%")
print(f"Percentual de coelhos: {(soma_coelho/(soma_sapo+soma_coelho+soma_rato))*100:,.2f}%")

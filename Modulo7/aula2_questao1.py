#Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com o nome do mês por extenso. 
#Dica: usando listas você não precisa fazer um "if" para cada mês.
#Ex:
#Digite uma data de nascimento: 29/10/1973
# Escreva um programa que solicita o nome do usuário e o imprime em forma de escada, como indicado no exemplo a seguir.

nasc = input("Digite a data de nascimento: ")
dia, mes, ano = map(int, nasc.split('/'))
meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro" ]
print(f"Voce nasceu em {dia} de {meses [mes-1]} de {ano}")
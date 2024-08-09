#Entrada de dados, idade de juliana e cris
idade_juliana =int(input("Digite a idade de Juliana: "))
idade_cris =int(input("Digite a idade de Cris: "))

#processamento, true para os dois maior de idade
resultado = idade_juliana >= 18 or idade_cris >= 18

#saida
print(resultado)

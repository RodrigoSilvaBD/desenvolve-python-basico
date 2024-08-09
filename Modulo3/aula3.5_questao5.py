#Você está projetando um sistema de autenticação baseado na análise da íris (parte colorida do olho). 
# Ao acionado, o sistema coleta e retorna 3 valores inteiros referentes a atributos da íris visível. 
# Mas o sistema não é perfeito, tendo uma margem de erro do sensor de +/- 5

#O código abaixo tem os atributos dos 4 usuários cadastrados no sistema. Você deve completar om código, 
# pedindo ao usuário para inserir uma nova leitura de padrão de íris. O programa deve comparar o padrão inserido com os 
# padrões cadastrados no banco de dados. 
# Se o padrão estiver dentro da tolerância estabelecida, o usuário é autenticado com sucesso. Caso contrário, a autenticação
#  falha.

#Dica: A função do python abs() retorna o valor absoluto de um elemento. Ex:

# >>> print(abs(987-982))
#  5
#  >>> print(abs(987-992))
#  5

iris1_a1, iris1_a2, iris1_a3 = 123, 456, 789
iris2_a1, iris2_a2, iris2_a3 = 987, 654, 321
iris3_a1, iris3_a2, iris3_a3 = 111, 222, 333
iris4_a1, iris4_a2, iris4_a3 = 444, 555, 666


atributo1, atributo2, atributo3 = int(input("insira o primeiro atributo do padrão de íris para autenticação: ")), int(input("insira o segundo atributo do padrão de íris para autenticação: ")), int(input("insira o terceiro atributo do  padrão de íris para autenticação: "))

resultado1_iris1 = abs(atributo1 - iris1_a1)
resultado2_iris1 = abs(atributo2 - iris1_a2)
resultado3_iris1 = abs(atributo3 - iris1_a3)
resultado1_iris2 = abs(atributo1 - iris2_a1)
resultado2_iris2 = abs(atributo2 - iris2_a2)
resultado3_iris2 = abs(atributo3 - iris2_a3)
resultado1_iris3 = abs(atributo1 - iris3_a1)
resultado2_iris3 = abs(atributo2 - iris3_a2)
resultado3_iris3 = abs(atributo3 - iris3_a3)
resultado1_iris4 = abs(atributo1 - iris4_a1)
resultado2_iris4 = abs(atributo2 - iris4_a2)
resultado3_iris4 = abs(atributo3 - iris4_a3)

if resultado1_iris1 <= 5 and resultado2_iris1 <= 5 and resultado3_iris1 <= 5:
    print("Autenticação bem-sucedida!")
    print("Usuário: 1")
elif resultado1_iris2 <= 5 and resultado2_iris2 <= 5 and resultado3_iris2 <= 5:
    print("Autenticação bem-sucedida!")
    print("Usuário: 2")
elif resultado1_iris3 <= 5 and resultado2_iris3 <= 5 and resultado3_iris3 <= 5:
    print("Autenticação bem-sucedida!")
    print("Usuário: 3")
elif resultado1_iris4 <= 5 and resultado2_iris4 <= 5 and resultado3_iris4 <= 5:
    print("Autenticação bem-sucedida!")
    print("Usuário: 4")
else:
    print("Autenticação falhou!")

#atributo1margemmais = atributo1 + 5
#atributo2margemmais = atributo2 + 5
#atributo3margemmais = atributo3 + 5
#atributo1margemmenos = atributo1 - 5
#atributo2margemmenos = atributo2 - 5
#atributo3margemmenos = atributo3 - 5

#if (iris1_a1 <= atributo1margemmais and iris1_a1 >= atributo1margemmenos) and (iris1_a2 <= atributo2margemmais and iris1_a2 >= atributo2margemmenos) and (iris1_a3 <= atributo3margemmais and iris1_a3 >= atributo3margemmenos):
#    print("Autenticação bem-sucedida!")
#    print("Usuário: 1")
#elif (atributo1 == iris2_a1 and atributo2 == iris2_a2 and atributo3 == iris2_a3):
#    print("Autenticação bem-sucedida!")
#    print("Usuário: 2")
#elif (atributo1 == iris3_a1 and atributo2 == iris3_a2 and atributo3 == iris3_a3):
#    print("Autenticação bem-sucedida!")
#    print("Usuário: 3")
#elif (atributo1 == iris4_a1 and atributo2 == iris4_a2 and atributo3 == iris4_a3):
#    print("Autenticação bem-sucedida!")
#    print("Usuário: 4")
#else:
#    print("Autenticação falhou!")


    # não entendi bem esse exercicio, procurar ajuda
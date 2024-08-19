# Crie um programa em Python que receba duas listas de números do usuário, podendo cada lista ter uma quantidade diferente de valores. 
# Em seguida, combine essas duas listas de forma alternada para formar uma terceira lista. Intercale os elementos até o final da primeira lista, 
# adicionando ao final os elementos remanescentes da maior lista.


num_elem_lista1 = input("Digite a quantidade de elementos da lista 1: ")
lista1 = []
#não consegui fazer que peça a quantidade de elementos

for i in num_elem_lista1:
    elem = input(f"Digite o numero {3} da lista")
    lista1.append(elem)
print(lista1)


num_elem_lista2 = int(input("Digite a quantidade de elementos da lista 2: "))
num_elem_lista2 = []
entrada2 = input()
if entrada2:
    lista2= [int(x) for x in entrada2.split()]



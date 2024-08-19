#Crie uma lista com 20 elementos, entre -10 e 10, gerados aleatoriamente.
# Em seguida encontre o intervalo que possui a maior quantidade de números negativos e delete ele da lista com o operador del.
# Você deve imprimir a lista antes e depois da deleção.

import random
elementos = []

for i in range(20):
    valor = random.randint(-10, 10)
    elementos.append(valor)
print(elementos)

inicio_fatia_maior, tam_fatia_maior = 0, 0
inicio_fatia_atual, tam_fatia_atual = 0, 0
for i in range(len(elementos)):
    print('Inicio do laço', i, elementos[i])
    if elementos[i] < 0:
        tam_fatia_atual += 1
        if tam_fatia_atual ==1:
            print('Inicio nova fatia', tam_fatia_atual)
            inicio_fatia_atual = i
    else:
        if tam_fatia_atual > tam_fatia_maior:
            print('Maior fatia até agora', tam_fatia_atual)
            tam_fatia_maior = tam_fatia_atual
            inicio_fatia_maior = inicio_fatia_atual
        tam_fatia_atual = 0
print(inicio_fatia_maior, tam_fatia_maior)
del elementos[inicio_fatia_atual:inicio_fatia_maior+tam_fatia_maior]
print(elementos)
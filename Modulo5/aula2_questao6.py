#Crie uma função lambda para verificar se um número é par ou ímpar.
# Em seguida, solicite ao usuário um número indefinidos de valores (até que o usuário digite 0).
# Para cada valor de entrada, informe se é par ou ímpar.

#Exemplo de interação:
#Digite os valores que deseja verificar a paridade (digite 0 para finalizar a entrada de dados):
#3
#ímpar
#8
#par
#12
#par
#5
#ímpar
#7ímpar



paridade = lambda x: 'par' if x % 2 == 0 else 'ímpar'

print("Digite os valores que deseja verificar a paridade (digite 0 para finalizar a entrada de dados):")
    
while True:
        try:
            valor = int(input())
            if valor == 0:
                break
            print(paridade(valor))
        except ValueError:
            print("Por favor, digite um número inteiro válido.")




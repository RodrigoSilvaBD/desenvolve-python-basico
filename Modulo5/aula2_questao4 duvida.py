#Crie a função inverteValor() que recebe um inteiro de qualquer tamanho e retorna esse valor invertido usando apenas operações aritméticas
#Crie a função verificaInverso() que recebe o valor original e o valor invertido e retorna verdadeiro se ambos forem igualmente par ou igualmente ímpar.
# Retorne falso caso contrário.
#No programa principal, peça um valor do usuário e imprima o retorno de ambas as funções.


def inverteValor(valor):
    valor_invertido = 0
    while (valor > 0):
        digito = valor % 10
        valor=valor //10
        print*(digito, end'=')

    return valor_invertido

def verificaInverso (valor, valor_invertido):
    inversao = inverteValor(valor)
    if ......
    return eh_inverso

n = int(input("Digite um numero inteiro com 2 ou mais digitos: "))
n_invertido = inverteValor(n)
print(n_invertido)
print(verificaInverso(n, n_invertido))
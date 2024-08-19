#Crie uma função em Python chamada soma_digitos que recebe um número inteiro como parâmetro e retorna a soma dos seus dígitos. 
# Por exemplo, para o número 123, a função deve retornar 6, (1+2+3).

    #O desafio aqui é separar os dígitos de um número inteiro usando operações aritméticas

    #No programa principal solicite ao usuário que insira um número e utilize a função soma_digitos para calcular e exibir a soma dos seus dígitos.




def somaDigitos(a):
    soma = 0
    while a:
        soma += a % 10
        a //= 10
    return soma
    #num_str = str(a)
    #soma = sum(int(i) for i in a)
    #return soma
# 
num= float(input("Digite numero com 2 ou mais digitos: "))
resultado = somaDigitos(num)
print(resultado)
#Faça um programa que leia um número de celular e, caso o número tenha apenas 8 dígitos, acrescente o 9 na frente. 
# Caso o número já tenha 9 dígitos, verifique se o primeiro dígito é 9. Adicione o separador "-" na sua impressão.
#Digite o número: 97651234
#Número completo: 99765-1234
#Digite o número: 980876543
#Número completo: 98087-6543 

def formatar_numero_celular(numero):

    if len(numero) == 8:
        numero = '9' + numero
    elif len(numero) == 9:
        if numero[0] != '9':
            return "Número inválido. O primeiro dígito deve ser 9 para números com 9 dígitos."
    else:
        return "Número inválido. Deve ter 8 ou 9 dígitos."

    return f'{numero[:5]}-{numero[5:]}'

numero_usuario = input("Digite o número de celular: ")
resultado = formatar_numero_celular(numero_usuario)
print(resultado)
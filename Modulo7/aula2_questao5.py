#De acordo com uma pesquisa do linguista Matt Davis, o cérebro humano consegue ler palavras com as letras embaralhadas,
# contanto que a primeira e a última letra estejam no lugar correto. Implemente uma função chamada embaralhar_palavras()
# para ajudar a testar a hipótese do Matt Davis. Sua função vai receber uma frase, embaralhar as letras internas de cada palavra
# e retornar a frase modificada. Dica: use a biblioteca random.

#Complete o seguinte código:
#def embaralhar_palavras(frase):
    #### Escreva a função

# Exemplo de uso:
#frase = "Python é uma linguagem de programação"
#resultado = embaralhar_palavras(frase)
#print(resultado)
# Possível saída: "Ptohyn é uma lignaugem de prarmoagãço"

import random

def embaralhar_palavras():
    # Solicita a frase ao usuário
    frase = input("Digite uma frase: ")
    
    def embaralhar_palavra(palavra):
        if len(palavra) <= 2:
            return palavra
        primeira_letra = palavra[0]
        ultima_letra = palavra[-1]
        letras_internas = list(palavra[1:-1])
        random.shuffle(letras_internas)  # Embaralha as letras internas
        return primeira_letra + ''.join(letras_internas) + ultima_letra
    
    # Divide a frase em palavras
    palavras = frase.split()
    # Embaralha cada palavra e recombine em uma nova frase
    palavras_embaralhadas = [embaralhar_palavra(palavra) for palavra in palavras]
    return ' '.join(palavras_embaralhadas)

# Exemplo de uso
resultado = embaralhar_palavras()
print(resultado)

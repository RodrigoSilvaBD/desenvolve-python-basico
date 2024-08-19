#Desenvolva um programa que verifique se uma frase fornecida pelo usuário é um palíndromo (ou seja, lida da mesma forma de trás para frente).
# Ignore espaços em branco ou sinais de pontuação, e considere maiúsculas e minúsculas da mesma forma. Seu programa deve continuar rodando 
# até que o usuário digite "Fim".Ex:

#Digite uma frase (digite "fim" para encerrar): Radar
#"Radar" é palíndromo
#Digite uma frase (digite "fim" para encerrar): Bom dia!
#"Bom dia!" não é palíndromo
#Digite uma frase (digite "fim" para encerrar): Ame o poema
#"Ame o poema" é palíndromo
#Digite uma frase (digite "fim" para encerrar): A Daniela ama a lei? Nada!
#"A Daniela ama a lei? Nada!" é palíndromo
#Digite uma frase (digite "fim" para encerrar): fim

import string

def main():
    while True:
        frase = input('Digite uma frase (digite "fim" para encerrar): ')
        
        if frase.lower() == "fim":
            break
        
        # Limpa a frase para remover espaços, pontuação e converter para minúsculas
        frase_limpa = ''.join(c.lower() for c in frase if c not in string.whitespace and c not in string.punctuation)
        
        # Verifica se a frase é um palíndromo
        if frase_limpa == frase_limpa[::-1]:
            print(f'"{frase}" é palíndromo')
        else:
            print(f'"{frase}" não é palíndromo')

# Executa o programa
if __name__ == "__main__":
    main()
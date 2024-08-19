#Baixe o arquivo contendo o roteiro do filme brasileiro "Estômago" (link a seguir) e salve em seu computador com o nome "estomago.txt". 

#Link: https://aplauso.imprensaoficial.com.br/edicoes/12.0.813.502/12.0.813.502.txt

#Em seguida crie um script em Python que abra o arquivo para leitura e imprima: 

#    O texto das primeiras 25 linhas
#    O número de linhas do arquivo
#    A linha com maior número de caracteres
#    O número de menções aos nomes dos personagens "Nonato" e "Íria" (inclua todas as variações de maiúsculas e minúsculas e atenção para não incluir a substring "iria" se ela fizer parte de outras palavras).



import re

def analisar_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            linhas = arquivo.readlines()
        
        # Imprimir as primeiras 25 linhas
        print("Primeiras 25 linhas:")
        for linha in linhas[:25]:
            print(linha.strip())
        
        # Número total de linhas
        total_linhas = len(linhas)
        print(f"\nNúmero total de linhas: {total_linhas}")
        
        # Linha com maior número de caracteres
        linha_max = max(linhas, key=len).strip()
        print(f"\nLinha com maior número de caracteres:\n{linha_max}")
        
        # Contar menções a "Nonato" e "Íria"
        texto_completo = ''.join(linhas).lower()
        count_nonato = len(re.findall(r'\bnonato\b', texto_completo))
        count_iria = len(re.findall(r'\bíria\b', texto_completo))
        
        print(f"\nNúmero de menções a 'Nonato': {count_nonato}")
        print(f"Número de menções a 'Íria': {count_iria}")
    
    except FileNotFoundError:
        print(f"O arquivo '{nome_arquivo}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Substitua 'nome_do_arquivo.txt' pelo nome correto do seu arquivo
analisar_arquivo('Estomago.txt')



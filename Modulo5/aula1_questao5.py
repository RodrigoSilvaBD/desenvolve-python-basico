#Você está trabalhando em um sistema de mensagens instantâneas, que deve permitir o uso de emojis nas conversas entre pessoas. Faça:
            #No terminal, instale a biblioteca emoji usando o gerenciador de pacotes pip

            #Conheça a função emoji.emojize()
#Seu programa deve apresentar para o usuário a lista de emojis disponíveis com o texto correspondente a cada emoji. 
# Em seguida, solicite uma frase codificada ao usuário e apresente ela decodificada com a visualização de emojis (emojizada).
#A seguir um exemplo de interação, com uma lista de emojis sugeridos. 
# Você pode consultar o texto que codifica outros emojis indo nessa página e passando o mouse por cima do emoji desejado. 

import emoji

emojis_disponiveis = {
    "🥇": ":1st_place_medal:",
    "🥈": ":2nd_place_medal:",
    "🥉": ":3rd_place_medal:",
    "🫡": ":saluting_face:"
}
print("Emojis disponíveis:")
for simbolo, codigo in emojis_disponiveis.items():
    print(f"{simbolo} - {codigo}")

frase = str(input("Digite uma frase e ela será emojizada: "))
print("Frase emojizada: ")
print(f"{emoji.emojize(frase, use_aliases=True)}")

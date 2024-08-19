#Implemente uma função em Python chamada validador_senha() onde é necessario que o usuario informe uma senha e que verifica se a senha fornecida
#  atende todos os seguintes critérios:

    #Pelo menos 8 caracteres de comprimento.
    #Contém pelo menos uma letra maiúscula e uma letra minúscula.
    #Contém pelo menos um número.
    #Contém pelo menos um caractere especial (por exemplo, @, #, $).

#Complete o seguinte código:
#def validador_senha(senha):
    #### Escreva a função

# Exemplo de uso:
#senha1 = "Senha123@"
#senha2 = "senhafraca"
#senha3 = "Senha_fraca"
#print(validador_senha(senha1))  # Saída esperada: True
#print(validador_senha(senha2))  # Saída esperada: False
#print(validador_senha(senha3))  # Saída esperada: False

import string

def validador_senha():
    # Solicita a senha ao usuário
    senha = input("Digite uma senha: ")

    # Verifica se a senha tem pelo menos 8 caracteres
    if len(senha) < 8:
        return False
    
    # Verifica se contém pelo menos uma letra maiúscula
    tem_maiuscula = any(c.isupper() for c in senha)
    
    # Verifica se contém pelo menos uma letra minúscula
    tem_minuscula = any(c.islower() for c in senha)
    
    # Verifica se contém pelo menos um número
    tem_numero = any(c.isdigit() for c in senha)
    
    # Verifica se contém pelo menos um caractere especial
    caracteres_especiais = string.punctuation
    tem_especial = any(c in caracteres_especiais for c in senha)
    
    # Retorna True se todas as condições forem atendidas
    return tem_maiuscula and tem_minuscula and tem_numero and tem_especial

# Exemplo de uso:
print(validador_senha())  # Solicita a senha e imprime se é válida ou não

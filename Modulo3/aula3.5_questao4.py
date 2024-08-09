#Você está implementando um sistema de desconto em uma loja online. 
# Escreva um programa em Python que calcula o desconto com base no valor total da compra e atribui diferentes níveis de desconto de acordo com as seguintes condições:

#    Se o valor total da compra for menor que R$ 50, não há desconto.
#    Se o valor total da compra for maior ou igual a R$ 50, atribua um desconto de 10%.
#    Se o valor total da compra for maior ou igual a R$ 100, atribua um desconto de 20%.

#Seguem alguns exemplos de interação com seu código no terminal. Preste atenção na formatação esperada para as saídas.

valor_compra = float(input("Digite o valor total da compra: "))

if  valor_compra > 100:
    print("Desconto aplicado de 20.0%")
    print(f"Valor final com desconto: {valor_compra - valor_compra*0.2}")
elif valor_compra >= 50:
    print("Desconto aplicado de 10.0%")
    print (f"Valor final com desconto: {valor_compra - valor_compra*0.1}")
else:
    valor_compra < 50
    print("Desconto aplicado de 0.0%")
    print(f"Valor final com desconto: {valor_compra}")

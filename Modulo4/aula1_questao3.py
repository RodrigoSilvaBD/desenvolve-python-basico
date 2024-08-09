

n1, n2, n3 = int(input("Digite o valor da primeira nota: ")), int(input("Digite o valor da segunda nota: ")), int(input("Digite o valor da terceira nota: "))

m = (n1+n2+n3)/3


if m >= 60:
    print("Aprovado")
    print("Fim")
elif m >= 40:
    print("Recuperação")
    print("Fim")
else:
    print("Reprovado")
    print("Fim")

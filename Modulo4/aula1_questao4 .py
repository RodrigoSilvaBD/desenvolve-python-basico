

n = int(input("Digite um valor n: "))

maior = 0

while n > 0:
    x = int(input("Digite um valor x: "))
    if x > maior:
        maior = x
        n -= 1
    else:
        n -= 1
print(f"{maior}")


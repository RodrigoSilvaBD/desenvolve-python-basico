#Entrada de dados, genero, idade e tempo 
genero = input()
idade = int(input())
tempo = int(input())


#processamento, mulher ter  > 60 homens > 65. tempo => 30. idade > 60 e tempo => 25
a = (genero) == 'f' and idade >= 60 or (genero == 'm' and idade >= 65)
b = tempo > 30
c = idade >= 60 and tempo >= 25

pode_aposentar = a or b or c

#saida
print(pode_aposentar)

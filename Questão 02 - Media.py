a = int(input("Digite aqui o valor: "))
cont = 0
soma = 0

while a >= 0: 
    cont = cont + 1
    soma = soma + a
    media = soma/cont
    a = int(input("Digite aqui o valor: "))
    
print(media)

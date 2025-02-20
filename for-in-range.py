#range

x = list(range(10))
print(x)

y = list(range(2,30,3))
print(y)

z = list(range(5,30,5))
print(z)

#lista sempre acaba antes do final
#range(começo,final,passo)


for i in range(-20,50,8):
    print(i)

for i in "ANCHIETA":
    print(i)

nome = input('Entre com seu nome completo: ')
lista = nome.split()
print(lista)

for i in lista:
    print(i)
    
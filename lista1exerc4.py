#4)	Faça um programa que receba
#dez números e armazene em uma
#lista. Em seguida calcule a
#soma de todos os números
#percorrendo novamente a lista.
#Apresente a soma e em seguida
#a média baseada na soma e 
#no número de números armazenados.
lista = [0] * 10
soma = 0
for i in range(10):
    print("Digite um numero")
    lista[i] = int(input())

for umnumero in lista:
    soma += umnumero
print("A soma e ", soma)
media = soma / 10
print("A media e ", media)


lista2 = []
soma = 0
for i in range(10):
    print("Digite um numero")
    lista2.append(int(input()))

for umnumero in lista2:
    soma += umnumero
print("Soma: ", soma)
media = soma / 10
print("Media ", media)
    
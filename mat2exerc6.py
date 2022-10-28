'''
6)	Faça um programa que carregue uma matriz 3 x 4, calcule e mostre:

a.	A quantidade de elementos pares
b.	A soma dos elementos ímpares
c.	A média de todos os elementos
'''
matriz = [[0] * 4 for i in range(3)]
for lin in range(3):
    for col in range(4):
        print("Digite um numero")
        matriz[lin][col] = int(input())

contapar = 0
for lin in range(3):
    for col in range(4):
        if matriz[lin][col] % 2 == 0:
            contapar += 1
print("O numero de numeros pares e ", contapar)
###b.	A soma dos elementos ímpares
soma = 0
for lin in range(3):
    for col in range(4):
        if matriz[lin][col] % 2 != 0:
            soma += matriz[lin][col]
print("A soma dos numeros impares e ", soma)

#c.	A média de todos os elementos
somatudo = 0
for lin in range(3):
    for col in range(4):
        somatudo += matriz[lin][col]
media = somatudo / 12
print("A media dos elementos e ", media)
"""
2)	Faça um programa que leia um vetor V
 contendo 18 elementos. A seguir, distribua 
 esses elementos em uma matriz 3x6. Ao 
 final, mostre a matriz gerada.
"""
from random import random
vetor = [0] * 18
matriz = [[0] * 6 for i in range(3)]

for i in range(18):
    vetor[i] = int(random() * 100)
print(vetor)
proxnumero = 0
for lin in range(3):
    for col in range(6):
        matriz[lin][col] = vetor[proxnumero]
        proxnumero += 1
print(matriz)
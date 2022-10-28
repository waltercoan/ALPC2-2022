'''
1)	Elaborar um programa que efetue a leitura de 20 valores 
inteiros em uma matriz A de duas dimensões com 4 linhas e
5 colunas. Construir um vetor B de para 4 elementos que 
seja formada pelo somatório dos elementos correspondentes de
cada linha da matriz A. Construir também um vetor C para 
5 elementos que seja formada pelo somatório dos elementos 
correspondentes de cada coluna da matriz A. Ao final o 
programa deverá apresentar o total do somatório dos elementos 
do vetor B com o somatório dos elementos do vetor C.
'''
matriz = [[0] * 5 for i in range(4)]
vetorB = [0] * 4
vetorC = [0] * 5
for lin in range(4):
    for col in range(5):
        print("Digite um numero")
        matriz[lin][col] = int(input())

for lin in range(4):
    for col in range(5):
        vetorB[lin] += matriz[lin][col]
print(vetorB)

for col in range(5):
    for lin in range(4):
        vetorC[col] += matriz[lin][col]
print(vetorC)
print(sum(vetorB) + sum(vetorC))
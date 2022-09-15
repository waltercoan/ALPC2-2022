#JAVA-C-C++-C#
#int[][] matriz = new int[num-linhas][num-colunas]
#int[][] matriz = new int[4][5]
#            num-col          num-lin
matriz = [[0] * 5 for i in range(4)]
#Gravar matriz[num-lin][num-col] = valor
matriz[0][0] = 100
#Ler valor matriz[num-lin][num-col]
print(matriz[0][0])
print(matriz)
print("\n"+("-" * 42))
for lin in range(4):
    print("|",end="")
    for col in range(5):
        print(matriz[lin][col], end="\t |")
    print("\n"+("-" * 42))

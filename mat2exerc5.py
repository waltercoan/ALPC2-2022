matriz = [[0] * 3 for lin in range(3)]
for lin in range(3):
    for col in range(3):
        print("Digite um numero")
        matriz[lin][col] = int(input())
print("Digite o multiplicador")
mult = int(input())

for lin in range(3):
    for col in range(3):
        print((matriz[lin][col] * mult),end=" ")
    print()
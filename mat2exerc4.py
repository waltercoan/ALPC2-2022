matriz = [[0] * 3 for i in range(10)]
for lin in range(10):
    print("Aluno: ", lin+1)
    for col in range(3):
        print("Nota: ", col+1)
        print("Digite a nota")
        matriz[lin][col] = float(input())

menornota = 0
numerodanota = 0
contaprova1 = 0
contaprova2 = 0
contaprova3 = 0
for lin in range(10):
    print("Aluno: ", lin+1)
    for col in range(3):
        if col == 0:
            menornota = matriz[lin][col]
            numerodanota = col + 1 
        else:
            if matriz[lin][col] < menornota:
                menornota = matriz[lin][col]
                numerodanota = col + 1 
    print("A prova ", numerodanota)
    print("teve a menor nota de :", menornota)
    '''
    if numerodanota == 1:
        contaprova1 += 1  
        contaprova1 += (numerodanota == 1?1:0)
    '''
    contaprova1 += 1 if numerodanota == 1 else 0
    contaprova2 += 1 if numerodanota == 2 else 0
    contaprova3 += 1 if numerodanota == 3 else 0

print("Qtd menor nota na prova 1: ", contaprova1)
print("Qtd menor nota na prova 2: ", contaprova2)
print("Qtd menor nota na prova 3: ", contaprova3)
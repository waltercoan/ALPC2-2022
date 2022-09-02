'''8
              +---+---+---+---+---+---+---+---+---+---+
listacontas = | 3 | 8 |   |   |   |   |   |   |   |   |
              +---+---+---+---+---+---+---+---+---+---+
                0   1   2   3   4   5   6   7   8   9
              +---+---+---+---+---+---+---+---+---+---+
listasaldos = |10 | 2 |   |   |   |   |   |   |   |   |
              +---+---+---+---+---+---+---+---+---+---+
                0   1   2   3   4   5   6   7   8   9
'''
opcao = 0
listacontas = [0] * 10
listasaldos = [0] * 10

for i in range(10):
    repete = True
    while repete:
        print("Digite o numero da conta")
        numconta = int(input())
        j=0
        while j < 10:
            if listacontas[j] == numconta:
                print("Conta Duplicada")
                repete = True
                break
            j += 1
        if j == 10:
            repete = False
            listacontas[i] = numconta
            print("Digite o saldo")
            listasaldos[i] = float(input())


## CADASTRO DAS CONTAS
while(opcao !=4):
    print("Sistema Bancário")
    print("1. Efetuar depósito")
    print("2. Efetuar saque")
    print("3. Consultar ativos")
    print("4. Finalizar")
    print("Digite o número da opção desejada\n")
    print()
    opcao = int(input())
    if opcao == 1:
        print("Deposito")
        #pedir o numero da conta
        #procurar na lista de contas o numero da conta digitado
        #caso encontrar, utilizar a posição onde foi encontrado
        #para atribuir o novo saldo (tem que pedir antes o valor do deposito)
        #caso contrário apresentar mensagem de erro do numero da conta

    if opcao == 2:
        print("Saque")

print("Até logo obrigado!")

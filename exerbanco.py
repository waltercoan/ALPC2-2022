opcao = 0
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
    if opcao == 2:
        print("Saque")

print("Até logo obrigado!")

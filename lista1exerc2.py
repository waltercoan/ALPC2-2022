#2)	Faça um programa que receba dez
#números e armazene em uma lista.
#Em seguida conte quantos números são
#impar e quantos são par. Apresente os
#contadores na tela.
# int lista[] = new int[10];
lista = [0] * 10
contapar = 0
contaimpar = 0
for i in range(10):
    print("Digite um numero")
    lista[i] = int(input())

for i in range(10):
    if lista[i] % 2 == 0:
        contapar += 1
    else:
        contaimpar += 1
print("Numero de numeros pares e ", contapar)
print("Numero de numeros impar e ", contaimpar)

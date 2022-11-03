'''
4)	Faça uma função que receba cinco valores
inteiros, e retorne o maior valor. Faça 
uma segunda função que receba também cinco 
valores e retorne o menor deles.
'''

#Função que retorna o maior valor entre 5 parametros
def maiorValor(n1:int, n2:int, n3:int, n4:int, n5:int):
    maior = n1
    if n2 > maior:
        maior = n2
    if n3 > maior:
        maior = n3
    if n4 > maior:
        maior = n4
    if n5 > maior:
        maior = n5
    return maior
#Função que retorna o menor valor entre 5 parametros
def menorValor(n1:int, n2:int, n3:int, n4:int, n5:int):
    menor = n1
    if n2 < menor:
        menor = n2
    if n3 < menor:
        menor = n3
    if n4 < menor:
        menor = n4
    if n5 < menor:
        menor = n5
    return menor

print("Digite o primeiro numero")
n1 = int(input())
print("Digite o segundo numero")
n2 = int(input())
print("Digite o terceiro numero")
n3 = int(input())
print("Digite o quarto numero")
n4 = int(input())
print("Digite o quinto numero")
n5 = int(input())

maior = maiorValor(n1, n2, n3, n4, n5)
menor = menorValor(n1, n2, n3, n4, n5)

print("O maior valor e ", maior)
print("O menor valor e ", menor)

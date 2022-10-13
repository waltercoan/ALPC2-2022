"""
1)	Faça uma função que receba três números inteiros: 
a,b e c, onde a é maior que 1. A função deve somar 
todos os inteiros entre b e c que sejam divisíveis 
por a (inclusive b e c) e retornar o resultado 
para a função principal.
"""

def somatudo(a:int,b:int,c:int):
    soma = 0
    for i in range(b,c+1):
        if i % a == 0:
            soma += i
    return soma

print("Digite o valor de A")
va = int(input())
print("Digite o valor de B")
vb = int(input())
print("Digite o valor de C")
vc = int(input())
guardar = somatudo(va,vb,vc)
print("A soma e ", guardar)
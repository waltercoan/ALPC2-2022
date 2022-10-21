'''
3)	Faça um programa que receba o estoque atual 
de três produtos que estão armazenados em quatro
armazéns e coloque esses dados em uma matriz 5x3. 
Sendo que a última linha da matriz contém o 
custo de cada produto, calcule e mostre:
a.	A quantidade de itens  armazenas em cada armazém
b.	Qual o armazém possui maior estoque do produto 2;
c.	Qual o armazém possui menor estoque
d.	Qual o custo total de cada produto
e.	Qual o custo total de cada armazém
'''
matriz = [[0] * 3 for i in range(5)]
for lin in range(4):
    print("Armazem: ", lin+1)
    for col in range(3):
        print("Produto: ", col+1)
        print("Digite a quantidade")
        matriz[lin][col] = int(input())

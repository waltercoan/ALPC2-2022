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

for col in range(3):
    print("Produto: ", col+1)
    print("Digite o custo")
    matriz[4][col] = float(input())

##a.	A quantidade de itens armazenadas em cada armazém
for lin in range(4):
    print("Armazem: ", lin+1)
    totarm = 0 
    for col in range(3):
        totarm += matriz[lin][col]
    print("Total ", totarm)
##b.	Qual o armazém que possui maior 
# estoque do produto 2;
omaior = 0
armazemmaiorqtd = 0
for lin in range(4):
    if matriz[lin][1] > omaior:
        omaior = matriz[lin][1]
        armazemmaiorqtd = lin

print("No armazem ", armazemmaiorqtd+1)
print("Possui a maior quantidade do prod 2 de: ", omaior)

#c.	Qual o armazém possui menor estoque
omenor = 0
oarmazemmenor = 0
for lin in range(4):
    totlin = 0
    for col in range(3):
        totlin += matriz[lin][col]
    if lin == 0:
        omenor = totlin
        oarmazemmenor = lin
    if totlin < omenor:
        omenor = totlin
        oarmazemmenor = lin
print("O armazem: ", oarmazemmenor + 1)
print("Possui a menor qtd de ", omenor)

##d.	Qual o custo total de cada produto
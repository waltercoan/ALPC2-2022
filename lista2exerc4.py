'''
VETORES4 - Faça um programa que receba 
a temperatura média de cada mês do ano 
e armazene-as em um vetor. Calcule e 
mostre a maior e a menor temperatura do 
ano e em que mês elas ocorreram (mostrar 
o mês por extenso: 1- Janeiro, 2 – Fevereiro). 
Desconsidere empates.
'''
listatemp = [0] * 12
listameses = ['JAN','FEV','MAR','ABR','MAI', \
    'JUN','JUL','AGO','SET','OUT','NOV','DEZ']

for i in range(12):
    print("Digite a temp media do mes ", listameses[i])
    listatemp[i] = float(input())

maiortemp = listatemp[0]
mesmaiortemp = 0
menortemp = listatemp[0]
mesmenortemp = 0
for i in range(12):
    if listatemp[i] < menortemp:
        menortemp = listatemp[i]
        mesmenortemp = i
    if listatemp[i] > maiortemp:
        maiortemp = listatemp[i]
        mesmaiortemp = i

print("A maior temp foi ", maiortemp, ' no mes ', listameses[mesmaiortemp])
print("A menor temp foi ", menortemp, ' no mes ', listameses[mesmenortemp])


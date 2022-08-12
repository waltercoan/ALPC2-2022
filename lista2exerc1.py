#Faça um programa que carregue 
#dois vetores de dez elementos 
#numéricos cada um e mostre um 
#vetor resultante da intercalação 
#desses dois vetores.

a = [10,20,30,40,50,60,70,80,90,100]
b = [15,25,35,45,55,65,75,85,95,105]
inter = [0] * 20

#logica muito doida para fazer intercalacao
proxlivre = 0
for i in range(10):
    inter[proxlivre] = a[i]
    proxlivre += 1
    inter[proxlivre] = b[i]
    proxlivre += 1

print(inter)
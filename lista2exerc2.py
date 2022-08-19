x = [10,20,30,40,50,60,70,80,90,100]
y = [1,20,3,40,5,60,7,80,9,100]
uniao = [0] * 20

#união de X com Y 
#(todos os elementos de X 
for i in range(10):
    uniao[i] = x[i]
#e os elementos de 
#Y que não estejam em X)
proxlivre = 10
for i in range(10): #indexador Y
    achei = False
    for j in range(10): #indexador X
        if y[i] == x[j]:
            achei = True
            break
    #if not achei:
    if achei == False:
        uniao[proxlivre] = y[i]
        proxlivre+=1

for i in range(proxlivre):
    print(uniao[i],end=", ")


#b.	a diferença entre X e Y 
# (todos os elementos de X 
# que não existam em Y)
dif = [0] * 10
proxlivre = 0
for i in range(10): #i indexa a lista X
    print(x[i])
    achei = False
    for j in range(10): #j indexa a lista Y
        print("\t", y[j])
        if x[i] == y[j]:
            achei = True
            print("ACHEI")
            break
    if not achei:
        dif[proxlivre] = x[i]
        proxlivre += 1
print(dif)

#c.	a soma entre X e Y (soma de 
# cada elemento de X com o 
# elemento de mesma posição em Y)
soma = [0] * 10
for i in range(10):
    soma[i] = x[i] + y[i]

print(soma)

#d.	produto entre X e Y (multiplicação de 
# cada elemento de X com o elemento 
# de mesma posição em Y)

prod = [0] * 10
for i in range(10):
    prod[i] = x[i] * y[i]

print(prod)

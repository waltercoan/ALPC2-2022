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
lista = [3,7,9,2,1,5]

valprocurado = 7

for i  in range(0,len(lista)-1):
    for j in range(i+1, len(lista)):
        if lista[i] > lista[j]:
            aux = lista[i]
            lista[i] = lista[j]
            lista[j] = aux
print('lista ', lista)

ini = 0
fim = len(lista) - 1
meio = 0
while(ini <= fim):
    meio = int((ini + fim) / 2)
    print("ini> ", ini)
    print("fim> ", fim)
    print("meio> ", meio)
    if lista[meio] == valprocurado:
        print("Achei o valor")
        break
    else:
        if valprocurado > lista[meio]:
            ini = meio + 1
        else:
            fim = meio - 1

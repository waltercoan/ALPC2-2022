'''
1.	Faça uma função que receba dois vetores 
A e B de dez elementos inteiros, por parâmetro. 
O procedimento deve determinar e mostrar um 
vetor C que contenha os elementos de A e B 
em ordem decrescente.
'''

def minhafuncao(lista1:list, lista2:list):
    novalista = []
    for i in lista1:
        novalista.append(i)
    for i in lista2:
        novalista.append(i)
    #algoritmo da bolha
    #dois laços de repetição aninhados
    # - 1 laço começa na posição ZERO e vai até a PENULTIMA
    for i in range(0,len(novalista)-1):
    # - 2 laço começa uma posição depois do primeiro laço e vai ate 
    #a ultima
        for j in range(i+1,len(novalista)):
    #Caso o valor indicado pelo laço for menor que o indicado
    #pelo laço 2, voce deve trocar os valores de lugar
            if novalista[i] < novalista[j]:
                aux = novalista[i]
                novalista[i] = novalista[j]
                novalista[j] = aux
                #novalista[i], novalista[j] = novalista[j], novalista[i]
    return novalista




#dunder methods
if __name__ == "__main__":
    lista1 = [0] * 10
    lista2 = [0] * 10
    for i in range(10):
        print("Digite um numero")
        lista1[i] = int(input())
    for i in range(10):
        print("Digite outro numero")
        lista2[i] = int(input())
    listaresultado = minhafuncao(lista1, lista2)
    print(listaresultado)
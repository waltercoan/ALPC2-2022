'''
5)	Foi realizada uma pesquisa de algumas características 
físicas de cinco habitantes de uma certa região. De 
cada habitante foram coletados os seguintes dados: 
sexo, cor dos olhos (A – Azuis ou C – Castanhos), 
cor dos cabelos (L – Louros, P – Pretos ou C – Castanhos) 
e idade.
a.	Faça uma função que leia esses dados 
em vetores. Determine, por meio de outra função, 
a média de idade das pessoas com olhos castanhos 
e cabelos pretos. Mostre esse resultado 
no programa principal.
b.	Faça uma função que determine e devolva ao programa principal a maior idade entre os habitantes.
c.	Faça uma função que determine e devolva ao programa principal a quantidade de indivíduos do sexo feminino cuja idade está entre 18 e 35 (inclusive) e que tenham olhos azuis e cabelos louros.
'''
sexo = [''] * 5
corolho = [''] * 5
corcabelo = [''] * 5
idade = [0] * 5

def lerdados():
    for i in range(5):
        print("Digite o sexo da pessoa M/F")
        sexo[i] = input()
        print("Digite a cor do olho A – Azuis ou C – Castanhos")
        corolho[i] = input()
        print("Digite a cor do cabelo L – Louros, \
        P – Pretos ou C – Castanhos")
        corcabelo[i] = input()
        print("Digite a idade")
        idade[i] = int(input())

#Determine, por meio de outra função, 
#a média de idade das pessoas com olhos castanhos 
#e cabelos pretos. Mostre esse resultado 
#no programa principal.
def media1():
    soma = 0
    conta = 0 
    global corolho
    global corcabelo
    global idade
    for i in range(5):
        if (corolho[i] == 'C' or corolho[i] == 'c') and \
            (corcabelo[i] == 'P' or corcabelo[i] == 'p'):
            soma += idade[i]
            conta += 1
    media = soma / conta
    return media
#Faça uma função que determine e devolva ao
#  programa principal a maior idade entre
#  os habitantes.
def maioridade():
    global idade
    omaior = idade[0]
    for i in range(5):
        if idade[i] > omaior:
            omaior = idade[i]
    return omaior

#c.	Faça uma função que determine e devolva ao 
# programa principal a quantidade de indivíduos 
# do sexo feminino cuja idade está 
# entre 18 e 35 (inclusive) e que tenham 
# olhos azuis e cabelos louros.
def contapessoas():
    global sexo
    global idade
    global corolho
    global corcabelo
    contador = 0
    for i in range(5):
        if (sexo[i] == "f" or sexo[i] == "F") and \
            (idade[i] > 18 and idade[i] <= 35) and \
            (corolho[i] == 'a' or corolho[i] == 'A') and \
            (corcabelo[i] == 'l' or corcabelo[i] == 'L'):
            contador += 1
    return contador
if __name__ == "__main__":
    lerdados()
    guardarmedia =  media1()
    print(f'A media e {guardarmedia}')
    #print('A media e', guardarmedia)
    guardaromaior = maioridade()
    print(f"A maior idade e {guardaromaior}")
    guardacontagem = contapessoas()
    print(f"A quantidade e {guardacontagem}")
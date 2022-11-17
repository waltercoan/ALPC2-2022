'''
2.	Faça uma função que receba, por parâmetro, a
 altura e o sexo de uma pessoa e retorne o seu 
 peso ideal. Para homens calcular o peso ideal 
 usando a fórmula a seguir: 
 pesoideal = 72.7 * alt – 58 e 
 para mulheres: pesoideal = 62.1 * alt – 44.7
'''
def calcpesoideal(altura:float, sexo:str):
    pesoideal = 0
    if sexo == 'm' or sexo == 'M':
        pesoideal = 72.7 * altura - 58
    else:
        pesoideal = 62.1 * altura - 44.7
    return pesoideal

if __name__ == "__main__":
    print("Digite o sexo da pessoa M/F")
    s = input()
    print("Digite a altura")
    a = float(input())
    print("", end="")
    #peso = calcpesoideal(a, s)
    peso = calcpesoideal(sexo=s , altura=a)
    print(peso)


def minhafuncao(numero:int=0):
    #salario = 10
    print(numero)
    if numero < 100:
        minhafuncao(numero+1)
def soma(num1:float, num2:float):
    resul = num1 + num2
    return resul

def zuera():
    return 1, "qqcoisa", 30.5

print("Passo 1")
print("Passo 2")
#minhafuncao()
guardaroresultado = soma(2,2)
print(guardaroresultado)
print("Passo 3")
x,y,z = zuera()

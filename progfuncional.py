calctab2 = lambda num1,num2: num1 * num2
print(calctab2(7,6))
outrafuncaomuitodoida = calctab2
print(outrafuncaomuitodoida(7,6))

def calctab(num1:int, num2:int):
    return num1 * num2

def gerartabuada(numero, regra):
    for i in range(11):
        print(regra(numero,i))

gerartabuada(7, calctab2)




res = calctab(7,9)
print(res)
num = int(input())
texto = input()

count=0
soma = 0
for i in range(0,num):
    if (texto[i] == "a" or texto[i] == "A"):
        count+=1
    else: 
        if count > 1:
            soma += count
        count=0
print(soma)

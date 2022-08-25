lista = [9,8,7,5,3]

print("Digite o valor procurado")
valproc = int(input())

achei = False
for i in range(5):
    if lista[i] == valproc:
        print("encontrei!!!")
        achei = True
        break
if not achei:
    print("O numero nao foi encontrado")

'''
Faça um programa para corrigir provas de múltipla
escolha com somatória. Cada prova tem dez
questões e cada questão vale 1 ponto. O 
primeiro conjunto de dados a ser lido é o gabarito 
da prova. Os outros dados serão os números dos 
alunos e sua respectivas respostas. Existem 15 
alunos matriculados. Calcule e mostre:
- Para cada aluno seu número e sua nota;
- A percentagem de aprovação, sabendo-se que a nota mínima é 6,0
'''
gaba = [0] * 10
nota = 0
contaaprovados = 0
print("Digite o gabarito")
for i in range(10):
    print("Questao ", i+1,":")
    gaba[i] = int(input())

for aluno in range(15):
    print("Aluno: ", aluno+1)
    print("Digite sua matricula")
    mat = int(input())
    for questao in range(10):
        print("Questao ", questao + 1)
        respaluno = int(input())
        #comparar a resposta do aluno com o gaba
        if respaluno == gaba[questao]:
            #se forem iguais somar um ponto na 
            #nota do aluno
            nota += 1  
    #mostrar a matricula e a nota do aluno
    print("Matricula ", mat)
    print("Nota final ", nota)
    if nota >= 6:
        contaaprovados +=1
    #ZERAR A NOTA DO ALUNO
    nota = 0

#fora dos blocos de repeticao
percaprov = (contaaprovados * 100) / 15
print("O perc de aprovados e ", percaprov)
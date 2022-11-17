class Pessoa:
    def __init__(self,nome:str, idade:int): #construtor
        self.nome = nome
        self.idade = idade
    
    def podeDirigir(self):
        if self.idade >= 18:
            print("pode dirigir")
        else:
            print("não pode dirigir")
    def __repr__(self):
        return f"Nome: {self.nome} \
             - Idade: {self.idade}"
    def __add__(self, x):
        self.idade += x

if __name__ == "__main__":
    #texto = "la" * 100
    #print(texto)
    zezinho = Pessoa("zezinho", 22)
    #zezinho.nome = "zezinho"
    #zezinho.idade = 12
    zezinho + 100
    #print(zezinho.idade)
    #zezinho.podeDirigir()
    print(zezinho)



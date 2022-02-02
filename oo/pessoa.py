class Pessoa:
    olhos = 2
    
    def __init__(self, *filhos, nome:str=None, idade:int=0) -> None:
        self.nome = nome
        self.idade = idade
        self.filhos = filhos
    
    def cumprimentar(self):
        return f"Ola {id(self)}"
        
if __name__ == "__main__":
    luisa = Pessoa(nome="Luisa")
    bruna = Pessoa(nome="Bruna")
    katia = Pessoa(luisa, bruna, nome="Katia")
    print(Pessoa.cumprimentar(katia))
    print(id(katia))
    print(katia.cumprimentar())
    print(katia.nome)
    print(katia.filhos)
    for filho in katia.filhos:
        print(filho.nome)
    
    bruna.olhos = 1
    
    katia.sobrenome = "Faria"
    print(katia.sobrenome)
    del katia.filhos
    print(katia.__dict__)
    print(luisa.__dict__)
    print(bruna.__dict__)
    
    print(Pessoa.olhos)
    print(katia.olhos)
    print(luisa.olhos)
    print(id(Pessoa.olhos), id(katia.olhos), id(luisa.olhos), id(bruna.olhos))
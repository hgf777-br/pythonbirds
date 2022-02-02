class Pessoa:
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
class Pessoa:
    def __init__(self, nome:str=None, idade:int=0) -> None:
        self.nome = nome
        self.idade = idade
    
    def cumprimentar(self):
        return f"Ola {id(self)}"
        
if __name__ == "__main__":
    p = Pessoa()
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
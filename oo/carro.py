class Direcao:
    rumos = ["Norte", "Leste", "Sul", "Oeste"]
    
    def __init__(self, direcao:str="Norte") -> None:
        self.direcao = self.rumos.index(direcao)
    
    def girar_a_direita(self) -> str:
        self.direcao = (self.direcao + 1) % 4
        return self.rumos[self.direcao]
    
    def girar_a_esquerda(self) -> str:
        self.direcao = (self.direcao - 1) % 4
        return self.rumos[self.direcao]
    
    def mostrar_direcao(self) -> str:
        return self.rumos[self.direcao]

class Motor:
    def __init__(self, velocidade:int=0) -> None:
        self.velocidade = velocidade

    def acelerar(self) -> int:
        self.velocidade += 1
        return self.velocidade
    
    def frear(self) -> int:
        self.velocidade -= 2
        self.velocidade = max(0, self.velocidade)
        return self.velocidade
        
        
class Carro:
    def __init__(self, direcao:Direcao, motor:Motor) -> None:
        self.motor = motor
        self.direcao = direcao
        
    def calcular_velocidade(self) -> str:
        return f"velocidade atual: {self.motor.velocidade}"
    
    def acelerar(self) -> None:
        self.motor.acelerar()
    
    def frear(self) -> None:
        self.motor.frear()
        
    def calcular_direcao(self) -> str:
        return f"o carro esta indo para o {self.direcao.mostrar_direcao()}"
    
    def girar_a_direita(self) -> str:
        return f"Virar para o {self.direcao.girar_a_direita()}"
        
    def girar_a_esquerda(self) -> str:
        return f"Virar para o {self.direcao.girar_a_esquerda()}"
    


if __name__ == "__main__":
    motor = Motor()
    direcao = Direcao()
    carro = Carro(direcao, motor)
    
    print(carro.calcular_velocidade())
    print(carro.calcular_direcao())
    print(carro.girar_a_direita())
    print(carro.calcular_direcao())
    print(carro.girar_a_esquerda())
    print(carro.calcular_direcao())
    carro.acelerar()
    carro.acelerar()
    print(carro.calcular_velocidade())
    carro.frear()
    carro.frear()
    carro.frear()
    carro.frear()
    print(carro.calcular_velocidade())
    
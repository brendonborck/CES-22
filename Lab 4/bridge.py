from abc import ABC, abstractmethod

# Cliente --------------------------------------------------------------------------------------------------------------

class Cliente(ABC):
    """
    Cliente
    """

    def __init__(self, type_vehicle, type_engine, color = "branco"):
        
        if type_engine == 1:
            self.engine = MotorEletrico()
        elif type_engine == 2:
            self.engine = MotorCombustao()
        else:
            self.engine = MotorHibrido()

        self.vehicle = Veiculo(self.engine, color)
        if type_vehicle == 1:
            self.vehicle = Caminhao(self.engine, color)
        elif type_vehicle == 2:
            self.vehicle = Carro(self.engine, color)
        elif type_vehicle == 3:
            self.vehicle = Onibus(self.engine, color)

        self.print_vehicle()
        pass

    def print_vehicle(self):
        print("Motor:", self.engine.return_motor())
        print("Cor:", self.vehicle.return_color())
        print("\n")


# Abstraction --------------------------------------------------------------------------------------------------------------

class Motor(ABC):
    """
    Veiculo motorizado
    """

    def __init__(self):
        self._motor = None

    def return_motor(self):
        return self._motor


# Refined Abstractions --------------------------------------------------------------------------------------------------------------

class MotorEletrico(Motor):
    """
    Tipo de motor: eletrico
    """
    def __init__(self):
        self._motor = "elétrico"

class MotorCombustao(Motor):
    """
    Tipo de motor: combustao
    """
    def __init__(self):
        self._motor = "combustão"

class MotorHibrido(Motor):
    """
    Tipo de motor: hibrido
    """
    def __init__(self):
        self._motor = "híbrido"


# Implementation --------------------------------------------------------------------------------------------------------------

class Veiculo(ABC):
    """
    Fabrica de veiculo
    """

    def __init__(self, motor: Motor, color = "branco"):
        self.motor = motor.return_motor()
        self.color = color
    
    def return_color(self):
        return self.color

# Concrete Implementations --------------------------------------------------------------------------------------------------------------

class Caminhao(Veiculo):
    """
    Fabrica: caminhao
    """

    def __init__(self, motor: Motor, color = "branco"):
        super().__init__(motor, color)
        print("Tipo de veículo: Caminhão")

class Carro(Veiculo):
    """
    Fabrica: carro
    """

    def __init__(self, motor: Motor, color = "branco"):
        super().__init__(motor, color)
        print("Tipo de veículo: Carro")

class Onibus(Veiculo):
    """
    Fabrica: onibus
    """

    def __init__(self, motor: Motor, color = "branco"):
        super().__init__(motor, color)
        print("Tipo de veículo: Ônibus")

# Main --------------------------------------------------------------------------------------------------------------

def main():

    print("Cliente requisita carro elétrico")
    Cliente(1, 1)

    print("Cliente requisita caminhão a combustão")
    Cliente(2, 2)

    print("Cliente requisita ônibus híbrido")
    Cliente(3, 3)

    print("Cliente requisita veículo híbrido padrão")
    Cliente(0, 3)

    print("Cliente requisita veículo elétrico rosa")
    Cliente(0, 1, "rosa")

if __name__ == "__main__":
    main()
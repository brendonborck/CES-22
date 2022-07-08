from abc import ABC, abstractmethod

# Produto --------------------------------------------------------------------------------------------------------------

class Bolo(ABC):
    """
    Produto: bolo
    """

    def __init__(self):
        self.cobertura = None
        self.recheio = None

    def set_cobertura(self, cobertura):
        self.cobertura = cobertura

    def set_recheio(self, recheio):
        self.recheio = recheio

    def print_bolo(self):
        print("Cobertura de", self.cobertura)
        print("Recheio de", self.recheio)
        print("\n")


# Construtor Abstrato --------------------------------------------------------------------------------------------------------------

class Construtor(ABC):
    """
    Construtor
    """

    def __init__(self):
        self.reset()

    def reset(self):
        self._product = Bolo()
        
    def print(self):
        self._product.print_bolo() 

    @abstractmethod
    def create_cobertura(self):
        pass

    @abstractmethod
    def create_recheio(self):
        pass


# Diretor --------------------------------------------------------------------------------------------------------------

class Diretor(ABC):
    """
    Diretor
    """

    def __init__(self):
        self._builder = None

    @property
    def builder(self) -> Construtor:
        return self._builder

    @builder.setter
    def builder(self, builder: Construtor):
        self._builder = builder

    def make_bolo(self, type: None):
        bolo_construtor = self._builder
        if type == 1:
            bolo_construtor = BoloAniversarioConstrutor()
        elif type == 2:
            bolo_construtor = BoloCasamentoConstrutor()
        elif type == 3:
            bolo_construtor = BoloFestaConstrutor()
        bolo_construtor.create_cobertura()
        bolo_construtor.create_recheio()
        bolo_construtor.print()
            

# Construtores Concretos --------------------------------------------------------------------------------------------------------------

class BoloAniversarioConstrutor(Construtor):
    """
    Construtor de bolo de aniversario
    """

    def __init__(self):
        self.reset()
        print("Tipo do bolo: Aniversário")

    def create_cobertura(self):
        self._product.cobertura = 'creme de avela'

    def create_recheio(self):
        self._product.recheio = 'chocolate'

class BoloCasamentoConstrutor(Construtor):
    """
    Construtor de bolo de casamento
    """

    def __init__(self):
        self.reset()
        print("Tipo do bolo: Casamento")

    def create_cobertura(self):
        self._product.cobertura = 'merengue'

    def create_recheio(self):
        self._product.recheio = 'mandioca'

class BoloFestaConstrutor(Construtor):
    """
    Construtor de bolo para festa informal
    """

    def __init__(self):
        self.reset()
        print("Tipo do bolo: Festa Informal")

    def create_cobertura(self):
        self._product.cobertura = 'brigadeiro'

    def create_recheio(self):
        self._product.recheio = 'cenoura'


# Main --------------------------------------------------------------------------------------------------------------

def main():

    diretor = Diretor()

    print("Cliente requisita bolo tipo 1")
    diretor.make_bolo(1)

    print("Cliente requisita bolo tipo 2")
    diretor.make_bolo(2)

    print("Cliente requisita bolo tipo 3")
    diretor.make_bolo(3)

if __name__ == "__main__":
    main()
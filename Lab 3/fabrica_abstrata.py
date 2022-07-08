from abc import ABC, abstractmethod

# Cliente --------------------------------------------------------------------------------------------------------------

class Cliente(ABC):
    """
    Cliente
    """

    def __init__(self, type):
        if type == 1:
            self.factory = BoloAniversarioFabrica()
        if type == 2:
            self.factory = BoloCasamentoFabrica()
        if type == 3:
            self.factory = BoloFestaFabrica()
        self.print_products()
        pass

    def print_products(self):
        product_a = self.factory.create_cobertura()
        product_b = self.factory.create_recheio()
        product_a.return_cobertura()
        product_b.return_recheio()
        print("\n")


# Fabrica Abstrata --------------------------------------------------------------------------------------------------------------

class FabricaAbstrata(ABC):
    """
    Fabrica abstrata
    """

    @abstractmethod
    def create_cobertura(self):
        pass

    @abstractmethod
    def create_recheio(self):
        pass


# Fabricas Concretas --------------------------------------------------------------------------------------------------------------

class BoloAniversarioFabrica(FabricaAbstrata):
    """
    Fabrica concreta: bolo de aniversario
    """

    def __init__(self):
        print("Tipo do bolo: Aniversário")

    def create_cobertura(self):
        return BoloAniversarioCobertura()

    def create_recheio(self):
        return BoloAniversarioRecheio()

class BoloCasamentoFabrica(FabricaAbstrata):
    """
    Fabrica concreta: bolo de casamento
    """

    def __init__(self):
        print("Tipo do bolo: Casamento")

    def create_cobertura(self):
        return BoloCasamentoCobertura()

    def create_recheio(self):
        return BoloCasamentoRecheio()

class BoloFestaFabrica(FabricaAbstrata):
    """
    Fabrica concreta: bolo para festa informal
    """

    def __init__(self):
        print("Tipo do bolo: Festa Informal")

    def create_cobertura(self):
        return BoloFestaCobertura()

    def create_recheio(self):
        return BoloFestaRecheio()


# Produtos Abstratos --------------------------------------------------------------------------------------------------------------

class CoberturaProdutoAbstrato(ABC):
    """
    Produto abstrato: tipo de cobertura
    """

    @abstractmethod
    def return_cobertura(self):
        pass


class RecheioProdutoAbstrato(ABC):
    """
    Produto abstrato: tipo de recheio
    """

    @abstractmethod
    def return_recheio(self):
        pass


# Produtos Concretos --------------------------------------------------------------------------------------------------------------

class BoloAniversarioCobertura(CoberturaProdutoAbstrato):
    """
    Produto concreto tipo cobertura: creme de avela
    """

    def return_cobertura(self):
        print("Cobertura de creme de avela")

class BoloCasamentoCobertura(CoberturaProdutoAbstrato):
    """
    Produto concreto tipo cobertura: merengue
    """

    def return_cobertura(self):
        print("Cobertura de merengue")

class BoloFestaCobertura(CoberturaProdutoAbstrato):
    """
    Produto concreto tipo cobertura: brigadeiro
    """

    def return_cobertura(self):
        print("Cobertura de brigadeiro")

class BoloAniversarioRecheio(RecheioProdutoAbstrato):
    """
    Produto concreto tipo recheio: chocolate
    """

    def return_recheio(self):
        print("Recheio de chocolate")

class BoloCasamentoRecheio(RecheioProdutoAbstrato):
    """
    Produto concreto tipo recheio: mandioca
    """

    def return_recheio(self):
        print("Recheio de mandioca")

class BoloFestaRecheio(RecheioProdutoAbstrato):
    """
    Produto concreto tipo cobertura: cenoura
    """

    def return_recheio(self):
        print("Recheio de cenoura")


# Main --------------------------------------------------------------------------------------------------------------

def main():

    print("Cliente requisita bolo tipo 1")
    Cliente(1)

    print("Cliente requisita bolo tipo 2")
    Cliente(2)

    print("Cliente requisita bolo tipo 3")
    Cliente(3)

if __name__ == "__main__":
    main()
from abc import ABC

class PizzaComponent(ABC):

    def getDescription(self):
        return self.__class__.__name__

    def getTotalCost(self):
        return self.__class__.cost

class Place(PizzaComponent):

    cost = 0.05

class Decorator(PizzaComponent):

    def __init__(self, pizzaComponent):
        self.component = pizzaComponent

    def getTotalCost(self):
        return self.component.getTotalCost() + PizzaComponent.getTotalCost(self)

    def getDescription(self):
        return self.component.getDescription() + ' ' + PizzaComponent.getDescription(self)

class Cheese(Decorator):

    cost = 0.4

    def __init__(self, pizzaComponent):
        Decorator.__init__(self, pizzaComponent)

class Dough(Decorator):

    cost = 0.6

    def __init__(self, pizzaComponent):
        Decorator.__init__(self, pizzaComponent)

class TomatoSauce(Decorator):

    cost = 0.5

    def __init__(self, pizzaComponent):
        Decorator.__init__(self, pizzaComponent)

class Pepper(Decorator):

    cost = 0.25

    def __init__(self, pizzaComponent):
        Decorator.__init__(self, pizzaComponent)

class Onion(Decorator):

    cost = 0.2

    def __init__(self, pizzaComponent):
        Decorator.__init__(self, pizzaComponent)

class Pepperoni(Decorator):

    cost = 1.0

    def __init__(self, pizzaComponent):
        Decorator.__init__(self, pizzaComponent)

print("Pepperoni Pizza - description and price")
pepperoni_pizza = Pepperoni(Pepper(Cheese(Onion(TomatoSauce(Dough(Place()))))))
print(pepperoni_pizza.getDescription()+ ': $' + str(pepperoni_pizza.getTotalCost()) + '\n')

double_cheese_pizza = Pepper(Cheese(Cheese(Onion(TomatoSauce(Dough(Place()))))))
print("Double Cheese Pizza - description and price")
print(double_cheese_pizza.getDescription()+ ': $' + str(double_cheese_pizza.getTotalCost()) + '\n')
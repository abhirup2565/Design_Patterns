from abc import ABC, abstractmethod

# ----- Base Component -----
class Coffee(ABC):
    @abstractmethod
    def cost(self):
        pass

# ----- Concrete Component -----
class SimpleCoffee(Coffee):
    def cost(self):
        return 5

# ----- Base Decorator -----
class CoffeeDecorator(Coffee):
    def __init__(self, coffee: Coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost()

# ----- Concrete Decorators -----
class MilkDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 2

class SugarDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 1


if __name__=="__main__":
    coffee = SimpleCoffee()
    print(coffee.cost())  # 5

    milk_coffee = MilkDecorator(coffee)
    print(milk_coffee.cost())  # 7

    sugar_milk_coffee = SugarDecorator(milk_coffee)
    print(sugar_milk_coffee.cost())  # 8

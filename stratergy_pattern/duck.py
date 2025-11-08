from abc import ABC, abstractmethod
from quack import Quack
from fly import FlyWithWings,FlyNoWay

class Duck(ABC):
    def __init__(self, fly_behavior, quack_behavior):
        self.fly_behavior = fly_behavior
        self.quack_behavior = quack_behavior

    def perform_fly(self):
        self.fly_behavior.fly()

    def perform_quack(self):
        self.quack_behavior.quack()

    def swim(self):
        print("All ducks float, even decoys!")

    @abstractmethod
    def display(self):
        pass

class MallardDuck(Duck):
    def __init__(self):
        super().__init__(FlyWithWings(), Quack())

    def display(self):
        print("I'm a real Mallard duck!")

class ModelDuck(Duck):
    def __init__(self):
        super().__init__(FlyNoWay(), Quack())

    def display(self):
        print("I'm a model duck (plastic)!")

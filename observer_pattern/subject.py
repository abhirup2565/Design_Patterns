from abc import ABC,abstractmethod

class Subject(ABC):
    def __init__(self):
        self.observers = []

    def add(self,observer):
        self.observers.append(observer)

    def remove(self,observer):
        self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.update(self)
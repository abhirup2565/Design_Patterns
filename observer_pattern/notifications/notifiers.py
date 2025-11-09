from .base import Observer

class Phone_Display(Observer):
    def update(self,subject):
        temperature = subject.temperature
        print(f"Phone display new Temperature : {temperature} deg C")

class Smartwatch_Display(Observer):
    def update(self,subject):
        temperature = subject.temperature
        print(f"Smartwatch display new Temperature : {temperature} deg C")

class TV_Display(Observer):
    def update(self,subject):
        temperature = subject.temperature
        print(f"TV display new Temperature : {temperature} deg C")
from observer import Observer

class Smartwatch_Display(Observer):
    def update(self,subject):
        temperature = subject.temperature
        print(f"Smartwatch display new Temperature : {temperature} deg C")
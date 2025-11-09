from observer import Observer

class Phone_Display(Observer):
    def update(self,subject):
        temperature = subject.temperature
        print(f"Phone display new Temperature : {temperature} deg C")
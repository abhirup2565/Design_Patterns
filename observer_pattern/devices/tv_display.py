from observer import Observer

class TV_Display(Observer):
    def update(self,subject):
        temperature = subject.temperature
        print(f"TV display new Temperature : {temperature} deg C")
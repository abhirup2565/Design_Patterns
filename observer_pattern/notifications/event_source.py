from .base import Subject

class WeatherStation(Subject):
    def __init__(self):
        super().__init__()
        self._temperature = 0

    @property
    def temperature(self):
        return self._temperature
    
    @temperature.setter
    def temperature(self,value):
        self._temperature = value
        print(f"Weather station temperature updated to {value}")
        self.notify()
from weather_station import WeatherStation
from devices.phone_display import Phone_Display
from devices.tv_display import TV_Display
from devices.smartwatch_display import Smartwatch_Display

if __name__ == "__main__":
    station = WeatherStation()
    phone = Phone_Display()
    tv = TV_Display()
    watch = Smartwatch_Display()

    station.add(phone)
    station.add(tv)
    station.add(watch)

    station.temperature = 30
    station.temperature = 25

    station.remove(tv)
    station.temperature = 20
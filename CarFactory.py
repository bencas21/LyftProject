from car import Car
from abc import ABC
from capulet_engine import CapuletEngine
from SpindlerBattery import SpindlerBattery
from willoughby_engine import WilloughbyEngine
from sternman_engine import SternmanEngine
from NubbinBattery import NubbinBattery

class CarFactory(Car,ABC):
    def create_calliope(current_date,last_service_date,current_milage,last_service_milage):
        newEngine = CapuletEngine(last_service_milage,current_milage)
        newBat = SpindlerBattery(last_service_date, current_date)
        newCar = Car(newEngine,newBat)
        return newCar
    def create_glissade(current_date,last_service_date,current_milage,last_service_milage):
        newEngine = WilloughbyEngine(last_service_milage,current_milage)
        newBat = SpindlerBattery(last_service_date, current_date)
        newCar = Car(newEngine,newBat)
        return newCar
    def create_palindrome(current_date,last_service_date,warning_light_on):
        newEngine = SternmanEngine(warning_light_on)
        newBat = SpindlerBattery(last_service_date, current_date)
        newCar = Car(newEngine,newBat)
        return newCar
    def create_rorschach(current_date,last_service_date,current_milage,last_service_milage):
        newEngine = WilloughbyEngine(last_service_milage,current_milage)
        newBat = NubbinBattery(last_service_date, current_date)
        newCar = Car(newEngine,newBat)
        return newCar
    def create_glissade(current_date,last_service_date,current_milage,last_service_milage):
        newEngine = CapuletEngine(last_service_milage,current_milage)
        newBat = NubbinBattery(last_service_date, current_date)
        newCar = Car(newEngine,newBat)
        return newCar






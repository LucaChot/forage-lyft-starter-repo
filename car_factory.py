from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from car import Car
from tires.carrigan import Carrigan
from tires.octoprime import Octoprime

class CarFactory():

    @classmethod
    def create_calliope(cls, last_service_date, current_mileage, last_service_mileage, tires):
        return Car(CapuletEngine(current_mileage, last_service_mileage), SpindlerBattery(last_service_date), Carrigan(tires))

    @classmethod
    def create_glissade(cls, last_service_date, current_mileage, last_service_mileage, tires):
        return Car(WilloughbyEngine(current_mileage, last_service_mileage), SpindlerBattery(last_service_date), Octoprime(tires))

    @classmethod
    def create_palindrome(cls, last_service_date, warning_light_on, tires):
        return Car(SternmanEngine(warning_light_on), SpindlerBattery(last_service_date), Carrigan(tires))

    @classmethod
    def create_rorschach(cls, last_service_date, current_mileage, last_service_mileage, tires):
        return Car(WilloughbyEngine(current_mileage, last_service_mileage), NubbinBattery(last_service_date), Octoprime(tires))

    @classmethod
    def create_thovex(cls, last_service_date, current_mileage, last_service_mileage, tires):
        return Car(CapuletEngine(current_mileage, last_service_mileage), NubbinBattery(last_service_date), Carrigan(tires))
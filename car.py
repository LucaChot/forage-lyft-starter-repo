from abc import ABC
from serviceable import Serviceable

class Car(Serviceable, ABC):
    def __init__(self,engine, battery, tires):
        self.engine = engine
        self.battery = battery
        self.tires = tires


    def needs_service(self):
        return self.engine.engine_should_be_serviced() or self.battery.needs_service()


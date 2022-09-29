from abc import ABC
from tires.tire import Tire

class Carrigan(Tire, ABC):

    def tire_should_be_serviced(self):
        for i in self.values:
            if i >= 0.9:
                return True
        return False
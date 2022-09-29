from abc import ABC
from tires.tire import Tire

class Octoprime(Tire, ABC):

    def tire_should_be_serviced(self):
        total = 0
        for i in self.values:
            total += i

        if total >= 3:
            return True
        else:
            return False
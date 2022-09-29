from abc import ABC, abstractmethod

class Tire(ABC):
    def __init__(self, values):
        self.values = values

    @abstractmethod
    def tire_should_be_serviced(self):
        pass
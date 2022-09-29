import unittest

from tires.carrigan import Carrigan
from tires.octoprime import Octoprime

class TestCarrigon(unittest.TestCase):

    def test_tires_should_not_be_serviced(self):
        values = [0.89, 0.7, 0.1, 0.6]

        tires = Carrigan(values)
        self.assertFalse(tires.tire_should_be_serviced())

    def test_tires_should_be_serviced(self):
        values = [0.89, 0.9, 0.1, 0.6]

        tires = Carrigan(values)
        self.assertTrue(tires.tire_should_be_serviced())

    def test_tires_should_be_serviced_cont(self):
        values = [0.89, 0.9, 0.9, 0.6]

        tires = Carrigan(values)
        self.assertTrue(tires.tire_should_be_serviced())


class TestOctoprime(unittest.TestCase):

    def test_tires_should_not_be_serviced(self):
        values = [0.89, 0.7, 0.1, 0.6]

        tires = Octoprime(values)
        self.assertFalse(tires.tire_should_be_serviced())

    def test_tires_should_be_serviced(self):
        values = [0.75, 0.75, 0.75, 0.75]

        tires = Octoprime(values)
        self.assertTrue(tires.tire_should_be_serviced())

    def test_tires_should_be_serviced_cont(self):
        values = [0.80, 0.9, 0.9, 0.8]

        tires = Octoprime(values)
        self.assertTrue(tires.tire_should_be_serviced())

if __name__ == '__main__':
    unittest.main()
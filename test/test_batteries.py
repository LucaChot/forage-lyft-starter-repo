import unittest
from datetime import datetime

from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery

class Spindler(unittest.TestCase):

    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)

        battery = SpindlerBattery(last_service_date)
        self.assertTrue(battery.needs_service())

    def test_battery_should__not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 2)

        battery = SpindlerBattery(last_service_date)
        self.assertFalse(battery.needs_service())

class Nubbin(unittest.TestCase):

    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)

        battery = NubbinBattery(last_service_date)
        self.assertTrue(battery.needs_service())

    def test_battery_should__not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)

        battery = NubbinBattery(last_service_date)
        self.assertFalse(battery.needs_service())

if __name__ == '__main__':
    unittest.main()
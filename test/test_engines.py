import unittest
from datetime import datetime

from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

class Capulet(unittest.TestCase):

    def test_engine_should_be_serviced(self):
        current_mileage = 30001
        last_service_mileage = 0

        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.engine_should_be_serviced())

    def test_engine_should_not_be_serviced(self):
        current_mileage = 30000
        last_service_mileage = 0

        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.engine_should_be_serviced())


class Willboughby(unittest.TestCase):

    def test_engine_should_be_serviced(self):
        current_mileage = 60001
        last_service_mileage = 0


        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.engine_should_be_serviced())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0


        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.engine_should_be_serviced())

class Sternman(unittest.TestCase):

    def test_engine_should_be_serviced(self):
        warning_light_is_on = True

        engine = SternmanEngine(warning_light_is_on)
        self.assertTrue(engine.engine_should_be_serviced())

    def test_engine_should_not_be_serviced(self):
        warning_light_is_on = False

        engine = SternmanEngine(warning_light_is_on)
        self.assertFalse(engine.engine_should_be_serviced())

if __name__ == '__main__':
    unittest.main()
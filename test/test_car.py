import unittest
from datetime import datetime

from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine 
from engine.willoughby_engine import WilloughbyEngine
from battery.SpindlerBattery import SpindlerBattery
from battery.NubbinBattery import NubbinBattery


class TestCapuletEngine(unittest.TestCase):

    def test_engine_should_be_serviced(self):
        current_mileage = 30001
        last_service_mileage = 0

        TestEngine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(CapuletEngine.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_mileage = 30000
        last_service_mileage = 0

        TestEngine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(CapuletEngine.needs_service())


class TestWilloughbyEngine(unittest.TestCase):

    def test_engine_should_be_serviced(self):
        current_mileage = 60001
        last_service_mileage = 0

        TestEngine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(TestEngine.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_mileage = 60000
        last_service_mileage = 0

        TestEngine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(TestEngine.needs_service())


class TestSternmanEngine(unittest.TestCase):

    def test_engine_should_be_serviced(self):
        warning_light_is_on = True

        TestEngine = SternmanEngine(warning_light_is_on)
        self.assertTrue(TestEngine.needs_service())

    def test_engine_should_not_be_serviced(self):
        warning_light_is_on = False

        TestEngine = SternmanEngine(warning_light_is_on)
        self.assertFalse(TestEngine.needs_service())


class TestNubbinBattery(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)

        TestBattery = NubbinBattery(last_service_date, today)
        self.assertTrue(NubbinBattery.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)

        car = NubbinBattery(last_service_date, today)
        self.assertFalse(NubbinBattery.needs_service())


class TestSpindlerBattery(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)

        TestBattery = SpindlerBattery(last_service_date, today)
        self.assertTrue(TestBattery.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)

        TestBattery = SpindlerBattery(last_service_date, today)
        self.assertFalse(TestBattery.needs_service())


if __name__ == '__main__':
    unittest.main()

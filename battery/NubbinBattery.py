from abc import ABC
from battery.battery import Battery

class NubbinBattery(Battery, ABC):
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        date_to_be_serviced = add_years(self.last_service_date,4)
        if date_to_be_serviced < self.current_date:
            return True
        else:
            return False


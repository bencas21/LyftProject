from abc import ABC
from tires.tires import Tires

class OctoprimeTires(Tires,ABC):
    def __init__(self, ArrayOfTires):
        self.ArrayOfTires = ArrayOfTires

    def needs_service(self):
        sum = 0
        for tire in ArrayOfTires:
            sum += tire
        
        if sum >= 3
            return true

        return false
~


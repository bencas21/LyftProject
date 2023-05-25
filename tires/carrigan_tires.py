from abc import ABC
from tires.tires import Tires

class CarriganTires(Tires,ABC):
    def __init__(self, ArrayOfTires):
        self.ArrayOfTires = ArrayOfTires
    
    def needs_service(self):
        for tire in ArrayOfTires:
            if tire >= 0.9:
                return true

        return false 

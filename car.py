from Serviceable import Serviceable 

class Car(Serviceable):
    def __init__(self, engine, battery,tires):
        self.engine = engine
        self.Battery = battery 
        self.Tires = tires 

    def needs_service(self):
        if self.engine.needs_service() or self.Battery.needs_service() or self.Tires.needs_service():
            return true
        else:
            return false

from abc import ABC, abstractmethod
from Serviceable import Serviceable
from engine import engine 
from battery import Battery 

class Car(Serviceable):
    def __init__(self, engine, battery):
        self.engine = engine
        self.Battery = battery 

    def needs_service(self):
        if self.engine.needs_service() or self.batter.needs_service():
            return true
        else:
            return false

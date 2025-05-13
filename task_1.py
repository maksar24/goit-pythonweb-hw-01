from abc import ABC, abstractmethod
from logger import logger


class Vehicle(ABC):
    def __init__(self, make: str, model: str, spec: str) -> None:
        self.make = make
        self.model = model
        self.spec = spec

    @abstractmethod
    def start_engine(self) -> None:
        pass


class Car(Vehicle):
    def start_engine(self) -> None:
        logger.info(f"{self.make} {self.model} ({self.spec}): Двигун запущено")


class Motorcycle(Vehicle):
    def start_engine(self) -> None:
        logger.info(f"{self.make} {self.model} ({self.spec}): Мотор заведено")


class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make: str, model: str) -> Vehicle:
        pass

    @abstractmethod
    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        pass


class USVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Car:
        return Car(make, model, "US Spec")

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        return Motorcycle(make, model, "US Spec")


class EUVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Car:
        return Car(make, model, "EU Spec")

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        return Motorcycle(make, model, "EU Spec")


# Використання
us_factory = USVehicleFactory()
vehicle1 = us_factory.create_car("Dodge", "SRT")
vehicle1.start_engine()

vehicle2 = us_factory.create_motorcycle("Harley-Davidson", "Sportster")
vehicle2.start_engine()

eu_factory = EUVehicleFactory()
vehicle3 = eu_factory.create_car("Volkswagen", "Golf")
vehicle3.start_engine()

vehicle4 = eu_factory.create_motorcycle("BMW", "R1200GS")
vehicle4.start_engine()

# Multiple Inheritance
# Problem: Create two classes Battery and Engine, and let the ElectricCar class inherit from both, demostrating  multiple inheritance.

class Battery:
    def __init__(self, battery):
        self.battery=battery

class Engine:
    def __init__(self, engine):
        self.engine=engine

class ElectricCar(Battery, Engine):
    def __init__(self, battery, engine, battery_size):
        Battery.__init__(self,battery)
        Engine.__init__(self, engine)
        self.battery_size=battery_size

my_car=ElectricCar("BATTERY", "ENGINE", "SIZE")
print(my_car.battery)

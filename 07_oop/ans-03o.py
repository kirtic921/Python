# Inheritance
# Problem: Create an ElectricCar class that inherits from the Car class and has an additional attribute battery_size.

class Car:
    def __init__(self, brand, model):
        self.brand=brand
        self.model=model

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        # instead of again writing self.brand and  self.model n all, write the above command
        self.battery_size=battery_size

my_car=Car("Tata", "Safari")
print(my_car.brand)

my_tesla=ElectricCar("Tesla", "Model-s", "346kwwh")
print(my_tesla.battery_size)
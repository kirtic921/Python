# Polymorphism
# Problem: Demonstrate polymorphism by defining a method fuel_type in both Car and ElectricCar classes, but with different behaviors.

class Car:
    def __init__(self, brand, model):
        self.brand=brand
        self.model=model
    def fuel_type(self):
        return "petrol and diesel"
    

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        # instead of again writing self.brand and  self.model n all, write the above command
        self.battery_size=battery_size
    def fuel_type(self):
        return "electric charge"


my_car=Car("Tata", "Safari")
print(my_car.fuel_type())

my_tesla=ElectricCar("Tesla", "Model-s", "346kwwh")
print(my_tesla.fuel_type())
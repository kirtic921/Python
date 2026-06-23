# Static method
# Problem: Add a static method to the Car class that returns a general description of a car.

class Car:
    def __init__(self, brand, model):
        self.brand=brand
        self.model=model
    @staticmethod
    def description():                       
        return "Cars are machines"


# here, didnt put (self) only (), as staticmethod already can be accessed via classes only and not by objects no need to link it using self


my_car=("Tesla", "Model-s")
# print(my_car.description())
print(Car.description())
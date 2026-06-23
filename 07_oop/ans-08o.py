# Property decorators
# Problem: Use a property decorator in the class Car to make the model attribute read only.

class Car:
    def __init__(self, brand, model):
        self.brand=brand
        self.model=model
    @property
    def read_model(self):
        return self.__model


my_car=Car("Toyota", "Corolla")
my_car.Car="Model-s"
print(my_car.model)

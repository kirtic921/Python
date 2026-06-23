# Encapsulation
# Problem: Modify the Car class to encapsulate the brand attribute, making it private, and provide a getter method for it.

class Car:
    def __init__(self, brand, model):
        self.__brand=brand
        self.model=model
    def get_brand(self):
        return self.__brand

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        # instead of again writing self.brand and  self.model n all, write the above command
        self.battery_size=battery_size


my_tesla=ElectricCar("Tesla", "Model-s", "346kwwh")
# print(my_tesla.__brand)
print(my_tesla.get_brand())

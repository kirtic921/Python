# Class Variables
# Problem: Add a class variable to Car that keeps track of the number of cars created.

class Car:
    total_cars=0
    def __init__ (self, brand, model):
        self.brand=brand
        self.model=model
        Car.total_cars+=1

Car("Tata", "Safari")
Car("Tesla", "Model-s")

print(Car.total_cars)

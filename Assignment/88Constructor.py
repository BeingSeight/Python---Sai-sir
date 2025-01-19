# 88. Constructor
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

car = Car("Toyota", "Camry", 2020)
print(car.make, car.model, car.year)

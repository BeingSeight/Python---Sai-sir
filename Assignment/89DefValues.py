# 89. Class with Default Values
class CarWithDefaults:
    def __init__(self, make="Default Make", model="Default Model", year=2020):
        self.make = make
        self.model = model
        self.year = year

car = CarWithDefaults()
print(car.make, car.model, car.year)
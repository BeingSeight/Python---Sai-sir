# 93. Encapsulation
class EncapsulationDemo:
    def __init__(self):
        self.__private_attribute = 0

    def get_private_attribute(self):
        return self.__private_attribute

    def set_private_attribute(self, value):
        if value >= 0:
            self.__private_attribute = value
        else:
            print("Value must be non-negative")

obj = EncapsulationDemo()
obj.set_private_attribute(10)
print("Private attribute:", obj.get_private_attribute())
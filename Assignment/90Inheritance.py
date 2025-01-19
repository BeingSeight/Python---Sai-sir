# 90. Inheritance
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Some sound")

class Dog(Animal):
    pass

dog = Dog("Buddy")
print(dog.name)
dog.speak()
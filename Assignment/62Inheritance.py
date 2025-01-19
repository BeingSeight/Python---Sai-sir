# 62. Class Inheritance
class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    def speak(self):
        print("Woof!")

animal = Animal()
animal.speak()
dog = Dog()
dog.speak()
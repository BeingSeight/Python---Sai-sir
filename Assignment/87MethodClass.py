# 87. Method in Class
class PersonWithGreet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name}.")
person = PersonWithGreet("Alice", 30)
person.greet()

# 86. Simple Class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
person = Person("Alice", 30)
print(person.name, person.age)
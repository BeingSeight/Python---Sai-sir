# 91. Method Overriding
class AnimalWithSpeak:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Some sound")

class DogWithOverride(AnimalWithSpeak):
    def speak(self):
        print("Woof!")

dog = DogWithOverride("Buddy")
dog.speak()
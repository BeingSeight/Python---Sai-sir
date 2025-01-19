# 94. Polymorphism
class Circle:
    def draw(self):
        print("Drawing a Circle")

class Triangle:
    def draw(self):
        print("Drawing a Triangle")

shapes = [Circle(), Triangle()]
for shape in shapes:
    shape.draw()
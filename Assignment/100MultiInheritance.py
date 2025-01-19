 # 100. Multiple Inheritance
class Parent1:
    def feature1(self):
        print("Feature 1 from Parent1")

class Parent2:
    def feature2(self):
        print("Feature 2 from Parent2")

class Child(Parent1, Parent2):
    def feature3(self):
        print("Feature 3 from Child")

child = Child()
child.feature1()
child.feature2()
child.feature3()

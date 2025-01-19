# 95. Class Method & Static Method
class Counter:
    count = 0

    @classmethod
    def increment(cls):
        cls.count += 1

    @staticmethod
    def display_message():
        print("This is a static method in the Counter class.")

Counter.increment()
Counter.display_message()
print("Count:", Counter.count)
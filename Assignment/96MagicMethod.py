# 96. Magic Methods
class MagicMethodDemo:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"MagicMethodDemo with value {self.value}"

obj = MagicMethodDemo(42)
print(obj)
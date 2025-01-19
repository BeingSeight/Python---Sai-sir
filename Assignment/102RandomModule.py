# 102. Use Random Module
import random

def random_element(lst):
    return random.choice(lst)

elements = [1, 2, 3, 4, 5]
print("Random element:", random_element(elements))
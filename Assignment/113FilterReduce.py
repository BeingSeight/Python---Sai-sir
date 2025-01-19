# 113. Filter & Reduce
from functools import reduce

numbers = [1, 2, 3, 4, 5, 6]
filtered = list(filter(lambda x: x % 2 != 0, numbers))
summed = reduce(lambda x, y: x + y, filtered)
print("Sum of odd numbers:", summed)
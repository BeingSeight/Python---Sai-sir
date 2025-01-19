# 46. Frequency of Elements
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
frequency = {}
for num in numbers:
    frequency[num] = frequency.get(num, 0) + 1
print(f"Frequency of elements: {frequency}")
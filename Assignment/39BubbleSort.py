# 39. Bubble Sort
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
n = len(numbers)
for i in range(n - 1):
    for j in range(n - i - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
print(f"Sorted list: {numbers}")
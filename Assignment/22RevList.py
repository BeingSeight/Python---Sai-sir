# 22. Reverse List (in-place)
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
n = len(numbers)
for i in range(n // 2):
    numbers[i], numbers[n - i - 1] = numbers[n - i - 1], numbers[i]
print(f"Reversed list: {numbers}")
# Minimum & Maximum in List (without min() or max())
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
minimum = maximum = numbers[0]
for num in numbers:
    if num < minimum:
        minimum = num
    if num > maximum:
        maximum = num
print(f"Minimum value: {minimum}")
print(f"Maximum value: {maximum}")
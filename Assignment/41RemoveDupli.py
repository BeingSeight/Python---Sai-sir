# 41. Remove Duplicates from List
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
unique_numbers = list(set(numbers))
print(f"List without duplicates: {unique_numbers}")
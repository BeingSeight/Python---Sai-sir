# 23. Count Occurrences in List
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
target = int(input("Enter the number to count: "))
count = sum(1 for num in numbers if num == target)
print(f"{target} appears {count} times.")
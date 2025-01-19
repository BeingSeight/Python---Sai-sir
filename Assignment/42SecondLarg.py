# 42. Second Largest Element
numbers = sorted(set(map(int, input("Enter unique numbers: ").split())), reverse=True)
if len(numbers) < 2:
    print("At least two unique numbers are required.")
else:
    print(f"The second largest element is: {numbers[1]}")
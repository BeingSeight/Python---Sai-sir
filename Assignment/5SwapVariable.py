# Write a program that swaps the values of two variables without using a temporary variable



num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2
print("After swapping: num1 = " + str(num1) + ", num2 = " + str(num2))

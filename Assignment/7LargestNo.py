# Prompt the user for three numbers and determine which one is the largest.
num1 = int(input("Enter a number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
if (num1 > num2) and (num1 > num3):
    print("The largest number is " + str(num1))
elif (num2 > num1) and (num2 > num3):
    print("The largest number is " + str(num2))
else:
    print("The largest number is " + str(num3))

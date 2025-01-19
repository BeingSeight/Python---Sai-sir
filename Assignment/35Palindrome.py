# 35. Palindrome Check (Number)
num = input("\nEnter a number: ")
if num == num[::-1]:
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")
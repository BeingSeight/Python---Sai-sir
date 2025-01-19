# 56. Exception Handling
def safe_int_conversion(s):
    try:
        return int(s)
    except ValueError:
        print("Invalid input: not an integer.")

value = input("Enter a number: ")
safe_int_conversion(value)

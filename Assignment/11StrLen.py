# Write a function that returns the length of a string without using the built-in len().

def str_len(string):
    count = 0
    for i in string:
        count += 1
    return count

string = input("Enter a string: ")
print("Length of the string is: ", str_len(string))

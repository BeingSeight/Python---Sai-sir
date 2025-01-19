# 51. File Read
file_name = input("Enter the file name to read: ")
try:
    with open(file_name, 'r') as file:
        print(file.read())
except FileNotFoundError:
    print("File not found.")

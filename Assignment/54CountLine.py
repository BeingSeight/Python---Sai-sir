# 54. Count Lines in File
file_name = input("Enter the file name: ")
try:
    with open(file_name, "r") as file:
        line_count = sum(1 for _ in file)
    print(f"The file contains {line_count} lines.")
except FileNotFoundError:
    print("File not found.")
# 53. File Copy
source = input("Enter the source file name: ")
destination = input("Enter the destination file name: ")
try:
    with open(source, "r") as src, open(destination, "w") as dest:
        dest.write(src.read())
    print(f"Contents copied from {source} to {destination}.")
except FileNotFoundError:
    print("Source file not found.")
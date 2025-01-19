# 52. File Write
text = input("Enter a string to write to a file: ")
with open("output.txt", "w") as file:
    file.write(text)
print("Text written to output.txt")
# 77. Write File
def write_to_file(file_path: str):
    line = input("Enter a line of text to write to the file: ")
    with open(file_path, 'w') as file:
        file.write(line)
write_to_file("output.txt")
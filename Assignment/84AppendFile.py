# 84. Append to File
def append_to_file(file_path: str):
    line = input("Enter a line of text to append to the file: ")
    with open(file_path, 'a') as file:
        file.write(line + '\n')
append_to_file("example.txt")
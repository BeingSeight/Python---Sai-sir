# 76. Read File
def read_file(file_path: str):
    try:
        with open(file_path, 'r') as file:
            contents = file.read()
            print(contents)
    except FileNotFoundError:
        print("File not found.")
read_file("example.txt")
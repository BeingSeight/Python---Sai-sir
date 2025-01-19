# 80. Line Count
def count_lines(file_path: str):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            print(len(lines))
    except FileNotFoundError:
        print("File not found.")
count_lines("example.txt")
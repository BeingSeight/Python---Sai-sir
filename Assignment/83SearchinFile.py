# 83. Search in File
def search_in_file(file_path: str, substring: str):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            for i, line in enumerate(lines, start=1):
                if substring in line:
                    print(f"Line {i}: {line.strip()}")
    except FileNotFoundError:
        print("File not found.")
search_in_file("example.txt", "search_term")
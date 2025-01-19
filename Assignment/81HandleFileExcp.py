# 81. Handle File Exceptions
def read_file_with_exceptions(file_path: str):
    try:
        with open(file_path, 'r') as file:
            contents = file.read()
            print(contents)
    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
read_file_with_exceptions("example.txt")
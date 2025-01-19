# 78. Copy File
def copy_file(source_path: str, dest_path: str):
    try:
        with open(source_path, 'r') as source_file:
            contents = source_file.read()
        with open(dest_path, 'w') as dest_file:
            dest_file.write(contents)
    except FileNotFoundError:
        print("Source file not found.")
copy_file("source.txt", "destination.txt")
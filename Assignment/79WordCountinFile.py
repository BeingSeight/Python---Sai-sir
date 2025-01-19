# 79. Word Count in File
def count_words(file_path: str):
    try:
        with open(file_path, 'r') as file:
            contents = file.read()
            words = contents.split()
            print(len(words))
    except FileNotFoundError:
        print("File not found.")
count_words("example.txt")
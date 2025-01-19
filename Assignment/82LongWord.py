# 82. Find Longest Word in File
def find_longest_word(file_path: str):
    try:
        with open(file_path, 'r') as file:
            words = file.read().split()
            longest_word = max(words, key=len)
            print(longest_word)
    except FileNotFoundError:
        print("File not found.")
find_longest_word("example.txt")
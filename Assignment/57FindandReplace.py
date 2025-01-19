# 57. Find & Replace in File
file_name = input("Enter the file name: ")
find_word = input("Enter the word to search for: ")
replace_word = input("Enter the replacement word: ")
try:
    with open(file_name, "r+") as file:
        content = file.read()
        content = content.replace(find_word, replace_word)
        file.seek(0)
        file.write(content)
        file.truncate()
    print("Replacement completed.")
except FileNotFoundError:
    print("File not found.")
string = input("Enter a string: ").lower()
vowel_count = sum(char in 'aeiou' for char in string)
print(f"Number of vowels: {vowel_count}")
# 72. Count Vowels (Recursive)
def count_vowels(s: str) -> int:
    if not s:
        return 0
    return (s[0].lower() in 'aeiou') + count_vowels(s[1:])

print(count_vowels("Recursive"))
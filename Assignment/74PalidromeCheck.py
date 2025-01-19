# 74. Palindrome Check (Recursive)
def is_palindrome(s: str) -> bool:
    s = ''.join(filter(str.isalnum, s)).lower()
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

print(is_palindrome("Able was I ere I saw Elba"))
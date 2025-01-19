# 26. Check Substring
s = input("Enter a string: ")
sub = input("Enter the substring to check: ")
if sub in s:
    print(f"'{sub}' is present in the string.")
else:
    print(f"'{sub}' is not present in the string.")
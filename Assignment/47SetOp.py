# 47. Set Operations
set1 = set(map(int, input("Enter elements of set1 separated by spaces: ").split()))
set2 = set(map(int, input("Enter elements of set2 separated by spaces: ").split()))
print(f"Union: {set1 | set2}")
print(f"Intersection: {set1 & set2}")
print(f"Difference (set1 - set2): {set1 - set2}")

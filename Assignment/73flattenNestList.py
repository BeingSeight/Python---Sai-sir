# 73. Flatten Nested List (Recursive)
def flatten(lst: list) -> list:
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result
print(flatten([1, [2, [3, 4], 5], 6]))
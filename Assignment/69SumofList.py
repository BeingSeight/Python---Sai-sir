# 69. Sum of List (Recursive)
def sum_list(lst: list) -> int:
    if not lst:
        return 0
    return lst[0] + sum_list(lst[1:])

print(sum_list([1, 2, 3, 4, 5]))
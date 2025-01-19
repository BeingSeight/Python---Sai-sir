# 70. Binary Search (Recursive)
def binary_search(arr: list, target: int, left: int, right: int) -> int:
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, right)
    else:
        return binary_search(arr, target, left, mid - 1)

print(binary_search([1, 2, 3, 4, 5], 3, 0, 4))
# 40. Binary Search (Iterative)
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
sorted_list = sorted(map(int, input("Enter a sorted list of numbers: ").split()))
target = int(input("Enter the number to search for: "))
position = binary_search(sorted_list, target)
if position != -1:
    print(f"Number found at index: {position}")
else:
    print("Number not found.")
# 48. Recursive Sum of List
def recursive_sum(lst):
    if not lst:
        return 0
    return lst[0] + recursive_sum(lst[1:])
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
print(f"The sum of the list is: {recursive_sum(numbers)}")
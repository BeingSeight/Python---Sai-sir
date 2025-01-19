# 44. Dictionary of Squares
n = int(input("Enter a number: "))
squares_dict = {x: x**2 for x in range(1, n + 1)}
print(f"Dictionary of squares: {squares_dict}")
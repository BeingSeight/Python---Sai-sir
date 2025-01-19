# 32. Fibonacci Sequence
n = int(input("Enter the number of Fibonacci numbers to display: "))
a, b = 0, 1
print("Fibonacci sequence:")
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
base = float(input("Enter the base: "))
exponent = int(input("Enter the exponent: "))
result = 1
for i in range(abs(exponent)):
    result *= base
result = result if exponent >= 0 else 1 / result
print(f"The result of {base} raised to the power of {exponent} is: {result}")
# 68. Power Function
def power(base: int, exp: int) -> int:
    if exp == 0:
        return 1
    return base * power(base, exp - 1)

print(power(2, 3))
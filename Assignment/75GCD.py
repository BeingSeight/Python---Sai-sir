# 75. GCD (Recursive)
def gcd(a: int, b: int) -> int:
    if b == 0:
        return a
    return gcd(b, a % b)
gcd(48, 18)

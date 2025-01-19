# 50. LCM
def lcm(a, b):
    return abs(a * b) // gcd(a, b)

print(f"The LCM of {a} and {b} is: {lcm(a, b)}")

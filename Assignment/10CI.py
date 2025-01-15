# Prompt for principal, rate, and time to calculate compound interest.

P = float(input("Enter the principle amount: "))
R = float(input("Enter the rate of interest: "))
T = float(input("Enter the time in years: "))
n = int(input("Enter the number of times interest is compounded per year: "))

CI = P * (1 + R/n)**(n*T) - P
print("Compound Interest is " + str(CI))

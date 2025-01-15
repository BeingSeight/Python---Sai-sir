# Prompt for principal, rate, and time to calculate simple interest

P = float(input("Enter the principle amount: "))
R = float(input("Enter the rate of interest: "))
T = float(input("Enter the time in years: "))

SI = (P * R * T) / 100
print("Simple Interest: ", str(SI))

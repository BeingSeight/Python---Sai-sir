# Multiples from 1 to 30
# num = int(input("Enter a number"))
# for i in range(1,31):
#    print(num, "x", i, "=", num*i)

# to print *
# for i in range(1, 6):
#    print("*"*i)

# to find if a number is prime or not
num = int(input("Enter a number"))
prime = False
for i in range(2, num/2):
    if (num*i == 0):
        prime = False
    if (prime):
        print("Prime number")
    else:
        print("Not a prime number")
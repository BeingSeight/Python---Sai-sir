# 36. Guess the Number (Game)
import random
target = random.randint(1, 10)
guess = None
while guess != target:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess < target:
        print("Too low!")
    elif guess > target:
        print("Too high!")
    else:
        print("You guessed it!")
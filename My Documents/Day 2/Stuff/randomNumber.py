import random
x = random.randint(0,100)
while True:
    guess = int(input("Guess a number 0-100: "))
    if guess == x:
        print("You got it",x, " !")
        break
    elif guess < x:
        print("Too low!")
    elif guess > x:
        print("Too high!")
    else
        print("HOW?")
print("The number is ". x)

from random import randrange

number = randrange(101)
count = 1

print("I've generated a number between 0-100, try to guess")

while True:
    guess = int(input(f"Guess #{count}: "))

    if guess < number:
        print("Increase!")
    elif guess > number:
        print("Decrease")
    else:
        print("That's correct my friend!")
        break

    count += 1

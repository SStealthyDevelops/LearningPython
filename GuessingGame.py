# Generate a random number between 1 an 100
# Guess the number (up to X amount of times)
# The game will tell you if you are getting closer or further
# Fully developed by Satvik Mathur.


import random
import math

randomNum = random.randint(1, 100)

guess = -1

previousGuess = -1

totalGuesses = 0
allowedGuesses = 10


# Attempt a guess
def attemptGuess():
    global totalGuesses
    global guess
    global previousGuess
    global allowedGuesses

    # Set previous guess before setting the new guess
    previousGuess = guess
    guess = input("What is your guess?")

    if not guess.isnumeric():
        print("Enter a number!")
        attemptGuess()

    if totalGuesses >= allowedGuesses:
        lose()

    guess = int(guess)

    if guess == randomNum:
        win()
    else:
        totalGuesses += 1
        checkResult(previousGuess, guess)
        attemptGuess()


# Colder or Warmer?
def checkResult(lastGuess, recentGuess):
    global totalGuesses

    if totalGuesses == 1:
        print("Try again!")
        return

# If the new guess is further from the true number than the old guess, it is colder. If not, it is warmer (or
    # equidistant)
    if abs((randomNum - lastGuess)) < abs((randomNum - recentGuess)):
        print("Colder!!")
    else:
        print("Warmer!!")


def win():
    print("You win!")
    exit(1)


def lose():
    print("You lost!!!!! The number was " + str(randomNum))
    exit(1)


attemptGuess()

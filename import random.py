import random

def main():
    """Start a colour guessing game."""
    print("Guess the colour!")

    rainbow = [
        "red",
        "orange",
        "yellow",
        "green",
        "blue",
        "indigo",
        "violet"
    ]

    x = random.choice(rainbow)
    print(x)  # For testing purposes, remove this line to hide the answer
    guess = None

    while x != guess:
        guess = str(input("What colour am I thinking of? ")).lower()

        if x == guess:
            print("You guessed {}. Congratulations you got it right!".format(guess))
            break
        else:
            print("You guessed {}. Unfortunately it's wrong. Try again!".format(guess))

main()
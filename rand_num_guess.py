#!/usr/bin/env python3
# Created By: Marcus Wehbi
# Date: Oct 6th, 2022
# This program asks the user for a number 0 and 9
# It then displays if they guessed the correct number
import random


def main():
    # declare variable
    correct_guess = random.randint(0, 9)  # a number between 0 and 9
    # get the users input (users guessed number)
    guessed_number = int(input("Choose a number between 0 and 9 : "))

    # check if the user selected the correct number
    if guessed_number == correct_guess:
        # if the user guessed correctly, tell them
        print("You guessed correctly.")

    # check if the user selected the incorrect number
    if guessed_number != correct_guess:
        # if the user guessed incorrectly, tell them
        print("You guessed wrong.")


if __name__ == "__main__":
    main()

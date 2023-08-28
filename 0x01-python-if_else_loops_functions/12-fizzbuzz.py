#!/usr/bin/python3
# 12-fizzbuzz.py

# This script implements the FizzBuzz problem.

def fizzbuzz():
    """Print the numbers from 1 to 100 separated by a space.

    For multiples of three, print Fizz instead of the number.
    For multiples of five, print Buzz instead of the number.
    For multiples of three and five, print FizzBuzz instead of the number.
    """
    # Iterate through numbers from 1 to 100
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            # Print FizzBuzz for multiples of both 3 and 5
            print("FizzBuzz ", end="")
        elif number % 3 == 0:
            # Print Fizz for multiples of 3
            print("Fizz ", end="")
        elif number % 5 == 0:
            # Print Buzz for multiples of 5
            print("Buzz ", end="")
        else:
            # Print the number for non-multiples of 3 and 5
            print("{} ".format(number), end="")

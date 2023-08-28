#!/usr/bin/python3
def magic_calculation(a, b):
    result = 0  # Initialize the result variable
    for i in range(1, 3):  # Loop from 1 to 2 (inclusive)
        try:
            if i > a:
                raise Exception('Too far')  # Raise an exception with a custom message
            else:
                result += a ** b / i  # Perform a calculation and update the result
        except:
            result = b + a  # Set the result to a new value if an exception occurs
            break  # Exit the loop
    return result  # Return the final result

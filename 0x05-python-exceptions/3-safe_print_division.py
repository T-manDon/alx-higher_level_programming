#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        div = a / b  # Attempt division
    except ZeroDivisionError:
        div = None  # Set div to None if division by zero occurs
    finally:
        print("Inside result: {}".format(div))  # Print the result (even if it's None)
        return div  # Return the result of the division or None if there was an exception

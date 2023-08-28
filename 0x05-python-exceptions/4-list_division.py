#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    # Initialize an empty list to store division results
    new_list = []

    # Iterate through the lists up to the specified list_length
    for i in range(0, list_length):
        try:
            div = my_list_1[i] / my_list_2[i]  # Perform division
        except TypeError:
            print("wrong type")  # Handle TypeError
            div = 0  # Set division result to 0
        except ZeroDivisionError:
            print("division by 0")  # Handle ZeroDivisionError
            div = 0  # Set division result to 0
        except IndexError:
            print("out of range")  # Handle IndexError
            div = 0  # Set division result to 0
        finally:
            new_list.append(div)  # Append the division result to the new list

    # Return the list of division results
    return new_list

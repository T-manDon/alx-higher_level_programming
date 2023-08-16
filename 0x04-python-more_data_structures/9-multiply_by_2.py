#!/usr/bin/python3
# 9-multiply_by_2.py

def multiply_values_by_2(a_dictionary):
    new_dict = a_dictionary.copy()

    for key in new_dict:
        new_dict[key] *= 2

    return new_dict

#!/usr/bin/python3

# Main string
original_str = "Python is an interpreted, interactive, object-oriented programming" \
               " language that combines remarkable power with very clear syntax"

# Extract and concatenate
new_str = original_str[39:67] + original_str[107:112] + original_str[:6]

# Print results
print(new_str)

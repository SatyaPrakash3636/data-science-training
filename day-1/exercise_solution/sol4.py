#! /usr/bin/env python3

# Display every third character of input string

# Asking user input
user_input = (input("Enter the string: "))

# Getting element at position of multiple of 3
result = user_input[::3]

# Printing result
print(f"Characters at position of multiple of 3 are: {result}")

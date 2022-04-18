#! /usr/bin/python3

# Reversing input string

# Asking user for input 
input_string = input("Enter the string: ")

# Reversing input string
reversed_string = input_string[::-1]

# Reversing input string with reversed method
reversed_string1 = "".join(list(reversed(input_string)))

# Printing the reversed string
print(f"Reversed string: {reversed_string}")
print(f"Reversed string using Reversed method: {reversed_string1}")

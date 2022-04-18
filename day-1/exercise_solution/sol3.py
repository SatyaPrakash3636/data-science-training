#! /usr/bin/env python3

# Find the result of the equation a^2 + 2ab + b^2 where a=10 and b=12

print("Solving equation : a^2 + 2ab + b^2")

# Asking user for value of a and b
a = int(input("Enter the value of a : "))
b = int(input("Enter the value of b : "))

# Solving the equation
result = a**2 + 2*a*b + b**2

# Print the result
print(f"Result of equation is : {result}")

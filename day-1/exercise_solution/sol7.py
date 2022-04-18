#! /usr/bin/env python3

# Create a two dimensional array with the following values ([1,2,3],[4,5,6]) from the keyboard

# User inpput
list_a = input("Enter the first array elements(a,b,c): ").split(",")
list_b = input("Enter the second array elements(a,b,c): ").split(",")

# Converting to integer
list_a = [ int(i.strip()) for i in list_a ]
list_b = [ int(i.strip()) for i in list_b ]

# Creating 2D array
list_c = [ list_a, list_b ]

# Printing 2D array
print(list_c)
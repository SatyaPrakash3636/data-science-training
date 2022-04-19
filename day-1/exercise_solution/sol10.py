#! /usr/bin/env python3

# Find whether the given three digit number is Armstrong or not
# (If the sum of the cubes of the individual digits of the number is equal to that number)

# Defining function to check if number is Armstrong or not
def check(a):
    a_list = list(a)
    result = 0
    for i in a_list:
        result += int(i) ** 3
    if result == int(a):
        return True
    else:
        return False


# Take user input
num = input("Enter thre number to check: ")

# Call function
result = check(num)

# Check the return value and show output
if result == True:
    print(f"Given number {num} is an Armstrong number")
else:
    print("Not an Armstrong number")

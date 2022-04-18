#! /usr/bin/env python3

# Find the total salary of an employee given his basic (hra=40% of basic, da is 20% of basic and  deduction 10% of gross)

# Asking user's base salary
base_salary = float(input("Enter your Base Salary(Rs): "))

hra = 0.4 * base_salary
da = 0.2 * base_salary
deduction = 0.1 * base_salary

# Gross Salary and Net Salary
gross_salary = base_salary + hra + da
net_salary = gross_salary - deduction

# Printing Gross Salary and Net Salary
print(f"Your Gross Salary is: Rs {gross_salary:.2f} and Net Salary is Rs {net_salary:.2f}")

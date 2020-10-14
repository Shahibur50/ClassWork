"""
Factorial version 1.3.10.20

Copyright (c) 2020 Shahibur Rahaman
Licensed under MIT
"""

def factorial(num):
	fact = num
	while num != 2:
		num = num - 1
		fact *= num
	return fact


num = int(input("Enter the number whose factorial is to be shown: "))

print(f"The value of factorial for the given number is {factorial(num)}.")

"""
Sum of digits version 1.2.10.20

Copyright (c) 2020 Shahibur Rahaman
Licensed under MIT
"""

def sum_of_digits(num):
	total_sum = 0
	while num % 10 != 0:
		total_sum += num % 10
		num //= 10
	return total_sum


num = int(input("Enter the number: "))

print(f"The sum of digits of the number {num} is {sum_of_digits(num)}.\n")
"""
Digit cube version 1.1.10.20

Copyright (c) 2020 Shahibur Rahaman
Licensed under MIT
"""

def digit_cubes():
	for num in range(100, 1001):
		digit_cubes = 0
		for i in str(num):
			digit_cubes += int(i) ** 3
		if digit_cubes == num:
			print(num)

digit_cubes()
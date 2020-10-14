"""
Reverse num  version 1.2.10.20

Copyright (c) 2020 Shahibur Rahaman
Licensed under MIT
"""

num = int(input("Enter the number whose reverse is to be shown: "))

reverse = 0
while num != 0:
	remainder = num % 10
	reverse = reverse * 10 + remainder
	num = num // 10
print(reverse)

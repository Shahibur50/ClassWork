"""
Prime number version 1.2.10.20

Copyright (c) 2020 Shahibur Rahaman
Licensed under MIT
"""

def prime(n):
	for i in range(2, n + 1):
		for j in range(2, i):
			if i % j == 0:
				print(i, "equals to", j, "*", i // j)
				break
		else:
			print(i, "is not a prime number")

prime(1000)
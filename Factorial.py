def factorial(num):
	fact = num
	while num != 2:
		num = num - 1
		fact *= num
	return fact


num = int(input("Enter the number whose factorial is to be shown: "))

print(f"The value of factorial for the given number is {factorial(num)}.")

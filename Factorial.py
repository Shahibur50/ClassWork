def factorial(num):
	fact = num
	for i in range(1, num - 1):
		fact = fact * (num - i)
	return fact


num = int(input("Enter the number whose factorial is to be shown: "))

print(f"The value of factorial for the given number is {factorial(num)}.")

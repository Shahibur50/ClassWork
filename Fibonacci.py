def words(term):
	for i in range(term):
		i += 1
		word = ""

		if i == 1:
			word += "th"
		elif i == 2:
			word += "nd"
		elif i == 3:
			word += "rd"
		else:
			word += "th"
	return word

def fib(term):
	a = 0
	b = 1
	for _ in range(term - 1):
		a, b = a + b, a
	return a


term = int(input("\nEnter the Fibonaaci term to be shown: "))

print(f"The {term}{words(term)} Fibonacci number is {fib(term)}.\n")

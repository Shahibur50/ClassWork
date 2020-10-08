terms = int(input("Enter the number of terms for average: "))

term_values = []

for term in range(terms):
	term += 1
	word = ""

	if term == 1:
		word += "st"
	elif term == 2:
		word += "nd"
	elif term == 3:
		word += "rd"
	else:
		word += "th"

	value = float(input(f"\nEnter the {term}{word} term: "))
	term_values.append(value)

total = 0

for value in term_values:
	total += value

print(f"\nThe average of given values is {round(total / terms, 2)}.")

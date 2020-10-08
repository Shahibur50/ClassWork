a = float(input("Enter the coefficient of a: "))
b = float(input("Enter the coefficient of b: "))
c = float(input("Enter the coefficient of c: "))

discriminant = (b ** 2) - (4 * a * c)

d = discriminant

root1 = (-b + (d ** 0.5)) / (2 * a)
root2 = (-b - (d ** 0.5)) / (2 * a)

r1 = root1
r2 = root2

eq1 = a * (r1 ** 2) + b * (r1 ** 1) + c
eq2 = a * (r2 ** 2) + b * (r2 ** 1) + c

if eq1 == 0 and eq2 == 0:
	print(f"\nThe roots are {r1} and {r2}.\n")
	if d == 0:
		print("The roots are real and equal.")
	elif d > 0:
		print("The roots are real and unequal.")
	else:
		print("The roots are imaginary/complex.")
else:
	print("The given values do not form a quadratic equation.")

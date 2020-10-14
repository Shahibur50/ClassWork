"""
Pythagorean triplet version 1.2.10.20

Copyright (c) 2020 Shahibur Rahaman
Licensed under MIT
"""

print("--------------------------------------------------------")
print("")
hypo = float(input("Enter the length of hypotenuse of triangle: "))
base = float(input("Enter the length of base of triangle: "))
height = float(input("Enter the length of height of triangle: "))

hy2 = hypo * hypo
ba2 = base * base
he2 = height * height

print("")
if hypo < base + height:
	if hy2 == ba2 + he2:
		print(f"The dimensions {hypo}, {base} and {height} forms a pythagorean triplet")
	else:
		print(f"The dimensions {hypo}, {base} and {height} are not a pythagorean triplet")
else:
	print("The given dimensions do not form a triangle.")
print("")
print("--------------------------------------------------------")
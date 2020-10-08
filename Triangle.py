a = float(input("Enter the First side: "))
b = float(input("Enter the second side: "))
c = float(input("Enter the third side: "))
u = input("Enter the unit of measurement: ")

sides = [a, b, c]

peri  = a + b + c
S = peri / 2
area = (S * (S - a) * (S - b) * (S - c)) ** 0.5

biggest_side = sides[0]
smallest_side = sides[0]
mid_side = sides[0]

bs = biggest_side
ms = mid_side
ss = smallest_side

for side in sides:
	if side > bs:
		bs = side
	elif side < ss:
		ss = side
for side in sides:
	if side > ss and side < bs:
		ms = side

def angle_teller(b, m, s):
	if b ** 2 < m ** 2 + s ** 2:
		print("\n|>The triangle is acute-angled-triangle.")
	elif b ** 2 > m ** 2 + s **2:
		print("\n|>The triangle is obtuse-angled-triangle.")

if bs < ms + ss:
	if a == b == c:
		print("\n|>The given dimensions form an equilateral triangle.\n")
		angle_teller(bs, ms, ss)
	elif a == b or b == c or a == c:
		print("\n|>The given dimensions form an isosceles triangle.")
		angle_teller(bs, ms, ss)
	elif bs ** 2 == ss ** 2 + ms ** 2:
		print("\n|>The given dimensions form a right-angled triangle, thus it is a pythagorean triplet.")
	elif a != b != c:
		print("\n|>The given dimensions form a scalene triangle.")
		angle_teller(bs, ms, ss)

	print(f"\n|>The perimeter of the triangle is {peri}{u} and the area of triangle is {round(area, 2)}{u}.\n")
else:
	print("\n|>The given dimensions do not form a triangle.\n")
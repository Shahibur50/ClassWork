num = int(input("Enter the number whose reverse is to be shown: "))

reverse = 0
while num != 0:
	remainder = num % 10
	reverse = reverse * 10 + remainder
	num = num // 10
print(reverse)

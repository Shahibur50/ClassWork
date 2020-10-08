def sum_of_digits(num):
	total_sum = 0
	while num % 10 != 0:
		total_sum += num % 10
		num //= 10
	return total_sum


num = int(input("Enter the number: "))

print(f"The sum of digits of the number {num} is {sum_of_digits(num)}.\n")
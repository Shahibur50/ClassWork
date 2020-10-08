word = input("Enter the word: ")

new_word = ""

for letter in word:
	new_word = letter + new_word

if new_word == word:
	print("The word is a palindrome.")
else:
	print("The word is not a palindrome.")
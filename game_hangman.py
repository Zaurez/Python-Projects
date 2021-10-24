import random

#list of word that system will check
word_list = ['love', 'game', 'hello', 'computer', 'yes', 'fox']

#selecting a word on random
selected_word = random.choice(word_list)
print(selected_word)

#input from user
# user_choice = input("Enter an alphabet: ")

#checking for alphabet in system selected word
attempt_count = 4
while attempt_count > 1:
	print("Attempts Left: ", attempt_count)
	user_choice = input("Enter an alphabet: ")

	if user_choice in selected_word:
		print(selected_word)
		print("Woah ! Alphabet found")
		attempt_count = 0
	else:
		# print("The system selected word:",selected_word)
		attempt_count = attempt_count - 1
		if attempt_count != 1:
			print("Try Again")
		else:
			print("Game Over")
			print("The system selected_word was: ", selected_word)

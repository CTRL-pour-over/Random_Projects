import random

def how_many_right(arg_word, user_input):
	correct_letters = 0
	for letter in arg_word:
		if letter in user_input:
			correct_letters += 1
	print(correct_letters, 'Correct letters')

def guess_the_word(arg_word, arg_first_letter, arg_last_letter, arg_under_scores): # Uses data from set_up_start()
	print("Guess the word: ", arg_first_letter, arg_under_scores, arg_last_letter)
	user_input = input('>> ').lower() # Ask the user to type something in
	if user_input == arg_word:
		print('Correct! Word was: ', arg_word)
	elif user_input in arg_word:
		print('Close...')
		how_many_right(arg_word, user_input)
	else:
		print('Wrong')
		how_many_right(arg_word, user_input)

def set_up_start():
   #index[   0		   1		2		3		4		5   ]
	li = ['apples', 'banana', 'car', 'rock', 'pasta', 'home'] # Make a list of words
	NUMBER = random.randint(0, 5) # This number = word in the list. UPDATE if more words are added.
	MAGIC_WORD = li[NUMBER] # Find the word in list position li[number]
	FIRST_LETTER = MAGIC_WORD[0] # Find the first letter in the word
	LAST_LETTER = MAGIC_WORD[-1] # Find the last letter in the word

	L = -2 # Calculate how many underscores for the word
	for letters in MAGIC_WORD:
		L += 1
		UNDER = '_ ' * L
	guess_the_word(MAGIC_WORD, FIRST_LETTER, LAST_LETTER, UNDER) # Call the next function
	
set_up_start() # Start the program
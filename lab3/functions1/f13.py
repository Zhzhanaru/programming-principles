# 13. Write a program able to play the 
# "Guess the number" - game, where the 
# number to be guessed is randomly chosen 
# between 1 and 20. This is how it should
# work when run in a terminal:

#     Hello! What is your name?
#     KBTU

#     Well, KBTU, I am thinking of a number between 1 and 20.
#     Take a guess.
#     12

#     Your guess is too low.
#     Take a guess.
#     16

#     Your guess is too low.
#     Take a guess.
#     19
from random import randrange

def gtn():
	print ("Hello! What is your name?")
	gamer_name = input()

	print ('Well, %s, I am thinking of a number between 1 and 20.' % gamer_name)
	
	my_number = randrange(1,21) 
	tries = 0 

	while True:
		print ('Take a guess.')

		gamer_guess = int(input())
		tries += 1

		if gamer_guess == my_number:
			print ('Good job, %s! You guessed my number in %d guesses!' % (gamer_name, tries))
			break
		elif gamer_guess < my_number:
			print ('Your guess is too low.')
		else:
			print ('Your guess is too high.')

#test
gtn()
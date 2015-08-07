#!/usr/bin/env python
# HW04_ex00

# Create a program that does the following:
#     - creates a random integer from 1 - 25
#     - asks the user to guess what the number is
#     - validates input is a number
#     - tells the user if they guess correctly
#         - if not: tells them too high/low
#     - only lets the user guess five times
#         - then ends the program
################################################################################
# Imports
import random
import sys

# Body

nr = (random.randint(1,25))
count= 0
while (count < 5):
	guess = raw_input ('You have 5 attempts to guess a number between 1-25: ')
	try: 
		guess_int = int(guess)         # note to self: if its actually an int, itll store it in guess_int or else throw an exception if not
	except:
		print 'Only enter a number'
		count = count +1
	else:
		if guess_int == nr:
				print "Congrats! You guessed the right number ", guess
				sys.exit()
		else:
			if guess_int < nr:
				print "Go higher"
				count = count +1
			else:
				print "Go lower"
				count = count +1
print 'Oops, the correct number was: ', nr

	






################################################################################
def main():


    print("Hello World!") # Remove this and replace with your function calls
    

if __name__ == '__main__':
    main()
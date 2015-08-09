#!/usr/bin/env python
# HW04_ex08_05

# The following program counts the number of times the letter a appears in a 
# string:

#     word = 'banana'
#     count = 0
#     for letter in word:
#         if letter == 'a':
#             count = count + 1
#     print count

# Encapsulate this code in a function named "count", and generalize it so that 
# it accepts the string and the letter as arguments.

################################################################################
# Imports


# Body

def count (word, l):
	index = 0
	for letter in word:
		if letter == l:
			index += 1
	print index


################################################################################
def main():

	count ('palindrome', 'i')
	count ('divided','d')
	count ('billabong', 'b')
	count ('ermmmmm', 'm')
    

if __name__ == '__main__':
    main()
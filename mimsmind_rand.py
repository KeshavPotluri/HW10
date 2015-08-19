import random

def get_randomdigit_lastname1lastname2(length):
	"""Generates the a random number that is of length that is provided by the
		user"""
	# Initialize the random number 
	randomNumber = ''

	# Generate an n digit random number as a string.
	for number in range(length):
		randomNumber = randomNumber + str(random.randint(0,9))

	# Return the random number
	return randomNumber


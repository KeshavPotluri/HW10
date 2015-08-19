###############################################################################
##############################   Functions   ##################################
###############################################################################
def seventeen():
	""" The function to let the user know how many marbles are left. Prompt the
	user to pick marbles. The computer picks the marbles next, informs the user
	about the number of marbles left and prompts the user to pick again. The 
	one to pick the last marbles loses. (This is designed so that user always
	loses)"""

	# Starts the game with 17 marbles left. Also valid choices are 1,2 and 3
	marblesLeft = 17
	validChoices = [1,2,3]

	# Start the game
	print "Let's play the game of Seventeen!"

	# Continue the game as long as marbles are left in the jar
	while  marblesLeft>0:

		# Takes the user input 
		print "Number of marbles left in the jar: {0}".format(marblesLeft)
		userInput = raw_input("Your turn: How many marbles will you remove (1-3)? ")

		# Check if the user entered a number
		try:
			userSelectedNumber = int(userInput)

		# If the user did not enter a number, prompt him to win
		except:
			print "Sorry, that is not a valid option. Try again!"
			continue

		# If the user enters a number
		else:

			# If the user enters a valid choice and the choice is less than the number of 
			# marbles left
			if (userSelectedNumber in validChoices) and (userSelectedNumber <= marblesLeft):

				# Decrement the marbles according to the user selection
				print "You removed {0} marbles.".format(userSelectedNumber)
				marblesLeft = marblesLeft - userSelectedNumber

				# If no marbles are left, user loses
				if marblesLeft == 0:
					print "There are no marbles left. Computer wins!"
					break

				# Else make the computer select marbles
				else:
					print "Number of marbles left in the jar: {0}".format(marblesLeft)
					print "Computer's turn..."

					# Make the computer select 4 - marbles the user selected. This makes
					# the user lose always.
					computerRemovedMarbles = 4 - userSelectedNumber
					marblesLeft = marblesLeft - computerRemovedMarbles
					print "Computer removed {0} marbles.".format(computerRemovedMarbles)
			else:
				print "Sorry, that is not a valid option. Try again!"
				continue
				
###############################################################################
################################   Main   #####################################
###############################################################################
def main(): 
	seventeen()

###############################################################################
############################   Boiler Plate   #################################
###############################################################################
if __name__ == '__main__':
    main()


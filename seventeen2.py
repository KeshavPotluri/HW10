###############################################################################
###############################   Imports   ###################################
###############################################################################

# Used to generate a random number.
import random

###############################################################################
##########################   Global Variables   ###############################
###############################################################################

# Variable that stores the number of marbles left.
marblesLeft = 17

# Variable to store the play sequence.
playSequence = ''

# variable to store the winner.
winner = ''

# variable to store the file output.
file_lines = ''

###############################################################################
##############################   Functions   ##################################
###############################################################################
def player_one_chance(playerOneSelection):
	""" Function that takes in the player one's selection from the file, 
	decrement the marble count, and modify the play sequence. """

	# Declare the variables are global to use the global variables.
	global marblesLeft
	global playSequence

	# If the marbles left are greater than the player selection, decrement
	# the marbles accordingly else the player takes all the marbles.
	if marblesLeft >= playerOneSelection:
		marblesLeft = marblesLeft - playerOneSelection
	else:
		marblesLeft = 0

	# Modify the play sequence.
	if playSequence == '':
		playSequence = str(playerOneSelection)
	else:
		playSequence = playSequence + "-" + str(playerOneSelection)

def player_two_chance(playerOneSelection):
	""" Function that takes in the player one's selection from the file, 
	generate the marble two count according to either of the three logics :
	player two always wins, player two enters a constant each time or player
	two enters a random number (uncomment the appropriate code to get the 
	desired logic),	decrement the marble count, and modify the play sequence. 
	"""
	# Declare the variables are global to use the global variables.
	global marblesLeft
	global playSequence

	# Uncomment any of the following to get a different logic for the 
	# player selection
	playerTwoSelection = 4 - playerOneSelection # Player 2 always wins
	#playerTwoSelection = 1 # Player 2 always selects 1
	#playerTwoSelection = random.randint(1,3) # Player 2 selects a random number

	# If the marbles left are greater than the player selection, decrement
	# the marbles accordingly else the player takes all the marbles.
	if marblesLeft >= playerTwoSelection:
		marblesLeft = marblesLeft - playerTwoSelection
	else:
		marblesLeft = 0

	# Modify the play sequence.
	playSequence = playSequence + "-" + str(playerTwoSelection)

def seventeen():
	""" Reads the input for player 1 from a file, generates selections for
		player 2, plays the seventeen game, records the play sequence and
		prints the output to a new file."""

	# Declare the variables are global to use the global variables.
	global marblesLeft
	global playSequence
	global file_lines
	global winner

	# Intialize the number of wins for both players.
	player1Wins = 0
	player2Wins = 0

	count = 1

	# Reads the player 1 sequence from a file
	with open("i206_placein_input_0.txt", 'r') as fin:
		
		# Each line represents player 1 turns for the game.
		for x in fin.readlines():

			# Re-initialize the values for each variable for every game.
			marblesLeft = 17
			playSequence = ''
			winner = ''

			# Remove the new line characters and the comma delimiters and get 
			# the player 1 turns into a list.
			text = x.strip()
			playerOneTurns = text.split(",")

			# For every turn for player 1
			for turn in playerOneTurns:

				# Run the player 1 chance
				player_one_chance(int(turn))

				# If there are no marbles left, player 2 wins
				if marblesLeft == 0:
					winner = "P2"
					player2Wins +=1
					break
				# Run the player 2 chance
				player_two_chance(int(turn))

				# If there are no marbles left, player 1 wins
				if marblesLeft == 0:
					winner = "P1"
					player1Wins +=1
					break

			# Record the game #, play sequence, winner for the game.
			file_lines = file_lines + ''.join(["Game #",str(count),". Play sequence: ",playSequence," Winner: ",winner,'\r\n'])
			count += 1

		# Append the number of wins for both the players.
		file_lines = file_lines + "Player 1 won {0} times; Player 2 won {1} times".format(player1Wins, player2Wins)

	# Write the results into a file.
	with open("i206_placein_output_0.txt", 'w') as fout:
		fout.writelines(file_lines) 
				
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


def get_bullcow(guess, rand_num):
	# Initialize the number of cows and bulls
	numberOfBulls = 0
	numberOfCows = 0
	tempRandomInteger = rand_num

	# Get the number of bulls by comparing digits at the same index
	for j in range(len(guess)):
		if guess[j] == rand_num[j]:
			numberOfBulls += 1
	# Get the number of cows + bulls by checking if the digit in the
	# guess occurs in the generated number
	for j in range(len(guess)):
		if guess[j] in tempRandomInteger:
			index = tempRandomInteger.find(guess[j])
			# remove the occurance so that it handles the condition where
			# digits repeat 777, 878 etc.
			temp = tempRandomInteger[:index] + tempRandomInteger[index+1:]
			tempRandomInteger = temp
			numberOfCows += 1
	# Remove the number of bulls from the number of cows because the above
	# counts the number of bulls in cows as well
	numberOfCows = numberOfCows - numberOfBulls
	return (numberOfCows , numberOfBulls)


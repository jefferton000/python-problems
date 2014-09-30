#!/usr/bin/python
# Randomly generate strings toward the goal string: "methinks it is like a weasel"

# Globals variables
goal_string = "methinks it is like a weasel"

# "main" function
def generate():
	current_string = ""
	string_list = []
	string_list_limit = 1000
	generation_count = 0           # generation = every 1000
	char_count = len(goal_string)  # decrements every generation count
	correction_index = 0           # position from 0-27
	done = False                   # program sentinel
	found_count = 0
	not_found_count = len(goal_string)

	# Generate and score 10 generations of 1000 strings
	while not done and generation_count < 10:
		if len(string_list) < string_list_limit:
			current_string = new_string()
			string_list.append(current_string)
			current_score = score(current_string)
		else:
			for string in string_list:
				highest_score = current_score #?
				best_string = current_string  #?
			generation_count += 1

		# "Hill climbing", generalize string generation, decrease # of chars to be generated.
		if more characters are found[higher score] (and are correct from start to index):
			current_string = new_string(char_count)
			# gradually generate less characters, based on the last index they were correct
			beginning(index=start to end)
			middle(index to end)
			end(index=end)
			(good from start to index, but not from index to end)


# Random string generator
def new_string(num_chars):

	# append needed amount to new list
	char_list = []
	#fill string to character limit w/ random chars, appending incrementally
	for 
	alphabet = "abcdefghijklmnopqrstuvwxyz "
	random.choice(string.letters())

	generated as letterlist

	stored as string

	checked as letterlist

	return gen_string


# Score the string
def score(string):
	ch_found = 0
	ch_not_found = 0
	percent = 0

	# for length in len(goal_string):
	
	for letter in goal:
		if letter not in string:
			not_found += 1
			print ("%s letters not found" (not_found))
		else:
			found += 1
			print ("%s letters found" (found))

	# compare score with 100 for remainder
	if found % str_limit == 0:
		percent = 100
	else:
		percent = ch_found / ch_not_found

	return percent

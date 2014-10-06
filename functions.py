#!/usr/bin/python
# Randomly generate strings toward the goal string: "methinks it is like a weasel"
import random
goal_string = "methinks it is like a weasel"
string_list_limit = 1000
	
# "main" function
def generate():
	string_list = []
	string_index = 0
	char_count = len(goal_string)
	goal_index = 0 # persistent location for new reduced string

	while len(string_list) < string_list_limit:
		# Generate new string to list
		random_string = new_string(char_count)
		string_list.append(random_string)

		# "Hill climbing"
		# Check each character, save index and reduce characters 
		for index, val in enumerate(string):
			if random_string[index] == goal_string[index]:
				char_count -= 1
				goal_index += 1             # for character list
				best_string = random_string
			else:
				break # stop matching

		string_index += 1

	# Score list for best string, using older way of indexing
	best_percent = 0
	best_string = ""
	for index, string in enumerate(string_list):			
		percent = score(string_list[index])
		next_percent = score([string_list[index+1])
		if percent < next_percent:
			best_percent = next_percent
			best_string = string_list[index+1]

	print "Result: ", best_string, best_percent

				
					
# Random string generator 
# Input: specified number of chars
# Output: randomly generated string from specified length
def new_string(num_chars):
	alphabet = "abcdefghijklmnopqrstuvwxyz "
	gen_string = ""
	char_list = []

	# generate list to character limit w/ random chars,
	for i in range(num_chars):
		char_list.append(random.choice( alphabet ))

	gen_string = ''.join(char_list)
	return gen_string


# Score the string
# String lengths must match, otherwise:
#   if index < len(string) and string[index] == goal_string[index]:
# Returns an integer representation of percentage
def score(string):
	found = 0
	goal = len(goal_string)
	percent = 0
	
	for index, item in enumerate(goal_string):
		if string[index] == goal_string[index]:
			found += 1

	percent = int(round(float(found) / float(goal), 2) * 100)
	
	return percent

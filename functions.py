#!/usr/bin/python
# Randomly generate strings toward the goal string: "methinks it is like a weasel"
import random
goal_string = "methinks it is like a weasel"
	
# "main" function
def generate():
	string_list = []
	char_count = len(goal_string)

	# populate list
	for i in range(10);
		random_string = new_string(char_count)
		string_list.append(random_string)
	
	goal_index = 0
	best_percent = 0
	best_string = ""
	# score the list, keep best string
	for i in range(len(string_list) - 1):
		percent = score(string_list[index])
		next_percent = score(string_list[index+1])
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
	
	for i in range(goal):
		if string[i] == goal_string[i]:
			found += 1

	percent = int(round(float(found) / float(goal), 2) * 100)
	
	return percent

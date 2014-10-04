#!/usr/bin/python
# Randomly generate strings toward the goal string: "methinks it is like a weasel"
import random
goal_string = "methinks it is like a weasel"
string_list_limit = 1000
	
# "main" function
def generate():
	string_list = []
	generation_count = 0
	char_count = len(goal_string)  # decrements every generation coun

	# Generate and score 10 generations of 1000 strings
	# Initial Testing: only use one generation
	while generation_count < 10:
		if len(string_list) < string_list_limit:
			current_string = new_string(char_count) # default length
			string_list.append(current_string)			
		else:
			# keep best percentage, scoring list
			for string in string_list:			# declare
				percent = score(string)         # declare
				next_percent = score(string_list.next())  # declare
				next_string = score(string_list.next())	  # declare
				if percent < next_percent
					best_percent = next_percent # declare
					best_string = next_string   # declare
			generation_count += 1
			#string_list = [] ==> Use when generation > 1


"""
		# "Hill climbing", make into own function? use char_list or char_count?
		new_list = list(new_string( len(shorterlist) ))
		index = len(new_list)
		start = len(goal_string) - index

		#  decrease # of chars to be generated, based on last correct index position
		#  correct from start to index, but not from index to end
		for index, val in enumerate(list(char_list), start = len(goal_string) - index):
			print i, val
                # OR
		for letter not in new_list:
			get index and store into another list			

		#if more characters are found (higher score)
		if found_count > not_found_count
			char_list = new_string(char_count) # char_count decreases
			char_list = list(current_string)
"""

# Random string generator based on number of chars entered
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
def score(string):
	ch_found = 0
	percent = 0
	
	# compare string with goal string, might need index: enum?
	for letter in goal_string:
		if letter in string:
			ch_found += 1

	# compare score with 100 for remainder
	if ch_found % len(goal_string) == 0:
		percent = 100
	else:
		percent = ch_found / len(goal_string)

	return percent

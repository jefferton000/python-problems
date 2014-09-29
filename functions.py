# Randomly generate strings toward the goal string: "methinks it is like a weasel"
# Proto-specification thoughts

globals?:
 goal string = "methinks it is like a weasel"
 current string = "???"
 character limit = 27?
 string limit = 1000
 generation count (every 1000 = generation)
 correction index = (position from 0-27)?

"main" function
---------------------------------
generate and score 1000 strings
keep highest scoring string per 1000, remove all others

A self correcting generator? #hill climbing
if more characters are found[higher score] (and are correct from start to index)
 gradually generate less characters, based on the last index they were correct
  beginning(index=start to end)
  middle(index to end)
  end(index=end)
 (good from start to index, but not from index to end)


random string generator
---------------------------------

result = random.random()
random.choice(string.letters())

choose letters by random.choice('abced... ')
fill string to character limit, incrementally

 generated as letterlist
 stored as string
 checked as letterlist



score the string
----------------------------------
def score(current_string):
	ch_found = 0
	ch_not_found = 0
	percent = 0
	get_index, set_index?
	
	for letter in goal:
		if letter not in current_string:
			not_found += 1
			print ("%s letters not found" (not_found))
		else:
			found += 1
			print ("%s letters found" (found))

	#	compare score with 100 for remainder
	if found % str_limit == 0:
		percent = 100
	else:
		percent = ch_found / ch_not_found

	return percent


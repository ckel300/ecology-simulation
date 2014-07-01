#!/usr/bin/python

"""
Conatins utility-type functions.

Function list:
die

generate_trees
generate_lumberjacks
generate_bears

log_month_to_file
find_string_in_file
"""

import sys
from random import randrange

def die(string='A fatal error has occured.'):
	"""
	A simple function that exits cleanly after printing a given string.
	"""

	print string
	sys.exit(0)

"""
Data Representation and Generation
==================================
 
Every "player" or "object" type is an entity (i.e. Trees, Bears, Lumberjacks)
An entity object is an "instance" of the entity (e.g. a single tree)
 
Each entity will be a list of tuples. Each tuple will be an entity object.
Trees: ('x/y', age in months, type). The first is the 'id' - the string 'x/y'. The second is the age in months, and the third
is the type of tree (0 for sapling, 1 for regular, 2 for elder)

Bears and Lumberjacks are similar. All entity objects will have the id but not all will have age or type
"""

def generate_trees(amount, board_dim):
	"""
	Generating the intial tree configuration with 'amount' number of trees. Returns the tree list.

	The amount and board_dim arguments could all have been global but I am passing them into a function
	to preserve loose coupling. Ideally, I want to be able to test all of these functions out of context and still
	have them work.

	Tree types:
	Sapling: 0
	Regular: 1 (default)
	Elder: 2
	"""

	trees = [0] * amount
	tree_ids = []

	default_type = 1
	default_age = 0

	x = 0
	loop_counter = 0
	while x < len(trees) and loop_counter < amount * 100:
		# Technically this while loop could run forever since it's using random. Might keep choosing taken spots,
		# which is why there's a loop_counter. The x variable is for the list, so can't use that. It increases in
		# the else part because thats the place where a 'loop through' is wasted.

		tree_x = randrange(board_dim) # x coord
		tree_y = randrange(board_dim) # y coord
		id_string = str(tree_x) + '/' + str(tree_y)

		if id_string not in tree_ids:
			# checking for conflicting IDs. If the tree already exists, can't put another tree there.
			trees[x] = (id_string, default_age, default_type)
			tree_ids.append(id_string)
			x += 1
		else:
			loop_counter += 1

	return trees

def generate_lumberjacks(amount, board_dim):
	"""
	Generating the intial lumberjack configuration with 'amount' number of lumberjacks. Returns the tree list.
	"""

	lumberjacks = [0] * amount
	lumberjack_ids = []

	x = 0
	loop_counter = 0
	while x < len(lumberjacks) and loop_counter < amount * 100:
		lumberjack_x = randrange(board_dim) # x coord
		lumberjack_y = randrange(board_dim) # y coord
		id_string = str(lumberjack_x) + '/' + str(lumberjack_y)

		if id_string not in lumberjack_ids:
			lumberjacks[x] = (id_string)
			lumberjack_ids.append(id_string)
			x += 1
		else:
			loop_counter += 1

	return lumberjacks

def generate_bears(amount, board_dim):
	"""
	Generating the intial bear configuration with 'amount' number of trees. Returns the tree list.

	Two options for bears - they could be required to NOT spawn where non-tree entities already are (and vice-versa) or
	it could not matter. For now I'll start with it not mattering.

	This is almost the exact same function as generate_trees and generate_lumberjacks
	"""

	bears = [0] * amount
	bear_ids = []

	x = 0
	loop_counter = 0
	while x < len(bears) and loop_counter < amount * 100:
		bear_x = randrange(board_dim) # x coord
		bear_y = randrange(board_dim) # y coord
		id_string = str(bear_x) + '/' + str(bear_y)

		if id_string not in bear_ids:
			bears[x] = (id_string)
			bear_ids.append(id_string)
			x += 1
		else:
			loop_counter += 1

	return bears

#========================================================

"""
Month/Year Logging
==================

Every month the following events will be logged. If none of these happen, then nothing will be logged.
Lumber harvested
Saplings created
Lumberjacks Maw'd
Trees become elder trees

Lumberjack hired
Bear captured by zoo
Bear added

AS WELL AS (originally planned only for year)

# of trees, saplings, and elders
# of lumberjacks
# of bears
# of lumberjacks hired
# of bears captured
# of mawings

Every year the following will be logged.
# of trees, saplings, and elders
# of lumberjacks
# of bears
# of lumberjacks hired
# of bears captured
# of mawings

All of these will be stored in a file data.txt (written to from main.py when a given event happens). Although the name of the
file should not change, a filename to pull data from will be passed as an argument to preserve loose coupling. We shoudln't
assume too much. These functions merely format everything accordingly and log it to a log file.
"""

# TODO: this should probably use a DB (overkill maybe? Nice learning experience though, ans would definitely make life easier)

def log_month_to_file(file_to_write, file_to_read):
	"""
	A function to log data into a filename. The data will be taken from file_to_read and will be written to file_to_write
	"""

	# TODO: make month number to be in the format of 0000, 0001, 0002, etc. rather than 1, 2, 3 etc.

def find_string_in_file(string, filename):
	"""
	This is a function to find a given string in a file. It doesn't cover te string spanning several lines, but
	we only need to find the line in which the string is in.

	Returns the whole line containing the search string as a string.

	This simply loops through the file checking every string.
	"""

	return_string = ""

	with open(filename, 'r') as file:
		for line in file:
			if string in line:
				return_string = line

	return return_string
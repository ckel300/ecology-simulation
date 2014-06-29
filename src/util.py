#!/usr/bin/python

"""
Conatins utility-type functions.

Function list:
generate_trees
generate_lumberjacks
generate_bears
"""

from random import randrange

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
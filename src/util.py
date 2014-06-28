#!/usr/bin/python

"""
Conatins utility-type functions.

Function list:
generate_trees
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
		# Technically this while loop could run forever since it's using random. Might keep chosing taken spots,
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
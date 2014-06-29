#!/usr/bin/python

"""Main entry point for the ecology simulation. This script also contains all the 'tick' logic"""

import sys
from random import randrange

import util

# percentage of the board each entity will take up

TREE_PERCENTAGE = 0.5 # 50%
LUMBERJACK_PERCENTAGE = 0.1 # 10%
BEAR_PERCENTAGE = 0.02 # 2%

def main():
	"""Main entry point for the script"""
	# TODO: implement argparse or optparse (not sure which is used in 2 and which in 3)

	board_dim = int(raw_input('Board dimension (N): '))
	board_size = board_dim**2

	trees = util.generate_trees(int(board_size * TREE_PERCENTAGE), board_dim)
	lumberjacks = util.generate_lumberjacks(int(board_size * LUMBERJACK_PERCENTAGE), board_dim)
	bears = util.generate_bears(int(board_size * BEAR_PERCENTAGE), board_dim)

	print trees, len(trees)
	print lumberjacks, len(lumberjacks)
	print bears, len(bears)

	return 0

if __name__ == '__main__':
	sys.exit(main())
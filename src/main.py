#!/usr/bin/python

"""Main entry point for the ecology simulation. This script also contains all the 'tick' logic"""

import sys
from random import randrange

from util import generate_trees

def main():
	"""Main entry point for the script"""
	# TODO: implement argparse or optparse (not sure which is used in 2 and which in 3)

	tree_amount = int(raw_input('Tree amount: '))
	board_dim = int(raw_input('Board dimension (N): '))

	trees = generate_trees(tree_amount, board_dim)
	print trees, len(trees)

	return 0

if __name__ == '__main__':
	sys.exit(main())
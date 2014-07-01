#!/usr/bin/python

"""Main entry point for the ecology simulation. This script also contains all the 'tick' logic"""

import sys
from random import randrange

import util

# percentage of the board each entity will take up

TREE_PERCENTAGE = 0.5 # 50%
LUMBERJACK_PERCENTAGE = 0.1 # 10%
BEAR_PERCENTAGE = 0.02 # 2%

MONTH = 0
YEAR = 0

DATA_FILE = 'data.txt'

def main():
	"""Main entry point for the script"""
	
	# TODO: implement argparse or optparse (not sure which is used in 2 and which in 3)

	print util.find_string_in_file('lumber_harvested', DATA_FILE)
	print util.find_string_in_file('saplings_created', DATA_FILE)

	util.log_month('log.txt', DATA_FILE)

	return 0

if __name__ == '__main__':
	sys.exit(main())
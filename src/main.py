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
MONTH_LOG = 'month_log.txt'
YEAR_LOG = 'year_log.txt'

def main():
	"""Main entry point for the script"""
	
	# TODO: implement argparse or optparse (not sure which is used in 2 and which in 3)

	util.log_month(MONTH, MONTH_LOG, DATA_FILE)

	return 0

if __name__ == '__main__':
	sys.exit(main())
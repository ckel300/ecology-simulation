#!/usr/bin/python

"""
Conatins utility-type functions.

Function list:
generate_trees
generate_lumberjacks
generate_bears

log_month
log_year
"""

import sys
import random

# This is probably not the best way to store data.
# Alternatives include DB, JSON, File.

month_events = [
    'lumber harvested',
    'spaling(s) created',
    'lumberjack(s) maw\'d',
    'elder(s) created',
    'lumberjack(s) hired',
    'bear(s) captured',
    'bear(s) added',
    'tree(s)',
    'sapling(s)',
    'elder(s)',
    'lumberjack(s)',
    'bear(s)'
]

MONTH_DATA = {event: 1 for event in month_events}


"""
Data Representation and Generation
==================================

Every "player" or "object" type is an entity (i.e. Trees, Bears, Lumberjacks)
An entity object is an "instance" of the entity (e.g. a single tree)

Each entity will be a list of tuples. Each tuple will be an entity object.

Trees: ('x/y', age in months, type). The first is the 'id' - the string 'x/y'.
The second is the age in months, and the third is the type of tree
(0 for sapling, 1 for regular, 2 for elder)

Bears and Lumberjacks are similar. All entity objects will have the id but not
all will have age or type
"""


def generate_trees(amount, board_dim):
    """
    Generating the intial tree configuration with 'amount' number of trees.
    Returns the tree list and tree id list.

    Tree types:
    Sapling: 0
    Regular: 1 (default)
    Elder: 2
    """

    # TODO - not important but an option - I could sort the trees list in some
    # in some specific order rather than at random.

    trees = [0] * amount
    tree_ids = []
    open_spots = [None] * (board_dim ** 2)  # to avoid appending
    for i in xrange(len(open_spots)):
        for x in xrange(board_dim):
            for y in xrange(board_dim):
                open_spots[i] = '/'.join([str(x), str(y)])

    default_type = 1
    default_age = 0

    x = 0
    while x < len(trees):
        id_string = random.choice(open_spots)
        trees[x] = (id_string, default_age, default_type)
        tree_ids.append(id_string)
        open_spots.remove(id_string)
        x += 1

    MONTH_DATA['tree(s)'] += amount

    return (trees, tree_ids)


def generate_lumberjacks(amount, board_dim):
    """
    Generating the intial lumberjack configuration with 'amount' number of
    lumberjacks. Returns the lumberjack list.
    """

    lumberjacks = [0] * amount
    lumberjack_ids = []
    open_spots = [None] * (board_dim ** 2)  # to avoid appending
    for i in xrange(len(open_spots)):
        for x in xrange(board_dim):
            for y in xrange(board_dim):
                open_spots[i] = '/'.join([str(x), str(y)])

    x = 0
    while x < len(lumberjacks):
        id_string = random.choice(open_spots)
        lumberjacks[x] = (id_string)
        lumberjack_ids.append(id_string)
        open_spots.remove(id_string)
        x += 1

    MONTH_DATA['lumberjack(s)'] += amount

    return lumberjacks


def generate_bears(amount, board_dim):
    """
    Generating the intial bear configuration with 'amount' number of bears.
    Returns the bear list.

    Two options for bears - they could be required to NOT spawn where non-tree
    entities already are (and vice-versa) or it could not matter. For now I'll
    start with it not mattering.

    This is almost the exact same function as generate_trees and
    generate_lumberjacks
    """

    bears = [0] * amount
    bear_ids = []
    open_spots = [None] * (board_dim ** 2)  # to avoid appending
    for i in xrange(len(open_spots)):
        for x in xrange(board_dim):
            for y in xrange(board_dim):
                open_spots[i] = '/'.join([str(x), str(y)])

    x = 0
    while x < len(bears):
        id_string = random.choice(open_spots)
        bears[x] = (id_string)
        bear_ids.append(id_string)
        open_spots.remove(id_string)
        x += 1

    MONTH_DATA['bear(s)'] += amount

    return bears

#############################################

"""
Month/Year Logging
==================

Every month the following events will be logged. If none of these happen,
then nothing will be logged.

Lumber harvested
Sapling(s) created
Lumberjack(s) Maw'd
Tree(s) become elder tree(s)

Lumberjack hired
Bear(s) captured
Bear(s) added

AS WELL AS (originally planned only for year)

# of trees, saplings, and elders
# of lumberjacks
# of bears

Every year the following will be logged.
# of trees, saplings, and elders
# of lumberjacks
# of bears
# of lumberjacks hired
# of bears captured
# of mawings

All of are stored in dictionaries - event_string: num_times.
The dicts will be stored in this file and imported from the main.py file.
"""

# TODO: this should probably use a DB (overkill maybe? Nice learning experience
# though, ans would definitely make life easier)


def log_month(month, log_file):
    """
    A function to log month data into a a log file. The data will be taken from
    the MONTH_DATA dict and will be written to log_file.

    The first part of the data is events, the second is stats.
    """

    # TODO: make month number to be in the format of 0000, 0001, 0002, etc.
    # rather than 1, 2, 3 etc.

    month = str(month)  # just making sure
    log_string = 'Month ' + month + ': [{number}] {event} this month.\n'

    with open(log_file, 'a') as log_file:
        log_file.write('MONTH {month}\n'.format(month=month))
        log_file.write('========\n')

        for event in MONTH_DATA.keys():
            log_file.write(
                log_string.format(number=MONTH_DATA[event], event=event)
            )


# def log_year(year, log_file, data_file):
#     """
#     Similar to the second part of log_month - I'm simply logging stats to a
#     year_log file.
#     """

#     year = str(year)  # just making sure...

#     # First I need to skip the events and find the stats
#     # TODO: change data file to have events/stats headings and then write a
#     # find finction
#     with open(data_file, 'r') as data_file, open(log_file, 'a') as log_file:
#         for line in data_file:
#             if line in ['\n', '\r\n']:
#                 break

#         stats = {}
#         for line in data_file:
#             line_list = line.split(DELIM)
#             stats.update({line_list[0]: line_list[1].strip('\n')})

#         # TODO: probably don't need dict for this...
#         # horrible spagetti-y code. Need to simplify. A lot. Too complicated.
#         string = 'Year ' + year + ': {0} tree(s), {1} sapling(s), {2} elder(s), {3} lumberjack(s), {4} bear(s), {5} mawing(s)\n'
#         string = string.format(stats['trees'], stats['saplings'], stats['elders'], stats['lumberjacks'], stats['bears'], stats['mawings'])
#         log_file.write(string)

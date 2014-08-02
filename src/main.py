#!/usr/bin/pytho

"""
Main entry point for the ecology simulation. This script also contains all
the 'tick' logic
"""

import sys
import random

import util

# percentage of the board each entity will take up

TREE_PERCENTAGE = 0.5  # 50%
LUMBERJACK_PERCENTAGE = 0.1  # 10%
BEAR_PERCENTAGE = 0.02  # 2%

MONTH = 0
YEAR = 0

MONTH_LOG = 'month_log.txt'
YEAR_LOG = 'year_log.txt'


def generate_surrounding_coords(x, y):
    return (
        (x - 1, y + 1), (x, y + 1), (x + 1, y + 1), (x + 1, y),
        (x + 1, y - 1), (x, y - 1), (x - 1, y - 1), (x - 1, y)
    )


def tick_tree(tree_tuple, tree_ids):
    """
    Given a tree tuple in the format of (id_string, age, type), this function
    updates the tree. This happens every month.

    tree_ids is passed to check for if adjacent cells are taken.

    The logic:
    A regular tree (type 1) has a 10% chance of spawning a sapling in an
    adjacent open spot.

    After 12 months of existence, a sapling (type 0) will upgrade to a tree

    After 120 months of existence, a tree will upgrade to an
    elder tree (type 2)

    Returns the updated tree tuple, a list containing new trees, and a list
    containing new ids
    """

    # TODO - handle board wrapping (i.e. the cell to the left of a cell on the
    # left edge is the rightest cell - the board wraps around)

    current_id, current_age, current_type = tree_tuple
    x, y = tuple([int(element) for element in current_id.split('/')])
    current_age += 1

    new_trees = []
    new_ids = []

    if current_age is 12 and current_type is 0:
        current_age = 0  # the age is reset. I could keep it going and upgrade
        # to elder at 120 + 12, but I rather reset
        current_type = 1

    elif current_age is 120 and current_type is 1:
        # no need to reset age here, no more use for it
        current_type = 2

    tree_percentages = {0: 0.0, 1: 0.1, 2: 0.2}  # by tree type

    surrounding_coords = generate_surrounding_coords(x, y)
    available_coords = [
        i for i in surrounding_coords
        if '/'.join(str(coord) for coord in i) not in tree_ids
    ]

    try:
        if random.random() < tree_percentages[current_type]:
            # creating a new tree tuple and adding it to new_trees
            new_coords = random.choice(available_coords)
            new_id = '/'.join(str(coord) for coord in new_coords)
            new_trees.append((new_id, 0, 0))  # appending sapling to new_trees
            new_ids.append(new_id)
    except IndexError:
        pass  # try/except instead of if block. random.choice will throw and
        # IndexError if available_coords is empty.
        # In that case, we don't place a sapling, just keep going.
        # I'm just avoiding LBYL.

    # the first is an updated tree tuple for the current tree
    return ((current_id, current_age, current_type), new_trees, new_ids)


def tick_lumberjack(lumberjack_tuple, lumberjack_ids, tree_ids):
    """
    Given a tree tuple in the format of (id_string, age, type), this function
    updates the tree. This happens every month.
    """


def main():
    """
    Main entry point for the script
    """

    # TODO: implement Click for CLI interface

    util.generate_trees(50, 10)
    util.generate_lumberjacks(5, 10)
    util.generate_bears(5, 10)
    util.log_month(MONTH, MONTH_LOG)
    util.log_year(YEAR, YEAR_LOG)

    current_trees, current_ids = util.generate_trees(10, 5)

    for index, tree in enumerate(current_trees):
        new_tree, new_trees, new_ids = tick_tree(tree, current_ids)
        current_trees[index] = new_tree

        if new_trees:
            current_trees += new_trees

        if new_ids:
            current_ids += new_ids

    return 0

if __name__ == '__main__':
    sys.exit(main())

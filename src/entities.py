#!/usr/bin/python

import random

BOARD_DIM = 10  # this will later be grabbed as input


def generate_surrounding_coords(x, y):
    """
    Generates the surrounding 8 coords of (x, y)
    """

    # these are necessary for board wrapping
    #
    # Every 'x' has three possible values - x-1, x, x+1.
    # We'll call these x_right, x, x_left
    # Same for 'y' - y_top, y, y_bot
    # Note - y_bot is y+1, even though it is bottom (imagine a 2D array)

    # defaults (since x and y never change, no need to define them):
    x_right = x + 1
    x_left = x - 1

    y_top = y - 1
    y_bot = y + 1

    if x > (BOARD_DIM - 2):  # -1 for array 0-indexing and another -1 for the
        # actual wrapping
        x_right = 0
    elif x < 1:
        x_left = BOARD_DIM - 1

    if y < 1:
        y_top = BOARD_DIM - 1
    elif y > (BOARD_DIM - 2):
        y_bot = 0

    return [
        (x_right, y_bot), (x, y_bot), (x_left, y_bot), (x_left, y),
        (x_left, y_top), (x, y_top), (x_right, y_top), (x_right, y)
    ]


class Tree(object):
    """
    A Tree object.

    Instance attributes:
    x_coord
    y_oord
    age
    tree_type (sap, tree, elder)

    Class attributes:
    trees
    tree_coords

    Methods:
    month_tick
    spawn_sapling
    """

    trees = []  # list of all tree objects
    tree_coords = []  # list of all tree coord tuples

    sap_spawn_percentages = {'sap': 0.1, 'tree': 0.1, 'elder': 0.2}

    def __init__(self, x, y, age=0, tree_type='tree'):
        self.x = x
        self.y = y
        self.age = age
        self.tree_type = tree_type
        self.surrounding_coords = generate_surrounding_coords(x, y)

        self.trees.append(self)
        self.tree_coords.append((x, y))

    def spawn_sapling(self, x, y):
        """
        Spawns a sapling at given x, y, and adds to trees list
        """
        self.trees.append(Tree(x, y, 'sap'))

    def month_tick(self):
        """
        Updates self based on following logic:
        A regular tree has a 10% chance of spawning a sapling in an
        adjacent open spot.

        After 12 months of existence, a sapling (type 0) will upgrade to a tree
        After 120 months of existence, a tree will upgrade to an
        elder tree (type 2)
        """

        self.age += 1

        if self.type == 'sap' and self.age >= 12:
            self.type = 'tree'
            self.age = 0  # reset age here to go to 120

        if self.type == 'tree' and self.age >= 120:
            self.type = 'elder'
            self.age = 0  # no need to reset here, but just in case

        # The sapling
        available_coords = [
            i for i in self.surrounding_coords
            if i not in self.tree_coords
        ]

        if random.random() < self.sap_spawn_percentages[self.type]:
            new_x, new_y = random.choice(available_coords)
            self.spawn_sapling(new_x, new_y)

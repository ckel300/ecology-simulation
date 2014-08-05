#!/usr/bin/python

import unittest

import src.entities as entities


class GenerateCoordsTest(unittest.TestCase):
    """
    Tests for the generate_surrounding_coords function
    """

    def test_generate_surrounding_coords_normal(self):
        """
        Does generate_surrounding_coords always return the surounding 8 coords?
        """
        self.assertEquals(entities.generate_surrounding_coords(5, 8), [
            (6, 9), (5, 9), (4, 9), (4, 8),
            (4, 7), (5, 7), (6, 7), (6, 8)
            ],
            msg='(5, 8) did not pass.'
        )

        self.assertEquals(entities.generate_surrounding_coords(3, 7), [
            (4, 8), (3, 8), (2, 8), (2, 7),
            (2, 6), (3, 6), (4, 6), (4, 7)
            ],
            msg='(3, 7) did not pass.'
        )

    def test_generate_surrounding_coords_edges(self):
        """
        Does generate_surrounding_coords always work for edges?
        """

        # upper edge
        self.assertEquals(entities.generate_surrounding_coords(5, 0), [
            (6, 1), (5, 1), (4, 1), (4, 0),
            (4, 9), (5, 9), (6, 9), (6, 0)
            ],
            msg='(5, 0) upper edge did not pass.'
        )

        # right edge
        self.assertEquals(entities.generate_surrounding_coords(9, 5), [
            (0, 6), (9, 6), (8, 6), (8, 5),
            (8, 4), (9, 4), (0, 4), (0, 5)
            ],
            msg='(9, 5) right edge did not pass.'
        )

        # lower edge
        self.assertEquals(entities.generate_surrounding_coords(4, 9), [
            (5, 0), (4, 0), (3, 0), (3, 9),
            (3, 8), (4, 8), (5, 8), (5, 9)
            ],
            msg='(4, 9) lower edge did not pass.'
        )

        # left edge
        self.assertEquals(entities.generate_surrounding_coords(0, 3), [
            (1, 4), (0, 4), (9, 4), (9, 3),
            (9, 2), (0, 2), (1, 2), (1, 3)
            ],
            msg='(0, 3) left edge did not pass.')

    def test_generate_surrounding_coords_corners(self):
        """
        Does generate_surrounding_coords always work for corners?
        """

        # upper left corner
        self.assertEquals(entities.generate_surrounding_coords(0, 0), [
            (1, 1), (0, 1), (9, 1), (9, 0),
            (9, 9), (0, 9), (1, 9), (1, 0)
            ],
            msg='(0, 0) upper left corner did not pass.'
            )

        # upper right corner
        self.assertEquals(entities.generate_surrounding_coords(9, 0), [
            (0, 1), (9, 1), (8, 1), (8, 0),
            (8, 9), (9, 9), (0, 9), (0, 0)
            ],
            msg='(9, 0) upper right corner did not pass.'
            )

        # lower right corner
        self.assertEquals(entities.generate_surrounding_coords(9, 9), [
            (0, 0), (9, 0), (8, 0), (8, 9),
            (8, 8), (9, 8), (0, 8), (0, 9)
            ],
            msg='(9, 9) lower right corner did not pass.'
            )

        # lower left corner
        self.assertEquals(entities.generate_surrounding_coords(0, 9), [
            (1, 0), (0, 0), (9, 0), (9, 9),
            (9, 8), (0, 8), (1, 8), (1, 9)
            ],
            msg='(0, 9) lower left corner did not pass.'
            )


class TreeTest(unittest.TestCase):
    """
    Tests for all the Tree functions
    """

    def setUp(self):
        self.trees = []

        # a tree of each type
        self.sapling = entities.Tree(7, 2, 3, 'sap')
        self.regular_tree = entities.Tree(5, 8, 56, 'tree')
        self.elder_tree = entities.Tree(2, 8, 124, 'elder')

        # a corner tree and an edge tree
        self.edge_reguler = entities.Tree(9, 7)
        self.corner_regular = entities.Tree(9, 0)

        self.trees.append(self.sapling)
        self.trees.append(self.regular_tree)
        self.trees.append(self.elder_tree)
        self.trees.append(self.edge_reguler)
        self.trees.append(self.corner_regular)

    def test_spawn_sapling(self):
        """
        Will spawn_sapling always correctly spawn a new tree?
        """

        # Not testing sapling since it shouldn't spawn a sap anyways

        ##############################
        # regular_tree sapling spawn #
        ##############################
        regular_sap_spawn = self.regular_tree.spawn_sapling()

        # checking that it is indeed a Tree object
        self.assertIsInstance(regular_sap_spawn, entities.Tree)

        # checking that x and y are in surrounding coords
        self.assertIn((regular_sap_spawn.x, regular_sap_spawn.y),
                      self.regular_tree.available_coords)

        # checking age and type
        self.assertEquals(regular_sap_spawn.age, 0)
        self.assertEquals(regular_sap_spawn.tree_type, 'sap')

        ############################
        # elder_tree sapling spawn #
        ############################
        elder_sap_spawn = self.elder_tree.spawn_sapling()

        self.assertIsInstance(elder_sap_spawn, entities.Tree)
        self.assertIn((elder_sap_spawn.x, elder_sap_spawn.y),
                      self.elder_tree.available_coords)
        self.assertEquals(elder_sap_spawn.age, 0)
        self.assertEquals(elder_sap_spawn.tree_type, 'sap')

    def tearDown(self):
        # resetting the trees list
        self.trees = []

        self.trees.append(self.sapling)
        self.trees.append(self.regular_tree)
        self.trees.append(self.elder_tree)
        self.trees.append(self.edge_reguler)
        self.trees.append(self.corner_regular)


if __name__ == '__main__':
    unittest.main()

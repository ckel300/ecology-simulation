#!/usr/bin/python

import unittest

import src.entities as entities


class TreeTest(unittest.TestCase):
    """
    Tests for all the Tree functions
    """

    def setUp(self):
        self.all_entity = []

        # a tree of each type
        self.sapling = entities.Tree(7, 2, 10, 'sap')
        self.regular_tree = entities.Tree(6, 9, 119, 'tree')
        self.elder_tree = entities.Tree(2, 8, 124, 'elder')

        # a corner tree and an edge tree
        self.edge_reguler = entities.Tree(9, 7)
        self.corner_regular = entities.Tree(9, 0)

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

        # checking that available_coords is fine in the sapling
        self.assertLessEqual(len(regular_sap_spawn.available_coords), 7)

        # checking age, type and lumber yield
        self.assertEquals(regular_sap_spawn.age, 0)
        self.assertEquals(regular_sap_spawn.tree_type, 'sap')
        self.assertEquals(regular_sap_spawn.lumber, 0)

        self.regular_tree.spawned_sapling = False  # cleanup for next part

        ############################
        # elder_tree sapling spawn #
        ############################
        elder_sap_spawn = self.elder_tree.spawn_sapling()

        self.assertIsInstance(elder_sap_spawn, entities.Tree)
        self.assertIn((elder_sap_spawn.x, elder_sap_spawn.y),
                      self.elder_tree.available_coords)

        self.assertLessEqual(len(elder_sap_spawn.available_coords), 7)

        self.assertEquals(elder_sap_spawn.age, 0)
        self.assertEquals(elder_sap_spawn.tree_type, 'sap')
        self.assertEquals(regular_sap_spawn.lumber, 0)

        self.elder_tree.spawned_sapling = False

    def test_month_tick(self):
        """
        Does month_tick properly 'tick' the trees everytime?
        """

        ######################
        # sapling month tick #
        ######################
        self.sapling.month_tick()  # changing state rather than returning new

        # checking age
        self.assertEquals(self.sapling.age, 11)

        # checking type
        self.assertEquals(self.sapling.tree_type, 'sap')

        # checking that sapling was NOT spawned
        self.assertEquals(self.sapling.spawned_sapling, False)

        ###########################
        # regular_tree month tick #
        ###########################
        self.regular_tree.month_tick()

        self.assertEquals(self.regular_tree.age, 0)
        self.assertEquals(self.regular_tree.tree_type, 'elder')
        self.assertEquals(self.regular_tree.spawned_sapling, True)

        #########################
        # elder_tree month tick #
        #########################
        self.elder_tree.month_tick()

        self.assertEquals(self.elder_tree.age, 125)
        self.assertEquals(self.elder_tree.tree_type, 'elder')
        self.assertEquals(self.elder_tree.spawned_sapling, True)

    def tearDown(self):
        # nothing here for now...
        pass

if __name__ == '__main__':
    unittest.main()
`
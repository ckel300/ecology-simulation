#!/usr/bin/python

import unittest

import entities


class TreeTest(unittest.TestCase):
    """
    Tests for the entities.Tree class and various helper functions.
    """

    def test_generate_surrounding_coords(self):
        """
        Does generate_surrounding_coords always return the surounding 8 coords
        """
        self.assertEquals(entities.generate_surrounding_coords(5, 8), [
            (6, 9), (5, 9), (4, 9), (4, 8),
            (4, 7), (5, 7), (6, 7), (6, 8)
            ]
        )

        self.assertEquals(entities.generate_surrounding_coords(3, 7), [
            (4, 8), (3, 8), (2, 8), (2, 7),
            (2, 6), (3, 6), (4, 6), (4, 7)
            ]
        )

if __name__ == '__main__':
    unittest.main()

#!/usr/bin/python

import unittest

import entities


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
        self.assertEquals(entities.generate_surrounding_coords(5, 0), [
            (6, 1), (5, 1), (4, 1), (4, 0),
            (4, 9), (5, 9), (6, 9), (6, 0)
            ],
            msg='(5, 0) upper edge did not pass.'
        )

if __name__ == '__main__':
    unittest.main()

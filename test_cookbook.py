"""
Test suite for Online Cookbook
"""

import unittest
import app

class TestCookbook(unittest.TestCase):

    def test_get_recipes(self):
        """
        Test to ensure we can read recipes collection from the database
        """
        recipes = list(app.get_recipes())
        self.assertTrue(len(recipes) > 0)

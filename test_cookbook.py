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

    def test_get_recipes_by_filters(self):
        """
        Test to ensure we can read subset of recipes based on type and cuisine filters
        """
        american_recipes = list(app.get_recipes_by_filters({'type':'','cuisine':'American'}))
        self.assertTrue(recipe['cuisine'] == 'american' for recipe in american_recipes)
        starter_recipes = list(app.get_recipes_by_filters(
            {'type': 'starter', 'cuisine': ''}))
        self.assertTrue(recipe['type'] ==
                        'starter' for recipe in starter_recipes)
        french_dessert_recipes = list(app.get_recipes_by_filters(
                {'type': 'dessert', 'cuisine': 'french'}))
        self.assertTrue(recipe['type'] ==
                        'dessert' and recipe['cuisine'] == 'french' for recipe in french_dessert_recipes)

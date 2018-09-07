"""
Test suite for Online Cookbook
"""

import unittest
import app
from bson.objectid import ObjectId


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
        american_recipes = list(app.get_recipes_by_filters(
            {'type': '', 'cuisine': 'American'}))
        self.assertTrue(recipe['cuisine'] ==
                        'american' for recipe in american_recipes)
        starter_recipes = list(app.get_recipes_by_filters(
            {'type': 'starter', 'cuisine': ''}))
        self.assertTrue(recipe['type'] ==
                        'starter' for recipe in starter_recipes)
        french_dessert_recipes = list(app.get_recipes_by_filters(
            {'type': 'dessert', 'cuisine': 'french'}))
        self.assertTrue(recipe['type'] ==
                        'dessert' and recipe['cuisine'] == 'french' for recipe in french_dessert_recipes)

    def test_add_recipe(self):
        """
        Test to ensure we can add a recipe to the database
        """
        new_recipe = {
            "_id": ObjectId("000000000000000000000001"),
            "name": "Traditional Victoria sponge",
            "time": {
                "hours": 1,
                "minutes": 5
            },
            "author": "5b648d93fb6fc072a40f6d8f",
            "description": "This is the traditional recipe for a Victoria sponge cake, a much loved English favourite. See footnote about weighing the eggs for best results. Serve with buttercream as in the recipe, or freshly whipped cream.",
            "ingredients": [
                "3 eggs",
                "150g(6 oz) self raising flour",
                "150g(6 oz) caster sugar",
                "150g(6 oz) butter or margarine",
                "1/2 teaspoon vanilla extract",
                "jam to sandwich the cake",
                "100g(4 oz) icing sugar",
                "50g(2 oz) butter",
                "1/2 teaspoon of vanilla extract"
            ],
            "method": [
                "Preheat the oven to 170 C / Gas 3. Place the shelf in the centre of the oven. Grease and line two 18cm(7 in) sandwich tins with baking parchment.",
                "Weigh the three eggs. Note the weight and measure the same amount of sugar, flour and butter.",
                "Sieve the flour into a bowl and add the sugar, butter or margarine and vanilla. Crack in the eggs and beat well with a wooden spoon or mixer, until the mixture is light coloured and fluffy. Divide the cake mixture between the tins and smooth the tops.",
                "Bake for 30 to 40 minutes or until golden brown. Cool for 5 minutes in the tins, then turn out onto a wire rack to cool completely.",
                "To make the buttercream, sieve the sugar into a bowl, add the butter and vanilla and beat well.",
                "To sandwich the cakes together: Add a layer of jam to the top of one of the sponges, followed by a layer of cream on top of the jam, finish by placing the last of the sponges on top. Dust with a layer of icing sugar if desired."
            ],
            "image_url": "http://ukcdn.ar-cdn.com/recipes/port500/88a85f78-14cb-4dab-89f5-67cea2fce3fa.jpg",
            "date_added": "Thu Sep 06 2018 12:56:46 GMT+0100 (IST)",
            "favourites": 105,
            "cuisine": "british",
            "type": "cake"
        }
        app.add_recipe(new_recipe)
        self.assertTrue(new_recipe in list(app.get_recipes()))

    def test_get_recipe_by_id(self):
        """
        Test to ensure we can get a recipe from the database by its id
        """
        recipe_id = '5b91483146073f953359fce8'
        self.assertEqual(app.get_recipe_by_id(recipe_id)[
                         'name'], 'Cinnamon Chocolate Soufflé')

    def test_update_recipe(self):
        """
        Test to ensure we can update a recipe in the database
        """
        recipe = app.get_recipe_by_id('5b91483146073f953359fce8')
        recipe['favourites'] = 289
        app.update_recipe(recipe)
        self.assertEqual(app.get_recipe_by_id(
            recipe['_id'])['favourites'], 289)

    def test_delete_recipe(self):
        """
        Test to ensure we can remove a recipe from the database
        """
        recipe_id = '000000000000000000000001'
        app.delete_recipe(recipe_id)
        self.assertNotIn(app.get_recipe_by_id(
            recipe_id), list(app.get_recipes()))

    def test_get_users(self):
        """
        Test to ensure we can read users from the database
        """
        self.assertTrue(len(list(app.get_users())) > 0)

    def test_create_user(self):
        """
        Test to ensure we can add a user to the database
        """
        new_user = {
            "_id": ObjectId("000000000000000000000002"),
            "name": "Polly O'Donovan",
            "username": "pollypocket",
            "my_recipes": [],
            "favourite_recipes": []
        }
        app.add_user(new_user)
        self.assertIn(new_user, list(app.get_users()))
        app.delete_user('000000000000000000000002')


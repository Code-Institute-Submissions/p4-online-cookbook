"""
Test suite for Online Cookbook
"""

import unittest
import app
from bson.objectid import ObjectId


class TestCookbook(unittest.TestCase):
    """
    Test suite for Online Cookbook
    """

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

    def test_get_recipe(self):
        """
        Test to ensure we can get a recipe from the database by its id
        """
        recipe_id = '5b91483146073f953359fce8'
        self.assertEqual(app.get_recipe(recipe_id)['name'], 'Cinnamon Chocolate Soufflé')

    def test_update_recipe(self):
        """
        Test to ensure we can update a recipe in the database
        """
        recipe_id = '5b91483146073f953359fce8'
        recipe_form = {
            "name": "Chocolate Soufflé",
            "hours": 0,
            "minutes": 30,
            "description": "So easy to make and so yummy!",
            "ingredients": "A little melted butter and caster sugar for coating the souffle dish\r\n75g (2 1/2 oz) plain chocolate\r\n1 tablespoon milk\r\n50g (2 oz) butter\r\n40g (1 1/2 oz) plain flour\r\n300ml milk\r\n1/2 tsp cinnamon powder\r\n5 eggs, seperated into yolks and whites\r\n2 tablespoons of caster sugar\r\n",
            "method": "Preheat over to 200 degrees C / gas mark 6.\r\nGrease an 8 inch souffle dish (or 4 small individual ramekins) with melted butter and dust with sugar.\r\nPut 1 tablespoon of milk and the chocolate in a heat-proof bowl and melt over hot boiling water. Set aside.\r\nMelt butter in a saucepan over gentle heat, then add the flour all at once; mix well and remove from the heat.\r\nAdd milk into flour mixture a little at a time, stirring constantly until the mixture forms a creamy paste.\r\nAdd melted chocolate, cinnamon and all five egg yolks. Mix well and set aside.\r\nWhisk five egg whites and add sugar, 1 tablespoon at a time. Keep whisking until egg whites look like foamy bubbles.\r\nSlowly add whisked egg whites into chocolate mixture. Pour into souffle dish and bake for 20 minutes.\r\nServe immediately.\r\n",
            "image_url": "http://ukcdn.ar-cdn.com/recipes/port250/67608ebb-163e-4682-b2f2-66e982331c3b.jpg",
            "cuisine": "french",
            "type": "dessert"
        }
        app.update_recipe(recipe_id, recipe_form)
        self.assertEqual(app.get_recipe(recipe_id)['name'], 'Chocolate Soufflé')
        #reset after test
        recipe_form['name'] = 'Cinnamon Chocolate Soufflé'
        app.update_recipe(recipe_id, recipe_form)

    def test_delete_recipe(self):
        """
        Test to ensure we can remove a recipe from the database
        """
        recipe_id = '000000000000000000000001'
        app.delete_recipe(recipe_id)
        self.assertNotIn(app.get_recipe(recipe_id),list(app.get_recipes()))

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

    def test_get_user_by_id(self):
        """
        Test to ensure we can get a user from the database by their id
        """
        user_id = "5b648d93fb6fc072a40f6d8f"
        self.assertEqual(app.get_user_by_id(user_id)['username'], 'sarahloh')

    def test_get_user_by_username(self):
        """
        Test to ensure we can get a user from the database by their username
        """
        username = "sarahloh"
        user_id = "5b648d93fb6fc072a40f6d8f"
        self.assertEqual(app.get_user_by_username(
            username)['_id'], ObjectId(user_id))

    def test_get_user_recipes(self):
        """
        Test to ensure we can get users' recipes
        """
        username = "sarahloh"
        self.assertIn(app.get_recipe('5b91483146073f953359fce8'),
                      list(app.get_user_recipes(username)))

    def test_get_user_favourites(self):
        """
        Test to ensure we can get users' favourite recipes
        """
        username = "sarahloh"
        self.assertIn(app.get_recipe('5b91483146073f953359fce8'),
                      app.get_user_favourites(username))

    def test_remove_user_recipe(self):
        """
        Test to ensure we can remove a recipe id from a user's list of recipes
        """
        username = "sarahloh"
        user_id = "5b648d93fb6fc072a40f6d8f"
        recipe_id = "5b8fc23a59d1979fc3608b0a"
        app.remove_user_recipe_from_list(user_id, 'my_recipes', recipe_id)
        self.assertNotIn(recipe_id, list(app.get_user_recipes(username)))

        # re-add recipe after test
        app.add_user_recipe_to_list(user_id, 'my_recipes', recipe_id)

    def test_add_user_recipe(self):
        """
        Test to ensure we can add a recipe id to a user's list of recipes
        """
        username = "sarahloh"
        user_id = "5b648d93fb6fc072a40f6d8f"
        recipe_id = "5b8fc23a59d1979fc3608b0a"

        # remove recipe before test
        app.remove_user_recipe_from_list(user_id, 'my_recipes', recipe_id)

        app.add_user_recipe_to_list(user_id, 'my_recipes', recipe_id)
        self.assertIn(app.get_recipe(recipe_id),
                      list(app.get_user_recipes(username)))

    def test_remove_user_favourite(self):
        """
        Test to ensure we can remove a recipe id from a user's favourites list
        """
        username = "sarahloh"
        user_id = "5b648d93fb6fc072a40f6d8f"
        recipe_id = "5b8fc23a59d1979fc3608b09"
        app.remove_user_recipe_from_list(
            user_id, 'favourite_recipes', recipe_id)
        self.assertNotIn(recipe_id, list(app.get_user_recipes(username)))

        # re-add recipe after test
        app.add_user_recipe_to_list(user_id, 'favourite_recipes', recipe_id)

    def test_add_user_favourite(self):
        """
        Test to ensure we can add a recipe id to a user's favourites list
        """
        username = "sarahloh"
        user_id = "5b648d93fb6fc072a40f6d8f"
        recipe_id = "5b8fc23a59d1979fc3608b09"

        # remove recipe before test
        app.remove_user_recipe_from_list(
            user_id, 'favourite_recipes', recipe_id)

        app.add_user_recipe_to_list(user_id, 'favourite_recipes', recipe_id)
        self.assertIn(app.get_recipe(recipe_id),
                      list(app.get_user_recipes(username)))

    def test_favourite_a_recipe(self):
        """
        Test to ensure we can increment a recipe's number of favourites
        """
        recipe_id = "5b8fc23a59d1979fc3608b0b"
        num_favs = app.get_recipe(recipe_id)['favourites']
        app.favourite_a_recipe(recipe_id)
        self.assertEqual(app.get_recipe(recipe_id)['favourites'], num_favs+1)

    def test_unfavourite_a_recipe(self):
        """
        Test to ensure we can decrement a recipe's number of favourites
        """
        recipe_id = "5b8fc23a59d1979fc3608b0b"
        num_favs = app.get_recipe(recipe_id)['favourites']
        app.unfavourite_a_recipe(recipe_id)
        self.assertEqual(app.get_recipe(recipe_id)['favourites'], num_favs-1)

    def test_authenticate_user(self):
        """
        Test to ensure that we can see if a user exists or not
        """
        username = "sarahloh"
        not_a_username = "ilovecake"
        self.assertTrue(app.authenticate_user(username))
        self.assertFalse(app.authenticate_user(not_a_username))

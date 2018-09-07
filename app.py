import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'sl_task_manager'
app.config["MONGO_URI"] = os.getenv('MONGO_URI')

mongo = PyMongo(app)


@app.route('/')
def index():
    """
    Display the recipes colection on index.html
    """
    return render_template("index.html", recipes=get_recipes())


def get_recipes():
    """
    Read all recipes fromthe database and return a list sorted by favourites in descending order
    """
    return mongo.db.recipes.find().sort('favourites', -1)


def get_recipes_by_filters(filters):
    """
    Read recipes from the database based on filters
    """
    if filters['type'] == '':
        return mongo.db.recipes.find({'cuisine': filters['cuisine']})
    elif filters['cuisine'] == '':
        return mongo.db.recipes.find({'type': filters['type']})
    else:
        return mongo.db.recipes.find({'type': filters['type'], 'cuisine': filters['cuisine']})


def add_recipe(recipe):
    """
    Add new recipe to the database
    """
    mongo.db.recipes.insert_one(recipe)


def get_recipe_by_id(recipe_id):
    """
    Get recipe from the database based on its id
    """
    return mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})


def update_recipe(recipe):
    """
    Update recipe in the datebase
    """
    mongo.db.recipes.replace_one({'_id': recipe['_id']}, recipe)


def delete_recipe(recipe_id):
    """
    Remove a recipe from the database based on its id
    """
    try:
        mongo.db.recipes.delete_one({'_id': ObjectId(recipe_id)})
    except:
        print('Recipe with id %s was not deleted' % recipe_id)


def get_users():
    """
    Read all users from the database
    """
    return mongo.db.users.find()


def add_user(user):
    """
    Add new user to the database
    """
    mongo.db.users.insert_one(user)


def delete_user(user_id):
    """
    Remove user from the database
    """
    mongo.db.users.delete_one({'_id': ObjectId(user_id)})


if __name__ == '__main__':
    app.run(host=os.getenv('IP'),
            port=os.getenv('PORT'),
            debug=True)

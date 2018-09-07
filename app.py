import os
from flask import Flask, render_template, redirect, request, url_for, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.secret_key = 'some_secret'

app.config["MONGO_DBNAME"] = 'sl_task_manager'
app.config["MONGO_URI"] = os.getenv('MONGO_URI')

mongo = PyMongo(app)


@app.route('/', defaults={'username':None})
@app.route('/<username>')
def index(username):
    """
    Display the recipes colection on index.html
    """
    return render_template("index.html", recipes=get_recipes(), user=get_user_by_username(username))


@app.route('/login',  methods=['POST'])
def login():
    """
    Authenticate a user and redirect back
    """
    username_input = request.form.get('username')
    if 'login' in request.form:
        if authenticate_user(username_input):
            flash('You were successfully logged in!')
            return redirect(url_for('index', username=username_input))
        else:
            flash('Sorry - that username is not registered!')
            return redirect(url_for('index'))
    else:
        # sign up was selected
        return redirect(url_for('signup', username=username_input))





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


def get_recipe(recipe_id):
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


def get_user_by_id(user_id):
    """
    Get user from the database by their id
    """
    return mongo.db.users.find_one({'_id': ObjectId(user_id)})


def get_user_by_username(username):
    """
    Get user from the database by their username
    """
    return mongo.db.users.find_one({'username': username})


def delete_user(user_id):
    """
    Remove user from the database
    """
    mongo.db.users.delete_one({'_id': ObjectId(user_id)})


def get_user_recipes(user_id):
    """
    Get user's recipes from the database
    """
    return mongo.db.recipes.find({'author': user_id})


def get_user_favourites(user_id):
    """
    Get user's favourite recipes from the database
    """
    favourite_ids = list(mongo.db.users.find_one({"_id": ObjectId(user_id)}, {
                         "_id": 0, "name": 0, "username": 0, "my_recipes": 0})['favourite_recipes'])
    return [get_recipe(recipe_id) for recipe_id in favourite_ids]


def add_user_recipe_to_list(user_id, list_name, recipe_id):
    """
    Add recipe id to user's my_recipes list
    """
    try:
        mongo.db.users.update_one({'_id': ObjectId(user_id)}, {
                                  '$push': {list_name: recipe_id}})
    except:
        print("Recipe id not added to user's list")


def remove_user_recipe_from_list(user_id, list_name, recipe_id):
    """
    Remove recipe id from user's recipe list
    """
    try:
        mongo.db.users.update_one({'_id': ObjectId(user_id)}, {
                                  '$pull': {list_name: recipe_id}})
    except:
        print("Recipe id not removed from user's list")


def favourite_a_recipe(recipe_id):
    """
    Increment a recipe's number of favourites
    """
    mongo.db.recipes.update_one({'_id': ObjectId(recipe_id)}, {'$inc': {'favourites': 1}})


def unfavourite_a_recipe(recipe_id):
    """
    Decrement a recipe's number of favourites
    """
    mongo.db.recipes.update_one({'_id': ObjectId(recipe_id)}, {
                                '$inc': {'favourites': -1}})


def authenticate_user(username):
    """
    Check if a user exists by their username
    """
    return True if get_user_by_username(username) else False


if __name__ == '__main__':
    app.run(host=os.getenv('IP'),
            port=os.getenv('PORT'),
            debug=True)

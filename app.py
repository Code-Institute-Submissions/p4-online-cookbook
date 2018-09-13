import os
from flask import Flask, render_template, redirect, request, url_for, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.secret_key = os.getenv('APP_SECRET_FLASH')

app.config["MONGO_DBNAME"] = 'sl_task_manager'
app.config["MONGO_URI"] = os.getenv('MONGO_URI')

mongo = PyMongo(app)


# ROUTES

@app.route('/', methods=['GET', 'POST'], defaults={'filter_type': 'all', 'filter_cuisine': 'all', 'username': None})
@app.route('/<filter_type>/<filter_cuisine>', defaults={'username': None})
@app.route('/<filter_type>/<filter_cuisine>/<username>', methods=['GET', 'POST'])
def index(filter_type, filter_cuisine, username):
    """
    Display the recipes colection on index.html
    """
    filters = {
        'type': filter_type,
        'cuisine': filter_cuisine
    }
    if request.method == 'GET':
        if username:
            return render_template("index.html", recipes=get_recipes_by_filters(filters), user=get_user_by_username(username), user_favs=get_user_favourites_ids(username), filters=filters)
        else:
            return render_template("index.html", recipes=get_recipes_by_filters(filters), filters=filters)
    else:
        # POST request
        new_filters = {
            'type': 'all' if request.form['type'] == 'All' else request.form['type'].lower(),
            'cuisine': 'all' if request.form['cuisine'] == 'All' else request.form['cuisine'].lower()
        }
        if username:
            return redirect(url_for('index', filter_type=new_filters['type'], filter_cuisine=new_filters['cuisine'], username=username))
        else:
            return redirect(url_for('index', filter_type=new_filters['type'], filter_cuisine=new_filters['cuisine']))


@app.route('/login',  methods=['POST'])
def login():
    """
    Authenticate a user and redirect back
    """
    username_input = request.form.get('username')
    if 'login' in request.form:
        if authenticate_user(username_input):
            flash('Welcome back %s!' % username_input)
            return redirect(url_for('index', filter_type='all', filter_cuisine='all', username=username_input))
        else:
            flash('Sorry - the username "%s" is not registered!' %
                  username_input)
            return redirect(url_for('index'))
    else:
        # sign up was selected
        return redirect(url_for('signup', username=username_input))


@app.route('/signup/', methods=['GET', 'POST'], defaults={'username': None})
@app.route('/signup/<username>')
def signup(username):
    """
    Render signup page with GET and register a new user with POST request
    """
    if request.method == 'GET':
        return render_template("signup.html", username=username)
    else:
        if authenticate_user(request.form['username']):
            error_msg = "The username '%s' is already taken!" % request.form['username']
            return render_template("signup.html", username=None, username_error=error_msg)
        else:
            new_user = {
                'name': request.form['name'],
                'username': request.form['username'],
                'my_recipes': [],
                'favourite_recipes': []
            }
            mongo.db.users.insert_one(new_user)
            flash('Welcome %s!' % new_user['username'])
            return redirect(url_for('index', filter_type='all', filter_cuisine='all', username=new_user['username']))


@app.route('/logout/<username>')
def logout(username):
    """
    Log user out
    """
    flash('Goodbye %s! You have been logged out.' % username)
    return redirect(url_for('index'))


@app.route('/favourite/<user_id>/<recipe_id>')
def favourite(user_id, recipe_id):
    """
    Handle user click on recipe favourite icon to add favourite
    """
    add_user_recipe_to_list(user_id, 'favourite_recipes', recipe_id)
    favourite_a_recipe(recipe_id)
    return redirect(request.args.get('next'))


@app.route('/unfavourite/<user_id>/<recipe_id>')
def unfavourite(user_id, recipe_id):
    """
    Handle user click on recipe favourite icon to remove from favourites
    """
    remove_user_recipe_from_list(user_id, 'favourite_recipes', recipe_id)
    unfavourite_a_recipe(recipe_id)
    return redirect(request.args.get('next'))


@app.route('/recipe/<recipe_id>/', defaults={'username': None})
@app.route('/recipe/<recipe_id>/<username>')
def recipe(recipe_id, username):
    """
    Render the recipe page
    """
    if username:
        return render_template("recipe.html", recipe=get_recipe(recipe_id), author=get_recipe_author(recipe_id), user=get_user_by_username(username), user_favs=get_user_favourites_ids(username))
    else:
        return render_template("recipe.html", recipe=get_recipe(recipe_id), author=get_recipe_author(recipe_id))


@app.route('/dashboard/<username>')
def dashboard(username):
    """
    Render the dashboard where users can manage recipes
    """
    return render_template('dashboard.html', user=get_user_by_username(username), recipes=get_user_recipes(username), favourites=get_user_favourites(username))


@app.route('/edit/<recipe_id>/<username>', methods=['GET', 'POST'])
def edit(recipe_id, username):
    """
    Render the edit template where the user can make changes to a recipe
    """
    if request.method == 'GET':
        return render_template('edit.html', recipe=get_recipe(recipe_id), user=get_user_by_username(username))
    else:
        update_recipe(recipe_id, request.form)
        return redirect(url_for('recipe', recipe_id=recipe_id, username=username))


# FUNCTIONS

def get_recipe_author(recipe_id):
    """
    Get author username for a recipe
    """
    return mongo.db.users.find_one({'my_recipes': {'$in': ['5b643f0dfb6fc072a40f32e4']}})['username']


def get_recipes():
    """
    Read all recipes fromthe database and return a list sorted by favourites in descending order
    """
    return mongo.db.recipes.find().sort('favourites', -1)


def get_recipes_by_filters(filters):
    """
    Read recipes from the database based on filters
    """
    if (filters['type'] == 'all' and filters['cuisine'] == 'all'):
        return mongo.db.recipes.find()
    elif filters['type'] == 'all':
        return mongo.db.recipes.find({'cuisine': filters['cuisine']})
    elif filters['cuisine'] == 'all':
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


def update_recipe(recipe_id,recipe_form):
    """
    Update recipe in the datebase
    """
    mongo.db.recipes.update_one({'_id': ObjectId(recipe_id)}, {
        '$set': {
            'name': recipe_form['name'],
            'time': {
                'hours': int(recipe_form['hours']),
                'minutes': int(recipe_form['minutes'])
            },
            'description': recipe_form['description'],
            'ingredients': recipe_form['ingredients'].split('\r\n')[:-1],
            'method': recipe_form['method'].split('\r\n')[:-1],
            'image_url': recipe_form['image_url'],
            'cuisine': recipe_form['cuisine'],
            'type': recipe_form['type']
    }})


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


def get_user_recipes(username):
    """
    Get user's recipes from the database
    """
    return mongo.db.recipes.find({'author': '%s' % get_user_by_username(username)['_id']})


def get_user_favourites(username):
    """
    Get user's favourite recipes from the database
    """
    return [get_recipe(recipe_id) for recipe_id in get_user_favourites_ids(username)]


def get_user_favourites_ids(username):
    """
    Get a list of ids for a user's favourite recipes from the database
    """
    favourites_ids = list(mongo.db.users.find_one({"username": username}, {"_id": 0, "name": 0, "username": 0, "my_recipes": 0})['favourite_recipes']) if username else []
    return favourites_ids


def add_user_recipe_to_list(user_id, list_name, recipe_id):
    """
    Add recipe id to user's my_recipes or favourite_recipes list
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
    mongo.db.recipes.update_one({'_id': ObjectId(recipe_id)}, {
                                '$inc': {'favourites': 1}})


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

import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo

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
        return mongo.db.recipes.find({ 'cuisine': filters['cuisine'] })
    elif filters['cuisine'] == '':
        return mongo.db.recipes.find({'type': filters['type']})
    else:
        return mongo.db.recipes.find({'type': filters['type'], 'cuisine': filters['cuisine']})

def add_recipe(recipe):
    """
    Add new recipe to the database
    """
    mongo.db.recipes.insert_one(recipe)


if __name__ == '__main__':
    app.run(host=os.getenv('IP'),
            port=os.getenv('PORT'),
            debug=True)

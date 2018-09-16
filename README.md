# Milestone Project - Online Cookbook

**Data Centric Development**

*Developer: sarahloh*

App available at


1. [Project Brief](#1-project-brief)
2. [Guidelines](#2-guidelines)
3. [Technologies](#3-technologies-and-dependencies)
4. [Workspace](#4-workspace)
5. [Workflow](#5-workflow)
6. [UXD](#6-uxd)
7. [Database Schema](#7-database-schema)
8. [Wireframes](#8-wireframes)
9. [Heroku Deployment](#9-heroku-deployment)
10. [Features](#10-features)
11. [Testing](#11-testing)
12. [How To Deploy Locally](#12-how-to-deploy-locally)
13. [Credits](#13-credits)

## 1 Project Brief

[Project brief available here](https://github.com/sarahloh/p4-online-cookbook/blob/master/resources/project_brief.md)


## 2 Guidelines

[Project guidelines available here](https://github.com/sarahloh/p4-online-cookbook/blob/master/resources/project_guidelines.md)


## 3 Technologies and Dependencies

**Backend**

- [Python3](https://www.python.org)
- [pip3](https://pip.pypa.io/en/stable/)
- [Flask](http://flask.pocoo.org)
- [flask-pymongo](http://flask-pymongo.readthedocs.io/en/latest/)
- [MongoDB](https://www.mongodb.com)
- [mLab](https://mlab.com)

**Frontend**

- [HTML5](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)
- [CSS3](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS3)
- [JavaScript](https://developer.mozilla.org/bm/docs/Web/JavaScript)
- [Bootstrap v4.1.1](https://getbootstrap.com/docs/4.1/)

**Version Control**

- [Git](https://git-scm.com)
- [Github](https://github.com)


## 4 Workspace

**Operating System** - [macOS High Sierra](https://en.wikipedia.org/wiki/MacOS_High_Sierra)

**Editor** - [Visual Studio Code](https://code.visualstudio.com)

**Language** - [Python3](https://www.python.org)

**Formatting** - [Autopep-8](https://marketplace.visualstudio.com/items?itemName=himanoa.Python-autopep8)


## 5 Workflow

- Create project directory with readme
- Create git repo
- Work on UXD up to and including the Scope plane
- Create database schema
- Create MongoDB database on mLab
- Work on Structure and Skeleton planes of UXD
- Create wireframes
- Get Flask app up and running
    - Install flask
    - Install flask-pymongo
    - Create app.py
- Deploy to Heroku
- Implement the features outlined in the Scope plane of UXD
- Test each feature and document it
- Make it look nice - complete Surface plane of UXD


## 6 UXD

### Strategy

| Focus                                | User Needs                                                            | Business Objectives                             |
|--------------------------------------|-----------------------------------------------------------------------|-------------------------------------------------|
| What are you aiming to achieve?      | I want to store and access cooking recipes |  |
|                                      | I want to find recipes for a particular cuisine, ingredient, country |  |
| For whom?                            | I want to see the most popular recipes |  |
| TARGET AUDIENCE                      | I want to add a new recipe |  |
|                                      | I want to view existing recipes |  |
|                                      | I want to edit a recipe |  |
|                                      | I want to remove an old recipe |  |
|                                      | I want to create an account to keep track of my recipes and favourites |  |

### Scope

| Focus                                | Functional Specification                                              | Content Requirements                            |
|--------------------------------------|-----------------------------------------------------------------------|-------------------------------------------------|
| Which features?                      | View all recipes ordered by number of favourites                      | [See database schema](#7-database-schema) |
| What’s on the table?                 | View all recipes using filters                                        |  |
|                                      | Add a new recipe                                                      |  |
|                                      | View a recipe                                                         |  |
|                                      | Edit a recipe                                                         |  |
|                                      | Delete a recipe                                                       |  |
|                                      | Create an account                                                     |  |
|                                      | Log in/out                                                            |  |
|                                      | Sign up                                                               |  |
|                                      | View a user profile page                                              |  |
|                                      | Favourite a recipe                                                    |  |
|                                      | Unfavourite a recipe                                                  |  |


### Structure

| Focus                                | Interaction Design                                                        | Information Architecture                                                               |
|--------------------------------------|---------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| How is the information structured?   | Where am I? / How did I get here? / What can I do here? / Where can I go? | Organizational/Navigational schema (tree/nested list/hub and spoke/dashboard) |
|                                      | Favourite a recipe by clicking heart icon, prompt to log in if not        | Tree structure |
| How is it logically grouped?         | Log in by entering username in a form                                     | Home |
|                                      | If you don't have a username, prompt to sign up                           | Recipe |
|                                      | Sign up by registering a unique username in a form                        | Manage Recipes |
|                                      | Click on Manage Recipes to view user profile page                         | - Add Recipe |
|                                      | Add and remove filters to alter recipe list displayed                     | - Edit Recipe |
|                                      | Use pagination to view recipe list                                        | Log In/Sign Up |
|                                      | Click on a recipe to view it in full                                      |  |
|                                      | Scroll through recipe page to view recipe content                         |  |
|                                      | Update and delete recipes from by clicking on icons on Manage Recipes     |  |
|                                      | Unfavourite a recipe by clicking the heart icon                           |  |
|                                      | Log out by clicking the log out icon                                      |  |

### Skeleton

| Focus                                      | Interface Design                                       | Navigational Design  | Information Design  |
|--------------------------------------------|--------------------------------------------------------|----------------------|---------------------|
| How will the information be represented?   | See wireframes                                         |                      |                     |
|                                            |                                                        | All Recipes          |  |
| How will the user navigate                 |                                                        | Manage Recipes       |  |
| to the information and features?           |                                                        | Add Recipe           |  |
|                                            |                                                        | Most Popular         |  |
|                                            |                                                        | (Log In / Log Out)   |  |
|                                            |                                                        |  |  |

### Surface

| Focus                                      | Visual Design                       |
|--------------------------------------------|-------------------------------------|
| What will the finished product look like?  |  |
|                                            |  |
| What colours, typography and               |  |
| design elements will be used?              |  |
|                                            |  |


## 7 Database Schema


[Project schema designs here](https://github.com/sarahloh/p4-online-cookbook/blob/master/resources/database_schemas)

**Recipe**

```javascript
{
    name: '',
    time: {
        hours: Number,
        minutes: Number
    },
    author: UserId,
    description: '',
    ingredients: [''],
    method: [''],
    image_url: '',
    date_added: Date,
    favourites: Number,
    cuisine: '',
    type: ''
}
```

**User**

```javascript
{
    name: '',
    username: '',
    my_recipes: [RecipeId],
    favourite_recipes: [RecipeId]
}
```

## 8 Wireframes

![Mobile Wireframes](https://raw.githubusercontent.com/sarahloh/p4-online-cookbook/master/static/images/readme/mobile_wireframes.jpg)

![Tablet Wireframes](https://raw.githubusercontent.com/sarahloh/p4-online-cookbook/master/static/images/readme/tablet_wireframes.jpg)

![Desktop Wireframes](https://raw.githubusercontent.com/sarahloh/p4-online-cookbook/master/static/images/readme/desktop_wireframes.jpg)


## 9 Heroku Deployment

1. Create a new app 'sl-online-cookbook' on heroku.com

2. Login to heroku with email and password
    - $ heroku login

3. Add heroku remote
    - $ heroku git:remote -a sl-online-cookbook

4. Add requirements.txt
    - $ sudo pip3 freeze --local > requirements.txt

5. Add Procfile (this tells heroku what to do with the project)
    - $ echo web: python run.py > Procfile

6. Git commit and push to heroku remote
    - $ git add Procfile
    - $ git ci -m 'Add requirements.txt and Procfile'
    - $ git push -u heroku master

7. Set up dynos
    - $ heroku ps:scale web=1

8. Setup config variables on heroku dashboard


## 10 Features

In this section, you should go over the different parts of your project, and describe each in a sentence or so.

- Feature 1 - View ordered list - allows users to view recipes ordered by favourites or date added, by clicking on links near the top of the home page
- Feature 2 - View filtered list - allows users to view recipes using filters, by choosing filter categories at the top of the home page
- Feature 3 - Add recipe - allows users to add a new recipe, by filling in a form
- Feature 4 - View recipe - allows users to view a single recipe, by clicking the link on a recipe card on the home page or the manage recipes page
- Feature 5 - Edit a recipe	- allows users to edit a recipe, by changing the values in a form
- Feature 6 - Delete a recipe - allows users to delete a recipe, by clicking on the trash icon on the recipe card on the manage recipes page
- Feature 7 - Create an account - allows users to create an account, by filling in a form
- Feature 8 - Log in/out - allows users to log out, by clicking log out in the navbar
- Feature 9 - View a user profile page - allows users to view their profile page, by clicking on manage recipes in the navbar
- Feature 10 - Favourite a recipe - allows users to favourite a recipe, by clicking on the heart icon on the recipe card
- Feature 11 - Unfavourite a recipe - allows users to unfavourite a recipe, by clicking on the heart icon on the recipe card

## 11 Testing

**Automated Tests**

I used the Test Before approach of Test-Driven Development in this project, writing a test that fails, and then writing the code to pass the test using Python's unittest class.

[Test file available here](https://github.com/sarahloh/p4-online-cookbook/blob/master/test_cookbook.py)

To run the file use the follwing terminal command:

```bash
python3 -m unittest test_cookbook.py
```

---

1. Sign up form:
    1. Go to the "Sign Up" page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit an existing username and verify that an error message appears
    4. Try to submit the form with all inputs valid and verify that a success message appears on home page.

2. Log in form:
    1. Go to the "Log in form" in navbar or sign up page
    2. Try to submit the empty form or incorrect username and verify that an error message appears
    3. Try to submit the form with all inputs valid and verify that a success message appears on home page.

3. Favourite a recipe:
    1. Try to favourite a recipe when not logged in and verify page redirects to sign up / log in page


---

I used a [Bootstrap](https://getbootstrap.com) grid to structure the frontend and and the site **responsive**. Using mobile first design, I started with the mobile screen and worked up through tablet, desktop and large desktop, altering the layout accordingly.

**Mobile**

- iPhone 5 Safari
- Chrome Developer Tools

**Tablet**

- Chrome Developer Tools

**Desktop**

- Chrome
- Safari


## 12 How To Deploy Locally

```console
$ git clone git@github.com:sarahloh/p4-online-cookbook.git
$ cd p4-online-cookbook
$ pip3 install -r requirements.txt
$ python3 app.py
```
App available at http://127.0.0.1:5000/


## 13 Credits

### Content & Media

Recipe content and media borrowed from [allrecipes.co.uk](http://allrecipes.co.uk)

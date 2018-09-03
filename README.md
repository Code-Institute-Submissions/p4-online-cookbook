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

**Package Manager** - [Homebrew](https://brew.sh)

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
    country_of_origin: '',
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

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:
- Different values for environment variables (Heroku Config Vars)?
- Different configuration files?
- Separate git branch?


<!-- 1. Create a new app 'online-cookbook' on heroku.com

2. Login to heroku with email abd password
    - $ heroku login

3. Add heroku remote
    - $ heroku git:remote -a online-cookbook

4. Add requirements.txt
    - $ sudo pip3 freeze --local > requirements.txt

5. Add Procfile (this tells heroku what to do with the project)
    - $ echo web: python run.py > Procfile

6. Git commit and push to heroku remote
    - $ git add Procfile
    - $ git ci -m 'Add Profile and requirements.txt for heroku deployment'
    - $ git push -u heroku master

7. Set up dynos
    - $ heroku ps:scale web=1

8. Setup config variables on heroku dashboard -->



## 10 Features

In this section, you should go over the different parts of your project, and describe each in a sentence or so.

### Existing Features

- Feature 1 - allows users X to achieve Y, by having them fill out Z
- ...

For some/all of your features, you may choose to reference the specific project files that implement them, although this is entirely optional.

In addition, you may also use this section to discuss plans for additional features to be implemented in the future:

### Features Left to Implement
- Another feature idea


## 11 Testing

In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and explain how to run them.

For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:

1. Contact form:
    1. Go to the "Contact Us" page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with an invalid email address and verify that a relevant error message appears
    4. Try to submit the form with all inputs valid and verify that a success message appears.

In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.

---

<!--

[**HTML Validator Results**]()

[**CSS Validator Results**]()




## 12 How To Deploy Locally

```console
$ git clone git@github.com:sarahloh/p4-online-cookbook.git
$ cd p4-online-cookbook
$ pip3 install -r requirements.txt
$ python3 app.py
```
App available at http://127.0.0.1:5000/

 -->

## 13 Credits

### Content

<!-- - The text for section Y was copied from the [Wikipedia article Z](https://en.wikipedia.org/wiki/Z) -->

### Media

<!-- - The photos used in this site were obtained from ... -->

### Acknowledgements

<!-- - I received inspiration for this project from X -->
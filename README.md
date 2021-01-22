# [Spicy Meals](https://spicy-meals.herokuapp.com/)
![readmeimg](static/images/readmeimg.PNG)
[Visit site](https://spicy-meals.herokuapp.com/)
## Introduction

Welcome to Spicy Meals! A place for all Spicy foods lovers for finding, loving and sharing. Here you can find all your favorite recipes. You can also add, edit, delete and store all your recipes in one place!

# UX

## Project Goals

The aim of the project is to create a website where users can add/edit delete spicy food recipes,search and find recipes from all around the world.

**Site Owner Goals:**

Provide a website for spicy food lovers to find and share recipes they love.

**User Stories**

As a User I would like to:

- Share recipes
- Edit recipes
- Deleting recipes
- Access the site from both mobile devices and desktop browsers.
- Be able to register an account and log in/out
- Be able to search recipes by country/region, meal type and author

## Design

**Icons**

[Font Awsome](https://fontawesome.com/)

**Colors**

- Paprika red #a51409
- Whitesmoke
- White

**Wireframe**

The wireframe is created using [Figma](figma.com)

[See wireframes here](https://www.figma.com/file/a7Ebh8RhP4decujnVingyN/Sample-File?node-id=213%3A185)

### **Database** [MongoDB](www.mongodb.com)

**meals**

_id: ObjectId

meal_type: breakfast

_id: ObjectId

meal_type: brunch

_id: ObjectId

meal_type: lunch


_id: ObjectId

meal_type: dinner


_id: ObjectId

meal_type: dessert

**recipe**

_id: ObjectId

meal_type:

meal_name:

meal_description:

cuisine:

cooking_time:

number_of_servings:

ingredients:

directions:

image_url:

author:

**users**

_id: ObjectId

username:

password:

# Features

### Existing Features

- Navbar that navigates you to different pages of the site depending whether you are logged in or not

- Users can sign up with a unique username and password

- Users can sign in with their unique username and password

- User can sign out

- User can add, update and delete recipes

- User can read and search recipe

### Features left to implement

- Commenting recipes
- Profile page
- Pagination in recipe gallery
- Change password
- Delete account
- Admin account 

## Defensive Design

1. User account
- Only a registered user can create a recipe
- Only the creator of the recipe can edit or delete own recipe
- Users password are hashed before storing in Database

2. Required input
- All html form inputs have required attribute
- Some input force pattern to prevent error and also regex check in python function

3. Limited Access
- Non logged user can only view recipes
- Prevent potential website crash if too many recipes are added. Since there is no pagination the page only display 100 recipes

# Technologies Used

 ## Languages
 - HTML 
 - CSS
 - PYTHON

 ## Libraries and Framworks
- [Flask](https://flask.palletsprojects.com/en/1.1.x/) + associated functions
- [Bootstrap](getbootstrap.com)
- [Fontawsome](fontawsome.com)

## Database
- [MongoDB](www.mongodb.com)

## Tools
- Figma
- Chrome devtools
- Git
- Github
- Gitpod
- Heroku
- Am I Responsive?

 # Testing

 This project as been tested through the whole process and a student from sti - Stockholm Technical Institute: 

Register/Create a new user.

Create a recipe.

Edit a recipe.

Delete a recipe.

Create an ingredient.

Edit an ingredient.

Delete an ingredient.

Search for a recipe.

Changing URL paths.

## Validators
### W3C Markup Validation
HTML validation.
### W3C CSS Validation
Was used to check CSS3 validation.
### Python syntax checker
Was used to check Python validation.
### PEP online
Was used to check PEP8 validation.
### AutoPrefixer
Was used to make sure that CSS3 was valid for all web browsers.
### Google Search Console
Was used to make sure that Responsive design worked on all devices. https://search.google.com/test/mobile-friendly?hl=sv
### Chrome DevTools
Was used to for debugging.

# Deployment

To be able to run this project, the following tools have to be installed:

- An IDE (I used GitPod online IDE for creating this project)
- MongoDB Atlas (for creation your database)
- Git
- PIP
- Python

### Directions:

1. Visit [My GitHub Repository](https://github.com/Yassinrby/spicy-meals) Clone or download , then "Download Zip" button, and after extract the Zip file to your folder.

2. Set up environment variables:
- Create .env file in the root directory.
- On the top of the file add 'import os' to set the environment variables in the operating system.
- Set the connection to your MongoDB database(MONGO_URI) and a SECRET_KEY with the following syntax: 
 os.environ["SECRET_KEY"] = "YourSecretKey"
 os.environ["MONGO_URI"] = "YourMongoURI"

 3. Install all requirements from the requirements.txt file putting this command into your terminal:
pip3 install -r requirements.txt

4. Create a database in MongoDB. (See database schema above)

## Heroku Deployment
To deploy the project to Heroku the following steps need to be completed:

1. Create a requirement.txt file, which contains a list of the dependencies.

2. Create a Procfile, in order to tell Heroku how to run the project.

3. git add, git commit and git push these files to GitHub repository

4. Create a new app in Heroku.

From the Heroku dashboard link the new Heroku app to your GitHub repository:

"Deploy" -> "Deployment method" -> "GitHub"
then "Enable automatic deployment"

In the Settings tab of the new Heroku app, click on "Reveal Config Vars" and set the following config vars:

IP : 0.0.0.0

PORT : 8080

MONGO_URI : link to your MongoDB database

SECRET_KEY : your secret key

DEBUG: FALSE

Note: your MONGO_URI and SECRET_KEY must match the ones you entered in .env.py file
The app will be deployed and ready to run. Click "Open App" to view the app.

[Click here to learn more](https://devcenter.heroku.com/articles/github-integration#manual-deploys)

# Credits

### Content
- Stackoverflow
- Youtube
- W3Schools
- MongoDB Documentation
- Flask Documentation
- Jinja Documentation
- Werkzeug Documentation

### Acknowledgments

A big thanks to my Mentor and Tutor Support att Code Institute!






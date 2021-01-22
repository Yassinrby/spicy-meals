import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
import re
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)


@app.route("/search", methods=["GET", "POST"])
def search():
    """
    This function allow user to search for meal type,
    country/origin of the meal and author

    """
    search = request.form.get("search")
    recipes = list(mongo.db.recipe.find({"$text": {"$search": search}}))
    return render_template("all_recipes.html", recipes=recipes)


@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    """
    Recipe get removed from db.
    Only the author of the recipe can delete recipe.
    """
    if 'user' not in session:
        flash('You must be logged in to delete the recipe!')
        return redirect(url_for('login'))

    user_session = mongo.db.users.find_one({'username': session['user']})

    recipe = mongo.db.recipe.find_one({"_id": ObjectId(recipe_id)})

    if recipe['author'] == user_session['username']:
        mongo.db.recipe.remove({"_id": ObjectId(recipe_id)})
        flash("Recipe Deleted!")
        return redirect(url_for("home"))

    else:
        flash('You can not delete this recipe...')
        return redirect(url_for('home'))


@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    """
    Recipe gets updated.
    Only the author of the recipe can update recipe.
    """

    if 'user' not in session:
        flash('You must be logged in to edit the recipe!')
        return redirect(url_for('login'))

    user_session = mongo.db.users.find_one({'username': session['user']})

    recipe = mongo.db.recipe.find_one({"_id": ObjectId(recipe_id)})

    if recipe['author'] == user_session['username']:
        if request.method == "POST":
            new_recipe = {
                "meal_type": request.form.get("meal_type"),
                "meal_name": request.form.get("meal_name"),
                "meal_description": request.form.get("meal_description"),
                "cuisine": request.form.get("cuisine"),
                "cooking_time": request.form.get("cooking_time"),
                "number_of_servings": request.form.get("number_of_servings"),
                "ingredients": request.form.get("ingredients"),
                "directions": request.form.get("directions"),
                "image_url": request.form.get("image_url"),
                "author": session["user"]
            }
            mongo.db.recipe.update({"_id": ObjectId(recipe_id)}, new_recipe)
            flash("Recipe Updated")
            return redirect(url_for("home"))
    else:
        flash('You can not change this recipe...')
        return redirect(url_for('home'))

    recipe = mongo.db.recipe.find_one({"_id": ObjectId(recipe_id)})

    meals = mongo.db.meals.find().sort("meal_type", 1)
    return render_template("edit_recipe.html", recipe=recipe, meals=meals)


@app.route("/recipe/<recipe_id>")
def recipe(recipe_id):
    """
    Displays detailed information about selected recipe.

    """
    selected_recipe = mongo.db.recipe.find_one(
        {"_id": ObjectId(recipe_id)})
    return render_template(
        "recipe.html", selected_recipe=selected_recipe)


@app.route("/all_recipes/")
def all_recipes():
    """
    Displays all recipes from the database.
    Limits gallery to max 100 recipes.

    """
    recipes = list(mongo.db.recipe.find().limit(100))
    return render_template("all_recipes.html", recipes=recipes)


@app.route("/register", methods=["GET", "POST"])
def register():
    """
    Created new user in db from HTML form.
    Checks if user exists and created session cookie.

    """
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("home", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """
    Sign in function, checks if username and password
    are valid and created session cookie.

    """
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get(
                        "password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome {}".format(request.form.get("username")))
                return redirect(url_for(
                    "home", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/logout")
def logout():
    """
    Sign out user, pop the session cookie
    and redirects to home page.

    """
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("home"))


@app.route("/add_recipe/", methods=["GET", "POST"])
def add_recipe():
    """
    Add recipe to db from HTML form. Only logged in
    user an access the function. Regex URL validation
    if it a url or empty starts with http/https otherwise the function
    dont get executed.

    """

    if 'user' not in session:
        flash('You must be logged in to add a recipe!')
        return redirect(url_for('login'))

    url = request.form.get('image_url')

    if url:
        match = re.search(r'^(http|https):\/\/', url)

        if not match:
            flash('Add a proper url or leave it empty!')
            return redirect(url_for('add_recipe'))

    if request.method == "POST":
        new_recipe = {
            "meal_type": request.form.get("meal_type"),
            "meal_name": request.form.get("meal_name"),
            "meal_description": request.form.get("meal_description"),
            "cuisine": request.form.get("cuisine"),
            "cooking_time": request.form.get("cooking_time"),
            "number_of_servings": request.form.get("number_of_servings"),
            "ingredients": request.form.get("ingredients"),
            "directions": request.form.get("directions"),
            "image_url": url,
            "author": session["user"]
        }
        mongo.db.recipe.insert_one(new_recipe)
        flash("Thank you the new recipe!")
        return redirect(url_for("home"))

    meals = mongo.db.meals.find().sort("meal_type", 1)
    return render_template("add_recipe.html", meals=meals)


@app.route("/")
@app.route("/home/")
def home():
    """
    Home page

    """
    recipes = mongo.db.recipe.find()
    return render_template("home.html", recipes=recipes)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)

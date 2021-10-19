"""Models for recipe conversion app"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """Data model for a user."""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer,
                        primary_key = True,
                        autoincrement = True,
                        nullable = False)

    email = db.Column(db.String(25),
                        nullable = False)

    password = db.Column(db.String(25),
                        nullable = False)

    recipes = db.relationship('Recipe', backref = 'user')

    def __repr__(self):
        return f'<User user_id = {self.user_id} email = {self.email} password = {self.password}>'

class Recipe(db.Model):
    """Data model for a recipe."""

    __tablename__ = 'recipes'

    recipe_id = db.Column(db.Integer,
                        primary_key = True,
                        autoincrement = True,
                        nullable = False)

    user_id = db.Column(db.Integer,
                        db.ForeignKey('users.user_id'))

    recipe_name = db.Column(db.String(50),
                        nullable = False)

    recipe_instructions = db.Column(db.String(2000),
                                    nullable = False)

    num_servings = db.Column(db.Integer)

    prep_time_in_hours = db.Column(db.Integer) 

    image = db.Column(db.String(1000))    

    ingredients = db.relationship('Ingredient', backref = 'recipe')

    #Also remember: recipes is a list of recipe objects (recipes has relationship to user class)

    def __repr__(self):
        return f'<Recipe recipe_id = {self.recipe_id} user_id = {self.user_id} recipe_name = {self.recipe_name} recipe_instructions = {self.recipe_instructions} num_servings = {self.num_servings} prep_time_in_hours = {self.prep_time_in_hours}>'

class Ingredient(db.Model):
    """Data model for an ingredient."""

    __tablename__ = 'ingredients'

    ingredient_id = db.Column(db.Integer,
                                primary_key = True,
                                autoincrement = True,
                                nullable = False)

    ingredient_name = db.Column(db.String(50),
                                nullable = False)

    recipe_id = db.Column(db.Integer,
                        db.ForeignKey('recipes.recipe_id'),
                        autoincrement = True,
                        nullable = False)

    measurement = db.Column(db.Float,           
                            nullable = False)

    ingredient_prep = db.Column(db.String(25),
                        nullable = False)

    #Also remember: ingredients is a list of ingredient objects (ingredients has relationship to recipe class)
    
    def __repr__(self):
        return f'<Ingredient ingredient_id = {self.ingredient_id} ingredient_name = {self.ingredient_name} recipe_id = {self.recipe_id} measurement = {self.measurement} ingredient_prep = {self.ingredient_prep}>'


def connect_to_db(flask_app, db_uri="postgresql:///RecipeBox", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


if __name__ == "__main__":
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)
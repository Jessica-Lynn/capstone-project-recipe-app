"""Models for recipe conversion app"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """Data model for a user."""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer,
                        primary_key=True,
                        autoincrement=True)

    email = db.Column(db.String(25),
                        nullable=False,
                        unique=True)

    password = db.Column(db.String(25),
                        nullable=False)

    recipes = db.relationship('Recipe', backref ='user')

    def __repr__(self):
        return f'<User user_id = {self.user_id} email = {self.email} password = {self.password}>'


class Recipe(db.Model):
    """Data model for a recipe."""

    __tablename__ = 'recipes'

    recipe_id = db.Column(db.Integer,
                        primary_key=True,
                        autoincrement=True)

    user_id = db.Column(db.Integer,
                        db.ForeignKey('users.user_id'))

    recipe_name = db.Column(db.String(50),
                        nullable=False)

    recipe_instructions = db.Column(db.String(2000))

    num_servings = db.Column(db.Integer)

    prep_time_in_min = db.Column(db.Integer) 

    cook_time_in_min = db.Column(db.Integer)

    image = db.Column(db.String(1000))    

    def __repr__(self):
        return f'<Recipe recipe_id = {self.recipe_id} user_id = {self.user_id} recipe_name = {self.recipe_name} recipe_instructions = {self.recipe_instructions} num_servings = {self.num_servings} prep_time_in_min = {self.prep_time_in_min} cook_time_in_min = {self.cook_time_in_min} image = {self.image}>'


class Ingredient(db.Model):
    """Data model for an ingredient."""

    __tablename__ = 'ingredients'

    ingredient_id = db.Column(db.Integer,
                                primary_key=True,
                                autoincrement=True)

    ingredient_name = db.Column(db.String(50),
                                nullable=False)
    
    def __repr__(self):
        return f'<Ingredient ingredient_id = {self.ingredient_id} ingredient_name = {self.ingredient_name}>'



class RecipeIngredient(db.Model):
    """Data Model for an Ingredient specific to a certain Recipe"""

    __tablename__ = 'recipe_ingredients'

    recipe_ingredient_id = db.Column(primary_key=True, 
                                    autoincrement=True)

    recipe_id = db.Column(db.Integer, 
                            db.ForeignKey('recipes.recipe_id'))               #foreign key relating back to the recipe table
    
    ingredient_id = db.Column(db.Integer, 
                                db.ForeignKey('ingredients.ingredient_id'))    #foreign key relating back to the ingredient table
    
    measurement = db.Column(db.Float, 
                            nullable=False)                   #API has this as a string -- but for conversion, would I want Int or Float?
    
    prep_info = db.Column(db.String(25))                        

    recipe = db.relationship('Recipe', backref='recipe_ingredient')
    ingredient = db.relationship('Ingredient', backref='recipe_ingredient')

    def __repr__(self):
        return f'< recipe_ingredient_id = {self.recipe_ingredient_id}, recipe_id = {self.recipe_id}, ingredient_id = {self.ingredient_id}, measurement = {self.measurement} prep_info = {self.prep_info}>'

    
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
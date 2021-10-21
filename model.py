"""Models for Recipe Conversion App"""

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

    num_servings = db.Column(db.String(25))

    prep_time_in_min = db.Column(db.String(30)) 

    cook_time_in_min = db.Column(db.String(30))

    image = db.Column(db.String(1000))    

    def __repr__(self):
        return f'<Recipe recipe_id = {self.recipe_id} user_id = {self.user_id} recipe_name = {self.recipe_name} recipe_instructions = {self.recipe_instructions} num_servings = {self.num_servings} prep_time_in_min = {self.prep_time_in_min} cook_time_in_min = {self.cook_time_in_min} image = {self.image}>'


class IngredientType(db.Model):
    """Data model for a GENERAL ingredient type (without measurements); 
    for example: flour, eggs, butter."""

    __tablename__ = 'ingredient_types'

    ingredient_id = db.Column(db.Integer,
                                primary_key=True,
                                autoincrement=True)

    ingredient_name = db.Column(db.String(50),
                                nullable=False)
    
    def __repr__(self):
        return f'<IngredientType ingredient_id = {self.ingredient_id} ingredient_name = {self.ingredient_name}>'



class IngredientDetail(db.Model):
    """Data Model for an Ingredient's Details; can be specific to a recipe_id.
    For example, for 'Funfetti Cake' with recipe_id = 1:    2 level cups gluten-free flour blend, 
                                                            2 eggs, whisked until blended,
                                                            4 tablespoons unsalted butter, at room temperature."""

    __tablename__ = 'ingredient_details'

    ingred_detail_id = db.Column(primary_key=True, 
                                autoincrement=True)

    recipe_id = db.Column(db.Integer, 
                            db.ForeignKey('recipes.recipe_id'))                     #foreign key relating back to the recipe table
    
    ingredient_id = db.Column(db.Integer, 
                                db.ForeignKey('ingredient_types.ingredient_id'))    #foreign key relating back to the ingredientType table
    
    measurement = db.Column(db.String(30), 
                            nullable=False)                                         #API has this as a string -- but for recipe conversion, double check if I would want Int or Float instead?
    
    prep_info = db.Column(db.String(25))                        

    recipe = db.relationship('Recipe', backref='ingredient_details')
    ingredient = db.relationship('IngredientType', backref='ingredient_details')

    def __repr__(self):
        return f'<IngredientDetail ingred_detail_id = {self.ingred_detail_id}, recipe_id = {self.recipe_id}, ingredient_id = {self.ingredient_id}, measurement = {self.measurement} prep_info = {self.prep_info}>'

    
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
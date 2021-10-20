"""CRUD operations."""

from model import db, User, Recipe, Ingredient, RecipeIngredient, connect_to_db


def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)  

    db.session.add(user)
    db.session.commit()

    return user



def create_recipe(recipe_name, recipe_instructions, num_servings, prep_time_in_min, cook_time_in_min, image):
    """Create and return a new recipe."""

    recipe = Recipe(
        recipe_name=recipe_name,
        recipe_instructions=recipe_instructions,
        num_servings=num_servings,
        prep_time_in_min=prep_time_in_min,
        cook_time_in_min=cook_time_in_min,
        image=image
    )

    db.session.add(recipe)
    db.session.commit()

    return recipe



def create_ingredient(ingredient_name):
    """Create and return a new ingredient."""

    ingredient = Ingredient(ingredient_name=ingredient_name)

    db.session.add(ingredient)
    db.session.commit()

    return ingredient



def create_recipe_specific_ingredient(measurement, prep_info):
    """Create and return an ingredient that is specific to a certain recipe id"""

    recipe_ingredient = RecipeIngredient(measurement=measurement, prep_info=prep_info)      #verify that I do not add forgein keys here because they are also on autoincrement

    db.session.add(recipe_ingredient)
    db.session.commit()

    return recipe_ingredient



if __name__ == '__main__':
    from server import app
    connect_to_db(app)

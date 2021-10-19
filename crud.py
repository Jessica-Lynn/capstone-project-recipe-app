"""CRUD operations."""

from model import db, User, Recipe, Ingredient, connect_to_db


def create_user(user_id, email, password):
    """Create and return a new user."""

    user = User(user_id=user_id, email=email, password=password)  #Note to self: add email here INSTEAD of username and correct this in model.py

    db.session.add(user)
    db.session.commit()

    return user



def create_recipe(recipe_id, user_id, recipe_name, recipe_instructions, num_servings, prep_time_in_hours, image):
    """Create and return a new recipe."""

    recipe = Recipe(
        recipe_id=recipe_id,
        user_id=user_id,
        recipe_name=recipe_name,
        recipe_instructions=recipe_instructions,
        num_servings=num_servings,
        prep_time_in_hours=prep_time_in_hours,
        image=image
    )

    db.session.add(recipe)
    db.session.commit()

    return recipe



def create_ingredient(ingredient_id, ingredient_name, recipe_id, measurement, ingredient_prep):
    """Create and return a new ingredient."""

    ingredient = Ingredient(ingredient_id=ingredient_id,
                            ingredient_name=ingredient_name,
                            recipe_id=recipe_id,
                            measurement=measurement,
                            ingredient_prep=ingredient_prep)

    db.session.add(ingredient)
    db.session.commit()

    return ingredient



if __name__ == '__main__':
    from server import app
    connect_to_db(app)

"""CRUD operations for Recipe Conversion App."""

from model import db, User, Recipe, IngredientType, IngredientDetail, connect_to_db


def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)  

    db.session.add(user)
    db.session.commit()

    return user



def create_recipe(user_id, recipe_name, recipe_instructions, num_servings, prep_time_in_min, cook_time_in_min):
    """Create and return a new recipe."""

    recipe = Recipe(
        user_id=user_id,
        recipe_name=recipe_name,
        recipe_instructions=recipe_instructions,
        num_servings=num_servings,
        prep_time_in_min=prep_time_in_min,
        cook_time_in_min=cook_time_in_min,
    )

    db.session.add(recipe)
    db.session.commit()

    return recipe



def create_ingredient_type(ingredient_name):
    """Create and return a new ingredient name."""

    ingredient = IngredientType(ingredient_name=ingredient_name)

    db.session.add(ingredient)
    db.session.commit()

    return ingredient



def create_ingredient_detail(recipe_id, ingredient_id, measurement, prep_info):
    """Create and return an ingredient's details using ingredient_id and recipe_id for a specific recipe."""

    ingredient_detail = IngredientDetail(recipe_id=recipe_id, ingredient_id=ingredient_id, measurement=measurement, prep_info=prep_info)      #verify that I do not add forgein keys here because they are also on autoincrement

    db.session.add(ingredient_detail)
    db.session.commit()

    return ingredient_detail



if __name__ == '__main__':
    from server import app
    connect_to_db(app)

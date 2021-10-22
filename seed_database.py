"""Script to Seed database for Recipe Conversion App"""

#   Automatically populate the database with data:
#       Use data from data/all_recipes.json to create recipes
#       Create 4 random users; for each user, create 3 recipes with their ingredients


import os
import json
from random import choice, randint

import crud
from model import db, Recipe, IngredientType, connect_to_db   #added code here-- from model.py, I'm importing db, Recipe class, and connecting to db
import server

#   Drop the database with dropdb
os.system("dropdb RecipeBox")

#   Create the database with createdb
os.system("createdb RecipeBox")

#   Use db.create_all to create tables
connect_to_db(server.app)
db.create_all()

#   Automatically populate the database with data:
#       Use data from data/all_recipes.json to create recipes
#       Create 5 random users; for each user, create recipes with their ingredients



    


# Create 5 users
for n in range(5):
    email = f"user{n}@test.com"  
    password = "test"

    user = crud.create_user(email, password)

funfetti_cake_recipe = Recipe(user_id=1,                             #not getting recipe_id from recipe class
                            recipe_name='funfetti cake', 
                            recipe_instructions='mix, bake', 
                            num_servings='12 servings', 
                            prep_time_in_min='15 min', 
                            cook_time_in_min='25 min', 
                            image='imageURL')

gluten_free_flour_blend = IngredientType(ingredient_name='gluten-free flour blend')
egg = IngredientType(ingredient_name='egg')
unsalted_butter = IngredientType(ingredient_name='unsalted butter')
granulated_sugar = IngredientType(ingredient_name='granulated sugar')





db.session.add_all([funfetti_cake_recipe])   #this is a list inside (); can add recipes to list
db.session.add_all([gluten_free_flour_blend, egg, unsalted_butter, granulated_sugar])
db.session.commit()
"""Script to Seed database for Recipe Conversion App"""


import os
import json


import crud
from model import db, User, Recipe, IngredientType, IngredientDetail, connect_to_db   #added code here-- from model.py, I'm importing db, Recipe class, and connecting to db
import server

#   Drop the database with dropdb
os.system("dropdb RecipeBox")

#   Create the database with createdb
os.system("createdb RecipeBox")

#   Use db.create_all to create tables
connect_to_db(server.app)
db.create_all()

#   Automatically populate the database with data:

#       Create 5 random users


GLUTEN_TO_GF= {
    'flour': 'gluten-free flour blend',
}


# Create 5 users
for n in range(5):
    email = f"user{n}@test.com"  
    password = "test"
    user = crud.create_user(email, password)


funfetti_cake_recipe = Recipe(user_id=1,
                              recipe_name='funfetti cake',          
                              recipe_instructions='mix, bake', 
                              num_servings='12 servings', 
                              prep_time_in_min='15 min', 
                              cook_time_in_min='25 min'             #removed image='imageURL'
                              )
db.session.add_all([funfetti_cake_recipe])
db.session.commit() 


INGREDIENTS = ['gluten-free flour blend', 'egg', 'unsalted butter', 'granulated sugar']

for ingredient in INGREDIENTS:
    i = IngredientType(ingredient_name=ingredient)
    db.session.add(i)
    db.session.commit()


MEASUREMENTS = ['1 cup', '1/2 cup']

for measurement in MEASUREMENTS:
    m = IngredientDetail(measurement=measurement)
    db.session.add(m)
    db.session.commit()


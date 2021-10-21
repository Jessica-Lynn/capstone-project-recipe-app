"""Script to Seed database for Recipe Conversion App"""

#   Automatically populate the database with data:
#       Use data from data/all_recipes.json to create recipes
#       Create 4 random users; for each user, create 3 recipes with their ingredients


import os
import json
from random import choice, randint

import crud
import model
import server

#   Drop the database with dropdb
os.system("dropdb RecipeBox")

#   Create the database with createdb
os.system("createdb RecipeBox")

#   Use db.create_all to create tables
model.connect_to_db(server.app)
model.db.create_all()

#   Automatically populate the database with data:
#       Use data from data/all_recipes.json to create recipes
#       Create 5 random users; for each user, create recipes with their ingredients

# Load recipe data from JSON file
with open('data/all_recipes.json') as f:        #need to create data json file!!!
    recipe_data = json.loads(f.read())

# Create ingredients, store them in list? 
# so we can use them to create fake recipes?

    #NOTE: Add code here



# Create 5 users
for n in range(5):
    email = f"user{n}@test.com"  
    password = "test"

    user = crud.create_user(email, password)


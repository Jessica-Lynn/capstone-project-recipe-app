"""Script to Seed database for Recipe App"""

import os
import json

import crud
import model
import server

os.system("dropdb RecipeBox")
os.system("createdb RecipeBox")

model.connect_to_db(server.app)
model.db.create_all()

# Load recipe data from JSON file
with open('data/all_recipes.json') as f:        #need to create data json file!!!
    all_recipe_data = json.loads(f.read())

# Create recipes, store them in list? 
# so we can use them to create fake recipes


"""Server for recipe conversion app."""

from flask import (Flask, render_template, request, flash, session,
                   redirect)

from model import connect_to_db
import crud


from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "RANDOM SECRET KEY"
app.jinja_env.undefined = StrictUndefined

# Replace this with routes and view functions!

@app.route('/')
def homepage():
    """View homepage. Has button for existing user to log in and button to create new account"""

    user_email = request.args.get('email')
    user_password = request.args.get('password')

    return render_template('homepage.html')



@app.route('/create_new_account')
def create_new_account():
    """Create new user account with email and password."""

    username = request.args.get('username')
    user_email = request.args.get('email')
    user_password = request.args.get('password')
    
    return render_template('create_new_account.html')

#need to set username to session; for create account and for log in


@app.route('/user_profile_page')
def user_profile_page():
    """Displays user's profile page."""

    return render_template('user_profile_page.html')



@app.route('/build_recipe')
def build_recipe():
    """ User can build a recipe and set it to dietary specification """

    return render_template('build_recipe.html')


@app.route('/get_ingredients', methods=['POST'])
def get_ingred_from_user():
    """ Get amount of all purpose flour user selects; convert to gluten-free flour """      
    
    GLUTEN_TO_GF = { 
        '1 cup all purpose flour': (('1 cup gluten-free flour', '0.25 tsp xantham gum')), 
        '2 cups all purpose flour': (('2 cups gluten-free flour', '0.50 tsp xantham gum')),
        '3 cups all purpose flour': (('3 cups gluten-free flour', '0.75 tsp xantham gum')),
        '4 cups all purpose flour': (('4 cups gluten-free flour', '1.00 tsp xantham gum')),
        '5 cups all purpose flour': (('5 cups gluten-free flour', '1.25 tsp xantham gum')),
        '6 cups all purpose flour': (('6 cups gluten-free flour', '1.50 tsp xantham gum')),
        '7 cups all purpose flour': (('7 cups gluten-free flour', '1.75 tsp xantham gum')),
        '8 cups all purpose flour': (('8 cups gluten-free flour', '2.00 tsp xantham gum')),
        '9 cups all purpose flour': (('9 cups gluten-free flour', '2.25 tsp xantham gum')),
        '10 cups all purpose flour': (('10 cups gluten-free flour', '2.50 tsp xantham gum')),
        '11 cups all purpose flour': (('11 cups gluten-free flour', '2.75 tsp xantham gum')),
        '12 cups all purpose flour': (('12 cups gluten-free flour', '3.00 tsp xantham gum')),
    }    #GLUTEN_TO_GF[1 cup all purpose flour] - Values- index 0 is gf flour; index 1 is xantham gum

    ap_flour = request.form['ap_flour']

    print(ap_flour) 

    #check ap_flour as a key in GLUTEN_TO_GF:
    #   for key in dictionary --- if key matches ap_flour --- get value for gf_flour; get value for xantham_gum

    for key in GLUTEN_TO_GF:
        if key == ap_flour:
            gf_flour = GLUTEN_TO_GF[key][0]
            xantham_gum = GLUTEN_TO_GF[key][1]

    recipe_flour_conversion = f'To make your recipe Gluten-Free, replace the {ap_flour} with {gf_flour} and add {xantham_gum}.'

    #Add the info below later:
    #       Use a gluten-free flour blend intended for 1:1 all purpose flour to gluten-free flour substitutions.
    #       The gluten-free flour blend should not have xantham gum listed in its ingredient list.
    #       For best results, the xantham gum is added based on the amount of gluten-free flour used. 
    #       f'For your recipe that uses {gf_flour}, add {xantham_gum}.'
    
    return recipe_flour_conversion

#   CREATE OBJECTS TO SAVE TO DATABASE
#       The way model.py is set up-- have to create recipe object first
#       To create a recipe object:
#           crud.create_recipe(user_id, recipe_name, recipe_instructions, num_servings, prep_time_in_min, cook_time_in_min)

#       To create an ingredient object:
#           1) Create IngredientType object
#              crud.create_ingredient_type(ingredient_name)
#           2) Create IngredientDetail object
#              crud.create_ingredient_detail(measurement, prep_info, recipe, ingredient)


#---------------------------------------------------------------------------------------------------------------------------------------


#   NEXT, ADD NECESSARY CHANGES FOR LIQUID AND EGG INGREDIENTS
#   For Liquids:
#       User enters decimal amount of TOTAL liquids used in recipe
#       Post request passes to view function
#       In view function:
#               decimal amount is a string -- change to float
#               set that float to variable and divide by 2  -- this is new liquid measurement for recipe

#   For Eggs:
#       user enters TOTAL number of eggs used in recipe
#       Post request passes to view function
#       In view function:
#           set that number to variable and multiply by 2 -- this is new egg measurement for recipe

     
#------------------------------------------------------------------------------------------------------------------------------
#-------------------------------PREVIOUS CODE IS BELOW THIS LINE---------------------------------------------------------------

#POST REQUESTS FOR '/get_ingredients':   
    # recipe_name = request.form.get('recipe_name')
    # recipe_instructions = request.form.get('recipe_instructions')
    # num_servings = request.form.get('num_servings')
    # prep_time_in_min = request.form.get('prep_time_in_min')
    # cook_time_in_min = request.form.get('cook_time_in_min')
    # ingredient = request.form['ingred_1']
    # measurement = request.form['ingred_1_M']
    # details = request.form.get('ingred_1_details')
    
#CODE TO CREATE RECIPE OBJECT SUCCESSFULLY:
    # create a recipe object:
    #       create_recipe(user_id, recipe_name, recipe_instructions, num_servings, prep_time_in_min, cook_time_in_min, image)
    #regular_recipe = crud.create_recipe(1, recipe_name, recipe_instructions, num_servings, prep_time_in_min, cook_time_in_min)  #removed image for now

#WORKING THROUGH ERRORS CREATING INGREDIENT OBJECTS:  
        #After I created a recipe object:
        #NOTE:     
            # for ingredient: it's from IngredientType Class
            # for measurement: it's from IngredientDetail Class
            #       NEITHER ARE PART OF MAKING RECIPE OBJECT

            # I have to create an IngredientType object FIRST (to get ingredient_name),
            #   then create an IngredientDetail object (to get measurment for ingredient_name),

#--------------------------------------------------------------------------------------------------------------------------
                                                     

@app.route('/display_recipe')
def display_recipe():
    """ User receives back recipe according to dietary specification """

    return render_template('display_recipe.html')



@app.route('/user_logged_out')
def user_logged_out():
    """Tells user that they've successfully logged out; has button that links back to homepage."""

    return render_template('user_logged_out.html')    



if __name__ == "__main__":
    # DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
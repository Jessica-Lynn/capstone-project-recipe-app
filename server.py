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


@app.route('/get_ingredients')
def get_ingred_from_user():
    """ Gets ingredients user enters; saves to session """      #Trying to add ingredient to session; to then display on next page


    ingred = request.args.get('ingred_1')           #Sets ingred to our request
    session['ingred_1'] = ingred                    #Adds ingred to session so we can access it
                                       
    return render_template('/display_recipe',       #Displays ingredients on next page
                            ingred_1=ingred_1)


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
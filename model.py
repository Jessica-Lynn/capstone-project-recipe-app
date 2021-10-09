"""Models for recipe conversion app"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Add classes here 
#   User
#   Recipes
#   Ingredients

                #NOTE: Need to finish postgresql:/// on line 13 below
def connect_to_db(flask_app, db_uri="postgresql:///______", echo=True):
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
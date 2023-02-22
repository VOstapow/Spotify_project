# 1. import Dependencies
import numpy as np
import json
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

# Next, Setup database
# engine - create_engine("insert sql Sandra cleaned")

# reflect an existing database into a new model
# base= automap_base()

#reflect the tables
# base.prepare(autoload_with=engine)

#Save the reference to the table
# spotify_db = base.

# 2. Create an app, being sure to pass __name__
app = Flask(__name__)


# 3. Define what to do when a user hits the index route
@app.route("/")
def home():
    print("Server received request for 'Home' page...")
    return "Danceability Hillbilly on The Move!"


#This runs the whole she-bang, I think
if __name__ == "__main__":
    app.run(debug=True)

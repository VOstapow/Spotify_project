# imports 
# %matplotlib inline
from matplotlib import style
style.use('fivethirtyeight')
import matplotlib.pyplot as plt

import numpy as np
import pandas as pd
import datetime as dt


# Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect

from flask import Flask, jsonify, request_finished
#################################################
engine = create_engine("sqlite:///db.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)

spotify = Base.classes.spotify
#################################################
app = Flask(__name__)
#################################################
# Data
session = Session(engine)
session.close
#################################################
@app.route("/")
def home():
    return(
    f"Welcome to the Climate Analysis API! <br/>"
    f"Available Routes:<br/>"
    f"Precipitation ----> /api/v1.0/precipitations <br/>"
    f"Station -----------> /api/v1.0/stations <br/>"
    f"Tobs -------------> /api/v1.0/tobs <br/>"
    f"Dates ------------> /api/v1.0/dates <br/>"
    f"Start -------------> /api/v1.0/dates/<start> <br/>"
    f"Start/End -------> /api/v1.0/dates/<start>/<end> <br/>"
    )
#################################################

#################################################
if __name__ == "__main__":
    app.run(debug=True)
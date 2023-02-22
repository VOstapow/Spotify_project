import pandas as pd
import matplotlib.pyplot as plt
from config import username, password

from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from flask import Flask, jsonify, request_finished 

engine = create_engine(f'postgresql://{username}:{password}@localhost:5432/spotify_db')
connection = engine.connect() 
spotify = pd.read_sql('select * from spotify_data', connection)
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
#################################################
#################################################
if __name__ == "__main__":
    app.run(debug=True)
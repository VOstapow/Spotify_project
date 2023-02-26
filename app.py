
#################################################
# Imports 
#################################################
import sqlite3
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect

from flask import Flask, jsonify, request

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/spotify_db.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
spotify = Base.classes.spotify

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes - HOME
##################################################
@app.route("/")
def home():
   return("Hi")
#################################################
@app.route('/api/v1.0/data')
def data():
    session = Session(engine)
    data = session.query(spotify.artist_names, spotify.rank, spotify.artist_genre, spotify.track_name, spotify.country, spotify.streams, spotify.danceability, spotify.tempo, spotify.loudness, spotify.acousticness, spotify.week).all()
    dict = []
    for row in data: 
        column = {}
        column["Artists"] = row[0]
        column["Rank"] = row[1]
        column["Genre"] = row[2]
        column["Track"] = row[3]
        column["Country"] = row[4]
        column["Streams"] = row[5]
        column["Danceability"] = row[6]
        column["Tempo"] = row[7]
        column["Loudness"] = row[8]
        column["Acousticness"] = row[9]
        column["Week"] = row[10]
        dict.append(column)
    session.close
        
    return jsonify(dict)
#################################################
@app.route('/api/v1.0/topArtists')
def topArtists():
    session = Session(engine)
    data = session.query(spotify.artist_names, spotify.streams, spotify.country).all()
    dict = []
    for row in data: 
        column = {}
        column["Artists"] = row[0]
        column["Streams"] = row[1]
        column["Country"] = row[2]
        dict.append(column)
    session.close
    
    return jsonify(dict)
#################################################
    
if __name__ == "__main__":
    app.run(debug=True)
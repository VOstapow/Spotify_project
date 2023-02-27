from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func ,inspect,Table, Column, ForeignKey
from flask import Flask, jsonify, render_template
import numpy as np
import psycopg2
username = 'postgres'
password = 'elizabeth1'
import pandas as pd
# from flask_cors import CORS
#Read data files
#=======================================================
spotify_df = pd.read_csv('fy_spotify_cleaned.csv')
spotify_df = pd.DataFrame(spotify_df)

#Connect to Database
#psql_conn_str = "postgres:postgres@localhost:5432/spotify_DB"
engine = create_engine(f'postgresql://{username}:{password}@localhost:5432/spotify_DB')
session = Session(engine)

Base = automap_base()
Base.prepare(engine, reflect=True)
table = Base.classes.keys()
#table = Base.metadata.tables['spotify_data']
t = Base.classes.spotify_data
print(table)

#write df to database
#spotify_df.to_sql(name='spotify_data',con=engine, if_exists='replace',index=False)

app = Flask(__name__)
@app.route("/")
def main():
    print("Server received request for 'Home' page...")
    return("<div ><p><h1> Welcome to Spotify Data Api!</h1></p>"
    "<li><strong> spotyify_table:</strong><font color='orange'> /api/v1.0/sdata</font></li>")

@app.route("/api/v1.0/sdata")
def sdataQuery():
    """Return a list of department details"""
    
    deptt = session.query(t.artist_names,t.rank,t.artist_genre, t.track_name, t.country, t.streams, t.danceability,
        t.tempo, t.loudness, t.acousticness, t.week).all()
    slist = []  
    for d in deptt:
        sdlist = {}
        sdlist['artists']=d[0]
        sdlist['rank']=d[1]
        sdlist['genre']=d[2]
        sdlist['track']=d[3]
        sdlist['country']=d[4]
        sdlist['streams']=d[5]
        sdlist['dance']=float(d[6])
        sdlist['tempo']=float(d[7])
        sdlist['loud']=float(d[8])
        sdlist['acoustic']=float(d[9])
        sdlist['weeks']=str(d[10])

        slist.append(sdlist)

    #dt = {d:n for d,n in deptt}
    return jsonify(slist)



if __name__ == "__main__":
    app.run(debug=True)
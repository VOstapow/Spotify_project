import sqlite3
import pandas as pd

from pathlib import Path

# Create new path for sqlite file 
database_path = "db.sqlite"
Path(database_path).touch()


conn = sqlite3.connect(database_path)
c = conn.cursor()

# Create table 
# Need primary key for table to be created 
c.execute('''create table spotify ( uri text primary key, 
          rank int, 
          artist_names text, 
          artist_id text, 
          artist_img text, 
          track_name text, 
          album_cover text, 
          peak_rank int, 
          weeks_on_chart int, 
          streams int, 
          week date, 
          country text, 
          danceability float, 
          acousticness float, 
          loudness float,
          tempo float)''')

# Reference from csv path 
csv = pd.read_csv("vang2.csv")
csv.to_sql("spotify", conn, if_exists='append', index=False)

conn.close()

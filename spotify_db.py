import sqlite3
import pandas as pd

from pathlib import Path

# Create new path for sqlite file 
database_path = "Resources/spotify_db.sqlite"
Path(database_path).touch()


conn = sqlite3.connect(database_path)
c = conn.cursor()

c.execute('drop table if exists spotify')

# Create table 
# Need primary key for table to be created (id interger primary key)
c.execute('''create table spotify (id int primary key,
          uri text, 
          rank int, 
          artist_names text, 
          artist_id text,
          artist_genre text, 
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

# REad csv file
csv = pd.read_csv("Resources/spotify.csv")
# Load data to SQLite
csv.to_sql("spotify", conn, if_exists='append', index=False)

conn.close()
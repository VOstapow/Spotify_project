-- Database: spotify_DB
-- DROP DATABASE IF EXISTS "spotify_DB";

CREATE DATABASE "spotify_DB"
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'English_United States.1252'
    LC_CTYPE = 'English_United States.1252'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;

--Create Tables
CREATE TABLE Spotify_data (
    id SERIAL not null primary key,	
    uri VARCHAR,
    rank INT,
    artist_names VARCHAR,
    artist_id VARCHAR (225),
    artist_genre VARCHAR (225),
    artist_img VARCHAR(225),
    track_name VARCHAR(225),
    album_cover VARCHAR(225), 
    peak_rank INT,
    weeks_on_chart INT,
    streams INT,
    week DATE,
    danceability DECIMAL,
    loudness DECIMAL,
    acousticness DECIMAL,
    tempo DECIMAL,
    country VARCHAR(225)
);
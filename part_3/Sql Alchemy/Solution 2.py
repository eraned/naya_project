'''
Part 1 - create the tables tracks, albums and artists both as SQLAlchemy Tables and as pandas DataFrames.
Part 2 - Answer the following questions in two ways - using SQLAlchemy and using pandas.
What is the size of the table tracks?
Which artist has the highest number of tracks?
'''

import pandas as pd
from sqlalchemy import create_engine, Table, MetaData, Column, Integer, String, Float
from sqlalchemy import select, desc
from sqlalchemy.sql import func


######################################     Part 1          #######################################################
# Create engine
engine = create_engine('sqlite:///chinook.db', echo=False)

# Create metadata
metadata = MetaData()
conn = engine.connect()

# Tracks
tracks = Table('tracks', metadata, autoload_with=engine)
query = select([tracks])
results = conn.execute(query).fetchall()
df_tracks = pd.DataFrame(results, columns=tracks.c.keys())
print(df_tracks.head())


# Albums
albums = Table('albums', metadata, autoload_with=engine)
query = select([albums])
results = conn.execute(query).fetchall()
df_albums = pd.DataFrame(results, columns=albums.c.keys())
print(df_albums.head())

# Artists
artists = Table('artists', metadata, autoload_with=engine)
query = select([artists])
results = conn.execute(query).fetchall()
df_artists = pd.DataFrame(results, columns=artists.c.keys())
print(df_artists.head())



######################################     Part 2          #######################################################

'What is the size of the table tracks?'
# SQL Alchemy
query = select([func.count()]).select_from(tracks)
print(conn.execute(query).fetchall())

# Pandas
print(len(df_tracks))


"-----------------------------------------------------------------------------------------------------------"
'Which artist has the highest number of tracks?'

# SQL Alchemy

join_stmt = tracks.join(albums, tracks.c.AlbumId == albums.c.AlbumId)\
    .join(artists, albums.c.ArtistId == artists.c.ArtistId)

query = select([artists.c.Name, func.count(tracks.c.TrackId).label('tracks_count')])\
    .select_from(join_stmt)\
    .group_by(artists.c.ArtistId)\
    .order_by(desc('tracks_count'))

print(conn.execute(query).fetchmany(5))

# Pandas

df_all = df_tracks\
    .join(df_albums.set_index('AlbumId'), on='AlbumId')\
    .join(df_artists.set_index('ArtistId'), on='ArtistId',
          lsuffix='_l', rsuffix='_r')
print(df_all.Name_r.value_counts()[:5])
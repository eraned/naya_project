'''
Task - Show the names of all the albums and their artists.
'''

import pandas as pd
from sqlalchemy import create_engine, Table, MetaData, Column, Integer, String, Float
from sqlalchemy import select, desc
from sqlalchemy.sql import func

# Create engine
engine = create_engine('sqlite:///chinook.db', echo=False)

# Create metadata
metadata = MetaData()
conn = engine.connect()

#create albums,artists table
artists = Table('artists', metadata, autoload_with=engine)
albums = Table('albums', metadata, autoload_with=engine)

# join between tables
join_stmt = artists.join(albums, artists.c.ArtistId == albums.c.ArtistId)

query = select([albums.c.Title, artists.c.Name],
               from_obj=join_stmt)
query = select([albums.c.Title, artists.c.Name]).select_from(join_stmt)
result = conn.execute(query)
print(result.fetchmany(5))
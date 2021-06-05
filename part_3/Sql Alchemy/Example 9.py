'''
Task - get albums table to pandas.
'''

import pandas as pd
from sqlalchemy import create_engine, Table, MetaData, Column, Integer, String, Float
from sqlalchemy import select, desc
from sqlalchemy.sql import func

df_movies = pd.read_csv('movies.csv')
print(df_movies.head())

df_ratings = pd.read_csv('ratings.csv')
print(df_ratings.head())

## Creating the tables
engine = create_engine('sqlite:///:memory:', echo=False)
metadata = MetaData()
conn = engine.connect()

movies = Table('movies', metadata,
    Column('movieID', Integer),
    Column('title', String),
    Column('genres', String),
)

ratings = Table('ratings', metadata,
    Column('userID', Integer),
    Column('movieID', Integer),
    Column('rating', Float),
    Column('timestamp', Integer)
)

metadata.create_all(engine)

## Inserting the data

for ind, row in df_movies.iterrows():
    ins = movies.insert().values(movieID=row.movieID, title=row.title, genres=row.genres)
    conn.execute(ins)

print(conn.execute(select([movies])).fetchmany(5))

for ind, row in df_ratings.iterrows():
    ins = ratings.insert().values(userID=row.userID, movieID=row.movieID, rating=row.rating, timestamp=row.timestamp)
    conn.execute(ins)

print(conn.execute(select([ratings])).fetchmany(5))
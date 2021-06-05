'''
Task - Show the names of the employees and their job title.
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

#create albums table
albums = Table('albums', metadata, autoload_with=engine)

query = select([albums.c.Title], whereclause=albums.columns.Title.like('%the best of%'))
query = select([albums]).where(albums.columns.Title.like('%the best of%'))

result = conn.execute(query)
print(result.fetchmany(5))
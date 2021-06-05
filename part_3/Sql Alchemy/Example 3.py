'''
Task - Show the names of the albums which contain the phrase "The best of".
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

# When we create a select() construct, SQLAlchemy looks around at the tables we’ve mentioned
# and then places them in the FROM clause of the statement.
# We can select the entire table or specific columns.
query = select([albums.c.Title], whereclause=albums.columns.Title.like('%the best of%'))
query = select([albums]).where(albums.columns.Title.like('%the best of%'))

result = conn.execute(query)
print(result.fetchmany(5))
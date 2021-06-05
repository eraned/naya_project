'''
Task - get albums table to pandas.
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

#create albums,customers table
albums = Table('albums', metadata, autoload_with=engine)

query = select([albums])
result = conn.execute(query)

df_albums = pd.DataFrame(result.fetchall(), columns=result.keys())
print(df_albums.head())



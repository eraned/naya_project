import pandas as pd
from sqlalchemy import create_engine, Table, MetaData, Column, Integer, String, Float
from sqlalchemy import select, desc
from sqlalchemy.sql import func

engine = create_engine('sqlite:///chinook.db', echo=False)

# Get tables name
print(engine.table_names())

# Create metadata
metadata = MetaData()

conn = engine.connect()

albums = Table('albums', metadata, autoload_with=engine)

print(albums)

query = select([albums])
result = conn.execute(query)
print(result.fetchmany(5))

query = '''
SELECT * FROM albums
WHERE Title LIKE '%the best of b%'
'''
result = conn.execute(query)
print(result.fetchall())

albums = Table('albums', metadata, autoload_with=engine)
# query = select([albums.c.AlbumId])
query = select([albums],whereclause=albums.columns.Title.like('%the best of%'))

result = conn.execute(query)
print(result.fetchmany(5))


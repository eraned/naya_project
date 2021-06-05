'''
Task - Create tables and database
'''

import pandas as pd
from sqlalchemy import create_engine, Table, MetaData, Column, Integer, String, Float
from sqlalchemy import select, desc
from sqlalchemy.sql import func

# Create engine
engine = create_engine('sqlite:///:memory:', echo=False)
# Create metadata
metadata = MetaData()

users = Table('users', metadata,
    Column('id', Integer),
    Column('name', String),
    Column('fullname', String),
)

addresses = Table('addresses', metadata,
    Column('id', Integer),
    Column('user_id', Integer),
    Column('email_address', String)
)

metadata.create_all(engine)

# All operations are sent to the database through the connection object.
conn = engine.connect()

query = users.insert().values(id=1234, name='jack', fullname='Jack Jones')
result = conn.execute(query)
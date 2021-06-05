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

#create employees table
employees = Table('employees', metadata, autoload_with=engine)

# When we create a select() construct, SQLAlchemy looks around at the tables we’ve mentioned
# and then places them in the FROM clause of the statement.
# We can select the entire table or specific columns.
query = select([employees])
result = conn.execute(query)
print(result.fetchmany(5))


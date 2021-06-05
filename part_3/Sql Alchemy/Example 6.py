'''
Task - Show for each customer (name) the number of invoinces they had.
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

#create invoices,customers table
invoices = Table('invoices', metadata, autoload_with=engine)
customers = Table('customers', metadata, autoload_with=engine)

query = select([customers.c.FirstName + " " + customers.c.LastName, func.count(invoices.c.InvoiceId)])\
            .select_from(invoices.join(customers, invoices.c.CustomerId == customers.c.CustomerId))\
            .group_by(invoices.c.CustomerId)
result = conn.execute(query)
print(result.fetchmany(5))
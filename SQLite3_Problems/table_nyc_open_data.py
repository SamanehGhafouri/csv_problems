import sqlite3

conn = sqlite3.connect('business_owners_info.db')
c = conn.cursor()

# Create Table
c.execute(""" CREATE TABLE business_owner(
FirstName 
LastName TEXT
BusinessNumber TEXT
ContactNumber TEXT
BusinessNumber TEXT)
""")
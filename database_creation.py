# Referenced from https://docs.python.org/3/library/sqlite3.html

import sqlite3

# create database connection and cursor object, then create table
con = sqlite3.connect("password_keeper.db")
cursor = con.cursor()
# cursor.execute("CREATE TABLE IF NOT EXISTS entries (name, username, email, password, note)")
cursor.execute("""
CREATE TABLE IF NOT EXISTS entries (name TEXT NOT NULL, 
               username TEXT NOT NULL, 
               email TEXT NOT NULL, 
               password TEXT NOT NULL, 
               note TEXT)
""")


# save changes and close
con.commit()
con.close()
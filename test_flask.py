#A testing file for testing how Flask and SQLite work together.

import sqlite3
from flask import Flask
app = Flask(__name__)



@app.route('/')
def add_entry():
   conn = sqlite3.connect('password_keeper.db')
   cursor = conn.cursor()
   cursor.execute("CREATE TABLE IF NOT EXISTS entries (name, username, email, password, note)")

   cursor.execute("INSERT INTO entries (name, username, email, password, note) VALUES (?, ?, ?, ?, ?)", 
                  ('John','JDOERUleZ321','JDOE123@mycu.com',12345,'NULL'))
   conn.commit()
   conn.close()
   return 'Data inserted successfully!'

if __name__ == '__main__':
   app.run(debug=True)
# Referenced from https://pythongeeks.org/flask-sqlite/ and https://www.delftstack.com/howto/python-flask/flask-request-json/ 
# Referenced from https://flask.palletsprojects.com/en/stable/patterns/sqlite3/# 


from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)
#Database = "password_keeper.db"

def get_data():
   conn = sqlite3.connect('password_keeper.db')
   return conn

@app.route('/')
def table_open():
   conn = get_data()   # Connect to SQLite database
   cursor= conn.cursor
   cursor.execute("CREATE TABLE IF NOT EXISTS entries (email, username, password, service, note)")     
   conn.commit()
   conn.close()
   return jsonify (good=f"Table created successfully!")



@app.route('/add_entry')
def add_entry():
   info = request.json
   conn = get_data()
   cursor = conn.cursor
   cursor.execute("""
    INSERT INTO entries (name, username, email, password, note)
    VALUES (?,?,?,?,?)""",
    (info['name'], info['username'], info['email'], info['password'], info.get['note']))
   cursor.commit()
   cursor.close()
   return jsonify (goodbye=f"Entry was added to database!")

#@app.route('/get_entry')
#def get_entry():

if __name__ == "__main__":
    app.run()

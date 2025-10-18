from flask import Flask, request
import database_functions
import sqlite3

app = Flask(__name__)

@app.route("/credentials/add")
def add_entry():
    con = sqlite3.connect("password_keeper.db")
    cursor = con.cursor()
    data = request.args.get('pass')
    database_functions.add_entry(cursor, data)
    con.commit()
    con.close()
    return "success"


if __name__ == "__main__":
    app.run()
from flask import Flask, request
import database_functions

app = Flask(__name__)

@app.route("/credentials/add")
def add_entry():
    data = request.args.get('pass')
    database_functions.add_entry(data)
    return "success"


if __name__ == "__main__":
    app.run()
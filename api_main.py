from flask import Flask, request
import database_functions

app = Flask(__name__)

@app.route("/credentials/add")
def add_entry():
    data = request.args.get('pass')
    database_functions.add_entry(data)
    return "Successfully Added!"

@app.route("/credentials/remove")
def remove_entry():
    data = request.args.get('pass')
    database_functions.remove_entry(data)
    return "Successfully Removed! "


@app.route("/credentials/update")
def update_entry():
    data = request.args.get('pass')
    database_functions.update_entry(data)
    return "Successfully Updated!"

@app.route("/credentials/get")
def get_entry():
    data = request.args.get('pass')
    database_functions.get_entry(data)
    return "Successfully Found!"

@app.route("/credentials/getall")
def get_all_entries():
    data = request.args.get('')
    database_functions.get_all_entries(data)
    return "Successfully Displayed All!"

if __name__ == "__main__":
    app.run()
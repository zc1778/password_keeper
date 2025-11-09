from flask import Flask, request, render_template, redirect
import database_functions

app = Flask(__name__)



@app.route('/index')
def index():
   return render_template('index.html')

@app.route('/login')
def login():
   return render_template('login.html')
   #Listen for login button click
   #Grab data from HTML Form
   #Cross check database for fail or success
   #if success
   #    return redirect(url_for('home'))

@app.route('/sign_up')
def sign_up():
   return render_template('sign_up.html')
   #Listen for register button click
   #Grab data from HTML Form
   #Cross check if info already exists
   #If success
   #    return redirect(url_for('home'))

@app.route('/home')
def home():
   return render_template('home.html')

@app.route('/add')
def add():
   return render_template('add.html')
   #Listen for add entry button click
   #Grab data from HTML Form
   #Insert data into database





#Various Flask Routes for master_table



@app.route("/credentials/add_mast", methods=['POST'])
def add_master_route():
    data = request.form.get('master_user')
    password = request.form.get('master_password')
    database_functions.add_master(data, password)
    return "Successfully Added!"


@app.route("/credentials/get_mast")
def get_master_route():
    data = request.args.get('pass')
    database_functions.get_master(data, data)
    return "Successfully Gotten!"


#Various Flask routes for entries

# @app.route("/credentials/remove")
# def remove_entry():
#     data = request.args.get('pass')
#     database_functions.remove_entry(data)
#     return "Successfully Removed! "


# @app.route("/credentials/update")
# def update_entry():
#     data = request.args.get('pass')
#     database_functions.update_entry(data)
#     return "Successfully Updated!"

# @app.route("/credentials/get")
# def get_entry():
#     data = request.args.get('pass')
#     database_functions.get_entry(data)
#     return "Successfully Found!"

# @app.route("/credentials/getall")
# def get_all_entries():
#     data = request.args.get('')
#     database_functions.get_all_entries(data)
#     return "Successfully Displayed All!"

if __name__ == "__main__":
     app.run()
#Here is a very useful source that shows how retrieve HTML using Flask: 
#  https://www.geeksforgeeks.org/html/retrieving-html-from-data-using-flask/





from flask import Flask, request, render_template, redirect
import database_functions

app = Flask(__name__)


@app.route('/index')
def index():
   return render_template('index.html')


@app.route('/login', methods = ["GET", "POST"])
def login():
   if request.method == "POST":
      user_email = request.form.get("email")
      user_password = request.form.get("password")
   return render_template('login.html')
   #Cross check database for fail or success
   #if success
   #    return redirect(url_for('home'))

@app.route('/sign_up', methods = ["GET", "POST"])
def sign_up():
   if request.method == "POST":
      user_email = request.form.get("email")
      user_password = request.form.get("password")
   return render_template('sign_up.html')
   #Cross check if info already exists
   #If success
   #    return redirect(url_for('home'))

@app.route('/home')
def home():
   return render_template('home.html')

@app.route('/add', methods = ["GET", "POST"])
def add():
   if request.method == "POST":
      user_email = request.form.get("email")
      user_password = request.form.get("password")
      user_username = request.form.get("username")
      user_service = request.form.get("service")
      user_note = request.form.get("note")
   return render_template('add.html')
   #Insert data into database



#Various Flask Routes for master_table



@app.route("/credentials/add_mast", methods=['POST'])
def add_master_route():
    data = request.form.get['master_user']
    password = request.form.get['master_password']
    database_functions.add_master(data, password)
    return "Successfully Added!"



@app.route("/credentials/get_mast")
def get_master_route():
    data = request.args.get('pass')
    database_functions.get_master(data)
    return "Successfully Gotten!"



@app.route("/credentials/remove", methods=['POST'])
def remove_entry():
     removes = request.form.get[id]
     data = request.args.get('pass')
     database_functions.remove_entry(removes)
     return "Successfully Removed!"


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
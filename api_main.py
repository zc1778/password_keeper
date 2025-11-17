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
      master = database_functions.get_master(user_email)
      if master and master[2] == user_password:
          return redirect(url_for('home'))
      else:
          return render_template('login.html', error="Sorry, your username or password is incorrect, please try again!")
   return render_template('login.html')


   #Cross check database for fail or success
   #if success
   #    return redirect(url_for('home'))

@app.route('/sign_up', methods = ["GET", "POST"])
def sign_up():
   if request.method == "POST":
      user_email = request.form.get("email")
      user_password = request.form.get("password")
      user_exists = database_functions.get_master(user_email)
      if user_exists:
          return render_template('sign_up.html', error="This user already exists, no need to sign up!")
      else:
          database_functions.add_master(user_email, user_password)
          return redirect(url_for('login.html'))
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
      database_functions.add_entry(user_email, user_password, user_username, user_service, user_note)
      return redirect(url_for('home'))
   return render_template('add.html')
   #Insert data into database



#Various Flask Routes for master_table



@app.route("/credentials/add_mast", methods=['POST'])
def add_master_route():
    data = request.form.get('master_user')
    password = request.form.get('master_password')
    if data and password:
        database_functions.add_master(data, password)
        return "Successfully Added!"
    return "Sorry, your entry wasn't added!"



@app.route("/credentials/get_mast")
def get_master_route():
    data = request.args.get('master_user')
    master = database_functions.get_master(data)
    if master:
        return f"Master ID: {master[0]}, User: {master[1]}"
    return "Successfully Not Gotten!"



@app.route("/credentials/add", methods=['POST'])
def add_entry():
   master_id =  request.form.get('master_id')
   email =  request.form.get('email')
   username =  request.form.get('username')
   password =  request.form.get('password')
   service = request.form.get('service')
   note =  request.form.get('note')
   if master_id and email and username and password and service and note:
        database_functions.add_master(master_id, email, username, password, service, note)
        return "Successfully Added!"
   return "Sorry, your entry wasn't added!"
        



@app.route("/credentials/remove", methods=['POST'])
def remove_entry():
     removes = request.form.get('id')
     if removes:
         database_functions.remove_entry(int(removes))
         return "Successfully Removed"
     return "Not Valid, Try Again!"


@app.route("/credentials/update", methods=['POST'])
def update_entry():
   id =  request.form.get('id')
   email =  request.form.get('email')
   username =  request.form.get('username')
   password =  request.form.get('password')
   note =  request.form.get('note')
   database_functions.update_entry(email,username, password, note, int(id))
   return "Successfully Updated!"

@app.route("/credentials/get")
def get_entry():
    data = request.args.get('service')
    getting = database_functions.get_entry_service(data)
    if getting:
        return f"Master ID: {getting[0]}, Email: {getting[1]}, Username: {getting[2]}, Password: {getting[3]}, Service: {getting[4]}, Note: {getting[5]}"
    return "The entry was not found!!"




#WIP

# @app.route("/credentials/getall")
# def get_all_entries():
#     master_stuff = request.args.get('master_id')
#     if master_stuff:
#         data = database_functions.get_all_entries(int(master_id))
#         return render_template('test.html', data=data)
#     return "Successfully Displayed All!"

if __name__ == "__main__":
     app.run()
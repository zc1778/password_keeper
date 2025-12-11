# These are the functions that should be called depending on the API request.
# The dots (...) in the queries should be filled in by whatever the parameters are.
# Every function takes a cursor object which should be initialized in the api file
#                                                               and passed into the function from there.
# Ideally, data should hold whatever request is passed into itand further logic may be written to hand more specific cases.

import sqlite3




#Here is the master_account functions for username and password


def add_master(master_user, master_password):
    con = sqlite3.connect("password_keeper.db")
    cursor = con.cursor()
    cursor.execute("INSERT INTO master_account (master_user, master_password) VALUES (?, ?)", 
                   (master_user, master_password)
                   )
    con.commit()
    con.close()


def get_master(master_user):
    con = sqlite3.connect("password_keeper.db")
    cursor = con.cursor() 
    cursor.execute("SELECT accountID, master_user, master_password FROM master_account WHERE master_user = ?",
                   (master_user,)
    )
    get_results = cursor.fetchone()
    con.close()
    return get_results



#Here is the entries functions for add, remove, update, delete, get service, and get all entries.



def add_entry(email, username, password, service, note):
    con = sqlite3.connect("password_keeper.db")
    cursor = con.cursor()
    cursor.execute("INSERT INTO entries (email, username, password, service, note) VALUES (?, ?, ?, ?, ?)", 
                   (email, username, password, service, note)
                   )
    con.commit()
    con.close()



def remove_entry(id):
    con = sqlite3.connect("password_keeper.db")
    cursor = con.cursor()
    cursor.execute("DELETE FROM entries where id = ?",
                   (id,)
                   )
    con.commit()
    con.close()



def update_entry(email, username, password, note, id):
    con = sqlite3.connect("password_keeper.db")
    cursor = con.cursor()
    cursor.execute( "UPDATE entries SET email = ?, SET username = ?, SET password = ?, SET note = ?, WHERE id = ?", (email, username, password, note, id))
    con.commit()
    con.close()




#This should be used with HTML to have an option where the user can search for passwords by entering a service (Example: Google, Blackboard, etc)
def get_entry_service(service):
    con = sqlite3.connect("password_keeper.db")
    cursor = con.cursor() 
    cursor.execute("SELECT master_id, email, username, password, service, note FROM entries WHERE service = ?",
                   (service,)
    )
    get_service = cursor.fetchone()
    con.close()
    return get_service



def get_all_entries(master_id):
    con = sqlite3.connect("password_keeper.db")
    cursor = con.cursor() 
    cursor.execute("SELECT * FROM entries")
    get_all = cursor.fetchall()
    con.close()
    return get_all


# # CITATION STUFF
# # https://stackoverflow.com/questions/16856647/sqlite3-programmingerror-incorrect-number-of-bindings-supplied-the-current-sta  error with insert into statement, needed a comma
# # https://stackoverflow.com/questions/48218065/objects-created-in-a-thread-can-only-be-used-in-that-same-thread error with connection object, calling across files maybe but just moved them into scope of the functions for now
# # https://www.geeksforgeeks.org/python/inserting-variables-to-database-table-using-python/ needed syntax for inserting with variables
# # https://www.geeksforgeeks.org/html/retrieving-html-from-data-using-flask/ 
# #
# #
# #
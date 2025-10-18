# These are the functions that should be called depending on the API request.
# The dots (...) in the queries should be filled in by whatever the parameters are.
# Every function takes a cursor object which should be initialized in the api file
#                                                               and passed into the function from there.
# Ideally, data should hold whatever request is passed into itand further logic may be written to hand more specific cases.

import sqlite3

def add_entry(data):
    con = sqlite3.connect("password_keeper.db")
    cursor = con.cursor()
    cursor.execute("INSERT INTO entries (password) VALUES (?)", (data,))
    con.commit()
    con.close()

def remove_entry(cursor, data):
    cursor.execute("DELETE FROM entries WHERE ... ")
    cursor.commit()

def update_entry(cursor, data):
    cursor.execute("UPDATE entries SET ... WHERE ...")
    cursor.commit()

def get_entry(cursor, data):
    result = cursor.execute("SELECT ... FROM ... WHERE ...")
    cursor.commit()

def get_all_entries(cursor):
    result = cursor.execute("SELECT * FROM entries")
    print(result)






# CITATION STUFF
# https://stackoverflow.com/questions/16856647/sqlite3-programmingerror-incorrect-number-of-bindings-supplied-the-current-sta  error with insert into statement, needed a comma
# https://stackoverflow.com/questions/48218065/objects-created-in-a-thread-can-only-be-used-in-that-same-thread error with connection object, calling across files maybe but just moved them into scope of the functions for now
# https://www.geeksforgeeks.org/python/inserting-variables-to-database-table-using-python/ needed syntax for inserting with variables
#
#
#
#
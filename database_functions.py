# These are the functions that should be called depending on the API request.
# The dots (...) in the queries should be filled in by whatever the parameters are.
# Every function takes a cursor object which should be initialized in the api file
#                                                               and passed into the function from there.
# Ideally, data should hold whatever request is passed into itand further logic may be written to hand more specific cases.

def add_entry(cursor, data):
    cursor.execute("INSERT INTO entries VALUES ...")
    cursor.commit()

def remove_entry(cursor, data):
    cursor.execute("DELETE FROM entries WHERE ... ")
    cursor.commit()

def update_entry(cursor, data):
    cursor.execute("UPDATE entries SET ... WHERE ...")
    cursor.commit()

def get_entry(cursor, data):
    result = cursor.execute("SELECT ... FROM ... WHERE ...")
    cursor.commit()